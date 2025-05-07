from scapy.all import rdpcap, UDP, NBNSQueryRequest
import sys

def extract_nbns_queries(pcap_file):
    packets = rdpcap(pcap_file)
    query_names = set()

    for pkt in packets:
        if pkt.haslayer(UDP) and pkt[UDP].dport == 137:
            if pkt.haslayer(NBNSQueryRequest):
                query = pkt[NBNSQueryRequest]
                query_names.add(query.QUESTION_NAME.strip())

    return sorted(query_names)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <file.pcap>")
        sys.exit(1)

    queries = extract_nbns_queries(sys.argv[1])
    for name in queries:
        print(name.decode())