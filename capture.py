from scapy.all import *
from analyzer import analyze_packet , show_statistics
from Bandwidth import calculate_bandwidth , show_bandwidth
from dns_analyzer import analyze_dns , show_dns_stats


packet_counter = 0

def packet_callback(packet):

    global packet_counter

    if IP in packet:
        packet_counter += 1

        print(
            f"{packet[IP].src} -> {packet[IP].dst}"
        )

        analyze_packet(
            packet,
            IP,
            TCP,
            UDP,
            ICMP
        )

        calculate_bandwidth(
            packet,
            TCP,
            UDP,
            ICMP

        )
        analyze_dns(packet)


        if packet_counter % 20 == 0:
            show_statistics()
            show_bandwidth()
            show_dns_stats()
sniff(prn = packet_callback , store = False)
