from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto

        print(f"IP Packet: {ip_src} -> {ip_dst}, Protocol: {proto}")

        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            print(f"TCP Segment: {src_port} -> {dst_port}")
        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            print(f"UDP Datagram: {src_port} -> {dst_port}")

def main():
    print("Starting network sniffer...")
    sniff(prn=packet_callback, store=0, count=10)
    print("Sniffing complete.")

if __name__ == "__main__":
    main()
