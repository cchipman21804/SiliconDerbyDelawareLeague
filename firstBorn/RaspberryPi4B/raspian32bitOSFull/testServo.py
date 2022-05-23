# Servo Test
from gpiozero import Servo
from time import sleep

servo = Servo(4,min_pulse_width=0.75/1000,max_pulse_width=2.25/1000)

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
