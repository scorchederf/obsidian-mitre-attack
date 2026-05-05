---
aliases: 
    - S0062
    
mitre-attack: https://attack.mitre.org/software/S0062
---

## S0062

[DustySky](https://attack.mitre.org/software/S0062) is multi-stage malware written in .NET that has been used by [Molerats](https://attack.mitre.org/groups/G0021) since May 2015. [^3]  [^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [DustySky](https://attack.mitre.org/software/S0062) has used both HTTP and HTTPS for C2.[^3]  |
| [[Software Discovery\|T1518]] | Software Discovery | [DustySky](https://attack.mitre.org/software/S0062) lists all installed software for the infected machine.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [DustySky](https://attack.mitre.org/software/S0062) can delete files it creates from the infected system.[^1]  |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [DustySky](https://attack.mitre.org/software/S0062) searches for removable media and duplicates itself onto it.[^3]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | The [DustySky](https://attack.mitre.org/software/S0062) dropper uses a function to obfuscate the name of functions and other parts of the malware.[^3]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [DustySky](https://attack.mitre.org/software/S0062) can compress files via RAR while staging data to be exfiltrated.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [DustySky](https://attack.mitre.org/software/S0062) has exfiltrated data to the C2 server.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [DustySky](https://attack.mitre.org/software/S0062) contains a keylogger.[^3]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [DustySky](https://attack.mitre.org/software/S0062) can detect connected USB devices.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | The [DustySky](https://attack.mitre.org/software/S0062) dropper uses Windows Management Instrumentation to extract information about the operating system and whether an anti-virus is active.[^3]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [DustySky](https://attack.mitre.org/software/S0062) created folders in temp directories to host collected files before exfiltration.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [DustySky](https://attack.mitre.org/software/S0062) achieves persistence by creating a Registry entry in `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`.[^3]  |
| [[Screen Capture\|T1113]] | Screen Capture | [DustySky](https://attack.mitre.org/software/S0062) captures PNG screenshots of the main screen.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [DustySky](https://attack.mitre.org/software/S0062) checks for the existence of anti-virus.[^3]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [DustySky](https://attack.mitre.org/software/S0062) searches for network drives and removable media and duplicates itself onto them.[^3]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [DustySky](https://attack.mitre.org/software/S0062) has two hard-coded domains for C2 servers; if the first does not respond, it will try the second.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [DustySky](https://attack.mitre.org/software/S0062) extracts basic information about the operating system.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [DustySky](https://attack.mitre.org/software/S0062) collects information about running processes from victims.[^3] [^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [DustySky](https://attack.mitre.org/software/S0062) scans the victim for files that contain certain keywords and document types including PDF, DOC, DOCX, XLS, and XLSX, from a list that is obtained from the C2 as a text file. It can also identify logical drives for the infected machine.[^3] [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Molerats\|G0021]] | Molerats |



## References

[^1]: [Kaspersky MoleRATs April 2019](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)


[^2]: [DustySky2](http://www.clearskysec.com/wp-content/uploads/2016/06/Operation-DustySky2_-6.2016_TLP_White.pdf)


[^3]: [DustySky](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)


