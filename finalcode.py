import tkinter
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import customtkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import cv2 as cv


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
junc = customtkinter.CTkButton(text="JUNCTION I",font=fonttup,master=frame3,)
cong = customtkinter.CTkLabel(text="Instances of high congestion = 5",font=fonttup2,master=frame3)



junc.place(relx=0.070,rely=0.1)
cong.place(relx=0.5,rely=0.3,anchor=tkinter.CENTER)




#Graph
frame2 = customtkinter.CTkFrame(master=root,width=500, height=1000,corner_radius=20)








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
                    fig.canvas.draw()
                    fig.canvas.flush_events()
                    plot1.plot(x2,y2)
                    canvas = FigureCanvasTkAgg(fig,master=frame2)
                    canvas.get_tk_widget().pack()
                    frame2.place(relx=0.5,rely=0.5,anchor=tkinter.W)
                    
                    
                    AVG_time.clear()
                    
                    
            count += 1
                
            framecount -= 1
            print(framecount)
                
            if framecount == 0:
                    break
        
capture.release()
cv.destroyAllWindows

mean = sum(allcars)/len(allcars)
avg = "Average emission = " + str(mean*121.3) + "g/km"
emm = customtkinter.CTkLabel(text= avg,font=fonttup2,master=frame3)
emm.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

root.mainloop()




