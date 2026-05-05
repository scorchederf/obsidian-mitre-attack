---
aliases: 
    - S0381
    
mitre-attack: https://attack.mitre.org/software/S0381
---

## S0381

[FlawedAmmyy](https://attack.mitre.org/software/S0381) is a remote access tool (RAT) that was first seen in early 2016. The code for [FlawedAmmyy](https://attack.mitre.org/software/S0381) was based on leaked source code for a version of Ammyy Admin, a remote access software.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [FlawedAmmyy](https://attack.mitre.org/software/S0381) has used `cmd` to execute commands on a compromised host.[^5]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [FlawedAmmyy](https://attack.mitre.org/software/S0381) can collect the victim's operating system and computer name during the initial infection.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [FlawedAmmyy](https://attack.mitre.org/software/S0381) can collect keyboard events.[^5]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [FlawedAmmyy](https://attack.mitre.org/software/S0381) enumerates the current user during the initial infection.[^1] [^5]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [FlawedAmmyy](https://attack.mitre.org/software/S0381) leverages WMI to enumerate anti-virus on the victim.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [FlawedAmmyy](https://attack.mitre.org/software/S0381) has established persistence via the `HKCU\SOFTWARE\microsoft\windows\currentversion\run` registry key.[^5]  |
| [[PowerShell\|T1059.001]] | PowerShell | [FlawedAmmyy](https://attack.mitre.org/software/S0381) has used PowerShell to execute commands.[^5]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [FlawedAmmyy](https://attack.mitre.org/software/S0381) will attempt to detect anti-virus products during the initial infection.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [FlawedAmmyy](https://attack.mitre.org/software/S0381) has used `rundll32` for execution.[^5]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [FlawedAmmyy](https://attack.mitre.org/software/S0381) will attempt to detect if a usable smart card is current inserted into a card reader.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [FlawedAmmyy](https://attack.mitre.org/software/S0381) has used HTTP for C2.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [FlawedAmmyy](https://attack.mitre.org/software/S0381) has sent data collected from a compromised host to its C2 servers.[^5]  |
| [[Screen Capture\|T1113]] | Screen Capture | [FlawedAmmyy](https://attack.mitre.org/software/S0381) can capture screenshots.[^5]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [FlawedAmmyy](https://attack.mitre.org/software/S0381) can transfer files from C2.[^5]  |
| [[Input Capture\|T1056]] | Input Capture | [FlawedAmmyy](https://attack.mitre.org/software/S0381) can collect mouse events.[^5]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [FlawedAmmyy](https://attack.mitre.org/software/S0381) has used SEAL encryption during the initial C2 handshake.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [FlawedAmmyy](https://attack.mitre.org/software/S0381) has collected information and files from a compromised machine.[^5]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [FlawedAmmyy](https://attack.mitre.org/software/S0381) can collect clipboard data.[^5]  |
| [[Data Obfuscation\|T1001]] | Data Obfuscation | [FlawedAmmyy](https://attack.mitre.org/software/S0381) may obfuscate portions of the initial C2 handshake.[^1]  |
| [[Msiexec\|T1218.007]] | Msiexec | [FlawedAmmyy](https://attack.mitre.org/software/S0381) has been installed via `msiexec.exe`.[^5]   |
| [[File Deletion\|T1070.004]] | File Deletion | [FlawedAmmyy](https://attack.mitre.org/software/S0381) can execute batch scripts to delete files.[^5]  |
| [[Local Groups\|T1069.001]] | Local Groups | [FlawedAmmyy](https://attack.mitre.org/software/S0381) enumerates the privilege level of the victim during the initial infection.[^1] [^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN6\|G0037]] | FIN6 |
| [[TA505\|G0092]] | TA505 |



## References

[^1]: [Proofpoint TA505 Mar 2018](https://www.proofpoint.com/us/threat-insight/post/leaked-ammyy-admin-source-code-turned-malware)


[^2]: [Trend Micro TA505 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/shifting-tactics-breaking-down-ta505-groups-use-of-html-rats-and-other-techniques-in-latest-campaigns/)


[^3]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)


[^4]: [Visa FIN6 Feb 2019](https://usa.visa.com/dam/VCOM/global/support-legal/documents/fin6-cybercrime-group-expands-threat-To-ecommerce-merchants.pdf)


[^5]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)


