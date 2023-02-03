from tkinter import *
from PIL import ImageTk,Image
from cars import no



#Declaring root shell
root = Tk()
root.title("Congestion tracker")
root.geometry("400x240")
root.iconbitmap(r"C:\Users\siddharth\Desktop\TISBHACKS\GUI\Comet-logo1.1.ico")

comet_logo = ImageTk.PhotoImage(Image.open(r"C:\Users\siddharth\Desktop\TISBHACKS\GUI\Screenshot 2023-01-31 195235.png").resize((200,200)))

comet_logolab = Label(image = comet_logo)
comet_logolab.grid(column=0,row=0)

#Welcome to Comet
font_tuple = ("Roboto",20,"bold","underline")
heading = Label(text="WELCOME TO COMET",font=font_tuple)
heading.grid(column=2,row=0,sticky=W+E)

frame1 = LabelFrame(root, text="Car feed", padx = 150,pady = 250,height=100,width=100)
frame1.grid(column=0,row=3,columnspan=2)
#Cars Image
my_img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\siddharth\Desktop\TISBHACKS\TESTS\fake.png"))
my_img2 = ImageTk.PhotoImage(Image.open(r"C:\Users\siddharth\Desktop\TISBHACKS\TESTS\fake2.png"))
my_img3 = ImageTk.PhotoImage(Image.open(r"C:\Users\siddharth\Desktop\TISBHACKS\carswork.jpg"))
images_list = [my_img1,my_img2,my_img3]

my_label = Label(frame1,image=my_img1)
my_label.pack()

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    
    #Change image
    my_label.destroy()
    my_label = Label(frame1,image=images_list[image_number-1])
    button_forward = Button(root,text=">>",command=lambda: forward(image_number+1))
    button_back = Button(root,text="<<",command=lambda: forward(image_number-1))

    #If image is 4, disable forward
    if image_number == 3:
        button_forward=Button(root,text=">>",state=DISABLED)

    my_label.pack()
    button_back.grid(row=4,column=0)
    button_forward.grid(row=4,column=2)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    #Change image
    my_label.destroy()
    my_label = Label(frame1,image=images_list[image_number-1])
    button_forward = Button(root,text=">>",command=lambda: forward(image_number+1))
    button_back = Button(root,text="<<",command=lambda: forward(image_number-1))

    #If image is 1, disable button
    if image_number == 1:
        button_back=Button(root,text="<<",state=DISABLED)
    
    my_label.pack()
    button_back.grid(row=4,column=0)
    button_forward.grid(row=4,column=2)

#Declare buttons
button_back = Button(root,text="<<",command=back,state=DISABLED)
button_quit = Button(root,text = "Exit Program",command=root.quit)
button_forward = Button(root,text=">>",command=lambda: forward(2))


#Display buttons in grid
button_back.grid(row=4,column=0)
button_quit.grid(row=4,column=1)
button_forward.grid(row=4,column=2)



#cars_1 = ImageTk.PhotoImage(Image.open(r"C:\Users\siddharth\Desktop\TISBHACKS\carswork.jpg"))

#c1 = Label(frame1, image=cars_1)
#c1.pack()



#Graphs for no.of cars

#Different pages for different intersections

#No. of cars, display density, emissions
frame2 = LabelFrame(root,text = "Data",padx=200,pady=250,height=100,width=100)
frame2.grid(column=2,row=3,columnspan=3,sticky=W+E)
cars1 = Label(frame2, text="Number of Cars in feed: "+ str(no))
cars1.pack()


root.mainloop()