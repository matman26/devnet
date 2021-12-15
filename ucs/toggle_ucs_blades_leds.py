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
    previous_oper_state = leds[0].oper_state

    if leds[0].oper_state == "on":
        leds[0].admin_state = "off"
    else:
        leds[0].admin_state = "on"
    
    handle.set_mo(leds[0])
    handle.commit()

    print(  "dn:", 
            compute_resource.dn,
            "leds previous", previous_oper_state,
            "leds current",leds[0].admin_state)