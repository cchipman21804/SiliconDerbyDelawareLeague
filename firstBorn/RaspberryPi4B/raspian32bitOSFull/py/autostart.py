import os
#
# specify folders
rootfldr = '/home/pi/SiliconDerbyDelawareLeague/firstBorn/RaspberryPi4B/raspian32bitOSFull/'
diagfldr = 'diagnostics/'
pyfldr = 'py/'
#
# specify Python scripts
script = [
          'test_OLED_display.py',
          'video-stream.py',
         # 'heartBeat.py',
          'randomDance.py'
         ]
#
# execute multiple Python scripts
os.system(f"python3 {rootfldr}{diagfldr}{script[0]} & python3 {rootfldr}{pyfldr}{script[1]} & python3 {rootfldr}{diagfldr}{script[2]}") # & python3 /var/www/html/wifi-car.py & python3 /var/www/html/system-status.py & python3 /var/www/html/tether.py")
