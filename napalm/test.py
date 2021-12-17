from napalm import get_network_driver
from pprint import pprint
import json

driver = get_network_driver('ios-xr')

device = driver(hostname='sandbox-iosxr-1.cisco.com',
                username='admin',
                password='C1sco12345')

device.open()

interfaces = device.get_interfaces()
pprint(interfaces)

cmds = [ 'show ip int brief', 'show ip route']
output_list = device.cli(cmds)

for output in output_list.keys():
    pprint(output)
