---
aliases: 
    - S1029
    
mitre-attack: https://attack.mitre.org/software/S1029
---

## S1029

[AuTo Stealer](https://attack.mitre.org/software/S1029) is malware written in C++ has been used by [SideCopy](https://attack.mitre.org/groups/G1008) since at least December 2021 to target government agencies and personnel in India and Afghanistan.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [AuTo Stealer](https://attack.mitre.org/software/S1029) can store collected data from an infected host to a file named `Hostname_UserName.txt` prior to exfiltration.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [AuTo Stealer](https://attack.mitre.org/software/S1029) can place malicious executables in a victim's AutoRun registry key or StartUp directory, depending on the AV product installed, to maintain persistence.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [AuTo Stealer](https://attack.mitre.org/software/S1029) has the ability to collect the username from an infected host.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [AuTo Stealer](https://attack.mitre.org/software/S1029) can use TCP to communicate with command and control servers.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell |  [AuTo Stealer](https://attack.mitre.org/software/S1029) can use `cmd.exe` to execute a created batch file.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [AuTo Stealer](https://attack.mitre.org/software/S1029) can exfiltrate data over actor-controlled C2 servers via HTTP or TCP.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [AuTo Stealer](https://attack.mitre.org/software/S1029) can use HTTP to communicate with its C2 servers.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [AuTo Stealer](https://attack.mitre.org/software/S1029) can collect data such as PowerPoint files, Word documents, Excel files, PDF files, text files, database files, and image files from an infected machine.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [AuTo Stealer](https://attack.mitre.org/software/S1029) has the ability to collect the hostname and OS information from an infected host.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [AuTo Stealer](https://attack.mitre.org/software/S1029) has the ability to collect information about installed AV products from an infected host.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[SideCopy\|G1008]] | SideCopy |



## References

[^1]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)


