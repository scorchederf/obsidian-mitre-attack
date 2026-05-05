---
aliases: 
    - S0251
    
mitre-attack: https://attack.mitre.org/software/S0251
---

## S0251

[Zebrocy](https://attack.mitre.org/software/S0251) is a Trojan that has been used by [APT28](https://attack.mitre.org/groups/G0007) since at least November 2015. The malware comes in several programming language variants, including C++, Delphi, AutoIt, C#, VB.NET, and Golang. [^5] [^1] [^2] [^4]  

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Zebrocy](https://attack.mitre.org/software/S0251) gathers the current time zone and date information from the system.[^10] [^4]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Zebrocy](https://attack.mitre.org/software/S0251) uses the `tasklist` and `wmic process get Capture, ExecutablePath` commands to gather the processes running on the system.[^1] [^10] [^2] [^11] [^8]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | One variant of [Zebrocy](https://attack.mitre.org/software/S0251) uses WMI queries to gather information.[^2]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Zebrocy](https://attack.mitre.org/software/S0251) uses `netstat -aon` to gather network connection information.[^11]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Zebrocy](https://attack.mitre.org/software/S0251) obtains additional code to execute on the victim's machine, including the downloading of a secondary payload.[^5] [^1] [^11] [^8]  |
| [[Screen Capture\|T1113]] | Screen Capture | A variant of [Zebrocy](https://attack.mitre.org/software/S0251) captures screenshots of the victim’s machine in JPEG and BMP format.[^1] [^10] [^2] [^11] [^8] [^4]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [Zebrocy](https://attack.mitre.org/software/S0251) enumerates information about connected storage devices.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Zebrocy](https://attack.mitre.org/software/S0251) gets the username from the system.[^10] [^4]  |
| [[Credential API Hooking\|T1056.004]] | Credential API Hooking | [Zebrocy](https://attack.mitre.org/software/S0251) installs an application-defined Windows hook to get notified when a network drive has been attached, so it can then use the hook to call its RecordToFile file stealing method.[^9]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Zebrocy](https://attack.mitre.org/software/S0251) has exfiltrated data to the designated C2 server using HTTP POST requests.[^8] [^4]   |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Zebrocy](https://attack.mitre.org/software/S0251) collects the OS version and computer name. [Zebrocy](https://attack.mitre.org/software/S0251) also runs the `systeminfo` command to gather system information. [^5] [^1] [^10] [^2] [^11] [^8] [^4]  |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [Zebrocy](https://attack.mitre.org/software/S0251) uses SMTP and POP3 for C2.[^5] [^1] [^10] [^2] [^11]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Zebrocy](https://attack.mitre.org/software/S0251) uses HTTP for C2.[^5] [^1] [^10] [^2] [^11] [^8]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Zebrocy](https://attack.mitre.org/software/S0251) runs the `ipconfig /all` command.[^11]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Zebrocy](https://attack.mitre.org/software/S0251) searches for files that are 60mb and less and contain the following extensions: .doc, .docx, .xls, .xlsx, .ppt, .pptx, .exe, .zip, and .rar. [Zebrocy](https://attack.mitre.org/software/S0251) also runs the `echo %APPDATA%` command to list the contents of the directory.[^9] [^10] [^11]  [Zebrocy](https://attack.mitre.org/software/S0251) can obtain the current execution path as well as perform drive enumeration.[^8] [^4]   |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Zebrocy](https://attack.mitre.org/software/S0251) creates an entry in a Registry Run key for the malware to execute on startup.[^10] [^11] [^8]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Zebrocy](https://attack.mitre.org/software/S0251)'s Delphi variant was packed with UPX.[^2] [^8]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Zebrocy](https://attack.mitre.org/software/S0251) collects the serial number for the storage volume C:\.[^5] [^1] [^10] [^2] [^11] [^8] [^4]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Zebrocy](https://attack.mitre.org/software/S0251)  has used a method similar to RC4 as well as AES for encryption and hexadecimal for encoding data before exfiltration. [^9] [^10] [^4]   |
| [[Logon Script (Windows)\|T1037.001]] | Logon Script (Windows) | [Zebrocy](https://attack.mitre.org/software/S0251) performs persistence with a logon script via adding to the Registry key `HKCU\Environment\UserInitMprLogonScript`.[^10]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Zebrocy](https://attack.mitre.org/software/S0251) uses cmd.exe to execute commands on the system.[^11] [^4]   |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Zebrocy](https://attack.mitre.org/software/S0251) uses SSL and AES ECB for encrypting C2 communications.[^10] [^11] [^4]   |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Zebrocy](https://attack.mitre.org/software/S0251) stores all collected information in a single file before exfiltration.[^10]  |
| [[Query Registry\|T1012]] | Query Registry | [Zebrocy](https://attack.mitre.org/software/S0251) executes the `reg query` command to obtain information in the Registry.[^11]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Zebrocy](https://attack.mitre.org/software/S0251) has a command to delete files and directories.[^10] [^11] [^4]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Zebrocy](https://attack.mitre.org/software/S0251) has used URL/Percent Encoding on data exfiltrated via HTTP POST requests.[^8]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Zebrocy](https://attack.mitre.org/software/S0251) identifies network drives when they are added to victim systems.[^9]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Zebrocy](https://attack.mitre.org/software/S0251) decodes its secondary payload and writes it to the victim’s machine. [Zebrocy](https://attack.mitre.org/software/S0251) also uses AES and XOR to decrypt strings and payloads.[^1] [^10]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Zebrocy](https://attack.mitre.org/software/S0251) scans the system and automatically collects files with the following extensions: .doc, .docx, ,.xls, .xlsx, .pdf, .pptx, .rar, .zip, .jpg, .jpeg, .bmp, .tiff, .kum, .tlg, .sbx, .cr, .hse, .hsf, and .lhz.[^10] [^11]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Zebrocy](https://attack.mitre.org/software/S0251) has a command to create a scheduled task for persistence.[^4]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Zebrocy](https://attack.mitre.org/software/S0251) has the capability to upload dumper tools that extract credentials from web browsers and store them in database files.[^11]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT28\|G0007]] | APT28 |



## References

[^1]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)


[^2]: [Unit42 Sofacy Dec 2018](https://unit42.paloaltonetworks.com/dear-joohn-sofacy-groups-global-campaign/)


[^3]: Zebrocy


[^4]: [CISA Zebrocy Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)


[^5]: [Palo Alto Sofacy 06-2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-sofacy-groups-parallel-attacks/)


[^6]: [CyberScoop APT28 Nov 2018](https://www.cyberscoop.com/apt28-brexit-phishing-accenture/)


[^7]: Zekapab


[^8]: [Accenture SNAKEMACKEREL Nov 2018](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)


[^9]: [Securelist Sofacy Feb 2018](https://securelist.com/a-slice-of-2017-sofacy-activity/83930/)


[^10]: [ESET Zebrocy Nov 2018](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)


[^11]: [ESET Zebrocy May 2019](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)


