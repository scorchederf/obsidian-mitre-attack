---
aliases: 
    - S9023
    
mitre-attack: https://attack.mitre.org/software/S9023
---

## S9023

[HiddenFace](https://attack.mitre.org/software/S9023) is a modular backdoor developed and used exclusively by [MirrorFace](https://attack.mitre.org/groups/G1054) since at least 2021. [HiddenFace](https://attack.mitre.org/software/S9023) can communicate both actively and passively and has been used against political and academic targets.[^2] [^5] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [HiddenFace](https://attack.mitre.org/software/S9023) has exploited vulnerabilities in FortiOS/FortiProxy devices for initial access.[^3]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [HiddenFace](https://attack.mitre.org/software/S9023) has used scheduled tasks for execution and persistence.[^3] [^5]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [HiddenFace](https://attack.mitre.org/software/S9023)'s passive mode listens on TCP 47000.[^5] [^2]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [HiddenFace](https://attack.mitre.org/software/S9023) can use RSA-2048 in addition to symmetric algorithms in C2.[^5]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [HiddenFace](https://attack.mitre.org/software/S9023) can act as an internal HTTP proxy within the targeted environment.[^5]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [HiddenFace](https://attack.mitre.org/software/S9023) has encrypted its payload with AES.[^3] [^2]  |
| [[Mutual Exclusion\|T1480.002]] | Mutual Exclusion | [HiddenFace](https://attack.mitre.org/software/S9023) can create a mutex to ensure only one instance is running at a time.[^3] <br> |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [HiddenFace](https://attack.mitre.org/software/S9023) can use a custom TCP protocol over Port 443 for C2.[^3] [^5] [^2]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [HiddenFace](https://attack.mitre.org/software/S9023) can sleep randomly between 30 and 60 seconds to avoid behavioral analysis.[^3]   |
| [[Fallback Channels\|T1008]] | Fallback Channels | [HiddenFace](https://attack.mitre.org/software/S9023) can use active and passive C2 modes that use different encryption algorithms and backdoor commands.[^5]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [HiddenFace](https://attack.mitre.org/software/S9023) can collect the username associated with the compromised host.[^3] <br> |
| [[Data from Local System\|T1005]] | Data from Local System | [HiddenFace](https://attack.mitre.org/software/S9023) can upload files from the victim machine to C2 nodes.[^5] [^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [HiddenFace](https://attack.mitre.org/software/S9023) can download files from the C2 to victim systems.[^5] [^2]  |
| [[Dynamic API Resolution\|T1027.007]] | Dynamic API Resolution | [HiddenFace](https://attack.mitre.org/software/S9023) can dynamically resolve Windows APIs.[^3] [^5]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [HiddenFace](https://attack.mitre.org/software/S9023) can identify processes identified with security applications and tooling.[^3] [^5]  |
| [[Timestomp\|T1070.006]] | Timestomp |  [HiddenFace](https://attack.mitre.org/software/S9023) can alter timestamps for directory content on targeted machines.[^3] [^5] [^2]  |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [HiddenFace](https://attack.mitre.org/software/S9023) has used dynamic domain generation algorithms in C2.[^3] [^5] [^1] [^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [HiddenFace](https://attack.mitre.org/software/S9023) can enumerate the hostname and username of the compromised system.[^3] [^5] [^2]  |
| [[MSBuild\|T1127.001]] | MSBuild | [HiddenFace](https://attack.mitre.org/software/S9023) can execute a malicious XML file using MSBuild.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [HiddenFace](https://attack.mitre.org/software/S9023) can check running processes against a list of blocklisted applications.[^3] <br> |
| [[Process Injection\|T1055]] | Process Injection | [HiddenFace](https://attack.mitre.org/software/S9023) can inject code directly into legitimate applications.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography |  [HiddenFace](https://attack.mitre.org/software/S9023) can use a randomly selected symmetric encryption algorithm for C2.[^3]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [HiddenFace](https://attack.mitre.org/software/S9023) can hide its IP lookup by using DNS over HTTPS (DoH) for C2.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [HiddenFace](https://attack.mitre.org/software/S9023) has the ability to decrypt its payload prior to execution.[^3] [^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [HiddenFace](https://attack.mitre.org/software/S9023) can store its configuration file in the Registry.[^2]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [HiddenFace](https://attack.mitre.org/software/S9023) can check for the presence of specific analysis tools and will terminate itself if they are found.[^5]  |
| [[Windows Host Firewall\|T1686.003]] | Windows Host Firewall |  [HiddenFace](https://attack.mitre.org/software/S9023) can reconfigure Windows firewalls to enable communication by adding a rule named “Cortana” to allow inbound connection to TCP/47000.[^3] [^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MirrorFace\|G1054]] | MirrorFace |



## References

[^1]: [Trend Micro Earth Kasha Updates APR 2025](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)


[^2]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)


[^3]: [ESET HiddenFace 2024](https://jsac.jpcert.or.jp/archive/2024/pdf/JSAC2024_2_8_Breitenbacher_en.pdf)


[^4]: NOOPDOOR


[^5]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)


