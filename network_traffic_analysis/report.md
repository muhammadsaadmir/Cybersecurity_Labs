# Network Traffic Analysis Report

## Objective
The goal of this lab was to capture and analyze network traffic using Wireshark to understand how devices communicate on local and external networks and identify potential security risks.

## Environment
- Operating System: macOS
- Tool: Wireshark
- Network: Local Wi-Fi network

---

## mDNS Analysis

Filter used: mdns

During packet capture, I observed multiple mDNS packets from Apple devices connected to my local Wi-Fi network.

Examples included:
- Muhammad-Saads-iPhone.local
- Muhammad Saad’s iPad
- _companion-link._tcp.local

These packets were sent to multicast address **224.0.0.251** using port **5353**.

### What this means
mDNS helps devices discover each other on the same local network for services like AirDrop, AirPlay, and device pairing.

### Security risk
This may expose:
- Device names
- Available services
- Active devices on the network

An attacker on public Wi-Fi could potentially gather this information.

---

## TCP Analysis

Filter used: tcp

I observed communication between my local device and external servers.

Example:
- Local IP → External IP

### TCP flags observed
ACK → confirms data was received

PSH, ACK → sends actual data

RST, ACK → resets connection

Retransmission → resends packets due to delays or packet loss

### Security relevance
TCP analysis helps identify:
- Failed connections
- Network instability
- Unusual communication patterns

---

## DNS Analysis

Filter used: dns

DNS traffic showed how websites are converted into IP addresses.

Example:
When visiting Google, DNS helps locate Google’s server.

### Security risk
Unencrypted DNS requests may expose browsing behavior on insecure networks.

---

## TLS Analysis

Filter used: tls

TLS traffic showed encrypted communication between my device and websites.

This helps protect:
- Passwords
- Personal information
- Secure browsing sessions

---

## Key Findings
- Apple devices were discoverable on the local network through mDNS
- TCP packets showed normal communication behavior
- DNS handled website lookups
- TLS protected internet communication

---

## Recommendations
- Avoid public Wi-Fi when possible
- Use VPNs on public networks
- Disable unnecessary device discovery services
- Monitor unusual network traffic

---

## Conclusion
This lab helped me understand real-world network communication and how packet analysis can be used to identify security risks.