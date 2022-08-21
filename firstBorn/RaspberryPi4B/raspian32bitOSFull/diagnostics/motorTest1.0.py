from gpiozero import PhaseEnableMotor
# https://gpiozero.readthedocs.io/en/stable/api_output.html#motor
#
from time import sleep
#
# This Python script will test the H-bridge and any connected DC motors
#
pgmName = 'motorTest v1.0'
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
# Define the motor speeds
#lSpd = 1.0
#lSpd = 0.25
#rSpd = 1.0
#rSpd = 0.25
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
# Test the motors & H-Bridge
# Run various control tests until poweroff
while True:
    stop()
    print(f"[{pgmName}]> STOPPED")
    sleep(1)
    print(f"[{pgmName}]> STRAIGHT FORWARD")
    straightFwd()
    sleep(1)
    stop()
    print(f"[{pgmName}]> STOPPED")
    sleep(1)
    print(f"[{pgmName}]> STRAIGHT REVERSE")
    straightRev()
    sleep(1)
    stop()
    print(f"[{pgmName}]> STOPPED")
    sleep(1)
    print(f"[{pgmName}]> FORWARD LEFT")
    fwdLeft()
    sleep(1)
    stop()
    print(f"[{pgmName}]> STOPPED")
    sleep(1)
    print(f"[{pgmName}]> FORWARD RIGHT")
    fwdRight()
    sleep(1)
    stop()
    print(f"[{pgmName}]> STOPPED")
    sleep(1)
    print(f"[{pgmName}]> REVERSE LEFT")
    revLeft()
    sleep(1)
    stop()
    print(f"[{pgmName}]> STOPPED")
    sleep(1)
    print(f"[{pgmName}]> REVERSE RIGHT")
    revRight()
    sleep(1)
    stop()
    print(f"[{pgmName}]> STOPPED")
    sleep(1)
    print(f"[{pgmName}]> CW SPIN")
    cwSpin()
    sleep(1)
    stop()
    print(f"[{pgmName}]> STOPPED")
    sleep(1)
    print(f"[{pgmName}]> CCW SPIN")
    ccwSpin()
    sleep(1)
    stop()
    print(f"[{pgmName}]> STOPPED")
    sleep(1)
    print(f"[{pgmName}]> ******************** STARTING OVER ******************** ")
