---
aliases: 
    - S1020
    
mitre-attack: https://attack.mitre.org/software/S1020
---

## S1020

[Kevin](https://attack.mitre.org/software/S1020) is a backdoor implant written in C++ that has been used by [HEXANE](https://attack.mitre.org/groups/G1001) since at least June 2020, including in operations against organizations in Tunisia.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[DNS\|T1071.004]] | DNS | Variants of [Kevin](https://attack.mitre.org/software/S1020) can communicate over DNS through queries to the server for constructed domain names with embedded information.[^1]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [Kevin](https://attack.mitre.org/software/S1020) can hide the current window from the targeted user via the `ShowWindow` API function.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Kevin](https://attack.mitre.org/software/S1020) can collect the MAC address and other information from a victim machine using `ipconfig/all`.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Kevin](https://attack.mitre.org/software/S1020) can Base32 encode chunks of output files during exfiltration.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Kevin](https://attack.mitre.org/software/S1020) can enumerate the OS version and hostname of a targeted machine.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Kevin](https://attack.mitre.org/software/S1020) can download files to the compromised host.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Kevin](https://attack.mitre.org/software/S1020) can send data from the victim host through a DNS C2 channel.[^1]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Kevin](https://attack.mitre.org/software/S1020) can use a custom protocol tunneled through DNS or HTTP.[^1]  |
| [[Data Transfer Size Limits\|T1030]] | Data Transfer Size Limits | [Kevin](https://attack.mitre.org/software/S1020) can exfiltrate data to the C2 server in 27-character chunks.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Kevin](https://attack.mitre.org/software/S1020) can delete files created on the victim's machine.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | Variants of [Kevin](https://attack.mitre.org/software/S1020) can communicate with C2 over HTTP.[^1]  |
| [[Native API\|T1106]] | Native API | [Kevin](https://attack.mitre.org/software/S1020) can use the `ShowWindow` API to avoid detection.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Kevin](https://attack.mitre.org/software/S1020) can upload logs and other data from a compromised host.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Kevin](https://attack.mitre.org/software/S1020) can use a renamed image of `cmd.exe` for execution.[^1]  |
| [[Junk Data\|T1001.001]] | Junk Data | [Kevin](https://attack.mitre.org/software/S1020) can generate a sequence of dummy HTTP C2 requests to obscure traffic.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Kevin](https://attack.mitre.org/software/S1020) has Base64-encoded its configuration file.[^1]  |
| [[Data Staged\|T1074]] | Data Staged | [Kevin](https://attack.mitre.org/software/S1020) can create directories to store logs and other collected data.[^1]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [Kevin](https://attack.mitre.org/software/S1020) can compile randomly-generated MOF files into the WMI repository to persistently run malware.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Kevin](https://attack.mitre.org/software/S1020) can assign hard-coded fallback domains for C2.[^1]  |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [Kevin](https://attack.mitre.org/software/S1020) can sleep for a time interval between C2 communication attempts.[^1]  |
| [[Rename Legitimate Utilities\|T1036.003]] | Rename Legitimate Utilities | [Kevin](https://attack.mitre.org/software/S1020) has renamed an image of `cmd.exe` with a random name followed by a `.tmpl` extension.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[HEXANE\|G1001]] | HEXANE |



## References

[^1]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)


