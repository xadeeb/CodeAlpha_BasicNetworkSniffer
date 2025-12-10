# Codec - Basic Network Sniffer

This project is a simple Python-based network packet sniffer built using the `scapy` library.

## Features
- Captures live packets from your network
- Extracts source and destination IPs
- Displays protocol information

## Requirements
- Python 3.x
- scapy

## Installation
```bash
pip install scapy
```

## Usage
```bash
sudo python3 network_sniffer.py
```

## Sample Output
```
Source: 192.168.1.2 -> Destination: 93.184.216.34 | Protocol: 6
Source: 10.0.0.5 -> Destination: 192.168.1.1 | Protocol: 6
```

---
> **Note:** Run as administrator/root since it captures packets from the network.
