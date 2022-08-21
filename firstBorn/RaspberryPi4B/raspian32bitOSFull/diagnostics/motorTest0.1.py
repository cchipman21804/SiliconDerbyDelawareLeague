from gpiozero import OutputDevice
from time import sleep
#
# This Python script will test the H-bridge and any connected DC motors
#
# This uses the OutputDevice module to independently control motor direction and motor activation
#
pgmName = 'motorTest v0.1'
#
# specify H-Bridge control pins
goL = 17 #23 or 17
dirL = 27 #24 or 27
goR = 23 #17 or 23   # Pin 5 goes HIGH
dirR = 24 #27 or 24  # Pin 6 goes HIGH
#
# create Motor classes with independent control pins & enable speed control if desired
motorLeftSpd = OutputDevice(goL)
motorLeftDir = OutputDevice(dirL)
motorRightSpd = OutputDevice(goR)
motorRightDir = OutputDevice(dirR)
#
# Define the directional control functions
#
def stop():
    # Stop both motors (motor direction is irrelevant)
    motorLeftSpd.off()
    motorRightSpd.off()
#
def straightFwd():
    # Set both motor directions to forward
    motorLeftDir.on()  # on() = forward, off() = reverse
    motorRightDir.on() # on() = forward, off() = reverse
    # Activate motors
    motorLeftSpd.on()  # on() = Full Speed
    motorRightSpd.on() # on() = Full Speed
#
def straightRev():
    # Run both motors in reverse
    motorLeftDir.off()  # on() = forward, off() = reverse
    motorRightDir.off() # on() = forward, off() = reverse
    # Activate motors
    motorLeftSpd.on()  # on() = Full Speed, off() = Full Stop
    motorRightSpd.on() # on() = Full Speed, off() = Full Stop
#
def fwdLeft():
    # Run right motor forward only
    motorRightDir.on()   # on() = forward, off() = reverse
    # Activate motors
    motorRightSpd.on()   # on() = Full Speed, off() = Full Stop
    motorLeftSpd.off()   # on() = Full Speed, off() = Full Stop
#
def fwdRight():
    # Run left motor forward only
    motorLeftDir.on()   # on() = forward, off() = reverse
    # Activate motors
    motorLeftSpd.on()   # on() = Full Speed, off() = Full Stop
    motorRightSpd.off() # on() = Full Speed, off() = Full Stop
#
def revLeft():
    # Run right motor reverse only
    motorRightDir.off() # on() = forward, off() = reverse
    # Activate motors
    motorLeftSpd.off()  # on() = Full Speed, off() = Full Stop
    motorRightSpd.on()  # on() = Full Speed, off() = Full Stop
#
def revRight():
    # Run left motor reverse only
    motorLeftDir.off()  # on() = forward, off() = reverse
    # Activate motors
    motorLeftSpd.on()   # on() = Full Speed, off() = Full Stop
    motorRightSpd.off() # on() = Full Speed, off() = Full Stop
#
def cwSpin():
    # Run left motor forward
    # Run right motor backward
    motorLeftDir.on()   # on() = forward, off() = reverse
    motorRightDir.off() # on() = forward, off() = reverse
    # Activate motors
    motorLeftSpd.on()   # on() = Full Speed, off() = Full Stop
    motorRightSpd.on()  # on() = Full Speed, off() = Full Stop
#
def ccwSpin():
    # Run left motor backward
    # Run right motor forward
    motorLeftDir.off()   # on() = forward, off() = reverse
    motorRightDir.on() # on() = forward, off() = reverse
    # Activate motors
    motorLeftSpd.on()   # on() = Full Speed, off() = Full Stop
    motorRightSpd.on()  # on() = Full Speed, off() = Full Stop
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
