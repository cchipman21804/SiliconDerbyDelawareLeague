from multiprocessing import Process
import os
#
# Start processes
def e(cmd):
    os.system(cmd)
#
def main():
# specify folders
    rootfldr = '/home/pi/SiliconDerbyDelawareLeague/firstBorn/RaspberryPi4B/raspian32bitOSFull/'
    diagfldr = 'diagnostics/'
    pyfldr = 'py/'
    pgmName = 'autostart'
#
# specify Python scripts
    script = [
              'test_OLED_display.py',
              'video-stream.py'
             ]
#
# execute multiple Python scripts
# os.system(f"python3 {rootfldr}{diagfldr}{script[0]} & python3 {rootfldr}{pyfldr}{script[1]} & python3 {rootfldr}{pyfldr}{script[2]}")
#
    cmdstr = f"python3 {rootfldr}{diagfldr}{script[0]}"
    p1 = Process(target=e, args=(cmdstr,))
    p1.start()
    
#    cmdstr = f"python3 {rootfldr}{pyfldr}{script[1]}"
#    p2 = Process(target=e, args=(cmdstr,))
#    p2.start()
    
#    cmdstr = f"python3 {rootfldr}{pyfldr}{script[2]}"
#    p3 = Process(target=control)
#    p3.start()
    
    p1.join()
#    p2.join()
#    p3.join()
#
if __name__ == '__main__':
    main()
