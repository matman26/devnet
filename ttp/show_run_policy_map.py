from ttp import ttp
from pprint import pprint

data = """
Building configuration...
policy-map POLICY1
 class class-default
  shape average 90000000
   service-policy BASE
policy-map POLICY2
 class class-default
  shape average percent 95
   service-policy BASE
policy-map POLICY3
 class class-default
  police 40400000
   service-policy BASE
"""

ttp_template = """
<group name="{{ map_name }}">
policy-map {{ map_name }}
 <group name="{{class_name}}">
 class {{ class_name }}
  <group name="shaping">
  <group name="absolute">
  shape average {{ value | WORD}}
  </group>
  <group name="relative">
  shape average percent {{ percent | WORD}}
  </group>
  </group>
  <group name="service-policy">
   service-policy {{ policy-name }}
  </group>
 </group>
</group>
"""

parser = ttp(data=data,template=ttp_template)
parser.parse()
results = parser.result(format='json')[0]
print(results)

