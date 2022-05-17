from gpiozero import Motor
# https://gpiozero.readthedocs.io/en/stable/api_output.html#motor
#
from time import sleep
#
# This Python script will test the H-bridge and any connected DC motors
#
# specify H-Bridge control pins
fwdL = 17 #23
revL = 27 #24
goL = None #22 # optional enable pin
fwdR = 23 #17
revR = 24 #27
goR = None #25 # optional enable pin
#
# create Motor classes with independent control pins & enable speed control if desired
motorLeft = Motor(fwdL,revL,None,pwm=True)
motorRight = Motor(fwdR,revR,None,pwm=True)
#
# Define the directional control functions
#
v=1
def stop():
    # Stop both motors
    motorLeft.stop()
    motorRight.stop()
#
# Specifying a value for v between 0 & 1 will control the motors' speed
def straightFwd():
    # Run both motors forward
#    if v == None: v = 1
    motorLeft.forward(speed=v)
    motorRight.forward(speed=v)
#
def straightRev():
    # Run both motors in reverse
#    if v == None: v = 1
    motorLeft.backward(speed=v)
    motorRight.backward(speed=v)
#
def fwdLeft():
    # Run right motor forward
#    if v == None: v = 1
    motorRight.forward(speed=v)
#
def fwdRight():
    # Run left motor forward
#    if v == None: v = 1
    motorLeft.forward(speed=v)
#
def revLeft():
    # Run right motor forward
#    if v == None: v = 1
    motorRight.backward(speed=v)
#
def revRight():
    # Run left motor forward
#    if v == None: v = 1
    motorLeft.backward(speed=v)
#
def cwSpin():
    # Run left motor forward
    # Run right motor backward
#    if v == None: v = 1
    motorLeft.forward(speed=v)
    motorRight.backward(speed=v)
#
def ccwSpin():
    # Run left motor forward
    # Run right motor backward
#    if v == None: v = 1
    motorLeft.backward(speed=v)
    motorRight.forward(speed=v)
#
# Test the motors & H-Bridge
# Run various control tests until poweroff
while True:
    stop()
    print("STOPPED")
    sleep(1)
    print("STRAIGHT FORWARD")
    straightFwd()
    sleep(1)
    stop()
    print("STOPPED")
    sleep(1)
    print("STRAIGHT REVERSE")
    straightRev()
    sleep(1)
    stop()
    print("STOPPED")
    sleep(1)
    print("FORWARD LEFT")
    fwdLeft()
    sleep(1)
    stop()
    print("STOPPED")
    sleep(1)
    print("FORWARD RIGHT")
    fwdRight()
    sleep(1)
    stop()
    print("STOPPED")
    sleep(1)
    print("REVERSE LEFT")
    revLeft()
    sleep(1)
    stop()
    print("STOPPED")
    sleep(1)
    print("REVERSE RIGHT")
    revRight()
    sleep(1)
    stop()
    print("STOPPED")
    sleep(1)
    print("CW SPIN")
    cwSpin()
    sleep(1)
    stop()
    print("STOPPED")
    sleep(1)
    print("CCW SPIN")
    ccwSpin()
    sleep(1)
    stop()
    print("STOPPED")
    sleep(1)
    print("\n ******************** STARTING OVER ******************** \n")
