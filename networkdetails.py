import os
import ipaddress

def networkdetails():
    var1 = "IPv4 Address"
    var2 = "Subnet Mask"

    ipconfcmd = os.popen("ipconfig").read()

    networklist = ipconfcmd.split("\n")

    for i in networklist:
        if (var1 in i):
            ipadr = i.split(":")[1].strip()
        elif (var2 in i):
            submask = i.split(":")[1].strip()

    result = "{}/{}".format(ipadr, submask)
    network = ipaddress.IPv4Network(result, strict=False)
    netaddr = str(network.network_address)
    postfix = ipaddress.IPv4Network("{}/{}".format(netaddr, submask)).prefixlen

    final_result = "{}/{}".format(netaddr, str(postfix))

    return ipadr, final_result
