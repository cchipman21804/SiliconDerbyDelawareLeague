import cv2
import numpy as np
#import os

#print(os.listdir())

# Raspberry Pi path for OpenCV data:
#/usr/local/lib/python3.9/dist-packages/cv2/data/
datafldr='/usr/local/lib/python3.9/dist-packages/cv2/data/'
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
face_cascade = cv2.CascadeClassifier(datafldr+'haarcascade_frontalcatface.xml')
cap = cv2.VideoCapture(0)

while (True):
    # CApture frame by frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        img_item = "myface.png"
        cv2.imwrite(img_item, roi_gray)

        color = (0,0,255) # BGR
        stroke = 4 # line thickness
        end_x = x+w
        end_y = y+h
        cv2.rectangle(frame,(x,y),(end_x,end_y),color,stroke)
        
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
