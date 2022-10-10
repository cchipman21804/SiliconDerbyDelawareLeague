# Display video stream
import cv2

stream = cv2.VideoCapture(0)

if not stream.isOpened():
    exit("No stream")

while True:
    ret, frame = stream.read()
    if not ret:
        print("No more stream")
        break
        
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
stream.release()
cv2.destroyAllWindows()
