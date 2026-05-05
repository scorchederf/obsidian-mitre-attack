---
aliases: 
    - S0520
    
mitre-attack: https://attack.mitre.org/software/S0520
---

## S0520

[BLINDINGCAN](https://attack.mitre.org/software/S0520) is a remote access Trojan that has been used by the North Korean government since at least early 2020 in cyber operations against defense, engineering, and government organizations in Western Europe and the US.[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has collected from a victim machine the system name, processor information, and OS version.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has executed commands via cmd.exe.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has used HTTPS over port 443 for command and control.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has downloaded files to a victim machine.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System |  [BLINDINGCAN](https://attack.mitre.org/software/S0520) has uploaded files from victim machines.[^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has attempted to hide its payload by using legitimate file names such as "iconcache.db".[^2]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has encoded its C2 traffic with Base64.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has obfuscated code using Base64 encoding.[^2]  |
| [[Code Signing\|T1553.002]] | Code Signing | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has been signed with code-signing certificates such as CodeRipper.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has deleted itself and associated artifacts from victim machines.[^2]  |
| [[Software Packing\|T1027.002]] | Software Packing | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has been packed with the UPX packer.[^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has sent user and system information to a C2 server via HTTP POST requests.[^1] [^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has collected the victim machine's local IP address information and MAC address.[^2]  |
| [[Timestomp\|T1070.006]] | Timestomp | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has modified file and directory timestamps.[^2] [^1]  |
| [[Shared Modules\|T1129]] | Shared Modules | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has loaded and executed DLLs in memory during runtime on a victim machine.[^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has lured victims into executing malicious macros embedded within Microsoft Office documents.[^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has used Rundll32 to load a malicious DLL.[^2]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has collected disk information, including type and free space available.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [BLINDINGCAN](https://attack.mitre.org/software/S0520) can search, read, write, move, and execute files.[^2] [^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has been delivered by phishing emails containing malicious Microsoft Office documents.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has encrypted its C2 traffic with RC4.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has used AES and XOR to decrypt its DLLs.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: [NHS UK BLINDINGCAN Aug 2020](https://digital.nhs.uk/cyber-alerts/2020/cc-3603)


[^2]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)


