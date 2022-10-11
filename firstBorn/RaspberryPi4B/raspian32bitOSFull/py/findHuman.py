import cv2
import numpy as np
#import os
from gpiozero import PhaseEnableMotor
from time import sleep

#
# Define the command motor control functions
#
def stop():
    # Stop both motors
    motorLeft.stop()
    motorRight.stop()
#
def cwSpin():
    # Run left motor forward
    # Run right motor backward
    motorLeft.forward()
    motorRight.backward()
#
def ccwSpin():
    # Run left motor forward
    # Run right motor backward
    motorLeft.backward()
    motorRight.forward()
#
def lmf(s):
    motorLeft.forward(speed=s) #speed=0.75)
#
def lmb(s):
    motorLeft.backward(speed=s) #speed=0.5)
#
def rmf(s):
    motorRight.forward(speed=s)
#
def rmb(s):
    motorRight.backward(speed=s) #speed=0.5)

#print(os.listdir())

# Raspberry Pi path for OpenCV data:
#/usr/local/lib/python3.9/dist-packages/cv2/data/
datafldr='/usr/local/lib/python3.9/dist-packages/cv2/data/'
face_cascade = cv2.CascadeClassifier(datafldr+'haarcascade_frontalface_default.xml')
# face_cascade = cv2.CascadeClassifier(datafldr+'haarcascade_frontalface_alt2.xml')
# face_cascade = cv2.CascadeClassifier(datafldr+'haarcascade_frontalcatface.xml')
cap = cv2.VideoCapture(0)

#
# specify H-Bridge control pins
goL = 23 #23 or 17
dirL = 24 #24 or 27
goR = 17 #17 or 23   # Pin 5 goes HIGH
dirR = 27 #27 or 24  # Pin 6 goes HIGH
#
# create Motor classes with independent control pins & enable speed control if desired
motorLeft = PhaseEnableMotor(dirL,goL,pwm=True)
motorRight = PhaseEnableMotor(dirR,goR,pwm=True)
#

while (True):
    stop() # Stop the motors
    # Capture frame by frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.7, minNeighbors=5)
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
#
# Send this to web server?
#        img_item = "myface.png"
#        cv2.imwrite(img_item, roi_gray)
#
        color = (255,255,255) # BGR
        stroke = 4 # line thickness
        end_x = x+w
        end_y = y+h
        cv2.rectangle(frame,(x,y),(end_x,end_y),color,stroke)
        
#        cwSpin()
#        sleep(0.25)
#        ccwSpin()
#        sleep(0.25)

        lmf(0.5) # Move toward the human
        rmf(0.5)

    # Display the resulting frame
    cv2.imshow('Where Is The Human?',frame)
    
    # Press 'Q' to quit
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
