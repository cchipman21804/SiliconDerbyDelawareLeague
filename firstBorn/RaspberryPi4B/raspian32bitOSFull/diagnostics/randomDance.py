from gpiozero import Motor
# https://gpiozero.readthedocs.io/en/stable/api_output.html#motor
#
import random
from time import sleep
#
# This Python script will perform a random dance by sending
# random commands to the H-bridge and any connected DC motors
#
# specify H-Bridge control pins
fwdL = 5 #23
revL = 6 #24
goL = None #13 # optional enable pin
fwdR = 23 #5
revR = 24 #6
goR = None #25 # optional enable pin
#
# create Motor classes with independent control pins & enable speed control if desired
motorLeft = Motor(fwdL,revL,None,pwm=True)
motorRight = Motor(fwdR,revR,None,pwm=True)
#
# Define the motor speeds
lSpd = 1
rSpd = 1
#
# Define the directional control functions
#
def stop():
    # Stop both motors
    motorLeft.stop()
    motorRight.stop()
#
# Specifying a value for v between 0 & 1 will control the motors' speed
def straightFwd(vl,vr):
    # Run both motors forward
    motorLeft.forward(speed=vl) # 1 = Full Speed
    motorRight.forward(speed=vr) # 1 = Full Speed
#
def straightRev(vl,vr):
    # Run both motors in reverse
    motorLeft.backward(speed=vl) # 1 = Full Speed
    motorRight.backward(speed=vr) # 1 = Full Speed
#
def fwdLeft(vl,vr):
    # Run right motor forward
    motorLeft.forward(speed=0) # vl) # 0 = Stopped
    motorRight.forward(speed=vr)
#
def fwdRight(vl,vr):
    # Run left motor forward
    motorLeft.forward(speed=vl)
    motorRight.forward(speed=0) # vr) # 0 = Stopped
#
def revLeft(vl,vr):
    # Run right motor forward
    motorLeft.backward(speed=0) # vl) # 0 = Stopped
    motorRight.backward(speed=vr)
#
def revRight(vl,vr):
    # Run left motor forward
    motorLeft.backward(speed=vl)
    motorRight.backward(speed=0) # vr) # 0 = Stopped
#
def cwSpin(vl,vr):
    # Run left motor forward
    # Run right motor backward
    motorLeft.forward(speed=vl)
    motorRight.backward(speed=vr)
#
def ccwSpin(vl,vr):
    # Run left motor forward
    # Run right motor backward
    motorLeft.backward(speed=vl)
    motorRight.forward(speed=vr)
#
# Test the motors & H-Bridge
# Run various control tests until poweroff
while True:
    move = random.randint(0,8)
    if move == 0:
        stop()
        print("STOPPED")
        sleep(1)
    elif move == 1:
        print("STRAIGHT FORWARD")
        straightFwd(lSpd,rSpd)
        sleep(1)
        stop()
        print("STOPPED")
        sleep(1)
    elif move == 2:
        print("STRAIGHT REVERSE")
        straightRev(lSpd,rSpd)
        sleep(1)
        stop()
        print("STOPPED")
        sleep(1)
    elif move == 3:
        print("FORWARD LEFT")
        fwdLeft(lSpd,rSpd)
        sleep(1)
        stop()
        print("STOPPED")
        sleep(1)
    elif move == 4:
        print("FORWARD RIGHT")
        fwdRight(lSpd,rSpd)
        sleep(1)
        stop()
        print("STOPPED")
        sleep(1)
    elif move == 5:
        print("REVERSE LEFT")
        revLeft(lSpd,rSpd)
        sleep(1)
        stop()
        print("STOPPED")
        sleep(1)
    elif move == 6:
        print("REVERSE RIGHT")
        revRight(lSpd,rSpd)
        sleep(1)
        stop()
        print("STOPPED")
        sleep(1)
    elif move == 7:
        print("CW SPIN")
        cwSpin(lSpd,rSpd)
        sleep(1)
        stop()
        print("STOPPED")
        sleep(1)
    elif move == 8:
        print("CCW SPIN")
        ccwSpin(lSpd,rSpd)
        sleep(1)
        stop()
        print("STOPPED")
        sleep(1)
    else:
        print("ERROR")
#    print("\n ******************** STARTING OVER ******************** \n")
