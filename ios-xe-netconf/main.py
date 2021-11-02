#/usr/env/python
from handlers.xml_handlers import xml_print
from ncclient import manager
from pprint import pprint
import netconf.filters


def get_xml_from_filter(netconf_manager,input_filter):
    xml_return = netconf_manager.get(input_filter).data_xml
    return xml_return

def connect_ios_xe():
    m =  manager.connect( host="sandbox-iosxe-latest-1.cisco.com", username="developer", password="C1sco12345", port="830", hostkey_verify=False) 
    return m

if __name__ == "__main__":
    connection = connect_ios_xe()
    output = get_xml_from_filter(connection,get_interface_filter)
    xml_print(output)
