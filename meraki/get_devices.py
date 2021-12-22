import requests
import json

_url = 'https://api.meraki.com/api/v0/organizations/681155'
token = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
resp = requests.get(_url, headers = { 'X-Cisco-Meraki-API-Key' : token })

#print(resp.text)

org = json.loads(resp.text)["id"]
print(org)

print("Getting Networks")
networks_url = f"https://api.meraki.com/api/v0/organizations/{org}/networks"

networks = requests.get(networks_url, headers = { 'X-Cisco-Meraki-API-Key' : token })
networks_dict = json.loads(networks.text)

for network in networks_dict:
    #print(network['id'])
    net_id = network['id']
    devices_url = f"https://api.meraki.com/api/v0/networks/{net_id}/devices"
    devices = requests.get(devices_url, headers = { 'X-Cisco-Meraki-API-Key' : token })
    devices_dict = json.loads(devices.text)

    print(devices_dict)
    if isinstance(devices_dict,list) and len(devices_dict) >= 1:
        for device in devices_dict:
            print(device.get('name',None))
    elif isinstance(devices_dict,dict):
        print(devices_dict.get('name',None))
    else:
        print("")

    print("------------------------------------------")
