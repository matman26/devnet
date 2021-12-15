from genie import testbed
from genie.utils.diff import Diff
from genie.libs.parser.utils import get_parser_exclude
tb = testbed.load('testbed.yaml')
device = tb.devices['iosxr1']
device.connect()
output = device.parse('show policy-map interface GigabitEthernet0/0/0/6')

print(output)


