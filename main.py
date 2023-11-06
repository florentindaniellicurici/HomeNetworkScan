import scapy.all as scapy

def scan(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broad = broadcast/arp_req
    ans = scapy.srp(arp_req_broad, timeout=1, verbose = False)[0]

    print(ans.summary())
#    print(ans.summary())
    print("IP\t\t MAC address")

    for element in ans:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
        print("________________________________")




scan("192.168.1.0/28")


