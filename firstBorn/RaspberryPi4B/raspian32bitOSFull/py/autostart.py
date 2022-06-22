import os
#
# specify folders
rootfldr = '/home/pi/SiliconDerbyDelawareLeague/firstBorn/RaspberryPi4B/raspian32bitOSFull'
diagfldr = '/diagnostics'
pyfldr = '/py'
#
# execute Python scripts
os.system(f"python3 {diagfldr}/test_OLED_display.py & python3 {pyfldr}/video-stream.py") # & python3 /var/www/html/wifi-car.py & python3 /var/www/html/system-status.py & python3 /var/www/html/tether.py")
