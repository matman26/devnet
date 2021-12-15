from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("10.10.20.110",
    "admin",
    "ciscopsdt")
handle.login()

#compute_resources = handle.query_classid("ComputeBlade","ComputeRackUnit")
compute_resources = handle.query_classid("ComputeBlade")
#for compute_resource_class in compute_resources:
for compute_resource in compute_resources:
    leds = handle.query_children(in_dn = compute_resource.dn, class_id="equipmentlocatorLed")
    print(compute_resource.dn,leds[0].oper_state)