#
# Current controls:
#
# Up Arrow --------- Left Motor Forward Full Speed
# Down Arrow ------- Left Motor Backward Full Speed
# Triangle Button -- Right Motor Forward Full Speed
# X Button --------- Right Motor Backward Full Speed
#
# L2 --------------- Left Motor Forward Speed Control
# R2 --------------- Right Motor Forward Speed Control
#
# L3 (Y-axis) ------ Left Motor Direction & Speed Control
# R3 (Y-axis) ------ Right Motor Direction & Speed Control
#
import datetime as dt # Generates timestamps for log
from gpiozero import PhaseEnableMotor
from pyPS4Controller.controller import Controller
import os # Retrieves list of input devices (including joysticks)
#
# Define controller connection & disconnection routines
#
def connect():
    stop()
    #pass
#
def disconnect():
    stop()
    #pass
#
# Define the command motor control functions
#
def stop():
    # Stop both motors
    motorLeft.stop()
    motorRight.stop()
#
# Specifying a value for v between 0 & 1 will control the motors' speed
def straightFwd():
    # Run both motors forward
    motorLeft.forward() # 1 = Full Speed
    motorRight.forward() # 1 = Full Speed
#
def straightRev():
    # Run both motors in reverse
    motorLeft.backward() # 1 = Full Speed
    motorRight.backward() # 1 = Full Speed
#
def fwdLeft():
    # Run right motor forward
#    motorLeft.stop() # vl) # 0 = Stopped
    motorRight.forward()
#
def fwdRight():
    # Run left motor forward
    motorLeft.forward()
#    motorRight.stop() # vr) # 0 = Stopped
#
def revLeft():
    # Run right motor forward
#    motorLeft.stop() # vl) # 0 = Stopped
    motorRight.backward()
#
def revRight():
    # Run left motor forward
    motorLeft.backward()
#    motorRight.stop() # vr) # 0 = Stopped
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
#
# This Python script will send commands to the H-bridge and any connected DC motors
# based on input from a PS4 controller
#
pgmName = 'control_v1.0'
upArwPrsMsg = 'Left Motor Forward'
trianglePrsMsg = 'Right Motor Forward'
dwnArwPrsMsg = 'Left Motor Reverse'
xPrsMsg = 'Right Motor Reverse'
upDwnArwRlsMsg = 'Left Motor Stop'
xRlsMsg = 'Right Motor Stop'
triangleRlsMsg = xRlsMsg
sqrPrsMsg = 'Look Left'
sqrRlsMsg = 'Look Straight Ahead'
crclPrsMsg = 'Look Right'
crclRlsMsg = sqrRlsMsg
L2RlsMsg = 'L2 Released'
R2RlsMsg = 'R2 Released'
L3JoyCntrMsg = 'L3 joystick centered'
R3JoyCntrMsg = 'R3 joystick centered'
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
class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_up_arrow_press(self):
        print(f"[{pgmName}] [{dt.datetime.now().strftime('%a %b %d %Y @%H:%M:%S.%f')}]> [{upArwPrsMsg}]")
        lmf(1.0)

    def on_triangle_press(self):
        print(f"[{pgmName}] [{dt.datetime.now().strftime('%a %b %d %Y @%H:%M:%S.%f')}]> [{trianglePrsMsg}]")
        rmf(1.0)

    def on_down_arrow_press(self):
        print(f"[{pgmName}] [{dt.datetime.now().strftime('%a %b %d %Y @%H:%M:%S.%f')}]> [{dwnArwPrsMsg}]")
        lmb(1.0)

    def on_x_press(self):
        print(f"[{pgmName}] [{dt.datetime.now().strftime('%a %b %d %Y @%H:%M:%S.%f')}]> [{xPrsMsg}]")
        rmb(1.0)

    def on_up_down_arrow_release(self):
        print(f"[{pgmName}] [{dt.datetime.now().strftime('%a %b %d %Y @%H:%M:%S.%f')}]> [{upDwnArwRlsMsg}]")
        stop()

    def on_x_release(self):
        print(f"[{pgmName}] [{dt.datetime.now().strftime('%a %b %d %Y @%H:%M:%S.%f')}]> [{xRlsMsg}]")
        stop()

    def on_triangle_release(self):
        print(f"[{pgmName}] [{dt.datetime.now().strftime('%a %b %d %Y @%H:%M:%S.%f')}]> [{triangleRlsMsg}]")
        stop()

    def on_L2_press(self,name):
        speed=(name+32768)/65535
        print(f"[{pgmName}] [{dt.datetime.now().strftime('%a %b %d %Y @%H:%M:%S.%f')}]> [Left Motor Speed: {speed:.2%}]")
        lmf(speed)

    def on_L2_release(self):
        print(f"[{pgmName}] [{dt.datetime.now().strftime('%a %b %d %Y @%H:%M:%S.%f')}]> [{L2RlsMsg}]")
        stop()

    def on_R2_press(self,name):
        speed=((name+32768)/65535)
        print(f"[{pgmName}] [{dt.datetime.now().strftime('%a %b %d %Y @%H:%M:%S.%f')}]> [Right Motor Speed: {speed:.2%}]")
        rmf(speed)

    def on_R2_release(self):
        print(f"[{pgmName}] [{dt.datetime.now().strftime('%a %b %d %Y @%H:%M:%S.%f')}]> [{R2RlsMsg}]")
        stop()

    def on_L3_y_at_rest(self):
        print(f"[{pgmName}] [{dt.datetime.now().strftime('%a %b %d %Y @%H:%M:%S.%f')}]> [{L3JoyCntrMsg}]")
        stop()

    def on_L3_up(self,name):
        print(f"[{pgmName}] [{dt.datetime.now().strftime('%a %b %d %Y @%H:%M:%S.%f')}]> [Left Motor Forward Speed: {abs(name)/32767}]")
        lmf(abs(name)/32767)

    def on_L3_down(self,name):
        print(f"[{pgmName}] [{dt.datetime.now().strftime('%a %b %d %Y @%H:%M:%S.%f')}]> [Left Motor Reverse Speed: {name/32767}]")
        lmb(name/32767)

    def on_R3_up(self,name):
        print(f"[{pgmName}] [{dt.datetime.now().strftime('%a %b %d %Y @%H:%M:%S.%f')}]> [Right Motor Forward Speed: {abs(name)/32767}]")
        rmf(abs(name)/32767)

    def on_R3_down(self,name):
        print(f"[{pgmName}] [{dt.datetime.now().strftime('%a %b %d %Y @%H:%M:%S.%f')}]> [Right Motor Reverse Speed: {name/32767}]")
        rmb(name/32767)

    def on_R3_y_at_rest(self):
        print(f"[{pgmName}] [{dt.datetime.now().strftime('%a %b %d %Y @%H:%M:%S.%f')}]> [{R3JoyCntrMsg}]")
        stop()
#
# Find all input devices
inputDevices = os.listdir('/dev/input')
#print(f"All Input Devices: {inputDevices}")
#
# Initialize list of joysticks
joysticks = []
for device in inputDevices:
    if 'js' in device:
        joysticks.append(device) # Add joystick devices to list of joysticks
#print(f"Joysticks: {joysticks}")
#
# Extract numerals from device names
for n,js in enumerate(joysticks):
    joysticks[n] = int(js[-1])
#print(f"Joysticks: {joysticks}")
#
# Use the joystick device with the highest number
thisone = "/dev/input/js" + str(max(joysticks))
#
controller = MyController(interface=thisone, connecting_using_ds4drv=False)
controller.debug = False
controller.listen(on_connect=connect, on_disconnect=disconnect)
#