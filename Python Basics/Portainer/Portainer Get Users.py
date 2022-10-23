'''
This script logs into Portainer using Local Account and gets a JWT
Then uses the JWT to connect back in and get a list of users
NB: apiuser is not an Admin account so cannot enumerate Admin users
'''
import requests
import sys

PortainerAuthMethods = ['local', 'LDAP', 'AD', 'OATH']
baseurl = 'http://192.168.0.16:9000/api/'

authBody = {'password': "testing123", 'username': "apiuser"}

#check login auth is set to Local Users
print('\n checking authentication is local username/password')
req = requests.get(baseurl + 'settings/public')
if req.status_code == 200:
    portainerStatus = req.json()
    portainerAuthMethod = portainerStatus['AuthenticationMethod']
    portainerAuthMethod = portainerAuthMethod -1
    print(' - Success, auth type is', PortainerAuthMethods[portainerAuthMethod])
elif req.status_code == 404:
    print(" - Server error or invalid API call")
else:
    print(" - Issue connecting to Portainer")

# now know local username/password auth get API key
if PortainerAuthMethods[portainerAuthMethod] == 'local':
    print('\n logging in using', authBody['username'], 'to get API key')
    
    req = requests.post(baseurl + 'auth', json = authBody)
    if req.status_code == 200:
        apiJwt = req.json()
        print(' - Success, jwt returned')
    else:
        print(" - Error:", req.status_code)
else:
    print(' - auth method not supported, exiting... \n')
    sys.exit()

token = apiJwt['jwt']
headers = {'Authorization': f'Bearer {token}'}

print('\n getting list of usernames using jwt')
users = requests.get(baseurl + 'users', headers=headers )
if users.status_code == 200:
    print(" - Local Users in Portainer are:"), 
    PortainerUsers = users.json()
    for PortainerUser in PortainerUsers:
            print("   *",PortainerUser['Username'])
else:
    print("Issue logging into Portainer using API Key")


