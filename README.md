# Basic Network Sniffer

This is a simple network sniffer implemented in Python using the Scapy library. It captures network packets and displays basic information about IP, TCP, and UDP traffic.

## Features

- Captures IP packets
- Displays source and destination IP addresses
- Identifies TCP and UDP traffic
- Shows source and destination ports for TCP and UDP

## Requirements

- Python 3.6+
- Scapy library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/network-sniffer.git
   cd network-sniffer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script with administrator/root privileges:

```
sudo python network_sniffer.py
```

The script will capture and display information for 10 packets, then exit.

## Sample Output

```
Starting network sniffer...
IP Packet: 192.168.1.5 -> 93.184.216.34, Protocol: 6
TCP Segment: 52431 -> 80
IP Packet: 93.184.216.34 -> 192.168.1.5, Protocol: 6
TCP Segment: 80 -> 52431
...
Sniffing complete.
```

## Caution

This tool is for educational purposes only. Ensure you have permission to capture network traffic on the network you're using. Unauthorized packet sniffing may be illegal in some jurisdictions.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
