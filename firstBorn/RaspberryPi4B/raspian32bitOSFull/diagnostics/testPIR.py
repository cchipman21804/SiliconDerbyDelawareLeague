#from gpiozero import DigitalInputDevice
from gpiozero import MotionSensor
#
pir = MotionSensor(12)
#
while True:
    if pir.motion_detected:
        print("SOMETHING MOVED!!!")
