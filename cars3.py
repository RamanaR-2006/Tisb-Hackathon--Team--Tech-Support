import matplotlib.pyplot as plt
import random
import time
import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=1.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions,interpolation=cv.INTER_AREA)
capture = cv.VideoCapture(r"C:\Users\siddharth\Desktop\TISBHACKS\GUI\dataset_video1 (1).avi")

plt.ion()

fig, ax = plt.subplots()
x2 = [0]
y2 = [0]

line = ax.plot(x2, y2)

count = 0

while True:
    isTrue, Frame = capture.read()
    scaleup = rescaleFrame(Frame)
    #cv.imshow('Scaled up', scaleup)

    gray = cv.cvtColor(scaleup, cv.COLOR_BGR2GRAY)
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
        cv.rectangle(scaleup, (x,y), (x+w, y+h), (0,255,0), thickness=1)

    #cv.imshow('Detected Cars', scaleup)
    

#capture.release()
#cv.destroyAllWindows

    
    
    AVG_time = []
    check = False
    while check == False:
        no = len(cars)
        time.sleep(3)
        AVG_time.append(no)
        while len(AVG_time) == 10:
            x2.append(count)
            y2.append(sum(AVG_time)/10)
            line.set_data(x2, y2)
            ax.relim()
            ax.autoscale_view()
            fig.canvas.draw()
            fig.canvas.flush_events()
            check = True
            plt.ioff()
            plt.show(block=False)
            AVG_time.clear()
    count += 1
    print(count)
    if count == 11:
        break