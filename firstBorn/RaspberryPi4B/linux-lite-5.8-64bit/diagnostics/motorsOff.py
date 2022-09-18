from gpiozero import OutputDevice
#
# Turn off all propulsion outputs to prevent unwanted movement during boot
# NOTE: This may not work because bootup takes quite some time
# The motor in question runs for almost a full minute before this script
# shuts it down.
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
stop()