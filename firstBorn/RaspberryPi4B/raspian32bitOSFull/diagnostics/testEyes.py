import json
#import os
import requests
from time import sleep
#
# Retrieve sensor data
url = 'http://192.168.1.177:8080'
#
reqHeader = {
    "Content-Type": "text/html;charset=UTF-8"
    }
payload = None
#
# Read Arduino sensors repeatedly
while True:
#    print("Retrieving JSON data from Arduino sensors...")
#
    result = requests.get(url, data = payload, headers = reqHeader, timeout = 3)
    status = result.status_code
#
# Successful result?
    if (status != 200):
        exit('\nUnsuccessful connection\n')
#
# Create dictionary from JSON result data
    jsonresult = json.loads(result.text)
#
#
# Count the number of records available for processing
    try:
        numRecords = len(jsonresult.get('sensors'))
    except TypeError:
        numRecords = 0
        exit(f'\nReturned Result:\n\n{result.text}\n')
#
# sensor dictionaries
    sensorValues = jsonresult.get('sensors')[0]
    values = sensorValues.get('values')
    sensorUnits = jsonresult.get('sensors')[1]
    units = sensorUnits = sensorUnits.get('units')
#
# sensor data
    temp = values.get('ambient_temp')
    tempUnit = units.get('ambient_temp')
    leftEye = values.get('left_eye')
    centerEye = values.get('center_eye')
    rightEye = values.get('right_eye')
    lightUnit = units.get('left_eye')
    occ = values.get('occupancy')
#
    print(f"| Temp: {temp} {tempUnit} | Left: {leftEye}{lightUnit} | Center: {centerEye}{lightUnit} | Right: {rightEye}{lightUnit} | Occupied: {occ} |")
    sleep(5)
#
