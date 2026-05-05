---
aliases: 
    - T1095
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1095-Non-Application_Layer_Protocol
tactic: 
     - Command and Control
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may use an OSI non-application layer protocol for communication between host and C2 server or among infected hosts within a network. The list of possible protocols is extensive.[^11]  Specific examples include use of network layer protocols, such as the Internet Control Message Protocol (ICMP), transport layer protocols, such as the User Datagram Protocol (UDP), session layer protocols, such as Socket Secure (SOCKS), as well as redirected/tunneled protocols, such as Serial over LAN (SOL).<br><br>ICMP communication between hosts is one example.[^10]  Because ICMP is part of the Internet Protocol Suite, it is required to be implemented by all IP-compatible hosts.[^4]  However, it is not as commonly monitored as other Internet Protocols such as TCP or UDP and may be used by adversaries to hide communications.<br><br>In ESXi environments, adversaries may leverage the Virtual Machine Communication Interface (VMCI) for communication between guest virtual machines and the ESXi host. This traffic is similar to client-server communications on traditional network sockets but is localized to the physical machine running the ESXi host, meaning it does not traverse external networks (routers, switches). This results in communications that are invisible to external monitoring and standard networking tools like tcpdump, netstat, nmap, and Wireshark. By adding a VMCI backdoor to a compromised ESXi host, adversaries may persistently regain access from any guest VM to the compromised ESXi host’s backdoor, regardless of network segmentation or firewall rules in place.[^1] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0262-QuasarRAT\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can use TCP for C2 communication.[^12]  |
| [[kb/mitre/attack/software/S0699-Mythic\|S0699]] | Mythic | [[kb/mitre/attack/software/S0699-Mythic\|Mythic]] supports WebSocket and TCP-based C2 profiles.[^7] 	 |
| [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|Brute Ratel C4]] has the ability to use TCP for external C2.[^6]  |
| [[kb/mitre/attack/software/S1144-FRP\|S1144]] | FRP | [[kb/mitre/attack/software/S1144-FRP\|FRP]] can communicate over TCP, TCP stream multiplexing, KERN Communications Protocol (KCP), QUIC, and UDP.[^2]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1030-Network_Segmentation\|M1030]] | Network Segmentation | Properly configure firewalls and proxies to limit outgoing traffic to only necessary ports and through proper network gateway systems. Also ensure hosts are only provisioned to communicate over authorized interfaces. |
| [[kb/mitre/attack/mitigations/M1031-Network_Intrusion_Prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. |
| [[kb/mitre/attack/mitigations/M1037-Filter_Network_Traffic\|M1037]] | Filter Network Traffic | Filter network traffic to prevent use of protocols across the network boundary that are unnecessary.  If VMCI is not required in ESXi environments, consider restricting guest virtual machines from accessing VMCI services.[^3]  |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Periodically investigate ESXi hosts for open VMCI ports. Running the `lsof -A` command and inspecting results with a type of `SOCKET_VMCI` will reveal processes that have open VMCI ports.[^8]  |






> [!info]- References
> [^1]: [Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/)

> [^2]: [FRP GitHub](https://github.com/fatedier/frp)

> [^3]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)

> [^4]: [Microsoft ICMP](http://support.microsoft.com/KB/170292)

> [^5]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)

> [^6]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)

> [^7]: [Mythc Documentation](https://docs.mythic-c2.net/)

> [^8]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)

> [^9]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)

> [^10]: [Cisco Synful Knock Evolution](https://blogs.cisco.com/security/evolution-of-attacks-on-cisco-ios-devices)

> [^11]: [Wikipedia OSI](http://en.wikipedia.org/wiki/List_of_network_protocols_%28OSI_model%29)

> [^12]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)


