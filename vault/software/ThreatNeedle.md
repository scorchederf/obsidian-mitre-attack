---
aliases: 
    - S0665
    
mitre-attack: https://attack.mitre.org/software/S0665
---

## S0665

[ThreatNeedle](https://attack.mitre.org/software/S0665) is a backdoor that has been used by [Lazarus Group](https://attack.mitre.org/groups/G0032) since at least 2019 to target cryptocurrency, defense, and mobile gaming organizations.  It is considered to be an advanced cluster of [Lazarus Group](https://attack.mitre.org/groups/G0032)'s Manuscrypt (a.k.a. NukeSped) malware family.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [ThreatNeedle](https://attack.mitre.org/software/S0665) can be loaded into the Startup folder (`%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\OneDrives.lnk`) as a Shortcut file for persistence.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [ThreatNeedle](https://attack.mitre.org/software/S0665) relies on a victim to click on a malicious document for initial execution.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [ThreatNeedle](https://attack.mitre.org/software/S0665) can run in memory and register its payload as a Windows service.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [ThreatNeedle](https://attack.mitre.org/software/S0665) can download additional tools to enable lateral movement.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [ThreatNeedle](https://attack.mitre.org/software/S0665) can collect system profile information from a compromised host.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [ThreatNeedle](https://attack.mitre.org/software/S0665) can obtain file and directory information.[^1]  |
| [[Compression\|T1027.015]] | Compression | [ThreatNeedle](https://attack.mitre.org/software/S0665) has been compressed and obfuscated.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [ThreatNeedle](https://attack.mitre.org/software/S0665) can collect data and files from a compromised host.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [ThreatNeedle](https://attack.mitre.org/software/S0665) has been compressed and obfuscated using RC4, AES, or XOR.[^1]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [ThreatNeedle](https://attack.mitre.org/software/S0665) can save its configuration data as a RC4-encrypted Registry key under `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\GameCon`.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [ThreatNeedle](https://attack.mitre.org/software/S0665) can modify the Registry to save its configuration data as the following RC4-encrypted Registry key: `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\GameCon`.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [ThreatNeedle](https://attack.mitre.org/software/S0665) can decrypt its payload using RC4, AES, or one-byte XORing.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [ThreatNeedle](https://attack.mitre.org/software/S0665) has been distributed via a malicious Word document within a spearphishing email.[^1]   |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [ThreatNeedle](https://attack.mitre.org/software/S0665) chooses its payload creation path from a randomly selected service name from netsvc.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: [Kaspersky ThreatNeedle Feb 2021](https://securelist.com/lazarus-threatneedle/100803/)


