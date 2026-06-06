from scapy.all import *
from collections import defaultdict

def analyze_pcap(file_name):

    packets = rdpcap(file_name)

    tcp_count = 0
    udp_count = 0
    icmp_count = 0

    ip_counter = defaultdict(int)

    for packet in packets:

        if IP in packet:

            ip_counter[
                packet[IP].src
            ] += 1

        if TCP in packet:
            tcp_count += 1

        elif UDP in packet:
            udp_count += 1

        elif ICMP in packet:
            icmp_count += 1

    print("\n===== PCAP ANALYSIS =====")

    print("Total Packets:", len(packets))

    print("\nProtocol Statistics")

    print("TCP :", tcp_count)
    print("UDP :", udp_count)
    print("ICMP:", icmp_count)

    print("\nTop Talkers")

    top = sorted(
        ip_counter.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for ip, count in top[:5]:
        print(ip, ":", count)