---
aliases: 
    - Silence
    - Whisper Spider
mitre-attack: https://attack.mitre.org/groups/G0091
---

## G0091

[Silence](https://attack.mitre.org/groups/G0091) is a financially motivated threat actor targeting financial institutions in different countries. The group was first seen in June 2016. Their main targets reside in Russia, Ukraine, Belarus, Azerbaijan, Poland and Kazakhstan. They compromised various banking systems, including the Russian Central Bank's Automated Workstation Client, ATMs, and card processing.[^5] [^3]  

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [Silence](https://attack.mitre.org/groups/G0091) has used port 444 when sending data about the system from the client to the server.[^6] 	 |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Silence](https://attack.mitre.org/groups/G0091) has used scheduled tasks to stage its operation.[^5]  |
| [[Process Injection\|T1055]] | Process Injection | [Silence](https://attack.mitre.org/groups/G0091) has injected a DLL library containing a Trojan into the fwmain32.exe process.[^6]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Silence](https://attack.mitre.org/groups/G0091) has used `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`, `HKLM\Software\Microsoft\Windows\CurrentVersion\Run`, and the Startup folder to establish persistence.[^6] 	 |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Silence](https://attack.mitre.org/groups/G0091) has used VBS scripts.[^5]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Silence](https://attack.mitre.org/groups/G0091) can create, delete, or modify a specified Registry key or value.[^6]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Silence](https://attack.mitre.org/groups/G0091) has used RDP for lateral movement.[^6] 	 |
| [[Video Capture\|T1125]] | Video Capture | [Silence](https://attack.mitre.org/groups/G0091) has been observed making videos of victims to observe bank employees day to day activities.[^3] [^6]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Silence](https://attack.mitre.org/groups/G0091) has used JS scripts.[^5]  |
| [[Compiled HTML File\|T1218.001]] | Compiled HTML File | [Silence](https://attack.mitre.org/groups/G0091) has weaponized CHM files in their phishing campaigns.[^5] [^3] [^1] [^6]  |
| [[Software Deployment Tools\|T1072]] | Software Deployment Tools | [Silence](https://attack.mitre.org/groups/G0091) has used RAdmin, a remote software tool used to remotely control workstations and ATMs.[^6]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Silence](https://attack.mitre.org/groups/G0091) can capture victim screen activity.[^3] [^6]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Silence](https://attack.mitre.org/groups/G0091) has used environment variable string substitution for obfuscation.[^5]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Silence](https://attack.mitre.org/groups/G0091) has used [Winexe](https://attack.mitre.org/software/S0191) to install a service on the remote system.[^3] [^6]  |
| [[External Proxy\|T1090.002]] | External Proxy | [Silence](https://attack.mitre.org/groups/G0091) has used ProxyBot, which allows the attacker to redirect traffic from the current node to the backconnect server via Sock4\Socks5.[^6] 	 |
| [[Code Signing\|T1553.002]] | Code Signing | [Silence](https://attack.mitre.org/groups/G0091) has used a valid certificate to sign their primary loader Silence.Downloader (aka TrueBot).[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Silence](https://attack.mitre.org/groups/G0091) has downloaded additional modules and malware to victim’s machines.[^6] 	 |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Silence](https://attack.mitre.org/groups/G0091) has used compromised credentials to log on to other systems and escalate privileges.[^6]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Silence](https://attack.mitre.org/groups/G0091) has used Nmap to scan the corporate network, build a network topology, and identify vulnerable hosts.[^6] 	 |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Silence](https://attack.mitre.org/groups/G0091) has used the Farse6.1 utility (based on [Mimikatz](https://attack.mitre.org/software/S0002)) to extract credentials from lsass.exe.[^6]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Silence](https://attack.mitre.org/groups/G0091) has used PowerShell to download and execute payloads.[^5] [^6]  |
| [[Tool\|T1588.002]] | Tool | [Silence](https://attack.mitre.org/groups/G0091) has obtained and modified versions of publicly-available tools like [Empire](https://attack.mitre.org/software/S0363) and [PsExec](https://attack.mitre.org/software/S0029).[^1]  [^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Silence](https://attack.mitre.org/groups/G0091) has deleted artifacts, including scheduled tasks, communicates files from the C2 and other logs.[^5] [^6] 	 |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Silence](https://attack.mitre.org/groups/G0091) has sent emails with malicious DOCX, CHM, LNK and ZIP attachments. [^5] [^3] [^6]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Silence](https://attack.mitre.org/groups/G0091) has named its backdoor "WINWORD.exe".[^6]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Silence](https://attack.mitre.org/groups/G0091) attempts to get users to launch malicious attachments delivered via spearphishing emails.[^5] [^3] [^6]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Silence](https://attack.mitre.org/groups/G0091) has used Windows command-line to run commands.[^5] [^3] [^6]  |
| [[Native API\|T1106]] | Native API | [Silence](https://attack.mitre.org/groups/G0091) has leveraged the Windows API, including using CreateProcess() or ShellExecute(), to perform a variety of tasks.[^3] [^6]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Empire\|S0363]] | Empire | [^1]  |
| [[Winexe\|S0191]] | Winexe | [^3]  |
| [[SDelete\|S0195]] | SDelete | [^6]  |



## References

[^1]: [Group IB Silence Aug 2019](https://www.group-ib.com/resources/threat-research/silence_2.0.going_global.pdf)


[^2]: Silence


[^3]: [SecureList Silence Nov 2017](https://securelist.com/the-silence/83009/)


[^4]: Whisper Spider


[^5]: [Cyber Forensicator Silence Jan 2019](https://web.archive.org/web/20220119133748/https://cyberforensicator.com/2019/01/20/silence-dissecting-malicious-chm-files-and-performing-forensic-analysis/)


[^6]: [Group IB Silence Sept 2018](https://go.group-ib.com/report-silence-en?_gl=1*d1bh3a*_ga*MTIwMzM5Mzc5MS4xNjk4OTI5NzY4*_ga_QMES53K3Y2*MTcwNDcyMjU2OS40LjEuMTcwNDcyMzU1Mi41My4wLjA.)


[^7]: [Crowdstrike GTR2020 Mar 2020](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)


