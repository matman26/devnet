from genie import testbed
from genie.utils.diff import Diff
from genie.libs.parser.utils import get_parser_exclude
tb = testbed.load('testbed.yaml')
device = tb.devices['csr1000v-1']
device.connect()
output = device.parse('show policy-map interface GigabitEthernet3')

print(output)


