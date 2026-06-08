from scapy.all import *
from analyzer import analyze_packet, show_statistics
from Bandwidth import calculate_bandwidth, show_bandwidth
from dns_analyzer import analyze_dns, show_dns_stats
from scapy.layers.dns import DNSQR
packet_counter = 0
captured_packets = []

def packet_callback(packet):

    global packet_counter

    if packet.haslayer(DNSQR):
        print("DNS found")

    if IP in packet:

        captured_packets.append(packet)

        packet_counter += 1

        print(
            f"{packet[IP].src} -> {packet[IP].dst}"
        )

        analyze_packet(packet, IP, TCP, UDP, ICMP)

        calculate_bandwidth(packet, TCP, UDP, ICMP)

        analyze_dns(packet)

        if packet_counter % 20 == 0:
            show_statistics()
            show_bandwidth()
            show_dns_stats()

def start_capture():

    try:
        sniff(
            prn=packet_callback,
            store=False,
            count = 300
            
        )

    except KeyboardInterrupt:

        print("\nSaving packets...")

        wrpcap(
            "capture.pcap",
            captured_packets
        )

        print("Saved to capture.pcap")