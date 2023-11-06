import os
import ipaddress

def networkdetails():
    var1 = "IPv4 Address"
    var2 = "Subnet Mask"

    ipconfcmd = os.popen("ipconfig").read()

    networklist = ipconfcmd.split("\n")

    print(networklist)

    for i in networklist:
        if (var1 in i):
            ipadr = i.split(":")[1]
        elif (var2 in i):
            submask = i.split(":")[1]

    result = "{}/{}".format(ipadr.strip(),submask.strip())

    network = ipaddress.IPv4Network(result, strict=False)
    netaddr = str(network.network_address)
    postfix = ipaddress.IPv4Network('0.0.0.0/255.255.255.0').prefixlen

    final_result = "{}/{}".format(netaddr,str(postfix))

    return ipadr, final_result


