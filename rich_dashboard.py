from rich.live import Live
from rich.table import Table
from rich.console import Console
import time

from analyzer import (
    get_protocol_stats,
    get_top_talkers
)

from Bandwidth import get_bandwidth_stats

console = Console()


def generate_dashboard():

    tcp, udp, icmp = get_protocol_stats()

    dashboard = Table(
        title="🚀 Network Traffic Analyzer"
    )

    dashboard.add_column(
        "Metric",
        style="cyan"
    )

    dashboard.add_column(
        "Value",
        style="green"
    )

    dashboard.add_row(
        "TCP Packets",
        str(tcp)
    )

    dashboard.add_row(
        "UDP Packets",
        str(udp)
    )

    dashboard.add_row(
        "ICMP Packets",
        str(icmp)
    )

    tcp_b, udp_b, icmp_b = get_bandwidth_stats()

    dashboard.add_row(
        "TCP Bytes",
        str(tcp_b)
    )

    dashboard.add_row(
        "UDP Bytes",
        str(udp_b)
    )

    dashboard.add_row(
        "ICMP Bytes",
        str(icmp_b)
    )

    top_talkers = get_top_talkers()

    top = sorted(
        top_talkers.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    for ip, count in top:

        dashboard.add_row(
            f"Top Talker {ip}",
            str(count)
        )

    return dashboard


def show_rich_dashboard():

    with Live(
        generate_dashboard(),
        refresh_per_second=1,
        console=console
    ) as live:

        while True:

            live.update(
                generate_dashboard()
            )

            time.sleep(2)