import os
import ipaddress

network = "192.168.1.0/24"

def find_empty_ips(network):
    empty_ips = []
    for ip in ipaddress.IPv4Network(network, strict=False).hosts():
        response = os.system(f"ping -c 1 {str(ip)}")
        if response != 0:
            empty_ips.append(str(ip))
    print("Empty IP Addresses:", empty_ips)

if __name__ == '__main__':
    find_empty_ips(network)
