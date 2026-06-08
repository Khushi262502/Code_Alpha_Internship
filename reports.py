import csv
from analyzer import (
    get_protocol_stats,
    get_top_talkers
)

from Bandwidth import get_bandwidth_stats

def generate_csv_report():

    tcp, udp, icmp = get_protocol_stats()

    tcp_b, udp_b, icmp_b = get_bandwidth_stats()

    top_talkers = get_top_talkers()

    with open(
        "network_report.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            ["Metric", "Value"]
        )

        writer.writerow(
            ["TCP Packets", tcp]
        )

        writer.writerow(
            ["UDP Packets", udp]
        )

        writer.writerow(
            ["ICMP Packets", icmp]
        )

        writer.writerow(
            ["TCP Bytes", tcp_b]
        )

        writer.writerow(
            ["UDP Bytes", udp_b]
        )

        writer.writerow(
            ["ICMP Bytes", icmp_b]
        )

        writer.writerow([])

        writer.writerow(
            ["Top Talker", "Packet Count"]
        )

        top = sorted(
            top_talkers.items(),
            key=lambda x: x[1],
            reverse=True
        )

        for ip, count in top[:5]:

            writer.writerow(
                [ip, count]
            )

    print(
        "CSV Report Generated"
    )