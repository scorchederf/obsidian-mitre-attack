---
aliases: 
    - S1013
    
mitre-attack: https://attack.mitre.org/software/S1013
---

## S1013

[ZxxZ](https://attack.mitre.org/software/S1013) is a trojan written in Visual C++ that has been used by [BITTER](https://attack.mitre.org/groups/G1002) since at least August 2021, including against Bangladeshi government personnel.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Native API\|T1106]] | Native API | [ZxxZ](https://attack.mitre.org/software/S1013) has used API functions such as `Process32First`, `Process32Next`, and `ShellExecuteA`.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [ZxxZ](https://attack.mitre.org/software/S1013) can download and execute additional files.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [ZxxZ](https://attack.mitre.org/software/S1013) has created a snapshot of running processes using `CreateToolhelp32Snapshot`.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [ZxxZ](https://attack.mitre.org/software/S1013) has collected the host name and operating system product name from a compromised machine.[^1]   |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [ZxxZ](https://attack.mitre.org/software/S1013) can search a compromised host to determine if it is running Windows Defender or Kasperky antivirus.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [ZxxZ](https://attack.mitre.org/software/S1013) has been disguised as a Windows security update service.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [ZxxZ](https://attack.mitre.org/software/S1013) can search the registry of a compromised host.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [ZxxZ](https://attack.mitre.org/software/S1013) has been encoded to avoid detection from static analysis tools.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [ZxxZ](https://attack.mitre.org/software/S1013) has used scheduled tasks for persistence and execution.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [ZxxZ](https://attack.mitre.org/software/S1013) has relied on victims to open a malicious attachment delivered via email.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [ZxxZ](https://attack.mitre.org/software/S1013) has been distributed via spearphishing emails, usually containing a malicious RTF or Excel attachment.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [ZxxZ](https://attack.mitre.org/software/S1013) can collect the username from a compromised host.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [ZxxZ](https://attack.mitre.org/software/S1013) can collect data from a compromised host.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [ZxxZ](https://attack.mitre.org/software/S1013) has used a XOR key to decrypt strings.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[BITTER\|G1002]] | BITTER |



## References

[^1]: [Cisco Talos Bitter Bangladesh May 2022](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)


