---
aliases: 
    - S1026
    
mitre-attack: https://attack.mitre.org/software/S1026
---

## S1026

[Mongall](https://attack.mitre.org/software/S1026) is a backdoor that has been used since at least 2013, including by [Aoqin Dragon](https://attack.mitre.org/groups/G1007).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Mongall](https://attack.mitre.org/software/S1026) can use HTTP for C2 communication.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Mongall](https://attack.mitre.org/software/S1026) has the ability to decrypt its payload prior to execution.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Mongall](https://attack.mitre.org/software/S1026) has relied on a user opening a malicious document for execution.[^1]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [Mongall](https://attack.mitre.org/software/S1026) can identify removable media attached to compromised hosts.[^1] <br> |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Mongall](https://attack.mitre.org/software/S1026) can identify drives on compromised hosts.[^1] <br> |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Mongall](https://attack.mitre.org/software/S1026) has the ability to RC4 encrypt C2 communications.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Mongall](https://attack.mitre.org/software/S1026) can use `rundll32.exe` for execution.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Mongall](https://attack.mitre.org/software/S1026) has the ability to upload files from victim's machines.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Mongall](https://attack.mitre.org/software/S1026) can use Base64 to encode information sent to its C2.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Mongall](https://attack.mitre.org/software/S1026) can download files to targeted systems.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Mongall](https://attack.mitre.org/software/S1026) can upload files and information from a compromised host to its C2 server.[^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Mongall](https://attack.mitre.org/software/S1026) can inject a DLL into `rundll32.exe` for execution.[^1] <br> |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Mongall](https://attack.mitre.org/software/S1026) can retrieve the hostname via `gethostbyname`.[^1] <br> |
| [[Software Packing\|T1027.002]] | Software Packing | [Mongall](https://attack.mitre.org/software/S1026) has been packed with Themida.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Mongall](https://attack.mitre.org/software/S1026) can establish persistence with the auto start function including using the value `EverNoteTrayUService`.[^1] <br> |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Aoqin Dragon\|G1007]] | Aoqin Dragon |



## References

[^1]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)


