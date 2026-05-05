---
aliases: 
    - S0433
    
mitre-attack: https://attack.mitre.org/software/S0433
---

## S0433

[Rifdoor](https://attack.mitre.org/software/S0433) is a remote access trojan (RAT) that shares numerous code similarities with [HotCroissant](https://attack.mitre.org/software/S0431).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Rifdoor](https://attack.mitre.org/software/S0433) has encrypted strings with a single byte XOR algorithm.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Rifdoor](https://attack.mitre.org/software/S0433) has the ability to identify the Windows version on the compromised host.[^1]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [Rifdoor](https://attack.mitre.org/software/S0433) has added four additional bytes of data upon launching, then saved the changed version as `C:\ProgramData\Initech\Initech.exe`.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Rifdoor](https://attack.mitre.org/software/S0433) has the ability to identify the IP address of the compromised host.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Rifdoor](https://attack.mitre.org/software/S0433) has created a new registry entry at `HKEY_CURRENT_USERS\Software\Microsoft\Windows\CurrentVersion\Run\Graphics` with a value of `C:\ProgramData\Initech\Initech.exe /run`.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Rifdoor](https://attack.mitre.org/software/S0433) has been distributed in e-mails with malicious Excel or Word documents.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Rifdoor](https://attack.mitre.org/software/S0433) has encrypted command and control (C2) communications with a stream cipher.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Rifdoor](https://attack.mitre.org/software/S0433) has the ability to identify the username on the compromised host.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Rifdoor](https://attack.mitre.org/software/S0433) has been executed from malicious Excel or Word documents containing macros.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Andariel\|G0138]] | Andariel |



## References

[^1]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)


[^2]: [AhnLab Andariel Subgroup of Lazarus June 2018](https://web.archive.org/web/20230213154832/http://download.ahnlab.com/global/brochure/%5BAnalysis%5DAndariel_Group.pdf)


