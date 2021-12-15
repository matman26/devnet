from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("10.10.20.110",
    "admin",
    "ciscopsdt")
handle.login()

blades = handle.query_classid("ComputeBlade")
for blade in blades:
    print(blade)