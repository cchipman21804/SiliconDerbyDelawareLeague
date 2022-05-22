from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep
#
b = TonalBuzzer(16)
#
b.play(b.max_tone)
sleep(0.1)
b.stop()