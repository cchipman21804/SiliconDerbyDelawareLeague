from gpiozero import RGBLED
import random
#from signal import pause
#from time import sleep

led = RGBLED(17,27,22)
# LED(##) = GPIO ##
#red = PWMLED(17)
#green = PWMLED(27)
#blue = PWMLED(22)

#thislong = 0.01

while True:
    maxred = random.random()
    maxgrn = random.random()
    maxblu = random.random()
    print(f"r={maxred}|g={maxgrn}|b={maxblu}")
    led.pulse(fade_in_time=2,fade_out_time=2,on_color=(maxred,maxgrn,maxblu),n=1,background=False)
#    print(f"r={maxred}")
#
# Increase brightness
#    for r in range(int(maxred * 255)):
#        redlevel = r / 255
#        red.value = redlevel
#        sleep(thislong)
#
# Dim
#    for r in range(int(maxred * 255),0,-1):
#        redlevel = r / 255
#        red.value = redlevel
#        sleep(thislong)
#pause()
