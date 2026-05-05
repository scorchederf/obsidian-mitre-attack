---
aliases: 
    - S0461
    
mitre-attack: https://attack.mitre.org/software/S0461
---

## S0461

[SDBbot](https://attack.mitre.org/software/S0461) is a backdoor with installer and loader components that has been used by [TA505](https://attack.mitre.org/groups/G0092) since at least 2019.[^1] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to get directory listings or drive information on a compromised host.[^1]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to clean up and remove data structures from a compromised host.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to decrypt and decompress its payload to enable code execution.[^1] [^3]  |
| [[Proxy\|T1090]] | Proxy | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to use port forwarding to establish a proxy between a target host and C2.[^1]  |
| [[Application Shimming\|T1546.011]] | Application Shimming | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to use application shimming for persistence if it detects it is running as admin on Windows XP or 7, by creating a shim database to patch services.exe.[^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to inject a downloaded DLL into a newly created rundll32.exe process.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [SDBbot](https://attack.mitre.org/software/S0461) has used rundll32.exe to execute DLLs.[^2]  |
| [[Software Packing\|T1027.002]] | Software Packing | [SDBbot](https://attack.mitre.org/software/S0461) has used a packed installer file.[^3]  |
| [[System Location Discovery\|T1614]] | System Location Discovery | [SDBbot](https://attack.mitre.org/software/S0461) can collected the country code of a compromised machine.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to add a value to the Registry Run key to establish persistence if it detects it is running with regular user privilege. [^1] [^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to access the file system on a compromised host.[^1]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to use RDP to connect to victim's machines.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to download a DLL from C2 to a compromised host.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to identify the OS version, OS bit information and computer name.[^1] [^2]  |
| [[Video Capture\|T1125]] | Video Capture | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to record video on a compromised host.[^1] [^3]  |
| [[Image File Execution Options Injection\|T1546.012]] | Image File Execution Options Injection | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to use image file execution options for persistence if it detects it is running with admin privileges on a Windows version newer than Windows 7.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to determine the domain name and whether a proxy is configured on a compromised host.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to identify the user on a compromised host.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to communicate with C2 with TCP over port 443.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [SDBbot](https://attack.mitre.org/software/S0461) has sent collected data from a compromised host to its C2 servers.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [SDBbot](https://attack.mitre.org/software/S0461) can enumerate a list of running processes on a compromised machine.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to use the command shell to execute commands on a compromised host.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to XOR the strings for its installer component with a hardcoded 128 byte key.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to delete files from a compromised host.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA505\|G0092]] | TA505 |



## References

[^1]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)


[^2]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)


[^3]: [IBM TA505 April 2020](https://web.archive.org/web/20200420201624/https://securityintelligence.com/posts/ta505-continues-to-infect-networks-with-sdbbot-rat/)


