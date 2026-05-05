---
aliases: 
    - Aoqin Dragon
mitre-attack: https://attack.mitre.org/groups/G1007
---

## G1007

[Aoqin Dragon](https://attack.mitre.org/groups/G1007) is a suspected Chinese cyber espionage threat group that has been active since at least 2013. [Aoqin Dragon](https://attack.mitre.org/groups/G1007) has primarily targeted government, education, and telecommunication organizations in Australia, Cambodia, Hong Kong, Singapore, and Vietnam. Security researchers noted a potential association between [Aoqin Dragon](https://attack.mitre.org/groups/G1007) and UNC94, based on malware, infrastructure, and targets.[^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Malicious File\|T1204.002]] | Malicious File | [Aoqin Dragon](https://attack.mitre.org/groups/G1007) has lured victims into opening weaponized documents, fake external drives, and fake antivirus to execute malicious payloads.[^1]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Aoqin Dragon](https://attack.mitre.org/groups/G1007) has spread malware in target networks by copying modules to folders masquerading as removable devices.[^1]  |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [Aoqin Dragon](https://attack.mitre.org/groups/G1007) has used a dropper that employs a worm infection strategy using a removable device to breach a secure network environment.[^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Aoqin Dragon](https://attack.mitre.org/groups/G1007) has used the Themida packer to obfuscate malicious payloads.[^1]  |
| [[Malware\|T1587.001]] | Malware | [Aoqin Dragon](https://attack.mitre.org/groups/G1007) has used custom malware, including [Mongall](https://attack.mitre.org/software/S1026) and [Heyoka Backdoor](https://attack.mitre.org/software/S1027), in their operations.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Aoqin Dragon](https://attack.mitre.org/groups/G1007) has run scripts to identify file formats including Microsoft Word.[^1]  |
| [[Masquerading\|T1036]] | Masquerading | [Aoqin Dragon](https://attack.mitre.org/groups/G1007) has used fake icons including antivirus and external drives to disguise malicious payloads.[^1]  |
| [[Tool\|T1588.002]] | Tool | [Aoqin Dragon](https://attack.mitre.org/groups/G1007) obtained the Heyoka open source exfiltration tool and subsequently modified it for their operations.[^1]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Aoqin Dragon](https://attack.mitre.org/groups/G1007) has exploited CVE-2012-0158 and CVE-2010-3333 for execution against targeted systems.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Mongall\|S1026]] | Mongall | [^1]  |
| [[Heyoka Backdoor\|S1027]] | Heyoka Backdoor | [^1]  |



## References

[^1]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)


