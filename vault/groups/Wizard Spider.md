---
aliases: 
    - Wizard Spider
    - UNC1878
    - TEMP.MixMaster
    - Grim Spider
    - FIN12
    - GOLD BLACKBURN
    - ITG23
    - Periwinkle Tempest
    - DEV-0193
    - Pistachio Tempest
    - DEV-0237
mitre-attack: https://attack.mitre.org/groups/G0102
---

## G0102

[Wizard Spider](https://attack.mitre.org/groups/G0102) is a Russia-based financially motivated threat group originally known for the creation and deployment of [TrickBot](https://attack.mitre.org/software/S0266) since at least 2016. [Wizard Spider](https://attack.mitre.org/groups/G0102) possesses a diverse arsenal of tools and has conducted ransomware campaigns against a variety of organizations, ranging from major corporations to hospitals.[^27] [^23] [^30] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Local Account\|T1136.001]] | Local Account | [Wizard Spider](https://attack.mitre.org/groups/G0102) has created local administrator accounts to maintain persistence in compromised networks.[^3]  |
| [[Code Signing Certificates\|T1588.003]] | Code Signing Certificates | [Wizard Spider](https://attack.mitre.org/groups/G0102) has obtained code signing certificates signed by DigiCert, GlobalSign, and COMOOD for malware payloads.[^24] [^3]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [Wizard Spider](https://attack.mitre.org/groups/G0102) has exploited or attempted to exploit Zerologon (CVE-2020-1472) and EternalBlue (MS17-010) vulnerabilities.[^31] [^20] [^4]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Wizard Spider](https://attack.mitre.org/groups/G0102) has archived data into ZIP files on compromised machines.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used `cmd.exe` to execute commands on a victim's machine.[^20] [^3]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used WMI and LDAP queries for network discovery and to move laterally. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also used batch scripts to leverage WMIC to deploy ransomware.[^13] [^23] [^31] [^2] [^3]  |
| [[Tool\|T1588.002]] | Tool | [Wizard Spider](https://attack.mitre.org/groups/G0102) has utilized tools such as [Empire](https://attack.mitre.org/software/S0363), [Cobalt Strike](https://attack.mitre.org/software/S0154), [Cobalt Strike](https://attack.mitre.org/software/S0154), [Rubeus](https://attack.mitre.org/software/S1071), [AdFind](https://attack.mitre.org/software/S0552), [BloodHound](https://attack.mitre.org/software/S0521), Metasploit, Advanced IP Scanner, Nirsoft PingInfoView, and SoftPerfect Network Scanner for targeting efforts.[^31] [^3]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Wizard Spider](https://attack.mitre.org/groups/G0102) has installed [TrickBot](https://attack.mitre.org/software/S0266) as a service named ControlServiceA in order to establish persistence.[^13] [^3]   |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used SMB to drop Cobalt Strike Beacon on a domain controller for lateral movement.[^24] [^20]  |
| [[Data Staged\|T1074]] | Data Staged | [Wizard Spider](https://attack.mitre.org/groups/G0102) has collected and staged credentials and network enumeration information, using  the networkdll and psfin [TrickBot](https://attack.mitre.org/software/S0266) modules.[^13]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used administrative accounts, including Domain Admin, to move laterally within a victim network.[^31]  |
| [[Process Injection\|T1055]] | Process Injection | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used process injection to execute payloads to escalate privileges.[^3]  |
| [[Remote Services\|T1021]] | Remote Services | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used the WebDAV protocol to execute [Ryuk](https://attack.mitre.org/software/S0446) payloads hosted on network file shares.[^3]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used RDP for lateral movement and to deploy ransomware interactively.[^13] [^23] [^24] [^3]  |
| [[Pass the Hash\|T1550.002]] | Pass the Hash | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used the `Invoke-SMBExec` PowerShell cmdlet to execute the pass-the-hash technique and utilized stolen password hashes to move laterally.[^3]  |
| [[Windows Permissions\|T1222.001]] | Windows Permissions | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used the icacls command to modify access control to backup servers, providing them with full control of all the system folders.[^16]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used stolen credentials to copy tools into the `%TEMP%` directory of domain controllers.[^13]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Wizard Spider](https://attack.mitre.org/groups/G0102) has lured victims to execute malware with spearphishing attachments containing macros to download either [Emotet](https://attack.mitre.org/software/S0367), Bokbot, [TrickBot](https://attack.mitre.org/software/S0266), or [Bazar](https://attack.mitre.org/software/S0534).[^13] [^30] [^3]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used scheduled tasks to establish persistence for [TrickBot](https://attack.mitre.org/software/S0266) and other malware.[^13] [^23] [^31] [^24] [^3]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Wizard Spider](https://attack.mitre.org/groups/G0102) used Base64 encoding to obfuscate an [Empire](https://attack.mitre.org/software/S0363) service and PowerShell commands.[^17] [^20]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used file deletion to remove some modules and configurations from an infected host after use.[^13]  |
| [[Group Policy Preferences\|T1552.006]] | Group Policy Preferences | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used PowerShell cmdlets `Get-GPPPassword` and `Find-GPOPassword` to find unsecured credentials in a compromised network group policy.[^3]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [Wizard Spider](https://attack.mitre.org/groups/G0102) has exfiltrated victim information using FTP.[^20] [^24]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Wizard Spider](https://attack.mitre.org/groups/G0102) has shut down or uninstalled security applications on victim systems that might prevent ransomware from executing.[^23] [^31] [^20] [^3]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used WMI to identify anti-virus products installed on a victim's machine.[^20]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Wizard Spider](https://attack.mitre.org/groups/G0102) has utilized `rundll32.exe` to deploy ransomware commands with the use of WebDAV.[^3]  |
| [[Kerberoasting\|T1558.003]] | Kerberoasting | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used Rubeus, MimiKatz Kerberos module, and the Invoke-Kerberoast cmdlet to steal AES hashes.[^20] [^31] [^23] [^24] [^3]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used macros to execute PowerShell scripts to download malware on victim's machines.[^13]  It has also used PowerShell to execute commands and move laterally through a victim network.[^23] [^31] [^2] [^3]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Wizard Spider](https://attack.mitre.org/groups/G0102) has exfiltrated stolen victim data to various cloud storage providers.[^3]   |
| [[Modify Registry\|T1112]] | Modify Registry | [Wizard Spider](https://attack.mitre.org/groups/G0102) has modified the Registry key `HKLM\System\CurrentControlSet\Control\SecurityProviders\WDigest` by setting the `UseLogonCredential` registry value to `1` in order to force credentials to be stored in clear text in memory. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also modified the WDigest registry key to allow plaintext credentials to be cached in memory.[^13] [^3]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used WMIC and vssadmin to manually delete volume shadow copies. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also used [Conti](https://attack.mitre.org/software/S0575) ransomware to delete volume shadow copies automatically with the use of vssadmin.[^3]   |
| [[External Remote Services\|T1133]] | External Remote Services | [Wizard Spider](https://attack.mitre.org/groups/G0102) has accessed victim networks by using stolen credentials to access the corporate VPN infrastructure.[^31]  |
| [[Winlogon Helper DLL\|T1547.004]] | Winlogon Helper DLL | [Wizard Spider](https://attack.mitre.org/groups/G0102) has established persistence using Userinit by adding the Registry key HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon.[^31]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used scheduled tasks to install [TrickBot](https://attack.mitre.org/software/S0266), using task names to appear legitimate such as WinDotNet, GoogleTask, or Sysnetsf.[^13]  It has also used common document file names for other malware binaries.[^31]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Wizard Spider](https://attack.mitre.org/groups/G0102) has identified domain admins through the use of `net group "Domain admins" /DOMAIN`. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also leveraged the PowerShell cmdlet `Get-ADComputer` to collect account names from Active Directory data.[^20] [^3]  |
| [[Backup Software Discovery\|T1518.002]] | Backup Software Discovery | [Wizard Spider](https://attack.mitre.org/groups/G0102) has utilized the PowerShell script `Get-DataInfo.ps1` to collect installed backup software information from a compromised machine.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used HTTP for network communications.[^13]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used Digicert code-signing certificates for some of its malware.[^24]  |
| [[Domain Account\|T1136.002]] | Domain Account | [Wizard Spider](https://attack.mitre.org/groups/G0102) has created and used new accounts within a victim's Active Directory environment to maintain persistence.[^3]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Wizard Spider](https://attack.mitre.org/groups/G0102) has staged ZIP files in local directories such as, `C:\PerfLogs\1\` and `C:\User\1\` prior to exfiltration.[^3]  |
| [[Name Resolution Poisoning and SMB Relay\|T1557.001]] | Name Resolution Poisoning and SMB Relay | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used the Invoke-Inveigh PowerShell cmdlets, likely for name service poisoning.[^31]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Wizard Spider](https://attack.mitre.org/groups/G0102) can transfer malicious payloads such as ransomware to compromised machines.[^3]  |
| [[NTDS\|T1003.003]] | NTDS | [Wizard Spider](https://attack.mitre.org/groups/G0102) has gained access to credentials via exported copies of the ntds.dit Active Directory database. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also created a volume shadow copy and used a batch script file to collect NTDS.dit with the use of the Windows utility, ntdsutil.[^31] [^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used [ipconfig](https://attack.mitre.org/software/S0100) to identify the network configuration of a victim machine. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also used the PowerShell cmdlet `Get-ADComputer` to collect IP address data from Active Directory.[^16] [^3]  |
| [[Email Accounts\|T1585.002]] | Email Accounts | [Wizard Spider](https://attack.mitre.org/groups/G0102) has leveraged ProtonMail email addresses in ransom notes when delivering [Ryuk](https://attack.mitre.org/software/S0446) ransomware.[^3]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used "whoami" to identify the local user and their privileges.[^16]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used valid credentials for privileged accounts with the goal of accessing domain controllers.[^13] [^3]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Wizard Spider](https://attack.mitre.org/groups/G0102) has lured victims into clicking a malicious link delivered through spearphishing.[^23]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Wizard Spider](https://attack.mitre.org/groups/G0102) has dumped the lsass.exe memory to harvest credentials with the use of open-source tool [LaZagne](https://attack.mitre.org/software/S0349).[^3]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Wizard Spider](https://attack.mitre.org/groups/G0102) has exfiltrated domain credentials and network enumeration information over command and control (C2) channels.[^13] [^3]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used spearphishing attachments to deliver Microsoft documents containing macros or PDFs containing malicious links to download either [Emotet](https://attack.mitre.org/software/S0367), Bokbot, [TrickBot](https://attack.mitre.org/software/S0266), or [Bazar](https://attack.mitre.org/software/S0534).[^13] [^2] [^3]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [Wizard Spider](https://attack.mitre.org/groups/G0102) has acquired credentials from the SAM/SECURITY registry hives.[^31]  |
| [[Service Stop\|T1489]] | Service Stop | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used taskkill.exe and net.exe to stop backup, catalog, cloud, and other services prior to network encryption.[^20]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Wizard Spider](https://attack.mitre.org/groups/G0102) has sent phishing emails containing a link to an actor-controlled Google Drive document or other free online file hosting services.[^23] [^24]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used networkdll for network discovery and psfin specifically for financial and point of sale indicators. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also used [AdFind](https://attack.mitre.org/software/S0552), `nltest/dclist`, and PowerShell script Get-DataInfo.ps1 to enumerate domain computers, including the domain controller.[^17] [^13] [^31] [^2] [^20] [^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Wizard Spider](https://attack.mitre.org/groups/G0102) has collected data from a compromised host prior to exfiltration.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used [Systeminfo](https://attack.mitre.org/software/S0096) and similar commands to acquire detailed configuration information of a victim's machine. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also utilized the PowerShell cmdlet `Get-ADComputer` to collect DNS hostnames, last logon dates, and operating system information from Active Directory.[^20] [^3]  |
| [[Windows Credential Manager\|T1555.004]] | Windows Credential Manager | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used PowerShell cmdlet `Invoke-WCMDump` to enumerate Windows credentials in the Credential Manager in a compromised network.[^3]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used the “net view” command to locate mapped network shares.[^23]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used `services.exe` to execute scripts and executables during lateral movement within a victim's network. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also used batch scripts that leverage [PsExec](https://attack.mitre.org/software/S0029) to execute a previously transferred ransomware payload on a victim's network.[^20] [^4] [^3]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Wizard Spider](https://attack.mitre.org/groups/G0102) has established persistence via the Registry key `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` and a shortcut within the startup folder.[^23] [^31]  |
| [[Windows Remote Management\|T1021.006]] | Windows Remote Management | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used Window Remote Management to move laterally through a victim network.[^23]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Wizard Spider](https://attack.mitre.org/groups/G0102) has injected malicious DLLs into memory with read, write, and execute permissions.[^23] [^24]  |
| [[BITS Jobs\|T1197]] | BITS Jobs | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used batch scripts that utilizes WMIC to execute a [BITSAdmin](https://attack.mitre.org/software/S0190) transfer of a ransomware payload to each compromised machine.[^3]   |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^27] [^2] [^31] [^20] [^24] [^4] [^16] [^3]  |
| [[BloodHound\|S0521]] | BloodHound | [^23] [^31] [^16] [^3]  |
| [[Empire\|S0363]] | Empire | [^13] [^23] [^31] [^3]  |
| [[BITSAdmin\|S0190]] | BITSAdmin | [^3]  |
| [[Nltest\|S0359]] | Nltest | [^31] [^20] [^24] [^4] [^16] [^2] [^3]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^31] [^23]  |
| [[LaZagne\|S0349]] | LaZagne | [^3]  |
| [[Ping\|S0097]] | Ping | [^20] [^23] [^4]  |
| [[Rubeus\|S1071]] | Rubeus | [^3]  |
| [[AdFind\|S0552]] | AdFind | [^17] [^20] [^24] [^2] [^3]  |
| [[PsExec\|S0029]] | PsExec | [^13] [^31] [^3]  |
| [[TrickBot\|S0266]] | TrickBot | [^13] [^23] [^16] [^30] [^3] [^19]  |
| [[Emotet\|S0367]] | Emotet | [^13] [^16]  |
| [[SystemBC\|S9001]] | SystemBC | [^19] [^11]  |
| [[Conti\|S0575]] | Conti | [^30] [^3] [^19]  |
| [[Diavol\|S0659]] | Diavol | [^19]  |
| [[Anchor\|S0504]] | Anchor | [^19]  |
| [[Dyre\|S0024]] | Dyre | [^29] [^6] [^22]  |
| [[Bazar\|S0534]] | Bazar | [^30] [^19]  |
| [[Ryuk\|S0446]] | Ryuk | [^27] [^2] [^23] [^31] [^20] [^24] [^4] [^16] [^30] [^3] [^19]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^31] [^23] [^20] [^24] [^4] [^16] [^30] [^3]  |
| [[GrimAgent\|S0632]] | GrimAgent | [^8]  |



## References

[^1]: DEV-0193


[^2]: [Red Canary Hospital Thwarted Ryuk October 2020](https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/)


[^3]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^4]: [DFIR Ryuk in 5 Hours October 2020](https://thedfirreport.com/2020/10/18/ryuk-in-5-hours/)


[^5]: GOLD BLACKBURN


[^6]: [CrowdStrike Wizard Spider March 2019](https://www.crowdstrike.com/blog/wizard-spider-lunar-spider-shared-proxy-module/)


[^7]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^8]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)


[^9]: [Secureworks Gold Blackburn Mar 2022](https://www.secureworks.com/research/threat-profiles/gold-blackburn)


[^10]: Pistachio Tempest


[^11]: [Microsoft_PistachioTempest_Jan2024](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/pistachio-tempest)


[^12]: Grim Spider


[^13]: [CrowdStrike Grim Spider May 2019](https://www.crowdstrike.com/blog/timelining-grim-spiders-big-game-hunting-tactics/)


[^14]: DEV-0237


[^15]: ITG23


[^16]: [Sophos New Ryuk Attack October 2020](https://news.sophos.com/en-us/2020/10/14/inside-a-new-ryuk-ransomware-attack/)


[^17]: [FireEye Ryuk and Trickbot January 2019](https://www.fireeye.com/blog/threat-research/2019/01/a-nasty-trick-from-credential-theft-malware-to-business-disruption.html)


[^18]: Periwinkle Tempest


[^19]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^20]: [DFIR Ryuk's Return October 2020](https://thedfirreport.com/2020/10/08/ryuks-return/)


[^21]: [IBM X-Force ITG23 Oct 2021](https://securityintelligence.com/posts/trickbot-gang-doubles-down-enterprise-infection/)


[^22]: [Malwarebytes TrickBot Sep 2019](https://blog.malwarebytes.com/trojans/2019/09/trickbot-adds-new-trick-to-its-arsenal-tampering-with-trusted-texts/)


[^23]: [DHS/CISA Ransomware Targeting Healthcare October 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-302a)


[^24]: [DFIR Ryuk 2 Hour Speed Run November 2020](https://thedfirreport.com/2020/11/05/ryuk-speed-run-2-hours-to-ransom/)


[^25]: UNC1878


[^26]: FIN12


[^27]: [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)


[^28]: TEMP.MixMaster


[^29]: [Forbes Dyre May 2017](https://www.forbes.com/sites/thomasbrewster/2017/05/04/dyre-hackers-stealing-millions-from-american-coporates/#601c77842a0a)


[^30]: [CrowdStrike Wizard Spider October 2020](https://www.crowdstrike.com/blog/wizard-spider-adversary-update/)


[^31]: [FireEye KEGTAP SINGLEMALT October 2020](https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html)


