from collections import defaultdict
from scapy.layers.dns import DNSQR

dns_counter = defaultdict(int)

def analyze_dns(packet):

    if packet.haslayer(DNSQR):

        domain = packet[DNSQR].qname.decode(
            errors="ignore"
        ).rstrip(".")

        dns_counter[domain] += 1

def show_dns_stats():

    print("\n===== DNS ANALYZER =====")

    top_domains = sorted(
        dns_counter.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for domain, count in top_domains[:5]:
        print(f"{domain} : {count}")