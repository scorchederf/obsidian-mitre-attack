---
aliases: 
    - S0446
    
mitre-attack: https://attack.mitre.org/software/S0446
---

## S0446

[Ryuk](https://attack.mitre.org/software/S0446) is a ransomware designed to target enterprise environments that has been used in attacks since at least 2018. [Ryuk](https://attack.mitre.org/software/S0446) shares code similarities with Hermes ransomware.[^14] [^10] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Ryuk](https://attack.mitre.org/software/S0446) can use anti-disassembly and code transformation obfuscation techniques.[^15]  |
| [[Native API\|T1106]] | Native API | [Ryuk](https://attack.mitre.org/software/S0446) has used multiple native APIs including `ShellExecuteW` to run executables,`GetWindowsDirectoryW` to create folders, and `VirtualAlloc`, `WriteProcessMemory`, and `CreateRemoteThread` for process injection.[^14]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Ryuk](https://attack.mitre.org/software/S0446) has called `CreateToolhelp32Snapshot` to enumerate all running processes.[^14]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Ryuk](https://attack.mitre.org/software/S0446) has used the C$ network share for lateral movement.[^6]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Ryuk](https://attack.mitre.org/software/S0446) has enumerated files and folders on all mounted drives.[^14] 	 |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Ryuk](https://attack.mitre.org/software/S0446) has used `vssadmin Delete Shadows /all /quiet` to to delete volume shadow copies and `vssadmin resize shadowstorage` to force deletion of shadow copies created by third-party applications.[^14]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [Ryuk](https://attack.mitre.org/software/S0446) has been observed to query the registry key `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Nls\Language` and the value `InstallLanguage`. If the machine has the value 0x419 (Russian), 0x422 (Ukrainian), or 0x423 (Belarusian), it stops execution.[^14]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [Ryuk](https://attack.mitre.org/software/S0446) can use stolen domain admin accounts to move laterally within a victim domain.[^4]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Ryuk](https://attack.mitre.org/software/S0446) has used `cmd.exe` to create a Registry entry to establish persistence.[^14]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Ryuk](https://attack.mitre.org/software/S0446) has constructed legitimate appearing installation folder paths by calling `GetWindowsDirectoryW` and then inserting a null byte at the fourth character of the path. For Windows Vista or higher, the path would appear as `C:\Users\Public`.[^14]  |
| [[Service Stop\|T1489]] | Service Stop | [Ryuk](https://attack.mitre.org/software/S0446) has called `kill.bat` for stopping services, disabling services and killing processes.[^14]  |
| [[Windows Permissions\|T1222.001]] | Windows Permissions | [Ryuk](https://attack.mitre.org/software/S0446) can launch `icacls <path> /grant Everyone:F /T /C /Q` to delete every access-based restrictions on files and directories.[^4]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Ryuk](https://attack.mitre.org/software/S0446) has stopped services related to anti-virus.[^10]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Ryuk](https://attack.mitre.org/software/S0446) can remotely create a scheduled task to execute itself on a system.[^4]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Ryuk](https://attack.mitre.org/software/S0446) has called `GetLogicalDrives` to emumerate all mounted drives, and `GetDriveTypeW` to determine the drive type.[^14]  |
| [[Traffic Signaling\|T1205]] | Traffic Signaling | [Ryuk](https://attack.mitre.org/software/S0446) has used Wake-on-Lan to power on turned off systems for lateral movement.[^6]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Ryuk](https://attack.mitre.org/software/S0446) has used a combination of symmetric (AES) and asymmetric (RSA) encryption to encrypt files. Files have been encrypted with their own AES key and given a file extension of .RYK. Encrypted directories have had a ransom note of RyukReadMe.txt written to the directory.[^14] [^15]  |
| [[Process Injection\|T1055]] | Process Injection | [Ryuk](https://attack.mitre.org/software/S0446) has injected itself into remote processes to encrypt files using a combination of `VirtualAlloc`, `WriteProcessMemory`, and `CreateRemoteThread`.[^14]  |
| [[Masquerading\|T1036]] | Masquerading | [Ryuk](https://attack.mitre.org/software/S0446) can create .dll files that actually contain a Rich Text File format document.[^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Ryuk](https://attack.mitre.org/software/S0446) has used the Windows command line to create a Registry entry under `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` to establish persistence.[^14]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Ryuk](https://attack.mitre.org/software/S0446) has called `GetIpNetTable` in attempt to identify all mounted drives and hosts that have Address Resolution Protocol (ARP) entries.[^14] [^6]   |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [Ryuk](https://attack.mitre.org/software/S0446) has attempted to adjust its token privileges to have the `SeDebugPrivilege`.[^14]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Wizard Spider\|G0102]] | Wizard Spider |
| [[FIN6\|G0037]] | FIN6 |



## References

[^1]: [Red Canary Hospital Thwarted Ryuk October 2020](https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/)


[^2]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^3]: [FireEye FIN6 Apr 2019](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)


[^4]: [ANSSI RYUK RANSOMWARE](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-006.pdf)


[^5]: [DFIR Ryuk in 5 Hours October 2020](https://thedfirreport.com/2020/10/18/ryuk-in-5-hours/)


[^6]: [Bleeping Computer - Ryuk WoL](https://www.bleepingcomputer.com/news/security/ryuk-ransomware-uses-wake-on-lan-to-encrypt-offline-devices/)


[^7]: [DHS/CISA Ransomware Targeting Healthcare October 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-302a)


[^8]: [Sophos New Ryuk Attack October 2020](https://news.sophos.com/en-us/2020/10/14/inside-a-new-ryuk-ransomware-attack/)


[^9]: [DFIR Ryuk 2 Hour Speed Run November 2020](https://thedfirreport.com/2020/11/05/ryuk-speed-run-2-hours-to-ransom/)


[^10]: [FireEye Ryuk and Trickbot January 2019](https://www.fireeye.com/blog/threat-research/2019/01/a-nasty-trick-from-credential-theft-malware-to-business-disruption.html)


[^11]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^12]: [DFIR Ryuk's Return October 2020](https://thedfirreport.com/2020/10/08/ryuks-return/)


[^13]: [FireEye KEGTAP SINGLEMALT October 2020](https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html)


[^14]: [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)


[^15]: [CrowdStrike Wizard Spider October 2020](https://www.crowdstrike.com/blog/wizard-spider-adversary-update/)


[^16]: Ryuk


