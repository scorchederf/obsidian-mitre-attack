---
aliases: 
    - S0148
    
mitre-attack: https://attack.mitre.org/software/S0148
---

## S0148

[RTM](https://attack.mitre.org/software/S0148) is custom malware written in Delphi. It is used by the group of the same name ([RTM](https://attack.mitre.org/groups/G0048)). Newer versions of the malware have been reported publicly as Redaman.[^3] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [RTM](https://attack.mitre.org/software/S0148) can attempt to run the program as admin, then show a fake error message and a legitimate UAC bypass prompt to the user in an attempt to socially engineer the user into escalating privileges.[^3]  |
| [[Remote Access Tools\|T1219]] | Remote Access Tools | [RTM](https://attack.mitre.org/software/S0148) has the capability to download a VNC module from command and control (C2).[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [RTM](https://attack.mitre.org/software/S0148) uses the command line and rundll32.exe to execute.[^3]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [RTM](https://attack.mitre.org/software/S0148) collects data from the clipboard.[^3] [^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [RTM](https://attack.mitre.org/software/S0148) can record keystrokes from both the keyboard and virtual keyboard.[^3] [^2]  |
| [[Dynamic Resolution\|T1568]] | Dynamic Resolution | [RTM](https://attack.mitre.org/software/S0148) has resolved [Pony](https://attack.mitre.org/software/S0453) C2 server IP addresses by either converting Bitcoin blockchain transaction data to specific octets, or accessing IP addresses directly within the Namecoin blockchain.[^4] [^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [RTM](https://attack.mitre.org/software/S0148) has been delivered via spearphishing attachments disguised as PDF documents.[^2]  |
| [[Compression\|T1027.015]] | Compression |  [RTM](https://attack.mitre.org/software/S0148) has been delivered to targets as various archive files including ZIP, 7-ZIP, and RAR.[^3] [^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [RTM](https://attack.mitre.org/software/S0148) tries to add a Registry Run key under the name "Windows Update" to establish persistence.[^3]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [RTM](https://attack.mitre.org/software/S0148) can obtain a list of smart card readers attached to the victim.[^3] [^2]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [RTM](https://attack.mitre.org/software/S0148) can obtain the victim time zone.[^3]  |
| [[Dynamic Data Exchange\|T1559.002]] | Dynamic Data Exchange | [RTM](https://attack.mitre.org/software/S0148) can search for specific strings within browser tabs using a Dynamic Data Exchange mechanism.[^3]  |
| [[Code Signing\|T1553.002]] | Code Signing | [RTM](https://attack.mitre.org/software/S0148) samples have been signed with a code-signing certificates.[^3]  |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [RTM](https://attack.mitre.org/software/S0148) can detect if it is running within a sandbox or other virtualized analysis environment.[^2] 	 |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [RTM](https://attack.mitre.org/software/S0148) tries to add a scheduled task to establish persistence.[^3] [^2]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [RTM](https://attack.mitre.org/software/S0148) has named the scheduled task it creates "Windows Update".[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [RTM](https://attack.mitre.org/software/S0148) encrypts C2 traffic with a custom RC4 variant.[^3]  |
| [[Modify Registry\|T1112]] | Modify Registry | [RTM](https://attack.mitre.org/software/S0148) can delete all Registry entries created during its execution.[^3]  |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | [RTM](https://attack.mitre.org/software/S0148) has used an RSS feed on Livejournal to update a list of encrypted C2 server names. [RTM](https://attack.mitre.org/software/S0148) has also hidden [Pony](https://attack.mitre.org/software/S0453) C2 server IP addresses within transactions on the Bitcoin and Namecoin blockchain.[^3] [^4] [^2]  |
| [[Native API\|T1106]] | Native API | [RTM](https://attack.mitre.org/software/S0148) can use the `FindNextUrlCacheEntryA` and `FindFirstUrlCacheEntryA` functions to search for specific strings within browser history.[^3]  |
| [[Automated Collection\|T1119]] | Automated Collection | [RTM](https://attack.mitre.org/software/S0148) monitors browsing activity and automatically captures screenshots if a victim browses to a URL matching one of a list of strings.[^3] [^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [RTM](https://attack.mitre.org/software/S0148) can obtain the victim username and permissions.[^3]  |
| [[Install Root Certificate\|T1553.004]] | Install Root Certificate | [RTM](https://attack.mitre.org/software/S0148) can add a certificate to the Windows store.[^3] [^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [RTM](https://attack.mitre.org/software/S0148) has initiated connections to external domains using HTTPS.[^2] 	 |
| [[Rundll32\|T1218.011]] | Rundll32 | [RTM](https://attack.mitre.org/software/S0148) runs its core DLL file using rundll32.exe.[^3] [^2]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [RTM](https://attack.mitre.org/software/S0148) used Port 44443 for its VNC module.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [RTM](https://attack.mitre.org/software/S0148) can obtain the computer name, OS version, and default language identifier.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [RTM](https://attack.mitre.org/software/S0148) can download additional files.[^3] [^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [RTM](https://attack.mitre.org/software/S0148) can check for specific files and directories associated with virtualization and malware analysis.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [RTM](https://attack.mitre.org/software/S0148) strings, network data, configuration, and modules are encrypted with a modified RC4 algorithm.[^3] [^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [RTM](https://attack.mitre.org/software/S0148) can obtain information about security software on the victim.[^3]  |
| [[Malicious File\|T1204.002]] | Malicious File | [RTM](https://attack.mitre.org/software/S0148) has relied on users opening malicious email attachments, decompressing the attached archive, and double-clicking the executable within.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [RTM](https://attack.mitre.org/software/S0148) can obtain information about process integrity levels.[^3]  |
| [[Software Discovery\|T1518]] | Software Discovery | [RTM](https://attack.mitre.org/software/S0148) can scan victim drives to look for specific banking software on the machine to determine next actions.[^3]  |
| [[Screen Capture\|T1113]] | Screen Capture | [RTM](https://attack.mitre.org/software/S0148) can capture screenshots.[^3] [^2]  |
| [[Clear Persistence\|T1070.009]] | Clear Persistence | [RTM](https://attack.mitre.org/software/S0148) has the ability to remove Registry entries that it created for persistence.[^3]  |
| [[Masquerading\|T1036]] | Masquerading | [RTM](https://attack.mitre.org/software/S0148) has been delivered as archived Windows executable files masquerading as PDF documents.[^2] 	 |
| [[File Deletion\|T1070.004]] | File Deletion | [RTM](https://attack.mitre.org/software/S0148) can delete all files created during its execution.[^3] [^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[RTM\|G0048]] | RTM |



## References

[^1]: Redaman


[^2]: [Unit42 Redaman January 2019](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)


[^3]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)


[^4]: [CheckPoint Redaman October 2019](https://research.checkpoint.com/2019/ponys-cc-servers-hidden-inside-the-bitcoin-blockchain/)


