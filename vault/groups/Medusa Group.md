---
aliases: 
    - Medusa Group
mitre-attack: https://attack.mitre.org/groups/G1051
---

## G1051

[Medusa Group](https://attack.mitre.org/groups/G1051) has been active since at least 2021 and was initially operated as a closed ransomware group before evolving into a Ransomware-as-a-Service (RaaS) operation. Some reporting indicates that certain attacks may still be conducted directly by the ransomware’s core developers. Public sources have also referred to the group as “Spearwing” or “Medusa Actors.” [^4]  [^1]  [Medusa Group](https://attack.mitre.org/groups/G1051) employs living-off-the-land techniques, frequently leveraging publicly available tools and common remote management software to conduct operations. The group engages in double extortion tactics, exfiltrating data prior to encryption and threatening to publish stolen information if ransom demands are not met. [^2]  For initial access, [Medusa Group](https://attack.mitre.org/groups/G1051) has exploited publicly known vulnerabilities, conducted phishing campaigns, and used credentials or access purchased from Initial Access Brokers (IABs). The group is opportunistic and has targeted a wide range of sectors globally. [^5] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has deleted recovery files such as shadow copies using `vssadmin.exe`.[^3] [^4] [^1] [^2]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized Windows Management Instrumentation to query system information.[^3] [^4] [^5]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized legitimate software services such as PDQ Deploy to transfer malicious binaries and tools to other victimized hosts within the target environment.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Medusa Group](https://attack.mitre.org/groups/G1051) has used vulnerable or signed drivers to modify security solutions on victim devices.[^4]  |
| [[Service Stop\|T1489]] | Service Stop | [Medusa Group](https://attack.mitre.org/groups/G1051) has terminated services related to backups, security, databases, communication, filesharing and websites.[^4] [^1] [^2]  |
| [[Native API\|T1106]] | Native API | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged Windows Native API functions to execute payloads.[^2]  |
| [[Web Services\|T1583.006]] | Web Services | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized a file hosting service named filemail[.]com to host a zip file that contained malicious payloads that facilitated follow-on actions.[^3]  |
| [[Upload Tool\|T1608.002]] | Upload Tool | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized a file hosting service called filemail[.]com to host a zip file that contained a RMM service such as ConnectWise.[^3]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Medusa Group](https://attack.mitre.org/groups/G1051) has obfuscated PowerShell scripts with Base64 encoding.[^4]  [Medusa Group](https://attack.mitre.org/groups/G1051) has also obfuscated the code of dropped kernel drivers using a software known as Safengine Shielden which randomized the code through code mutations and then leveraged an embedded virtual machine interpreter to execute the code.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has searched for files within the victim environment for encryption and exfiltration.[^3] [^4] [^2]  [Medusa Group](https://attack.mitre.org/groups/G1051) has also identified files associated with remote management services.[^3] [^4]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Medusa Group](https://attack.mitre.org/groups/G1051) has modified Registry keys to elevate privileges, maintain persistence and allow remote access.[^4]  |
| [[Tool\|T1588.002]] | Tool | [Medusa Group](https://attack.mitre.org/groups/G1051) has obtained and leveraged numerous RMM services, along with publicly available tools used for scanning.[^3] [^4] [^1]  [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized tools such as Advanced IP Scanner and SoftPerfect Network scanner for user, system and network discovery.[^4]  [Medusa Group](https://attack.mitre.org/groups/G1051) has also acquired tools for command and control and defense evasion which include tunneling tools Ligolo and Cloudflared.[^4] <br> |
| [[Local Account\|T1087.001]] | Local Account | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged `net user` for account discovery.[^1]  |
| [[Social Media Accounts\|T1585.001]] | Social Media Accounts | [Medusa Group](https://attack.mitre.org/groups/G1051) has created social media accounts including Telegram and X to publicize their activities.[^3] [^6]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized [Rclone](https://attack.mitre.org/software/S1040) to exfiltrate data from victim environments to cloud storage.[^4] [^1]  |
| [[Clear Command History\|T1070.003]] | Clear Command History | [Medusa Group](https://attack.mitre.org/groups/G1051) has cleared command history by running the PowerShell command `Remove-Item (Get-PSReadlineOption).HistorySavePath`.[^4]  |
| [[Acquire Access\|T1650]] | Acquire Access | [Medusa Group](https://attack.mitre.org/groups/G1051) has purchased user credentials and other sensitive data from Initial Access Brokers (IABs).[^3] [^6] [^4] [^5]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Medusa Group](https://attack.mitre.org/groups/G1051) has communicated through reverse or bind shells over port 443 (HTTPS).[^4]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized [PsExec](https://attack.mitre.org/software/S0029) to execute batch scripts that modify firewall settings.[^4]   [Medusa Group](https://attack.mitre.org/groups/G1051) has also enabled and modified firewall rules to allow for RDP connections for lateral movement and device interactions.[^4]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized the `ShowWindow` API function to hide the current window.[^2]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has identified network shares using `cmd.exe /c net share`.[^4]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [Medusa Group](https://attack.mitre.org/groups/G1051) has used TOR nodes for communications.[^3] [^6] [^1]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged public facing vulnerabilities in their campaigns against victim organizations to gain initial access.[^3] [^1]  [Medusa Group](https://attack.mitre.org/groups/G1051) has also utilized CVE-2024-1709 in ScreenConnect, and CVE-2023-48788 in Fortinet EMS for initial access to victim environments.[^4]  |
| [[MMC\|T1218.014]] | MMC | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged Microsoft Management Console (MMC) to facilitate lateral movement and to interact locally or remotely with victim devices using the command `mmc.exe compmgmt.msc /computer:{hostname/ip}`.[^4]  |
| [[Email Accounts\|T1585.002]] | Email Accounts | [Medusa Group](https://attack.mitre.org/groups/G1051) has created email accounts used in ransomware negotiations.[^4]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized compromised legitimate local and domain accounts within the victim environment to facilitate remote access and lateral movement sometimes in combination with [PsExec](https://attack.mitre.org/software/S0029).[^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged [certutil](https://attack.mitre.org/software/S0160), PowerShell, and Windows Command to download additional tools to include RMM services.[^4]  [Medusa Group](https://attack.mitre.org/groups/G1051) has also engaged in “Bring Your Own Vulnerable Driver” (BYOVD) and downloaded vulnerable or signed drivers to the victim environment to disable security tools.[^4] [^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized a hard-coded security tool process list that identifies and terminates using an undocumented IOCTL code 0x222094.[^3]  |
| [[Component Object Model\|T1559.001]] | Component Object Model | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged Component Object Model (COM) to bypass UAC.[^5]  |
| [[Remote Access Tools\|T1219]] | Remote Access Tools | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged Remote Access Software for lateral movement and data exfiltration.[^3] [^4] [^1] [^2]  [Medusa Group](https://attack.mitre.org/groups/G1051) has also been known to utilize Remote Access Software such as AnyDesk, Atera, ConnectWise, eHorus, N-Able, PDQ Deploy, PDQ Inventory, SimpleHelp and Splashtop.[^4]  |
| [[NTDS\|T1003.003]] | NTDS | [Medusa Group](https://attack.mitre.org/groups/G1051) has accessed the ntds.dit file to engage in credential dumping.[^1]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has used PDQ Inventory to get an inventory of the endpoints on the network.[^1]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized [PsExec](https://attack.mitre.org/software/S0029) to execute scripts and commands within victim environments.[^3] [^4] [^1]  [Medusa Group](https://attack.mitre.org/groups/G1051) has also used the Windows service RoboCopy to search and copy data for exfiltration.[^1]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged [Mimikatz](https://attack.mitre.org/software/S0002) to dump LSASS to harvest credentials.[^4]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Medusa Group](https://attack.mitre.org/groups/G1051) has used HTTPS for command and control.[^4]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Medusa Group](https://attack.mitre.org/groups/G1051) has encrypted files using AES-256 encryption which then appends the file extension “.medusa” to encrypted files and leaves a ransomware note named “!READ_ME_MEDUSA!!!.txt.”[^3] [^4] [^1] [^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged PowerShell for execution and defense evasion.[^6] [^4] [^5]  [Medusa Group](https://attack.mitre.org/groups/G1051) has also utilized PowerShell to execute a bitsadmin transfer from file hosting site.[^3]  |
| [[Domain Account\|T1136.002]] | Domain Account | [Medusa Group](https://attack.mitre.org/groups/G1051) has created a domain account within the victim environment.[^4]  |
| [[Financial Theft\|T1657]] | Financial Theft | [Medusa Group](https://attack.mitre.org/groups/G1051) has stolen and encrypted victims' data in order to extort victims into paying a ransom.[^3] [^6] [^4] [^5] [^1] [^2]  |
| [[Device Driver Discovery\|T1652]] | Device Driver Discovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has queried drivers on the victim device through the command `driverquery`.[^4]  |
| [[Prevent Command History Logging\|T1690]] | Prevent Command History Logging | [Medusa Group](https://attack.mitre.org/groups/G1051) has removed PowerShell command history through the use of the PSReadLine module by running the PowerShell command `Remove-Item (Get-PSReadlineOption).HistorySavePath`.[^4]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Medusa Group](https://attack.mitre.org/groups/G1051) has packed the code of dropped kernel drivers using the packer ASM Guard.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Medusa Group](https://attack.mitre.org/groups/G1051) has deleted previously installed tools.[^4]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Medusa Group](https://attack.mitre.org/groups/G1051) has used Windows Command Prompt to control and execute commands on the system to include ingress, network, and filesystem enumeration activities.[^4]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized the `net group` command to query domain groups within the victim environment.[^4]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized vulnerable or signed drivers to kill or delete services associated with endpoint detection and response (EDR) tools.[^4]  |
| [[Web Shell\|T1505.003]] | Web Shell | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized webshells to an exploited Microsoft Exchange Server.[^3]  |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [Medusa Group](https://attack.mitre.org/groups/G1051) has manually turned off and encrypted virtual machines.[^4]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has detected security solutions for termination or deletion within the victim device using hard-coded lists of strings containing security product executables.[^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has obtained host network details utilizing the command `cmd.exe /c ipconfig /all`.[^4]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Medusa Group](https://attack.mitre.org/groups/G1051) has terminated antivirus services utilizing the gaze.exe executable and utilizing `psexec.exe`.[^3] [^4] [^1]  [Medusa Group](https://attack.mitre.org/groups/G1051) has also leveraged I/O control codes (IOCTLs) for terminating and deleting processes of identified security tools.[^3]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has the capability to use living off the land (LOTL) binaries to perform network enumeration.[^4]  [Medusa Group](https://attack.mitre.org/groups/G1051) has also utilized the publicly available scanning tool SoftPerfect Network Scanner (`netscan.exe`) to discover device hostnames and network services.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized [PsExec](https://attack.mitre.org/software/S0029) to execute `quser` to discover the user session information.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged `cmd.exe` to identify system info `cmd.exe /c systeminfo`.[^4]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Medusa Group](https://attack.mitre.org/groups/G1051) has used RDP to conduct lateral movement and exfiltrate data.[^4]  [Medusa Group](https://attack.mitre.org/groups/G1051) has also utilized the Windows executable `mstsc.exe` for RDP activities through the command `mstsc.exe /v:{hostname/ip}`.[^4]  |
| [[Software Deployment Tools\|T1072]] | Software Deployment Tools | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized software deployment and management solutions to deploy their encryption payload to include BigFix and PDQ Deploy.[^4]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Medusa Group](https://attack.mitre.org/groups/G1051) has attempted to bypass UAC using Component Object Model (COM) interface.[^5]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[certutil\|S0160]] | certutil | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized [certutil](https://attack.mitre.org/software/S0160) to download additional tools within victim environments.[^4]  |
| [[Rclone\|S1040]] | Rclone | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged [Rclone](https://attack.mitre.org/software/S1040) to exfiltrate data from victim environments.[^4] [^1]  |
| [[Mimikatz\|S0002]] | Mimikatz | [Medusa Group](https://attack.mitre.org/groups/G1051) has used [Mimikatz](https://attack.mitre.org/software/S0002) to dump LSASS for credential harvesting.[^4]  |
| [[PsExec\|S0029]] | PsExec | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized [PsExec](https://attack.mitre.org/software/S0029) to facilitate execution, lateral movement, defense evasion, and exfiltration.[^4]  |
| [[Medusa Ransomware\|S1244]] | Medusa Ransomware | [Medusa Group](https://attack.mitre.org/groups/G1051) has used [Medusa Ransomware](https://attack.mitre.org/software/S1244) for ransomware activities.[^3] [^4] [^1] [^2]  |



## References

[^1]: [Broadcom Medusa Ransomware Medusa Group March 2025](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)


[^2]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)


[^3]: [Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)


[^4]: [CISA Medusa Group Medusa Ransomware March 2025](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)


[^5]: [Intel471 Medusa Ransomware May 2025](https://www.intel471.com/blog/threat-hunting-case-study-medusa-ransomware)


[^6]: [Check Point Medusa Ransomware April 2025](https://www.checkpoint.com/cyber-hub/threat-prevention/ransomware/medusa-ransomware-group/)


