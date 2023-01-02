'''
This script adds 2 new statically assigned Devices to a Site in Netbox

'''
import requests

devicesBody = [{ "name": "Test Router 1", "device_type": 1, "device_role": 1, "tenant": 5, "site": 13 },
{ "name": "Test Router 2", "device_type": 1, "device_role": 1, "tenant": 5, "site": 13 }]

url = 'http://192.168.0.16:8080/api/dcim/devices/'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 0123456789abcdef0123456789abcdef01234567'
}

for deviceBody in devicesBody:

    response = requests.post(url, headers=headers, json=deviceBody, verify=False)

    if response.status_code == 201:
        print(" - Success, the below item was added:")
        output = response.json()
        print(output)
    else:
        print(" FAILED with error code", response.status_code)
        output = response.json()
        print(output)   