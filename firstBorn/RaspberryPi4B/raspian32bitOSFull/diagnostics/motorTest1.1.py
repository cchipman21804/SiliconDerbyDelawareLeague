from gpiozero import OutputDevice
#
# This Python script will test the H-bridge and any connected DC motors
#
# This uses the OutputDevice module to independently control motor direction and motor activation
# PhaseEnableMotor module did not perform this function satisfactorily
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

