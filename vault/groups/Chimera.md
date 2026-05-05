---
aliases: 
    - Chimera
mitre-attack: https://attack.mitre.org/groups/G0114
---

## G0114

[Chimera](https://attack.mitre.org/groups/G0114) is a suspected China-based threat group that has been active since at least 2018 targeting the semiconductor industry in Taiwan as well as data from the airline industry.[^2] [^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[DLL\|T1574.001]] | DLL | [Chimera](https://attack.mitre.org/groups/G0114) has used side loading to place malicious DLLs in memory.[^1]  |
| [[Remote Data Staging\|T1074.002]] | Remote Data Staging | [Chimera](https://attack.mitre.org/groups/G0114) has staged stolen data on designated servers in the target environment.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Chimera](https://attack.mitre.org/groups/G0114) has used scheduled tasks to invoke Cobalt Strike including through batch script `schtasks /create /ru "SYSTEM" /tn "update" /tr "cmd /c c:\windows\temp\update.bat" /sc once /f /st` and to maintain persistence.[^2] [^1]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Chimera](https://attack.mitre.org/groups/G0114) has used [PsExec](https://attack.mitre.org/software/S0029) to deploy beacons on compromised systems.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Chimera](https://attack.mitre.org/groups/G0114) has used [Cobalt Strike](https://attack.mitre.org/software/S0154) C2 beacons for data exfiltration.[^1]   |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Chimera](https://attack.mitre.org/groups/G0114) has used a valid account to maintain persistence via scheduled task.[^2]  |
| [[Pass the Hash\|T1550.002]] | Pass the Hash | [Chimera](https://attack.mitre.org/groups/G0114) has dumped password hashes for use in pass the hash authentication attacks.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Chimera](https://attack.mitre.org/groups/G0114) has used HTTPS for C2 communications.[^1]  |
| [[Native API\|T1106]] | Native API | [Chimera](https://attack.mitre.org/groups/G0114) has used direct Windows system calls by leveraging Dumpert.[^2]  |
| [[Domain Controller Authentication\|T1556.001]] | Domain Controller Authentication | [Chimera](https://attack.mitre.org/groups/G0114)'s malware has altered the NTLM authentication program on domain controllers to allow [Chimera](https://attack.mitre.org/groups/G0114) to login without a valid credential.[^2] 	 |
| [[DNS\|T1071.004]] | DNS | [Chimera](https://attack.mitre.org/groups/G0114) has used [Cobalt Strike](https://attack.mitre.org/software/S0154) to encapsulate C2 in DNS traffic.[^1]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has `nltest /domain_trusts` to identify domain trust relationships.[^1]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Chimera](https://attack.mitre.org/groups/G0114) has used gzip for Linux OS and a modified RAR software to archive data on Windows hosts.[^2] [^1]  |
| [[Windows Remote Management\|T1021.006]] | Windows Remote Management | [Chimera](https://attack.mitre.org/groups/G0114) has used WinRM for lateral movement.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has utilized multiple commands to identify data of interest in file and directory listings.[^1]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Chimera](https://attack.mitre.org/groups/G0114) has has used `net user /dom` and `net user Administrator` to enumerate domain accounts including administrator accounts.[^2] [^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used `tasklist` to enumerate processes.[^1]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Chimera](https://attack.mitre.org/groups/G0114) has used Windows admin shares to move laterally.[^2] [^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Chimera](https://attack.mitre.org/groups/G0114) has used PowerShell scripts to execute malicious payloads and the DSInternals PowerShell module to make use of Active Directory features.[^2] [^1] 	 |
| [[NTDS\|T1003.003]] | NTDS | [Chimera](https://attack.mitre.org/groups/G0114) has gathered the SYSTEM registry and ntds.dit files from target systems.[^2]  [Chimera](https://attack.mitre.org/groups/G0114) specifically has used the NtdsAudit tool to dump the password hashes of domain users via `msadcs.exe "NTDS.dit" -s "SYSTEM" -p RecordedTV_pdmp.txt --users-csv RecordedTV_users.csv` and used ntdsutil to copy the Active Directory database.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Chimera](https://attack.mitre.org/groups/G0114) has staged stolen data locally on compromised hosts.[^1]  |
| [[Sharepoint\|T1213.002]] | Sharepoint | [Chimera](https://attack.mitre.org/groups/G0114) has collected documents from the victim's SharePoint.[^1]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used `net share` and `net view` to identify network shares of interest.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Chimera](https://attack.mitre.org/groups/G0114) has renamed malware to GoogleUpdate.exe and WinRAR to jucheck.exe, RecordedTV.ms, teredo.tmp, update.exe, and msadcs1.exe.[^2]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Chimera](https://attack.mitre.org/groups/G0114) has copied tools between compromised hosts using SMB.[^1]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used `net start` and `net use` for system service discovery.[^1]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Chimera](https://attack.mitre.org/groups/G0114) has encoded PowerShell commands.[^2] 	 |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [Chimera](https://attack.mitre.org/groups/G0114) has cleared event logs on compromised hosts.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used [ipconfig](https://attack.mitre.org/software/S0100), [Ping](https://attack.mitre.org/software/S0097), and `tracert` to enumerate the IP address and network environment and settings of the local host.[^1]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used the `get -b <start ip> -e <end ip> -p` command for network scanning as well as a custom Python tool  packed into a Windows executable named Get.exe to scan IP ranges for HTTP.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used the `quser` command to show currently logged on users.[^1]   |
| [[Local Account\|T1087.001]] | Local Account | [Chimera](https://attack.mitre.org/groups/G0114) has used `net user` for account discovery.[^1]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Chimera](https://attack.mitre.org/groups/G0114) has encapsulated [Cobalt Strike](https://attack.mitre.org/software/S0154)'s C2 protocol in DNS and HTTPS.[^1]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [Chimera](https://attack.mitre.org/groups/G0114) has used compromised domain accounts to gain access to the target environment.[^1]  |
| [[Local Groups\|T1069.001]] | Local Groups | [Chimera](https://attack.mitre.org/groups/G0114) has used `net localgroup administrators` to identify  accounts with local administrative rights.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used `time /t` and `net time \\ip/hostname` for system time discovery.[^1]  |
| [[Password Policy Discovery\|T1201]] | Password Policy Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used the NtdsAudit utility to collect information related to accounts and passwords.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used `netstat -ano | findstr EST` to discover network connections.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Chimera](https://attack.mitre.org/groups/G0114) has used the Windows Command Shell and batch scripts for execution on compromised hosts.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Chimera](https://attack.mitre.org/groups/G0114) has performed file deletion to evade detection.[^2]   |
| [[Password Spraying\|T1110.003]] | Password Spraying | [Chimera](https://attack.mitre.org/groups/G0114) has used multiple password spraying attacks against victim's remote services to obtain valid user and administrator accounts.[^1]  |
| [[Local Email Collection\|T1114.001]] | Local Email Collection | [Chimera](https://attack.mitre.org/groups/G0114) has harvested data from victim's e-mail including through execution of `wmic /node:<ip> process call create "cmd /c copy c:\Users\<username>\<path>\backup.pst c:\windows\temp\backup.pst" copy "i:\<path>\<username>\My Documents\<filename>.pst"<br>copy`.[^1]  |
| [[Data from Network Shared Drive\|T1039]] | Data from Network Shared Drive | [Chimera](https://attack.mitre.org/groups/G0114) has collected data of interest from network shares.[^1]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Chimera](https://attack.mitre.org/groups/G0114) has used custom DLLs for continuous retrieval of data from memory.[^1]  |
| [[External Remote Services\|T1133]] | External Remote Services | [Chimera](https://attack.mitre.org/groups/G0114) has used legitimate credentials to login to an external VPN, Citrix, SSH, and other remote services.[^2] [^1]  |
| [[Credential Stuffing\|T1110.004]] | Credential Stuffing | [Chimera](https://attack.mitre.org/groups/G0114) has used credential stuffing against victim's remote services to obtain valid accounts.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used `fsutil fsinfo drives`, `systeminfo`, and `vssadmin list shadows` for system information including shadow volumes and drive information.[^1]  |
| [[Remote Email Collection\|T1114.002]] | Remote Email Collection | [Chimera](https://attack.mitre.org/groups/G0114) has harvested data from remote mailboxes including through execution of `\\<hostname>\c$\Users\<username>\AppData\Local\Microsoft\Outlook*.ost`.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [Chimera](https://attack.mitre.org/groups/G0114) has queried Registry keys using `reg query \\<host>\HKU\<SID>\SOFTWARE\Microsoft\Terminal Server Client\Servers` and `reg query \\<host>\HKU\<SID>\Software\Microsoft\Windows\CurrentVersion\Internet Settings`.[^1]  |
| [[Tool\|T1588.002]] | Tool | [Chimera](https://attack.mitre.org/groups/G0114) has obtained and used tools such as [BloodHound](https://attack.mitre.org/software/S0521), [Cobalt Strike](https://attack.mitre.org/software/S0154), [Mimikatz](https://attack.mitre.org/software/S0002), and [PsExec](https://attack.mitre.org/software/S0029).[^2] [^1]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Chimera](https://attack.mitre.org/groups/G0114) has exfiltrated stolen data to OneDrive accounts.[^1]  |
| [[Timestomp\|T1070.006]] | Timestomp | [Chimera](https://attack.mitre.org/groups/G0114) has used a Windows version of the Linux `touch` command to modify the date and time stamp on DLLs.[^1]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has utilized various scans and queries to find domain controllers and remote services in the target environment.[^1]  |
| [[Credentials\|T1589.001]] | Credentials | [Chimera](https://attack.mitre.org/groups/G0114) has collected credentials for the target organization from previous breaches for use in brute force attacks.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Chimera](https://attack.mitre.org/groups/G0114) has used WMIC to execute remote commands.[^2] [^1]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Chimera](https://attack.mitre.org/groups/G0114) has used RDP to access targeted systems.[^2]  |
| [[Multi-Factor Authentication Interception\|T1111]] | Multi-Factor Authentication Interception | [Chimera](https://attack.mitre.org/groups/G0114) has registered alternate phone numbers for compromised users to intercept 2FA codes sent via SMS.[^1]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used `type \\<hostname>\c$\Users\<username>\Favorites\Links\Bookmarks bar\Imported From IE\*citrix*` for bookmark discovery.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Chimera](https://attack.mitre.org/groups/G0114) has remotely copied tools and malware onto targeted systems.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^1]  |
| [[BloodHound\|S0521]] | BloodHound | [^2]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^2] [^1]  |
| [[esentutl\|S0404]] | esentutl | [^1]  |
| [[PsExec\|S0029]] | PsExec | [^1]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^2] [^1]  |



## References

[^1]: [NCC Group Chimera January 2021](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)


[^2]: [Cycraft Chimera April 2020](https://cycraft.com/download/CyCraft-Whitepaper-Chimera_V4.1.pdf)


[^3]: Chimera


