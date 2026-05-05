---
aliases: 
    - S1147
    
mitre-attack: https://attack.mitre.org/software/S1147
---

## S1147

[Nightdoor](https://attack.mitre.org/software/S1147) is a backdoor exclusively associated with [Daggerfly](https://attack.mitre.org/groups/G1034) operations. [Nightdoor](https://attack.mitre.org/software/S1147) uses common libraries with [MgBot](https://attack.mitre.org/software/S1146) and [MacMa](https://attack.mitre.org/software/S1016), linking these malware families together.[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Service\|T1102]] | Web Service | [Nightdoor](https://attack.mitre.org/software/S1147) can utilize Microsoft OneDrive or Google Drive for command and control purposes.[^2] [^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Nightdoor](https://attack.mitre.org/software/S1147) can collect information on installed applications via Windows registry keys, as well as collecting information on running processes.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Nightdoor](https://attack.mitre.org/software/S1147) uses scheduled tasks for persistence to load the final malware payload into memory.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Nightdoor](https://attack.mitre.org/software/S1147) can collect information about disk drives, their total and free space, and file system type.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Nightdoor](https://attack.mitre.org/software/S1147) creates a cmd.exe shell to send and receive commands from the command and control server via open pipes.[^1]  |
| [[Hijack Execution Flow\|T1574]] | Hijack Execution Flow | [Nightdoor](https://attack.mitre.org/software/S1147) uses a legitimate executable to load a malicious DLL file for installation.[^1]  |
| [[System Checks\|T1497.001]] | System Checks | [Nightdoor](https://attack.mitre.org/software/S1147) embeds code from the public `al-khaser` project, a repository that works to detect virtual machines, sandboxes, and malware analysis environments.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Nightdoor](https://attack.mitre.org/software/S1147) can identify the system local time information.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Nightdoor](https://attack.mitre.org/software/S1147) gathers information on victim system network configuration such as MAC addresses.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Nightdoor](https://attack.mitre.org/software/S1147) can self-delete.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Nightdoor](https://attack.mitre.org/software/S1147) gathers information on victim system users and usernames.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Nightdoor](https://attack.mitre.org/software/S1147) gathers information on the victim system such as CPU and Computer name as well as device drivers.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Nightdoor](https://attack.mitre.org/software/S1147) stores network configuration data in a file XOR encoded with the key value of `0x7A`.[^1]  |
| [[Application Layer Protocol\|T1071]] | Application Layer Protocol | [Nightdoor](https://attack.mitre.org/software/S1147) uses TCP and UDP communication for command and control traffic.[^2] [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Daggerfly\|G1034]] | Daggerfly |



## References

[^1]: [Symantec Daggerfly 2024](https://symantec-enterprise-blogs.security.com/threat-intelligence/daggerfly-espionage-updated-toolset)


[^2]: [ESET EvasivePanda 2024](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)


