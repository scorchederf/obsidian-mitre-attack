---
aliases: 
    - T1090
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1090-Proxy
tactic: 
     - Command and Control
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may use a connection proxy to direct network traffic between systems or act as an intermediary for network communications to a command and control server to avoid direct connections to their infrastructure. Many tools exist that enable traffic redirection through proxies or port redirection, including [[kb/mitre/attack/software/S0040-HTRAN\|HTRAN]], ZXProxy, and ZXPortMap. [^10]  Adversaries use these types of proxies to manage command and control communications, reduce the number of simultaneous outbound network connections, provide resiliency in the face of connection loss, or to ride over existing trusted communications paths between victims to avoid suspicion. Adversaries may chain together multiple proxies to further disguise the source of malicious traffic.<br><br>Adversaries can also take advantage of routing schemes in Content Delivery Networks (CDNs) to proxy command and control traffic.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0040-HTRAN\|S0040]] | HTRAN | [[kb/mitre/attack/software/S0040-HTRAN\|HTRAN]] can proxy TCP socket connections to obfuscate command and control infrastructure.[^1] [^4]  |
| [[kb/mitre/attack/software/S0108-netsh\|S0108]] | netsh | [[kb/mitre/attack/software/S0108-netsh\|netsh]] can be used to set up a proxy tunnel to allow remote host access to an infected host.[^5]  |
| [[kb/mitre/attack/software/S0262-QuasarRAT\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can communicate over a reverse proxy using SOCKS5.[^9] [^3]  |
| [[kb/mitre/attack/software/S0332-Remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] uses the infected hosts as SOCKS5 proxies to allow for tunneling and proxying.[^7] [^6]  |
| [[kb/mitre/attack/software/S0378-PoshC2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] contains modules that allow for use of proxies in command and control.[^13]  |
| [[kb/mitre/attack/software/S0508-ngrok\|S0508]] | ngrok | [[kb/mitre/attack/software/S0508-ngrok\|ngrok]] can be used to proxy connections to machines located behind NAT or firewalls.[^8] [^12]  |
| [[kb/mitre/attack/software/S1144-FRP\|S1144]] | FRP | [[kb/mitre/attack/software/S1144-FRP\|FRP]] can proxy communications through a server in public IP space to local servers located behind a NAT or firewall.[^2]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1020-SSL_TLS_Inspection\|M1020]] | SSL／TLS Inspection | If it is possible to inspect HTTPS traffic, the captures can be analyzed for connections that appear to be domain fronting. |
| [[kb/mitre/attack/mitigations/M1031-Network_Intrusion_Prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific C2 protocol used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool C2 signatures over time or construct protocols in such a way as to avoid detection by common defensive tools. [^11]  |
| [[kb/mitre/attack/mitigations/M1037-Filter_Network_Traffic\|M1037]] | Filter Network Traffic | Traffic to known anonymity networks and C2 infrastructure can be blocked through the use of network allow and block lists. It should be noted that this kind of blocking may be circumvented by other techniques like [[kb/mitre/attack/techniques/T1090.004-Domain_Fronting\|Domain Fronting]]. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1090.001-Internal_Proxy\|T1090.001]] | Internal Proxy |
| [[kb/mitre/attack/techniques/T1090.002-External_Proxy\|T1090.002]] | External Proxy |
| [[kb/mitre/attack/techniques/T1090.003-Multi-hop_Proxy\|T1090.003]] | Multi-hop Proxy |
| [[kb/mitre/attack/techniques/T1090.004-Domain_Fronting\|T1090.004]] | Domain Fronting |




> [!info]- References
> [^1]: [Operation Quantum Entanglement](https://web.archive.org/web/20210920193513/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-operation-quantum-entanglement.pdf)

> [^2]: [FRP GitHub](https://github.com/fatedier/frp)

> [^3]: [Volexity Patchwork June 2018](https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/)

> [^4]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)

> [^5]: [Securelist fileless attacks Feb 2017](https://securelist.com/fileless-attacks-against-enterprise-networks/77403/)

> [^6]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)

> [^7]: [Riskiq Remcos Jan 2018](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)

> [^8]: [MalwareBytes Ngrok February 2020](https://blog.malwarebytes.com/threat-analysis/2020/02/fraudsters-cloak-credit-card-skimmer-with-fake-content-delivery-network-ngrok-server/)

> [^9]: [GitHub QuasarRAT](https://github.com/quasar/QuasarRAT)

> [^10]: [Trend Micro APT Attack Tools](http://blog.trendmicro.com/trendlabs-security-intelligence/in-depth-look-apt-attack-tools-of-the-trade/)

> [^11]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)

> [^12]: [Zdnet Ngrok September 2018](https://www.zdnet.com/article/sly-malware-author-hides-cryptomining-botnet-behind-ever-shifting-proxy-service/)

> [^13]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)


