from analyzer import get_protocol_stats, get_top_talkers
from Bandwidth import get_bandwidth_stats
from Visualization import (
    plot_protocols,
    plot_top_talkers,
    plot_bandwidth
)

def show_dashboard():

    tcp, udp, icmp = get_protocol_stats()

    print("TCP =", tcp)
    print("UDP =", udp)
    print("ICMP =", icmp)

    ip_counter = get_top_talkers()
    print("Top Talkers =", ip_counter)

    tcp_b, udp_b, icmp_b = get_bandwidth_stats()

    print("Bandwidth =", tcp_b, udp_b, icmp_b)

    plot_protocols(tcp, udp, icmp)

    if len(ip_counter) > 0:
        plot_top_talkers(ip_counter)

    if tcp_b + udp_b + icmp_b > 0:
        plot_bandwidth(tcp_b, udp_b, icmp_b)