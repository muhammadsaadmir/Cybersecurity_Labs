# Network Traffic Analysis & Threat Detection Lab

## Objective
This project focuses on analyzing network traffic using Wireshark to understand common network protocols and identify potential security risks.

## Tools Used
- Wireshark
- macOS
- Local Wi-Fi Network

## Protocols Analyzed
- mDNS
- TCP
- DNS
- UDP
- TLS

## Screenshots

### mDNS Analysis
![mDNS Analysis](screenshots/mdns-analysis.png)

### TCP Analysis
![TCP Analysis](screenshots/tcp-analysis.png)

## Key Findings
- Observed mDNS traffic used for local device discovery.
- Identified Apple device names and local services being advertised on the network.
- Analyzed TCP communication including ACK, RST, and retransmission packets.
- Observed local device communication with external servers.

## Security Risks
- mDNS can expose device names and available services on local networks.
- Public Wi-Fi users may be vulnerable to device enumeration.
- TCP retransmissions and reset packets can help identify network issues or unusual behavior.

## Recommendations
- Avoid using public Wi-Fi without protection.
- Disable unnecessary local discovery services when not needed.
- Use firewalls and secure network settings.
- Monitor unusual traffic patterns.