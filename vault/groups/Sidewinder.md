---
aliases: 
    - Sidewinder
    - T-APT-04
    - Rattlesnake
mitre-attack: https://attack.mitre.org/groups/G0121
---

## G0121

[Sidewinder](https://attack.mitre.org/groups/G0121) is a suspected Indian threat actor group that has been active since at least 2012. They have been observed targeting government, military, and business entities throughout Asia, primarily focusing on Pakistan, China, Nepal, and Afghanistan.[^2] [^3] [^4] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Sidewinder](https://attack.mitre.org/groups/G0121) has exploited vulnerabilities to gain execution including CVE-2017-11882 and CVE-2020-0674.[^2] [^4]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Sidewinder](https://attack.mitre.org/groups/G0121) has used the Windows service `winmgmts:\\.\root\SecurityCenter2` to check installed antivirus products.[^1]  |
| [[Mshta\|T1218.005]] | Mshta | [Sidewinder](https://attack.mitre.org/groups/G0121) has used `mshta.exe` to execute malicious payloads.[^1] [^7]  |
| [[Spearphishing Link\|T1598.003]] | Spearphishing Link | [Sidewinder](https://attack.mitre.org/groups/G0121) has sent e-mails with malicious links to credential harvesting websites.[^2]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Sidewinder](https://attack.mitre.org/groups/G0121) has used tools to obtain the current system time.[^2]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Sidewinder](https://attack.mitre.org/groups/G0121) has sent e-mails with malicious links often crafted for specific targets.[^2] [^4]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Sidewinder](https://attack.mitre.org/groups/G0121) has collected stolen files in a temporary folder in preparation for exfiltration.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Sidewinder](https://attack.mitre.org/groups/G0121) has used tools to identify running processes on the victim's machine.[^2]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Sidewinder](https://attack.mitre.org/groups/G0121) has used JavaScript to drop and execute malware loaders.[^2] [^7]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Sidewinder](https://attack.mitre.org/groups/G0121) has used base64 encoding and ECDH-P256 encryption for payloads.[^2] [^1] [^4]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [Sidewinder](https://attack.mitre.org/groups/G0121) has configured tools to automatically send collected files to attacker controlled servers.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Sidewinder](https://attack.mitre.org/groups/G0121) has used LNK files to download remote files to the victim's network.[^2] [^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Sidewinder](https://attack.mitre.org/groups/G0121) has added paths to executables in the Registry to establish persistence.[^1] [^7] [^4]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Sidewinder](https://attack.mitre.org/groups/G0121) has used HTTP in C2 communications.[^2] [^1] [^7]  |
| [[Dynamic Data Exchange\|T1559.002]] | Dynamic Data Exchange | [Sidewinder](https://attack.mitre.org/groups/G0121) has used the ActiveXObject utility to create OLE objects to obtain execution through Internet Explorer.[^1] [^7]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Sidewinder](https://attack.mitre.org/groups/G0121) has used malware to collect information on files and directories.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Sidewinder](https://attack.mitre.org/groups/G0121) has used malware to collect information on network interfaces, including the MAC address.[^2]  |
| [[Spearphishing Attachment\|T1598.002]] | Spearphishing Attachment | [Sidewinder](https://attack.mitre.org/groups/G0121) has sent e-mails with malicious attachments that lead victims to credential harvesting websites.[^2] [^1] [^4]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Sidewinder](https://attack.mitre.org/groups/G0121) has used base64 encoding for scripts.[^2] [^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Sidewinder](https://attack.mitre.org/groups/G0121) has used PowerShell to drop and execute malware loaders.[^2]  |
| [[Software Discovery\|T1518]] | Software Discovery | [Sidewinder](https://attack.mitre.org/groups/G0121) has used tools to enumerate software installed on an infected host.[^2] [^1]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Sidewinder](https://attack.mitre.org/groups/G0121) has used VBScript to drop and execute malware loaders.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Sidewinder](https://attack.mitre.org/groups/G0121) has used tools to collect the computer name, OS version, installed hotfixes, as well as information regarding the memory and processor on a compromised host.[^2] [^7]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Sidewinder](https://attack.mitre.org/groups/G0121) has used tools to automatically collect system and network configuration information.[^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Sidewinder](https://attack.mitre.org/groups/G0121) has sent e-mails with malicious attachments often crafted for specific targets.[^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Sidewinder](https://attack.mitre.org/groups/G0121) has named malicious files `rekeywiz.exe` to match the name of a legitimate Windows executable.[^7]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Sidewinder](https://attack.mitre.org/groups/G0121) has lured targets to click on malicious links to gain execution in the target environment.[^2] [^1] [^7] [^4]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Sidewinder](https://attack.mitre.org/groups/G0121) has lured targets to click on malicious files to gain execution in the target environment.[^2] [^1] [^7] [^4]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Sidewinder](https://attack.mitre.org/groups/G0121) has used tools to identify the user of a compromised host.[^2]  |
| [[DLL\|T1574.001]] | DLL | [Sidewinder](https://attack.mitre.org/groups/G0121) has used DLL side-loading to drop and execute malicious payloads including the hijacking of the legitimate Windows application file rekeywiz.exe.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Koadic\|S0250]] | Koadic | [^2]  |



## References

[^1]: [Rewterz Sidewinder APT April 2020](https://www.rewterz.com/threats/sidewinder-apt-group-campaign-analysis)


[^2]: [ATT Sidewinder January 2021](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)


[^3]: [Securelist APT Trends April 2018](https://securelist.com/apt-trends-report-q1-2018/85280/)


[^4]: [Cyble Sidewinder September 2020](https://cybleinc.com/2020/09/26/sidewinder-apt-targets-with-futuristic-tactics-and-techniques/)


[^5]: T-APT-04


[^6]: Rattlesnake


[^7]: [Rewterz Sidewinder COVID-19 June 2020](https://www.rewterz.com/articles/analysis-on-sidewinder-apt-group-covid-19)


