---
aliases: 
    - S1182
    
mitre-attack: https://attack.mitre.org/software/S1182
---

## S1182

[MagicRAT](https://attack.mitre.org/software/S1182) is a remote access tool developed in C++ and exclusively used by the [Lazarus Group](https://attack.mitre.org/groups/G0032) threat actor in operations. [MagicRAT](https://attack.mitre.org/software/S1182) allows for arbitrary command execution on victim machines and provides basic remote access functionality.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File Deletion\|T1070.004]] | File Deletion | [MagicRAT](https://attack.mitre.org/software/S1182) can delete files on victim systems, including itself.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [MagicRAT](https://attack.mitre.org/software/S1182) can import and execute additional payloads.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [MagicRAT](https://attack.mitre.org/software/S1182) stores configuration data in files and file paths mimicking legitimate operating system resources.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [MagicRAT](https://attack.mitre.org/software/S1182) allows for the execution of arbitrary commands on the victim system.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [MagicRAT](https://attack.mitre.org/software/S1182) stores base64 encoded command and contorl URLs in a configuraiton file, with each URL prefixed with the value `LR02DPt22R`.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [MagicRAT](https://attack.mitre.org/software/S1182) can persist via scheduled tasks.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [MagicRAT](https://attack.mitre.org/software/S1182) uses HTTP POST communication for command and control.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [MagicRAT](https://attack.mitre.org/software/S1182) collects system network information using commands such as `ipconfig /all`.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [MagicRAT](https://attack.mitre.org/software/S1182) exfiltrates data via HTTP over existing command and control channels.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [MagicRAT](https://attack.mitre.org/software/S1182) can persist using malicious LNK objects in the victim machine Startup folder.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [MagicRAT](https://attack.mitre.org/software/S1182) collects basic system information from victim machines.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [MagicRAT](https://attack.mitre.org/software/S1182) stores command and control URLs using base64 encoding in the malware's configuration file.[^1]  |
| [[Masquerade File Type\|T1036.008]] | Masquerade File Type | [MagicRAT](https://attack.mitre.org/software/S1182) can download additional executable payloads that masquerade as GIF files.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: [Cisco MagicRAT 2022](https://blog.talosintelligence.com/lazarus-magicrat/)


