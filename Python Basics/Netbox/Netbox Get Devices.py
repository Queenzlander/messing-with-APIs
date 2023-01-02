'''
This script retuns a list of Devices
'''
import requests
import json

payload = {}
url = 'http://192.168.0.16:8080/api/dcim/devices'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 0123456789abcdef0123456789abcdef01234567',
}

response = requests.request("GET", url, headers=headers, data = payload)

devices = response.json()
for device in devices['results']:
    print(device)
    # deviceName = site['name']
    # deviceCount = site['device_count']
    # print(" Site called {0} has {1} devices".format(deviceName, deviceCount))
