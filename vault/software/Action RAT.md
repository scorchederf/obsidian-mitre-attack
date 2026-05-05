---
aliases: 
    - S1028
    
mitre-attack: https://attack.mitre.org/software/S1028
---

## S1028

[Action RAT](https://attack.mitre.org/software/S1028) is a  remote access tool written in Delphi that has been used by [SideCopy](https://attack.mitre.org/groups/G1008) since at least December 2021 against Indian and Afghani government personnel.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Action RAT](https://attack.mitre.org/software/S1028) can use Base64 to decode actor-controlled C2 server communications.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Action RAT](https://attack.mitre.org/software/S1028) has the ability to download additional payloads onto an infected machine.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Action RAT](https://attack.mitre.org/software/S1028) can use WMI to gather AV products installed on an infected host.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Action RAT](https://attack.mitre.org/software/S1028) can use HTTP to communicate with C2 servers.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Action RAT](https://attack.mitre.org/software/S1028) has the ability to collect the MAC address of an infected host.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information |  [Action RAT](https://attack.mitre.org/software/S1028)'s commands, strings, and domains can be Base64 encoded within the payload.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Action RAT](https://attack.mitre.org/software/S1028) has the ability to collect the hostname, OS version, and OS architecture of an infected host.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Action RAT](https://attack.mitre.org/software/S1028) has the ability to collect drive and file information on an infected machine.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery |  [Action RAT](https://attack.mitre.org/software/S1028) has the ability to collect the username from an infected host.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Action RAT](https://attack.mitre.org/software/S1028) can identify AV products on an infected host using the following command: `cmd.exe WMIC /Node:localhost /Namespace:\\root\SecurityCenter2 Path AntiVirusProduct Get displayName /Format:List`.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Action RAT](https://attack.mitre.org/software/S1028) can collect local data from an infected machine.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Action RAT](https://attack.mitre.org/software/S1028) can use `cmd.exe` to execute commands on an infected host.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[SideCopy\|G1008]] | SideCopy |



## References

[^1]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)


