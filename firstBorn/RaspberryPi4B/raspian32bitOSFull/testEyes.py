from gpiozero import Button
#from gpiozero import LightSensor
#
leftEye = Button(19,pull_up=True)
#centerEye
#rightEye
#
while True:
    print(leftEye.value)