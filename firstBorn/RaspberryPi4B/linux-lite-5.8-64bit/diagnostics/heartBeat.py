from gpiozero import Button
#from gpiozero import DigitalInputDevice
from gpiozero import RGBLED
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep
import random
#
quiet = Button(12,pull_up=True)
#quiet = DigitalInputDevice(12,pull_up=True)
#
bzr = TonalBuzzer(16)
#
led = RGBLED(17,27,22)
# LED(##) = GPIO ##
#red = PWMLED(17)
#green = PWMLED(27)
#blue = PWMLED(22)
#
thislong = 0.1
#
def beepbeep():
    bzr.play(bzr.max_tone)
    sleep(thislong)
    bzr.stop()
    sleep(thislong)
    bzr.play(bzr.max_tone)
    sleep(thislong)
    bzr.stop()
#
while True:
    maxred = random.random()
    maxgrn = random.random()
    maxblu = random.random()
    print(f"r={maxred}|g={maxgrn}|b={maxblu}")
    if not quiet.is_pressed:
#    if not quiet.value:
        beepbeep()
    led.pulse(fade_in_time=2,fade_out_time=2,on_color=(maxred,maxgrn,maxblu),n=1,background=False)
#