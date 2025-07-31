import scapy.all as scapy

def packet_callback(packet):
    if packet.haslayer(scapy.IP):
        ip_layer = packet[scapy.IP]
        proto = packet[scapy.IP].proto
        print(f"Source: {ip_layer.src} -> Destination: {ip_layer.dst} | Protocol: {proto}")

scapy.sniff(prn=packet_callback, store=0)
