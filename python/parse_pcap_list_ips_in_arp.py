from scapy.all import rdpcap, ARP
import ipaddress

def extract_unique_arp_ips(pcap_file):
    packets = rdpcap(pcap_file)
    ip_set = set()

    for pkt in packets:
        if pkt.haslayer(ARP):
            arp = pkt[ARP]
            ip_set.add(arp.psrc)
            ip_set.add(arp.pdst)

    return sorted(ip_set, key=lambda ip: ipaddress.IPv4Address(ip))

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <file.pcap>")
        sys.exit(1)

    ips = extract_unique_arp_ips(sys.argv[1])
    for ip in ips:
        print(ip)
