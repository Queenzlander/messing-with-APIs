'''
This script adds IP Addresses to Netbox

'''
import requests

ipaddrsBody = [{ "address": "10.45.2.1/32", "tenant": 5, "role": 'loopback' },
{ "address": "10.45.2.2/32", "tenant": 5, "role": 'loopback' }]

url = 'http://192.168.0.16:8080/api/ipam/ip-addresses/'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 0123456789abcdef0123456789abcdef01234567'
}

for ipaddrBody in ipaddrsBody:

    response = requests.post(url, headers=headers, json=ipaddrBody, verify=False)

    if response.status_code == 201:
        print(" - Success, the below item was added:")
        output = response.json()
        print(output)
    else:
        print(" FAILED with error code", response.status_code)
        output = response.json()
        print(output)   