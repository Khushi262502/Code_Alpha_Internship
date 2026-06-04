from collections import defaultdict

# Protocol Counters
tcp_count = 0
udp_count = 0
icmp_count = 0

# Total packets
total_packets = 0

# Top Talkers
ip_counter = defaultdict(int)


def analyze_packet(packet, IP, TCP, UDP, ICMP):

    global tcp_count, udp_count, icmp_count
    global total_packets

    total_packets += 1

    src = packet[IP].src

    ip_counter[src] += 1

    if TCP in packet:
        tcp_count += 1

    elif UDP in packet:
        udp_count += 1

    elif ICMP in packet:
        icmp_count += 1


def show_statistics():

    print("\n===== PROTOCOL STATISTICS =====")
    print("Total Packets:", total_packets)
    print("TCP:", tcp_count)
    print("UDP:", udp_count)
    print("ICMP:", icmp_count)

    print("\n===== TOP TALKERS =====")

    top = sorted(
        ip_counter.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for ip, count in top[:5]:
        print(f"{ip} : {count}")

