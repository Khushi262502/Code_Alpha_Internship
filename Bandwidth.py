from scapy.all import *
total_bytes = 0
tcp_bytes = 0
udp_bytes = 0
icmp_bytes = 0

def calculate_bandwidth(packet,TCP,UDP,ICMP):
    global total_bytes
    global tcp_bytes
    global udp_bytes
    global icmp_bytes

    packet_size = len(packet)
    total_bytes += packet_size

    if TCP in packet:
        tcp_bytes += packet_size
    elif UDP in packet:
        udp_bytes += packet_size
    elif ICMP in packet:
        icmp_bytes += packet_size
    


def show_bandwidth():
    print("\n------Bandwidth------")

    print(
        f"Total Traffic : {total_bytes/1024:.2f} KB"
    )

    print(
        f"TCP Traffic   : {tcp_bytes/1024:.2f} KB"
    )

    print(
        f"UDP Traffic   : {udp_bytes/1024:.2f} KB"
    )

    print(
        f"ICMP Traffic  : {icmp_bytes/1024:.2f} KB"
    )

def get_bandwidth_stats():
    return tcp_bytes, udp_bytes, icmp_bytes
