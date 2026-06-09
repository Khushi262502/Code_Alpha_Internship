# Network Traffic Analyzer

## Overview

Network Traffic Analyzer is a Python-based cybersecurity project that captures and analyzes network packets in real time. The tool monitors network activity, identifies protocols, tracks bandwidth usage, detects top communicating hosts (Top Talkers), analyzes DNS traffic, and generates reports.

The project uses Scapy for packet capture, Rich for live terminal dashboards, and Matplotlib for data visualization.

---

## Features

* Real-Time Packet Capture
* Protocol Analysis (TCP, UDP, ICMP)
* Top Talkers Detection
* Bandwidth Monitoring
* DNS Traffic Analysis
* PCAP File Analysis
* Live Dashboard using Rich
* Data Visualization using Matplotlib
* TXT Report Generation
* CSV Report Generation

---

## Technologies Used

* Python 3
* Scapy
* Rich
* Matplotlib
* CSV Module

---

## Project Structure

Network_Analyzer/

├── capture.py

├── analyzer.py

├── Bandwidth.py

├── dns_analyzer.py

├── pcap_analyzer.py

├── Visualization.py

├── dashboard.py

├── rich_dashboard.py

├── reports.py

├── main.py

├── capture.pcap

├── network_report.txt

├── network_report.csv

└── README.md

---

## How It Works

1. Scapy captures packets from the active network interface.
2. Each packet is analyzed for:

   * Source IP
   * Destination IP
   * Protocol Type
   * Packet Size
3. Statistics are updated in real time.
4. Rich Dashboard displays live traffic information.
5. Reports are generated in TXT and CSV formats.
6. PCAP files can be analyzed offline.

---

## Running the Project

### Clone Repository

git clone https://github.com/Khushi262502/Code_Alpha_Internship.git

cd Code_Alpha_Internship

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

Windows:

venv\Scripts\activate

### Install Dependencies

pip install scapy rich matplotlib

### Run Project

python main.py

---

## Sample Features

### Protocol Statistics

* TCP Packet Count
* UDP Packet Count
* ICMP Packet Count

### Top Talkers

Displays IP addresses generating the highest traffic.

### Bandwidth Monitoring

Tracks protocol-wise bandwidth consumption.

### DNS Analyzer

Monitors DNS queries and requested domains.

### PCAP Analyzer

Analyzes previously captured packet files.

---

## Reports

The project automatically generates:

* network_report.txt
* network_report.csv

These reports can be used for further network analysis.

---

## Future Improvements

* Port Scan Detection
* Suspicious Traffic Alerts
* GeoIP Tracking
* Web Dashboard
* Database Integration
* Machine Learning-Based Traffic Classification

---

## Author

Khushi Singh

Cybersecurity & Python Enthusiast

---

## License

This project is developed for educational and internship purposes.
