from collections import defaultdict
from scapy.layers.dns import DNSQR

dns_counter = defaultdict(int)

def analyze_dns(packet):

    try:

        if packet.haslayer(DNSQR):

            domain = packet[DNSQR].qname.decode(
                errors="ignore"
            ).rstrip(".")

            dns_counter[domain] += 1

            print(f"DNS Query: {domain}")
            print(f"DNS Counter: {dict(dns_counter)}")

    except Exception as e:

        print("DNS Error:", e)


def show_dns_stats():

    print("\n===== DNS ANALYZER =====")

    top_domains = sorted(
        dns_counter.items(),
        key=lambda x: x[1],
        reverse=True
    )

    if not top_domains:
        print("No DNS queries captured yet.")
        return

    for domain, count in top_domains[:5]:
        print(f"{domain} : {count}")


def get_dns_stats():

    return dns_counter