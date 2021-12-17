from ttp import ttp
from pprint import pprint

data = """
Wed Dec 15 12:20:10.392 brz
GigabitEthernet0/0/0/9 direction input: Service Policy not installed

GigabitEthernet0/0/0/9 output: p1

Class CLASS-PHB-SIG
  Classification statistics          (packets/bytes)     (rate - kbps)
    Matched             :         83941489765/6177036085298        2569
    Transmitted         :         83941492398/6177036296961        2515
    Total Dropped       :                   0/0                    2332
  Queueing statistics
    Queue ID                             : 65834
    High watermark                       : N/A
    Inst-queue-len  (packets)            : 0
    Avg-queue-len                        : N/A
    Taildropped(packets/bytes)           : 0/0
    Queue(conform)      :         83941492398/6177036296961        2515
    Queue(exceed)       :                   0/0                    0
    RED random drops(packets/bytes)      : 0/0

Class CLASS-PHB-GPRS
  Classification statistics          (packets/bytes)     (rate - kbps)
    Matched             :         89642626192/54564870497246       9782
    Transmitted         :         89642627472/54564871241434       9206
    Total Dropped       :                   0/0                    0
  Queueing statistics
    Queue ID                             : 65835
    High watermark                       : N/A
    Inst-queue-len  (packets)            : 0
    Avg-queue-len                        : N/A
    Taildropped(packets/bytes)           : 0/0
    Queue(conform)      :         89642627472/54564871241434       9206
    Queue(exceed)       :                   0/0                    0
    RED random drops(packets/bytes)      : 0/0

Class CLASS-PHB-DCR
  Classification statistics          (packets/bytes)     (rate - kbps)
    Matched             :          4694465116/601917998750         178
    Transmitted         :          4694465219/601918012926         182
    Total Dropped       :                   0/0                    0
  Queueing statistics
    Queue ID                             : 65836
    High watermark                       : N/A
    Inst-queue-len  (packets)            : 0
    Avg-queue-len                        : N/A
    Taildropped(packets/bytes)           : 0/0
    Queue(conform)      :          4694465219/601918012926         182
    Queue(exceed)       :                   0/0                    0
    RED random drops(packets/bytes)      : 0/0

    WRED profile for WRED Curve 1
    RED Transmitted (packets/bytes)            : N/A
    RED random drops(packets/bytes)            : 0/0
    RED maxthreshold drops(packets/bytes)      : N/A
    RED ecn marked & transmitted(packets/bytes): N/A
    WRED profile for WRED Curve 2
    RED Transmitted (packets/bytes)            : N/A
    RED random drops(packets/bytes)            : 0/0
    RED maxthreshold drops(packets/bytes)      : N/A
    RED ecn marked & transmitted(packets/bytes): N/A
    WRED profile for WRED Curve 3
    RED Transmitted (packets/bytes)            : N/A
    RED random drops(packets/bytes)            : 0/0
    RED maxthreshold drops(packets/bytes)      : N/A
    RED ecn marked & transmitted(packets/bytes): N/A
Class class-default
  Classification statistics          (packets/bytes)     (rate - kbps)
    Matched             :        251075007073/283959953844390      61048
    Transmitted         :        251074762994/283959719728364      51819
    Total Dropped       :              250191/241316424            0
  Queueing statistics
    Queue ID                             : 65837
    High watermark                       : N/A
    Inst-queue-len  (packets)            : 0
    Avg-queue-len                        : N/A
    Taildropped(packets/bytes)           : 250142/241306751
    Queue(conform)      :        251074762994/283959719728364      51819
    Queue(exceed)       :                   0/0                    0
    RED random drops(packets/bytes)      : 49/9673

    WRED profile for WRED Curve 1
    RED Transmitted (packets/bytes)            : N/A
    RED random drops(packets/bytes)            : 49/9673
    RED maxthreshold drops(packets/bytes)      : N/A
    RED ecn marked & transmitted(packets/bytes): N/A
"""

#abc = "{{ ignore("\s+") }}Matched{{ ignore("\s+") }}+:{{ignore("\s+")}}{{ matched | WORD }}{{ rate | PHRASE }}"
ttp_template = """
<doc>
Returns XPaths
- /interfaces/{interface_name}/direction/{'input'|'output'}/policy_map
- /interfaces/{interface_name}/direction/{'input'|'output'}/policy_name/{POLICY_NAME}/drop_bytes
- /interfaces/{interface_name}/direction/{'input'|'output'}/policy_name/{POLICY_NAME}/drop_packets
- /interfaces/{interface_name}/direction/{'input'|'output'}/policy_name/{POLICY_NAME}/drop_rate
- /interfaces/{interface_name}/direction/{'input'|'output'}/policy_name/{POLICY_NAME}/matched_packets
- /interfaces/{interface_name}/direction/{'input'|'output'}/policy_name/{POLICY_NAME}/matched_bytes
- /interfaces/{interface_name}/direction/{'input'|'output'}/policy_name/{POLICY_NAME}/match_rate
</doc>
<group name="interfaces">
 <group name="{{interface_name}}">
  <group name="direction">
   <group name="{{ direction }}">
{{ interface_name }} direction {{ direction | WORD }}: {{ policy_status | PHRASE }}
   </group>
   <group name="{{ direction }}">
{{ interface_name }} {{ direction | WORD }}: {{ policy_map | WORD }}
    <group name="{{drop_rate}}">
Class {{ class | WORD }}
    Matched             :                   {{ matched_packets | WORD }}/{{ matched_bytes | WORD }}                    {{ match_rate | WORD }}
    Total Dropped       :                   {{ drop_packets | WORD }}/{{ drop_bytes | WORD }}                    {{ drop_rate | WORD }}
    </group>
   </group>
  </group>
 </group>
</group>
"""

parser = ttp(data=data,template=ttp_template)
parser.parse()
results = parser.result(format='json')[0]
print(results)

