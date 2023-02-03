import tkinter
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import customtkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import cv2 as cv
import PIL.Image, PIL.ImageTk


'''fig = Figure(figsize=(10,8),dpi=100)
y = [i**2 for i in range(101)]'''
allcars = []
graphcheck = False
root = customtkinter.CTk()
root.title("Congestion Overlooking Metropolitan Electronic Tracker")
root.iconbitmap(r"C:\Users\siddharth\Desktop\TISBHACKS\GUI\Comet-logo1.1.ico")
root.geometry("400x200")

#Theme
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
comet_logo = ImageTk.PhotoImage(Image.open(r"C:\Users\siddharth\Desktop\TISBHACKS\TISBHACKSV2\comet logo final probably v2.png"))

frame1 = customtkinter.CTkFrame(master=root,width=500, height=1000,corner_radius=20)
comet = customtkinter.CTkLabel(master=frame1,image=comet_logo)
comet.place(relx=0.5,rely=0.4,anchor=tkinter.CENTER)
frame1.place(relx=0.27,rely=0.5,anchor=tkinter.E)

#Central data
frame3 = customtkinter.CTkFrame(master=root,width=400, height=1000, corner_radius=20)
frame3.place(relx=0.385,rely=0.5,anchor=tkinter.CENTER)

fonttup = ("Source Code Pro",60,"bold","underline")
fonttup2 = ("Source Code Pro",20,"bold",)
fonttup3 = ("Source Code Pro",15,"bold",)
junc = customtkinter.CTkButton(text="JUNCTION I",font=fonttup,master=frame3,)




junc.place(relx=0.070,rely=0.1)





#Graph
frame2 = customtkinter.CTkFrame(master=root,width=500, height=1000,corner_radius=20)
frame2.place(relx=0.5,rely=0.5,anchor=tkinter.W)
video = cv.VideoCapture(r"C:\Users\siddharth\Downloads\scuffedassbitchasspart2.mp4")

label = customtkinter.CTkLabel(frame2)
label.pack()

def rescaleFrame(frame, scale=0.4):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions,interpolation=cv.INTER_AREA)

def update_frame():
    ret, frame = video.read()
    frame = rescaleFrame(frame)
    if not ret:
        return
    
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    frame = PIL.Image.fromarray(frame)
    frame = PIL.ImageTk.PhotoImage(frame)

    label.configure(image=frame)
    label.image = frame

    root.after(int(1000/30), update_frame)

update_frame()






capture = cv.VideoCapture(r"C:\Users\siddharth\Desktop\TISBHACKS\TISBHACKSV2\dataset_video1 (1) (1).avi")



framecount = 500

fig, ax = plt.subplots()
plot1 = fig.add_subplot(111)
x2 = [0]
y2 = [0]
    
line, = ax.plot(x2, y2)

AVG_time = []

count = 0
while True:
        
                
                
            isTrue, Frame = capture.read()
            #scaleup = rescaleFrame(Frame)
            #cv.imshow('Scaled up', scaleup)

            gray = cv.cvtColor(Frame, cv.COLOR_BGR2GRAY)
            #cv.imshow('Grayscale Car', gray)

            blur = cv.GaussianBlur(gray,(5,5),0)
            #cv.imshow('Blur', blur)
            dilated = cv.dilate(blur,np.ones((3,3)))
            kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (2, 2))
            closing = cv.morphologyEx(dilated, cv.MORPH_CLOSE, kernel) 

            car_cascade_src = 'cars.xml'
            car_cascade = cv.CascadeClassifier(car_cascade_src)
            cars = car_cascade.detectMultiScale(closing, 1.1, 1)

                
                

            for (x, y, w, h) in cars:
                cv.rectangle(Frame, (x,y), (x+w, y+h), (0,255,0), thickness=1)
                
            #cv.imshow('Detected Cars', Frame)
            if cv.waitKey(20) & 0xFF==ord('d'):
                break

                
                
            no = len(cars) 
            AVG_time.append(no)
            allcars.append(no)
            print(AVG_time)
            while len(AVG_time) == 10:
                    
                    x2.append(count)
                    y2.append(sum(AVG_time)/10)
                    line.set_data(x2, y2)
                    ax.relim()
                    ax.autoscale_view()
                    
                    
                    
                    AVG_time.clear()
                    
                    
            count += 1
                
            framecount -= 1
            print(framecount)
                
            if framecount == 0:
                    break
        
capture.release()
cv.destroyAllWindows

mean = sum(allcars)/len(allcars)

avg1 = 0
f_avgList = []
total = 0
compare = 0
count1 = 0
congestion_tracker =0
for i in allcars:
    dif = i - mean
    if allcars.index(i) != 0:
        compare = allcars[allcars.index(i)-1]
        temp = i - compare
        if temp <= -2 or temp >= 2:
            f_avgList.append(f_avg)
            count1 = 0
            total = 0
    if dif <= 0:
        scale_factor = 0.95
        total += i
        count1 += 1
        avg1 = total/count1
        f_avg = avg1 * scale_factor
    elif 0 < dif <= 2:
        scale_factor = 0.87
        total += i
        count1 += 1
        avg1 = total/count1
        f_avg = avg1 * scale_factor
    elif 2 < dif <= 4:
        scale_factor = 0.79
        total += i
        count1 += 1
        avg1 = total/count1
        f_avg = avg1 * scale_factor
    elif 4 < dif <= 6:
        scale_factor = 0.71
        total += i
        count1 += 1
        avg1 = total/count1
        f_avg = avg1 * scale_factor
    elif dif > 6:
        congestion_tracker += 1
        scale_factor = 0.63
        total += i
        count1 += 1
        avg1 = total/count1
        f_avg = avg1 * scale_factor
final_avg = sum(f_avgList)/len(f_avgList)
congy = "Instances of high congestion = " + str(congestion_tracker)
cong = customtkinter.CTkLabel(text=congy,font=fonttup2,master=frame3)
cong.place(relx=0.5,rely=0.3,anchor=tkinter.CENTER)

avg = "Average emission = " + str(final_avg*121.3) + "g/km"
emm = customtkinter.CTkLabel(text= avg,font=fonttup3,master=frame3)
emm.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

root.mainloop()




