---
aliases: 
    - S1132
    
mitre-attack: https://attack.mitre.org/software/S1132
---

## S1132

[IPsec Helper](https://attack.mitre.org/software/S1132) is a post-exploitation remote access tool linked to [Agrius](https://attack.mitre.org/groups/G1030) operations. This malware shares significant programming and functional overlaps with [Apostle](https://attack.mitre.org/software/S1133) ransomware, also linked to [Agrius](https://attack.mitre.org/groups/G1030). [IPsec Helper](https://attack.mitre.org/software/S1132) provides basic remote access tool functionality such as uploading files from victim systems, running commands, and deploying additional payloads.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Indicator Removal\|T1070]] | Indicator Removal | [IPsec Helper](https://attack.mitre.org/software/S1132) can delete various registry keys related to its execution and use.[^1]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [IPsec Helper](https://attack.mitre.org/software/S1132) can download additional payloads from command and control nodes and execute them.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [IPsec Helper](https://attack.mitre.org/software/S1132) can identify the process it is currently running under and its number, and pass this back to a command and control node.[^1]  |
| [[Clear Persistence\|T1070.009]] | Clear Persistence | [IPsec Helper](https://attack.mitre.org/software/S1132) can delete various service traces related to persistent execution when commanded.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [IPsec Helper](https://attack.mitre.org/software/S1132) can make arbitrary changes to registry keys based on provided input.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [IPsec Helper](https://attack.mitre.org/software/S1132) contains an embedded XML configuration file with an encrypted list of command and control servers. These are written to an external configuration file during execution.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [IPsec Helper](https://attack.mitre.org/software/S1132) can run arbitrary PowerShell commands passed to it.[^1]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [IPsec Helper](https://attack.mitre.org/software/S1132) can run arbitrary Visual Basic scripts and commands passed to it.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [IPsec Helper](https://attack.mitre.org/software/S1132) can identify specific files and folders for follow-on exfiltration.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [IPsec Helper](https://attack.mitre.org/software/S1132) can run arbitrary commands passed to it through `cmd.exe`.[^1]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [IPsec Helper](https://attack.mitre.org/software/S1132) will sleep for a random number of seconds, iterating 200 times over sleeps between one to three seconds, before continuing execution flow.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [IPsec Helper](https://attack.mitre.org/software/S1132) connects to command and control servers via HTTP POST requests based on parameters hard-coded into the malware.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [IPsec Helper](https://attack.mitre.org/software/S1132) exfiltrates specific files through its command and control framework.[^1]  |
| [[Service Execution\|T1569.002]] | Service Execution | [IPsec Helper](https://attack.mitre.org/software/S1132) is run as a Windows service in victim environments.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [IPsec Helper](https://attack.mitre.org/software/S1132) can delete itself when given the appropriate command.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Agrius\|G1030]] | Agrius |



## References

[^1]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)


