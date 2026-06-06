import matplotlib.pyplot as plt

def plot_protocols(tcp,udp,icmp):
    labels = ["TCP" , "UDP" ,"ICMP"]

    values = [tcp , udp , icmp]

    plt.figure(figsize=(6,4))

    plt.bar(labels , values)

    plt.title("Protocols Distribution")

    plt.xlabel("Protocols")

    plt.ylabel("Packet Count")

    plt.show()

def plot_top_talkers(ip_counter):

    top = sorted(
        ip_counter.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    ips = [item[0] for item in top]

    counts = [item[1] for item in top]

    plt.figure(figsize=(8,4))

    plt.bar(ips, counts)

    plt.title("Top Talkers")

    plt.xlabel("IP Address")

    plt.ylabel("Packets")

    plt.xticks(rotation=30)

    plt.show()

def plot_bandwidth(tcp, udp, icmp):

    labels = ["TCP", "UDP", "ICMP"]

    values = [tcp, udp, icmp]

    plt.figure(figsize=(6,4))

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )

    plt.title("Bandwidth Usage")

    plt.show()