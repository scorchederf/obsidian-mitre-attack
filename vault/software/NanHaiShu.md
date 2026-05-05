---
aliases: 
    - S0228
    
mitre-attack: https://attack.mitre.org/software/S0228
---

## S0228

[NanHaiShu](https://attack.mitre.org/software/S0228) is a remote access tool and JScript backdoor used by [Leviathan](https://attack.mitre.org/groups/G0065). [NanHaiShu](https://attack.mitre.org/software/S0228) has been used to target government and private-sector organizations that have relations to the South China Sea dispute. [^3]  [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [NanHaiShu](https://attack.mitre.org/software/S0228) encodes files in Base64.[^2]  |
| [[JavaScript\|T1059.007]] | JavaScript | [NanHaiShu](https://attack.mitre.org/software/S0228) executes additional Jscript code on the victim's machine.[^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [NanHaiShu](https://attack.mitre.org/software/S0228) can change Internet Explorer settings to reduce warnings about malware activity.[^3]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [NanHaiShu](https://attack.mitre.org/software/S0228) executes additional VBScript code on the victim's machine.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [NanHaiShu](https://attack.mitre.org/software/S0228) can gather information about the victim proxy server.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [NanHaiShu](https://attack.mitre.org/software/S0228) can download additional files from URLs.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [NanHaiShu](https://attack.mitre.org/software/S0228) launches a script to delete their original decoy file to cover tracks.[^2]  |
| [[Mshta\|T1218.005]] | Mshta | [NanHaiShu](https://attack.mitre.org/software/S0228) uses mshta.exe to load its program and files.[^2]  |
| [[DNS\|T1071.004]] | DNS | [NanHaiShu](https://attack.mitre.org/software/S0228) uses DNS for the C2 communications.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [NanHaiShu](https://attack.mitre.org/software/S0228) modifies the %regrun% Registry to point itself to an autostart mechanism.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [NanHaiShu](https://attack.mitre.org/software/S0228) can gather the victim computer name and serial number.[^3]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [NanHaiShu](https://attack.mitre.org/software/S0228) collects the username from the victim.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Leviathan\|G0065]] | Leviathan |



## References

[^1]: [CISA AA21-200A APT40 July 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-200a)


[^2]: [fsecure NanHaiShu July 2016](https://www.f-secure.com/documents/996508/1030745/nanhaishu_whitepaper.pdf)


[^3]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)


[^4]: NanHaiShu


