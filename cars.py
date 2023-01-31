import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.7):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions,interpolation=cv.INTER_AREA)

img = cv.imread('cars4.webp')
cv.imshow('Car', img)

scaleup = rescaleFrame(img)
cv.imshow('Scaled up', scaleup)

gray = cv.cvtColor(scaleup, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Car', gray)

blur = cv.GaussianBlur(gray,(5,5),0)
cv.imshow('Blur', blur)

dilated = cv.dilate(blur,np.ones((3,3)))
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (2, 2))
closing = cv.morphologyEx(dilated, cv.MORPH_CLOSE, kernel) 

car_cascade_src = 'cars.xml'
car_cascade = cv.CascadeClassifier(car_cascade_src)
cars = car_cascade.detectMultiScale(closing, 1.1, 1)

print(len(cars))

for (x, y, w, h) in cars:
    cv.rectangle(scaleup, (x,y), (x+w, y+h), (0,255,0), thickness=1)

cv.imshow('Detected Cars', scaleup)
cv.waitKey(0)