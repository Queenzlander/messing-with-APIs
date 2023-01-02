'''
This script add a new statically assigned Site to Netbox
NB: next iteration to include reading in list of sites from a csv file...
'''
import requests

siteBodys = [{ "name": "Cape Lambert", "slug": "capelambert", "status": "active", "region": 4, "time_zone": "Australia/Perth"},
{ "name": "Dampier", "slug": "dampier", "status": "active", "region": 4, "time_zone": "Australia/Perth"},
{ "name": "Hope Downs 1", "slug": "hopedowns1", "status": "active", "region": 4, "time_zone": "Australia/Perth"},
{ "name": "Hope Downs 4", "slug": "hopedowns4", "status": "active", "region": 4, "time_zone": "Australia/Perth"},
{ "name": "Western Creek", "slug": "westerncreek", "status": "active", "region": 4, "time_zone": "Australia/Perth"}]

url = 'http://192.168.0.16:8080/api/dcim/sites/'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 0123456789abcdef0123456789abcdef01234567'
}

for siteBody in siteBodys:

    response = requests.post(url, headers=headers, json=siteBody, verify=False)

    if response.status_code == 201:
        print(" - Success, the below item was added:")
        output = response.json()
        print(output)
    else:
        print(" FAILED with error code", response.status_code)
        output = response.json()
        print(output)   