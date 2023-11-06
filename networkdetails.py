import os
import ipaddress

def networkdetails():
    var1 = "IPv4 Address"
    var2 = "Subnet Mask"

    ipconfcmd = os.popen("ipconfig").read()
    networklist = ipconfcmd.split("\n")

    for i in networklist:
        if (var1 in i):
            ipadr = i.split(":")[1]
        elif (var2 in i):
            submask = i.split(":")[1]

    print(ipadr)
    print(submask)

    result = "{}/{}".format(ipadr.strip(),submask.strip())
    print(result)

    network = ipaddress.IPv4Network(result, strict=False)
    print(network.network_address)


