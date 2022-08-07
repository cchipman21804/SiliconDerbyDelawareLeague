from gpiozero import OutputDevice
#
# This Python script will test the H-bridge and any connected DC motors
#
pgmName = 'motorTest2'
#
# specify H-Bridge control pins
goL = 23 #23 or 5
dirL = 24 #24 or 6
goR = 5 #5 or 23
dirR = 6 #6 or 24
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
    # Stop both motors
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
    motorLeftSpd.on()  # on() = Full Speed
    motorRightSpd.on() # on() = Full Speed
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

