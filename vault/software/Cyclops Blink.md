---
aliases: 
    - S0687
    
mitre-attack: https://attack.mitre.org/software/S0687
---

## S0687

[Cyclops Blink](https://attack.mitre.org/software/S0687) is a modular malware that has been used in widespread campaigns by [Sandworm Team](https://attack.mitre.org/groups/G0034) since at least 2019 to target Small/Home Office (SOHO) network devices, including WatchGuard and Asus. [Cyclops Blink](https://attack.mitre.org/software/S0687) is assessed to be a replacement for [VPNFilter](https://attack.mitre.org/software/S1010), a similar platform targeting network devices.[^3] [^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Native API\|T1106]] | Native API | [Cyclops Blink](https://attack.mitre.org/software/S0687) can use various Linux API functions including those for execution and discovery.[^3]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Cyclops Blink](https://attack.mitre.org/software/S0687) can encrypt C2 messages with AES-256-CBC sent underneath TLS. OpenSSL library functions are also used to encrypt each message using a randomly generated key and IV, which are then encrypted using a hard-coded RSA public key.[^3]  |
| [[Timestomp\|T1070.006]] | Timestomp | [Cyclops Blink](https://attack.mitre.org/software/S0687) has the ability to use the Linux API function `utime` to change the timestamps of modified firmware update images.[^3]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Cyclops Blink](https://attack.mitre.org/software/S0687) can rename its running process to `[kworker:0/1]` to masquerade as a Linux kernel thread. [Cyclops Blink](https://attack.mitre.org/software/S0687) has also named RC scripts used for persistence after WatchGuard artifacts.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Cyclops Blink](https://attack.mitre.org/software/S0687) has the ability to query device information.[^3]  |
| [[Component Firmware\|T1542.002]] | Component Firmware | [Cyclops Blink](https://attack.mitre.org/software/S0687) has maintained persistence by patching legitimate device firmware when it is downloaded, including that of WatchGuard devices.[^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Cyclops Blink](https://attack.mitre.org/software/S0687) can upload files from a compromised host.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Cyclops Blink](https://attack.mitre.org/software/S0687) can use the Linux API `statvfs` to enumerate the current working directory.[^3] [^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Cyclops Blink](https://attack.mitre.org/software/S0687) has the ability to upload exfiltrated files to a C2 server.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Cyclops Blink](https://attack.mitre.org/software/S0687) can enumerate the process it is currently running under.[^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Cyclops Blink](https://attack.mitre.org/software/S0687) can use the Linux API `if_nameindex` to gather network interface names.[^3] [^1]  |
| [[Non-Standard Encoding\|T1132.002]] | Non-Standard Encoding | [Cyclops Blink](https://attack.mitre.org/software/S0687) can use a custom binary scheme to encode messages with specific commands and parameters to be executed.[^3]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [Cyclops Blink](https://attack.mitre.org/software/S0687) has used [Tor](https://attack.mitre.org/software/S0183) nodes for C2 traffic.[^2]  |
| [[Inter-Process Communication\|T1559]] | Inter-Process Communication | [Cyclops Blink](https://attack.mitre.org/software/S0687) has the ability to create a pipe to enable inter-process communication.[^1]  |
| [[Network Device Firewall\|T1686.002]] | Network Device Firewall | [Cyclops Blink](https://attack.mitre.org/software/S0687) can modify the Linux iptables firewall to enable C2 communication on network devices via a stored list of port numbers.[^3] [^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Cyclops Blink](https://attack.mitre.org/software/S0687) has the ability to download files to target systems.[^3] [^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Cyclops Blink](https://attack.mitre.org/software/S0687) can download files via HTTP and HTTPS.[^3] [^1]  |
| [[RC Scripts\|T1037.004]] | RC Scripts | [Cyclops Blink](https://attack.mitre.org/software/S0687) has the ability to execute on device startup, using a modified RC script named S51armled.[^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Cyclops Blink](https://attack.mitre.org/software/S0687) can decrypt and parse instructions sent from C2.[^3]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Cyclops Blink](https://attack.mitre.org/software/S0687) can use DNS over HTTPS (DoH) to resolve C2 nodes.[^1]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [Cyclops Blink](https://attack.mitre.org/software/S0687) can use non-standard ports for C2 not typically associated with HTTP or HTTPS traffic.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Sandworm Team\|G0034]] | Sandworm Team |



## References

[^1]: [Trend Micro Cyclops Blink March 2022](https://www.trendmicro.com/en_us/research/22/c/cyclops-blink-sets-sights-on-asus-routers--.html)


[^2]: [NCSC CISA Cyclops Blink Advisory February 2022](https://www.ncsc.gov.uk/news/joint-advisory-shows-new-sandworm-malware-cyclops-blink-replaces-vpnfilter)


[^3]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)


