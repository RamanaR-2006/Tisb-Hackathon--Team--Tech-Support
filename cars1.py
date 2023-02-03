import cv2 as cv
import numpy as np

num_cars = []
countcars=0
count=500
'''def rescaleFrame(frame, scale=1.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions,interpolation=cv.INTER_AREA)'''
capture = cv.VideoCapture(r"C:\Users\siddharth\Desktop\TISBHACKS\GUI\dataset_video1 (1).avi")

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

    print(len(cars))
    no = len(cars)
    num_cars.append(no)
    countcars += no
    print(num_cars)
    print(countcars)
    count -= 1

    if count == 0:
        break

    for (x, y, w, h) in cars:
        cv.rectangle(Frame, (x,y), (x+w, y+h), (0,255,0), thickness=1)

    cv.imshow('Detected Cars', Frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
print('a')
capture.release()
cv.destroyAllWindows