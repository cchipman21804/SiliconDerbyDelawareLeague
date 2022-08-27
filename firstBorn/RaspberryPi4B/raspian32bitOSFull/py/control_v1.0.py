from gpiozero import PhaseEnableMotor
from pyPS4Controller.controller import Controller
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
# Define the directional control functions
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
    motorLeft.stop() # vl) # 0 = Stopped
    motorRight.forward()
#
def fwdRight():
    # Run left motor forward
    motorLeft.forward()
    motorRight.stop() # vr) # 0 = Stopped
#
def revLeft():
    # Run right motor forward
    motorLeft.stop() # vl) # 0 = Stopped
    motorRight.backward()
#
def revRight():
    # Run left motor forward
    motorLeft.backward()
    motorRight.stop() # vr) # 0 = Stopped
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
def lmf():
    motorLeft.forward()
#
def lmb():
    motorLeft.backward()
#
def rmf():
    motorRight.forward()
#
def rmb():
    motorRight.backward()
#
# This Python script will send commands to the H-bridge and any connected DC motors
# based on input from a PS4 controller
#
pgmname = 'control_v1.0'
#
# specify H-Bridge control pins
goL = 17 #23 or 17
dirL = 27 #24 or 27
goR = 23 #17 or 23   # Pin 5 goes HIGH
dirR = 24 #27 or 24  # Pin 6 goes HIGH
#
# create Motor classes with independent control pins & enable speed control if desired
motorLeft = PhaseEnableMotor(dirL,goL,pwm=False)
motorRight = PhaseEnableMotor(dirR,goR,pwm=False)
#
class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_up_arrow_press(self):
        print(f"[{pgmname}]> Left Motor Forward")
        lmf()

    def on_triangle_press(self):
        print(f"[{pgmname}]> Right Motor Forward")
        rmf()

    def on_down_arrow_press(self):
        print(f"[{pgmname}]> Left Motor Reverse")
        lmb()

    def on_x_press(self):
        print(f"[{pgmname}]> Right Motor Reverse")
        rmb()

    def on_up_down_arrow_release(self):
        print(f"[{pgmname}]> Left Motor Stop")
        stop()

    def on_x_release(self):
        print(f"[{pgmname}]> Right Motor Stop")
        stop()

    def on_triangle_release(self):
        print(f"[{pgmname}]> Right Motor Stop")
        stop()

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen(on_connect=connect, on_disconnect=disconnect)
#
