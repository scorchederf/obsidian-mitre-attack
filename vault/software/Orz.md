---
aliases: 
    - S0229
    
mitre-attack: https://attack.mitre.org/software/S0229
---

## S0229

[Orz](https://attack.mitre.org/software/S0229) is a custom JavaScript backdoor used by [Leviathan](https://attack.mitre.org/groups/G0065). It was observed being used in 2014 as well as in August 2017 when it was dropped by Microsoft Publisher files. [^6]  [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Orz](https://attack.mitre.org/software/S0229) can gather victim drive information.[^6]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Orz](https://attack.mitre.org/software/S0229) can execute shell commands.[^6]  [Orz](https://attack.mitre.org/software/S0229) can execute commands with JavaScript.[^6]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | Some [Orz](https://attack.mitre.org/software/S0229) versions have an embedded DLL known as MockDll that uses [Process Hollowing](https://attack.mitre.org/techniques/T1055/012) and regsvr32 to execute another payload.[^6]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [Orz](https://attack.mitre.org/software/S0229) has used Technet and Pastebin web pages for command and control.[^6]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Orz](https://attack.mitre.org/software/S0229) can gather a process list from the victim.[^6]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Orz](https://attack.mitre.org/software/S0229) can gather the victim OS version and whether it is 64 or 32 bit.[^6]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [Orz](https://attack.mitre.org/software/S0229) can overwrite Registry settings to reduce its visibility on the victim.[^6]  |
| [[Software Discovery\|T1518]] | Software Discovery | [Orz](https://attack.mitre.org/software/S0229) can gather the victim's Internet Explorer version.[^6]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Orz](https://attack.mitre.org/software/S0229) can download files onto the victim.[^6]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Orz](https://attack.mitre.org/software/S0229) can perform Registry operations.[^6]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Orz](https://attack.mitre.org/software/S0229) can gather victim proxy information.[^6]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | Some [Orz](https://attack.mitre.org/software/S0229) versions have an embedded DLL known as MockDll that uses process hollowing and [Regsvr32](https://attack.mitre.org/techniques/T1218/010) to execute another payload.[^6]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | Some [Orz](https://attack.mitre.org/software/S0229) strings are base64 encoded, such as the embedded DLL known as MockDll.[^6]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Leviathan\|G0065]] | Leviathan |



## References

[^1]: Orz


[^2]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)


[^3]: [CISA AA21-200A APT40 July 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-200a)


[^4]: [Accenture MUDCARP March 2019](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)


[^5]: AIRBREAK


[^6]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)


