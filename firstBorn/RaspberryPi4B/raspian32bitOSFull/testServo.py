# Servo Test
from gpiozero import Servo
from time import sleep

servo = Servo(4)

while True:
    servo.min()
    print("Looking Right")
    sleep(1)
    servo.mid()
    print("Looking Straight")
    sleep(1)
    servo.max()
    print("Looking Left")
    sleep(1)
    servo.mid()
    print("Looking Straight")
    sleep(1)
