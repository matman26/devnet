# from pprint import pprint
import requests

base_url = 'https://10.10.20.49/'
nso_username = 'developer'
nso_password = 'C1sco12345'

devices_endpoint = 'restconf/data/tailf-ncs:devices/device'

target_url = base_url + devices_endpoint
print(target_url)

output = requests.get(target_url,
                      headers={'Content-Type': 'application/yang-data+json'},
                      auth=(nso_username, nso_password),
                      verify=False)


print(output.text)
