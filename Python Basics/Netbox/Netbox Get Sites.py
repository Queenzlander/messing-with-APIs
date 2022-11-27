'''
This script retuns a list of Sites and number of devices within the Site 
'''
import requests
import json

payload = {}
url = 'http://192.168.0.16:8080/api/dcim/sites'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 0123456789abcdef0123456789abcdef01234567',
}

response = requests.request("GET", url, headers=headers, data = payload)

sites = response.json()
for site in sites['results']:
    deviceName = site['name']
    deviceCount = site['device_count']
    print(" Site called {0} has {1} devices".format(deviceName, deviceCount))
