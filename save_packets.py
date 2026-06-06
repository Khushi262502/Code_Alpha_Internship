# save_packets.py

from scapy.all import *

print("Capturing 50 packets...")

packets = sniff(count=50)

wrpcap("capture.pcap", packets)

print("PCAP file saved!")