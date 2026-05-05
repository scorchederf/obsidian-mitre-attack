---
aliases: 
    - S0452
    
mitre-attack: https://attack.mitre.org/software/S0452
---

## S0452

[USBferry](https://attack.mitre.org/software/S0452) is an information stealing malware and has been used by [Tropic Trooper](https://attack.mitre.org/groups/G0081) in targeted attacks against Taiwanese and Philippine air-gapped military environments. [USBferry](https://attack.mitre.org/software/S0452) shares an overlapping codebase with [YAHOYAH](https://attack.mitre.org/software/S0388), though it has several features which makes it a distinct piece of malware.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Local Account\|T1087.001]] | Local Account | [USBferry](https://attack.mitre.org/software/S0452) can use `net user` to gather information about local accounts.[^1] 	 |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [USBferry](https://attack.mitre.org/software/S0452) can use `net view` to gather information about remote systems.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [USBferry](https://attack.mitre.org/software/S0452) can detect the victim's file or folder list.[^1] 	 |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [USBferry](https://attack.mitre.org/software/S0452) can check for connected USB devices.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [USBferry](https://attack.mitre.org/software/S0452) can detect the infected machine's network topology using `ipconfig` and `arp`.[^1] 	 |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [USBferry](https://attack.mitre.org/software/S0452) can execute various Windows commands.[^1] 	 |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [USBferry](https://attack.mitre.org/software/S0452) can copy its installer to attached USB storage devices.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [USBferry](https://attack.mitre.org/software/S0452) can execute rundll32.exe in memory to avoid detection.[^1] 	 |
| [[Data from Local System\|T1005]] | Data from Local System | [USBferry](https://attack.mitre.org/software/S0452) can collect information from an air-gapped host machine.[^1] 	 |
| [[Process Discovery\|T1057]] | Process Discovery | [USBferry](https://attack.mitre.org/software/S0452) can use `tasklist` to gather information about the process running on the infected system.[^1] 	 |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [USBferry](https://attack.mitre.org/software/S0452) can use `netstat` and `nbtstat` to detect active network connections.[^1] 	 |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Tropic Trooper\|G0081]] | Tropic Trooper |



## References

[^1]: [TrendMicro Tropic Trooper May 2020](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)


