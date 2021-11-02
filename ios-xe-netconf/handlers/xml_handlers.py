import xml.dom.minidom

def xml_print(xml_string):
    parsed = xml.dom.minidom.parseString(xml_string)
    print(parsed.toprettyxml())
