---
aliases: 
    - S1025
    
mitre-attack: https://attack.mitre.org/software/S1025
---

## S1025

[Amadey](https://attack.mitre.org/software/S1025) is a Trojan bot that has been used since at least October 2018.[^2] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Amadey](https://attack.mitre.org/software/S1025) has searched for folders associated with antivirus software.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Amadey](https://attack.mitre.org/software/S1025) has obfuscated strings such as antivirus vendor names, domains, files, and others.[^3]  |
| [[Fast Flux DNS\|T1568.001]] | Fast Flux DNS | [Amadey](https://attack.mitre.org/software/S1025) has used fast flux DNS for its C2.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Amadey](https://attack.mitre.org/software/S1025) has checked for a variety of antivirus products.[^2] [^3]  |
| [[Native API\|T1106]] | Native API | [Amadey](https://attack.mitre.org/software/S1025) has used a variety of Windows API calls, including `GetComputerNameA`, `GetUserNameA`, and `CreateProcessA`.[^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Amadey](https://attack.mitre.org/software/S1025) can collect information from a compromised host.[^3]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Amadey](https://attack.mitre.org/software/S1025) has sent victim data to its C2 servers.[^3]  |
| [[Mark-of-the-Web Bypass\|T1553.005]] | Mark-of-the-Web Bypass | [Amadey](https://attack.mitre.org/software/S1025) has modified the `:Zone.Identifier` in the ADS area to zero.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Amadey](https://attack.mitre.org/software/S1025) can download and execute files to further infect a host machine with additional malware.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Amadey](https://attack.mitre.org/software/S1025) has collected the computer name and OS version from a compromised machine.[^2] [^3]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Amadey](https://attack.mitre.org/software/S1025) has overwritten registry keys for persistence.[^3]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Amadey](https://attack.mitre.org/software/S1025) has changed the Startup folder to the one containing its executable by overwriting the registry keys.[^2] [^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Amadey](https://attack.mitre.org/software/S1025) has decoded antivirus name strings.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Amadey](https://attack.mitre.org/software/S1025) has collected the user name from a compromised host using `GetUserNameA`.[^3]  |
| [[System Location Discovery\|T1614]] | System Location Discovery | [Amadey](https://attack.mitre.org/software/S1025) does not run any tasks or install additional malware if the victim machine is based in Russia.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Amadey](https://attack.mitre.org/software/S1025) has used HTTP for C2 communications.[^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Amadey](https://attack.mitre.org/software/S1025) can identify the IP address of a victim machine.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Kimsuky\|G0094]] | Kimsuky |
| [[TA505\|G0092]] | TA505 |



## References

[^1]: [Mandiant APT43 March 2024](https://services.google.com/fh/files/misc/apt43-report-en.pdf)


[^2]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)


[^3]: [BlackBerry Amadey 2020](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)


