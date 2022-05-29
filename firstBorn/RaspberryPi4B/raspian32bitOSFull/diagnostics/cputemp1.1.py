# This is used to display the current CPU temperature on a PHP webpage
from gpiozero import CPUTemperature
tc = CPUTemperature().temperature
tf = str(round((9/5*tc+32),1)) # Convert to degF
while len(tf) < 6:
    tf = ' ' + tf
print(f"{tf} F")
#
# Write the string value to a text file in the /tmp folder
# for use by the PHP webpage
#with open('/tmp/cputemp','w') as t:
#     t.write(str(tf))
