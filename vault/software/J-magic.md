---
aliases: 
    - S1203
    
mitre-attack: https://attack.mitre.org/software/S1203
---

## S1203

[J-magic](https://attack.mitre.org/software/S1203) is a custom variant of the [cd00r](https://attack.mitre.org/software/S1204) backdoor tailored to target Juniper routers that was first observed during the [J-magic Campaign](https://attack.mitre.org/campaigns/C0050) in mid-2023. [J-magic](https://attack.mitre.org/software/S1203) monitors TCP traffic for five predefined parameters or "magic packets" to be sent by the attackers before activating on compromised devices.[^1] <br><br>

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [J-magic](https://attack.mitre.org/software/S1203) can rename itself as “[nfsiod 0]” to masquerade as the local Network File System (NFS) asynchronous I/O server.[^1]  |
| [[Clear Command History\|T1070.003]] | Clear Command History | [J-magic](https://attack.mitre.org/software/S1203) can overwrite previously executed command line arguments.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [J-magic](https://attack.mitre.org/software/S1203) can monitor incoming C2 communications sent over TCP to the compromised host.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [J-magic](https://attack.mitre.org/software/S1203) can compare the host and remote IPs to check if a received packet is from the infected machine.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [J-magic](https://attack.mitre.org/software/S1203) can communicate back to send a challenge to C2 infrastructure over SSL.[^1]  |
| [[Traffic Signaling\|T1205]] | Traffic Signaling | [J-magic](https://attack.mitre.org/software/S1203) can monitor TCP traffic for packets containing one of five different predefined parameters and will spawn a reverse shell if one of the parameters and the proper response string to a subsequent challenge is received.[^1]  |
| [[Network Sniffing\|T1040]] | Network Sniffing | [J-magic](https://attack.mitre.org/software/S1203) has a pcap listener function that can create an Extended Berkley Packet Filter (eBPF) on designated interfaces and ports.[^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | The [J-magic](https://attack.mitre.org/software/S1203) agent is executed through a command line argument which specifies an interface and listening port.[^1]  |




## References

[^1]: [Lumen J-Magic JAN 2025](https://blog.lumen.com/the-j-magic-show-magic-packets-and-where-to-find-them/)


