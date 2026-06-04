from scapy.all import *
from analyzer import analyze_packet , show_statistics

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


        if packet_counter % 20 == 0:
            show_statistics()
sniff(prn = packet_callback , store = False)
