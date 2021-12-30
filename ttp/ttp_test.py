#!/usr/bin/python3
from ttp import ttp
from pprint import pprint

data = """
l2vpn bridge group BRIDGE_GROUP1 bridge-domain DOMAIN1
l2vpn bridge group BRIDGE_GROUP1 bridge-domain DOMAIN1 mtu 1546
l2vpn bridge group BRIDGE_GROUP1 bridge-domain DOMAIN1 interface GigabitEthernet0/0/1
l2vpn bridge group BRIDGE_GROUP1 bridge-domain DOMAIN1 neighbor 172.16.0.1 pw-id 10
l2vpn bridge group BRIDGE_GROUP1 bridge-domain DOMAIN1 neighbor 172.16.0.1 pw-id 10 pw-class CLASS1
l2vpn bridge group BRIDGE_GROUP1 bridge-domain DOMAIN1
l2vpn bridge group BRIDGE_GROUP1 bridge-domain DOMAIN1 mtu 1546
l2vpn bridge group BRIDGE_GROUP1 bridge-domain DOMAIN1 interface GigabitEthernet0/0/3
l2vpn bridge group BRIDGE_GROUP1 bridge-domain DOMAIN1 neighbor 172.16.0.10 pw-id 10
l2vpn bridge group BRIDGE_GROUP1 bridge-domain DOMAIN1 neighbor 172.16.0.10 pw-id 10 pw-class CLASS1
l2vpn bridge group BRIDGE_GROUP2 bridge-domain DOMAIN1
l2vpn bridge group BRIDGE_GROUP2 bridge-domain DOMAIN1 mtu 1546
l2vpn bridge group BRIDGE_GROUP2 bridge-domain DOMAIN1 interface GigabitEthernet0/0/2
l2vpn bridge group BRIDGE_GROUP2 bridge-domain DOMAIN1 neighbor 172.16.0.2 pw-id 20
l2vpn bridge group BRIDGE_GROUP2 bridge-domain DOMAIN1 neighbor 172.16.0.2 pw-id 20 pw-class CLASS1
"""

ttp_template = """
<doc>
Returns XPaths
 /group_names/group_name/bridge_domains/bridge_domain/interface_name
 /group_names/group_name/bridge_domains/bridge_domain/pwd_class
 /group_names/group_name/bridge_domains/bridge_domain/neighbor
 /group_names/group_name/bridge_domains/bridge_domain/pwd_id
 /group_names/group_name/bridge_domains/bridge_domain/mtu
</doc>
<group name="group_names">
 <group name="{{ group_name }}">
  <group name="neighbors">
   <group name="{{ neighbor }}">
l2vpn bridge group {{ group_name }} bridge-domain {{ bridge_domain }}
l2vpn bridge group {{ group_name }} bridge-domain {{ bridge_domain }} mtu {{ mtu }}
l2vpn bridge group {{ group_name }} bridge-domain {{ bridge_domain }} interface {{ interface_name }}
l2vpn bridge group {{ group_name }} bridge-domain {{ bridge_domain }} neighbor {{ neighbor }}  pw-id {{ pwd_id }}
l2vpn bridge group {{ group_name }} bridge-domain {{ bridge_domain }} neighbor {{ neighbor }}  pw-id {{ pwd_id }} pw-class {{ pwd_class }}
   </group>
  </group>
 </group>
</group>
"""

parser = ttp(data=data,template=ttp_template)
parser.parse()
results = parser.result(format='json')[0]
print(results)
