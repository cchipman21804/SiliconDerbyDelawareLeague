from gpiozero import PhaseEnableMotor,Servo
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
pgmName = 'control_v1.1'
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
#
# specify H-Bridge control pins
goL = 23 #23 or 17
dirL = 24 #24 or 27
goR = 17 #17 or 23   # Pin 5 goes HIGH
dirR = 27 #27 or 24  # Pin 6 goes HIGH
#
# create Motor classes with independent control pins & enable speed control if desired
motorLeft = PhaseEnableMotor(dirL,goL,pwm=False)
motorRight = PhaseEnableMotor(dirR,goR,pwm=False)
#
# hard-coded values for min & max pulse width are suitable for the
# Parallex Standard Servo (#900-00005) 180 degree movement connected to GPIO pin 4
servo = Servo(4,min_pulse_width=0.75/1000,max_pulse_width=2.25/1000)
#
class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_up_arrow_press(self):
        print(f"[{pgmName}]> {upArwPrsMsg}")
        lmf()

    def on_triangle_press(self):
        print(f"[{pgmName}]> {trianglePrsMsg}")
        rmf()

    def on_down_arrow_press(self):
        print(f"[{pgmName}]> {dwnArwPrsMsg}")
        lmb()

    def on_x_press(self):
        print(f"[{pgmName}]> {xPrsMsg}")
        rmb()

    def on_up_down_arrow_release(self):
        print(f"[{pgmName}]> {upDwnArwRlsMsg}")
        stop()

    def on_x_release(self):
        print(f"[{pgmName}]> {xRlsMsg}")
        stop()

    def on_triangle_release(self):
        print(f"[{pgmName}]> {triangleRlsMsg}")
        stop()

#    def on_L3_x_at_rest(self):
    def on_square_press(self):
        print(f"[{pgmName}]> {sqrPrsMsg}")
        servo.max()

#    def on_L3_left(self):
    def on_square_release(self):
        print(f"[{pgmName}]> {sqrRlsMsg}")
        servo.mid()

    def on_circle_release(self):
        print(f"[{pgmName}]> {crclRlsMsg}")
        servo.mid()

#    def on_L3_right(self):
    def on_circle_press(self):
        print(f"[{pgmName}]> {crclPrsMsg}")
        servo.min()

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen(on_connect=connect, on_disconnect=disconnect)
#
