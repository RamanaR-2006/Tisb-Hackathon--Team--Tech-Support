import matplotlib.pyplot as plt
import random
import time
import cv2 as cv
import numpy as np

framecount = 500

'''def rescaleFrame(frame, scale=1.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height
    return cv.resize(frame, dimensions,interpolation=cv.INTER_AREA)'''
capture = cv.VideoCapture(r"C:\Users\siddharth\Desktop\TISBHACKS\TISBHACKSV2\dataset_video1 (1) (1).avi")
plt.ion()

fig, ax = plt.subplots()
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
    
    cv.imshow('Detected Cars', Frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

    
    
    no = len(cars) 
    AVG_time.append(no)
    print(AVG_time)
    while len(AVG_time) == 10:
        x2.append(count)
        y2.append(sum(AVG_time)/10)
        line.set_data(x2, y2)
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.ioff()
        plt.show(block=False)
        AVG_time.clear()
        print(AVG_time)
    count += 1
    
    framecount -= 1
    print(framecount)

    if framecount == 0:
        break

capture.release()
cv.destroyAllWindows
