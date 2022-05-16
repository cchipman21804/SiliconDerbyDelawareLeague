from gpiozero import Motor
# https://gpiozero.readthedocs.io/en/stable/api_output.html#motor
#from datetime import datetime, timedelta
from time import sleep
#
# This Python script will test the H-bridge and any connected DC motors
#
# specify H-Bridge control pins
fwdL = 0 #10
revL = 5 #9
goL = None #11 # optional enable pin
fwdR = 10 #0
revR = 9 #5
goR = None #6 # optional enable pin
#
# create Motor class
motorLeft = Motor(fwdL,revL)
motorRight = Motor(fwdR,revR)
#
# test the motor & H-Bridge
#
def stop():
    # Stop both motors
    motorLeft.stop()
    motorRight.stop()
    sleep(1)
#
def straightFwd():
    # Run both motors forward
    motorLeft.forward()
    motorRight.forward()
#    sleep(1)
def straightRev():
    # Run both motors in reverse
    motorLeft.reverse()
    motorRight.reverse()
#    sleep(1)
#
# Run forward for 1 second
stop() # Stops motors for 1 second
straightFwd()
sleep(1)
stop() # Stops motors for 1 second
#
# Run in reverse for 1 second
straightRev()
sleep(1)
stop() # Stops motors for 1 second
