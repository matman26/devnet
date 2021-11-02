#!/bin/sh

# AUTHOR: Matheus Augusto da Silva
# This points to the DevNet Sandbox
# See https://devnetsandbox.cisco.com/RM/Diagram/Index/a9487767-deef-4855-b3e3-880e7f39eadc?diagramType=Topology
curl --request GET -L \
  --url https://api.meraki.com/api/v0/organizations \
  --header 'X-Cisco-Meraki-API-Key: 6bec40cf957de430a6f1f2baa056b99a4fac9ea0' 2>/dev/null | python -m json.tool

echo "======================================"
echo "Getting a specific organization by ID:"
echo "======================================"
org_id="463308"

curl --request GET -L \
  --url https://api.meraki.com/api/v0/organizations/${org_id} \
  --header 'X-Cisco-Meraki-API-Key: 6bec40cf957de430a6f1f2baa056b99a4fac9ea0' 2>/dev/null | python -m json.tool

echo "======================================="
echo "Getting a network from organization ID:"
echo "======================================="

curl --request GET -L \
  --url https://api.meraki.com/api/v0/organizations/${org_id}/networks \
  --header 'X-Cisco-Meraki-API-Key: 6bec40cf957de430a6f1f2baa056b99a4fac9ea0' 2>/dev/null | python -m json.tool
