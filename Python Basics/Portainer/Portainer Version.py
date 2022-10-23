'''
This script makes a simple unauthenticated (public) request to Portainer
'''
import requests

url = 'http://192.168.0.16:9000/api/status'

req = requests.get(url)
if req.status_code == 200:
    portainerStatus = req.json()
    portainerVersion = portainerStatus['Version']
    print("\nThe version of Portainer is", portainerVersion, "\n")
elif req.status_code == 404:
    print("invalid API call")
else:
    print("Issue connecting to Portainer")