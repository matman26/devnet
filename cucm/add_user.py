"""This adds a new CUCM end user from the CUCM AXL API using SOAP and the requests library.

See devnet sandbox for CUCM 12.0 at https://devnetsandbox.cisco.com/RM/Topology
"""
import requests
import xml.etree.ElementTree as et
from copy import copy

def dictify(r,root=True):
    """
    Turn xml parsed from etree into dict.

    Taken from https://stackoverflow.com/questions/2148119/how-to-convert-an-xml-string-to-a-dictionary
    """
    if root:
        return {r.tag: dictify(r, False)}
    d = copy(r.attrib)
    if r.text:
        d["_text"] = r.text
    for x in r.findall("./*"):
        if x.tag not in d:
            d[x.tag] = []
        d[x.tag].append(dictify(x, False))
    return d


payload = """
<soap:Envelope xmlns:soap='http://schemas.xmlsoap.org/soap/envelope/' xmlns:ns='http://www.cisco.com/AXL/API/12.0'>
  <soap:Body>
    <ns:addUser>
      <user>
        <firstName>AutomationUser</firstName>
        <displayName>Robot</displayName>
        <lastName>Bot</lastName>
        <userid>automationuser</userid>
        <password>cisco123</password>
        <pin>12345</pin>
      </user>
    </ns:addUser>
  </soap:Body>
</soap:Envelope>
"""

headers = {
    'Content-Type': 'text/xml; charset=utf-8'
    
}

url = 'https://10.10.20.1:8443/axl/'

response = requests.post(url,
                         data=payload,
                         headers=headers,
                         auth=('administrator',
                               'ciscopsdt'),
                         verify=False)

parsed = et.fromstring(response.text)
print(dictify(parsed))
