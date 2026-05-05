---
aliases: 
    - S1204
    
mitre-attack: https://attack.mitre.org/software/S1204
---

## S1204

[cd00r](https://attack.mitre.org/software/S1204) is an open-source backdoor for UNIX and UNIX-variant operating systems that was orginally released in 2000. [cd00r](https://attack.mitre.org/software/S1204) source code is primarily based on a packet-capturing program as it utilizes a sniffer to listen for specific sequences of network traffic or "secret knock" before executing the attacker's code.[^1] [^2] <br><br>

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [cd00r](https://attack.mitre.org/software/S1204) can monitor incoming C2 communications sent over TCP to the compromised host.[^1] [^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [cd00r](https://attack.mitre.org/software/S1204) can discover the IP for the network interface on the compromised device.[^1]  |
| [[Network Sniffing\|T1040]] | Network Sniffing | [cd00r](https://attack.mitre.org/software/S1204) can use the libpcap library to monitor captured packets for specifc sequences.[^1]  |
| [[Port Knocking\|T1205.001]] | Port Knocking | [cd00r](https://attack.mitre.org/software/S1204) can monitor for a single TCP-SYN packet to be sent in series to a configurable set of ports (200, 80, 22, 53 and 3 in the original code) before opening a port for communication.[^1] [^2]  |




## References

[^1]: [Hartrell cd00r 2002](https://www.giac.org/paper/gcih/342/handle-cd00r-invisible-backdoor/103631)


[^2]: [Lumen J-Magic JAN 2025](https://blog.lumen.com/the-j-magic-show-magic-packets-and-where-to-find-them/)


