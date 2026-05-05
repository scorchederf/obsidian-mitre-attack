---
aliases: 
    - S1150
    
mitre-attack: https://attack.mitre.org/software/S1150
---

## S1150

[ROADSWEEP](https://attack.mitre.org/software/S1150) is a ransomware that was deployed against Albanian government networks during [HomeLand Justice](https://attack.mitre.org/campaigns/C0038) along with the [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) backdoor.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File Deletion\|T1070.004]] | File Deletion | [ROADSWEEP](https://attack.mitre.org/software/S1150) can use embedded scripts to remove itself from the infected host.[^2] [^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | The [ROADSWEEP](https://attack.mitre.org/software/S1150) binary contains RC4 encrypted embedded scripts.[^2] [^1] [^3]  |
| [[Code Signing\|T1553.002]] | Code Signing | [ROADSWEEP](https://attack.mitre.org/software/S1150) has been digitally signed with a certificate issued to the Kuwait Telecommunications Company KSC.[^1]  |
| [[Inter-Process Communication\|T1559]] | Inter-Process Communication | [ROADSWEEP](https://attack.mitre.org/software/S1150) can pipe command output to a targeted process.[^2]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [ROADSWEEP](https://attack.mitre.org/software/S1150) can RC4 encrypt content in blocks on targeted systems.[^2] [^1] [^3]  |
| [[Internal Defacement\|T1491.001]] | Internal Defacement | [ROADSWEEP](https://attack.mitre.org/software/S1150) has dropped ransom notes in targeted folders prior to encrypting the files.[^3] <br> |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [ROADSWEEP](https://attack.mitre.org/software/S1150) can decrypt embedded scripts prior to execution.[^2] [^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [ROADSWEEP](https://attack.mitre.org/software/S1150) has been placed in the start up folder to trigger execution upon user login.[^3]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [ROADSWEEP](https://attack.mitre.org/software/S1150) can enumerate logical drives on targeted devices.[^2] [^3] <br> |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [ROADSWEEP](https://attack.mitre.org/software/S1150) can identify removable drives attached to the victim's machine.[^2]  |
| [[Service Stop\|T1489]] | Service Stop | [ROADSWEEP](https://attack.mitre.org/software/S1150) can disable critical services and processes.[^2]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [ROADSWEEP](https://attack.mitre.org/software/S1150) requires four command line arguments to execute correctly, otherwise it will produce a message box and halt execution.[^2] [^1] [^3] <br> |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [ROADSWEEP](https://attack.mitre.org/software/S1150) can enumerate files on infected devices and avoid encrypting files with .exe, .dll, 	.sys, .lnk, or . lck extensions.[^2] [^1] [^3]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [ROADSWEEP](https://attack.mitre.org/software/S1150) has the ability to disable `SystemRestore` and Volume Shadow Copies.[^2] [^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [ROADSWEEP](https://attack.mitre.org/software/S1150) can open cmd.exe to enable command execution.[^2] [^3]  |




## References

[^1]: [CISA Iran Albanian Attacks September 2022](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a)


[^2]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)


[^3]: [Microsoft Albanian Government Attacks September 2022](https://www.microsoft.com/en-us/security/blog/2022/09/08/microsoft-investigates-iranian-attacks-against-the-albanian-government/)


