---
aliases: 
    - S1242
    
mitre-attack: https://attack.mitre.org/software/S1242
---

## S1242

[Qilin](https://attack.mitre.org/software/S1242) is a ransomware family operated as a ransomware-as-a-service (RaaS) that has been active since at least 2022. It includes variants written in Go and Rust capable of targeting Windows, Linux, and VMware ESXi environments. [Qilin](https://attack.mitre.org/software/S1242) shares functionality overlaps with [Black Basta](https://attack.mitre.org/software/S1070), [REvil](https://attack.mitre.org/software/S0496), and [BlackCat](https://attack.mitre.org/software/S1068) ransomware. [Qilin](https://attack.mitre.org/software/S1242) affiliates have targeted multiple entities worldwide with the majority of victims in the US, France, Canada, and the UK, primarily in the manufacturing, technology, financial services, and healthcare sectors.[^4] [^11] [^3] [^10] [^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Qilin](https://attack.mitre.org/software/S1242) can employ several code obfuscation methods, including renaming functions, altering control flows, and encrypting strings.[^9]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Qilin](https://attack.mitre.org/software/S1242) can detect whether a system is running FreeBSD, VMkernel (ESXi), Nutanix AHV, or a standard Linux distribution to enable platform-specific encryption behaviors.[^5]  |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [Qilin](https://attack.mitre.org/software/S1242) can use an embedded [Mimikatz](https://attack.mitre.org/software/S0002) module for token manipulation.[^1]  |
| [[Mutual Exclusion\|T1480.002]] | Mutual Exclusion | [Qilin](https://attack.mitre.org/software/S1242) can create a mutex to ensure only one instance is running.[^6]  |
| [[Winlogon Helper DLL\|T1547.004]] | Winlogon Helper DLL | [Qilin](https://attack.mitre.org/software/S1242) can configure a Winlogon registry entry.[^4] <br> |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [Qilin](https://attack.mitre.org/software/S1242) can initiate a reboot of the backup server to hinder recovery.[^1]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [Qilin](https://attack.mitre.org/software/S1242) can use WinSCP for the secure file transfer of the Linux ransomware binary to a targeted system.[^5]  |
| [[Local Account\|T1087.001]] | Local Account | [Qilin](https://attack.mitre.org/software/S1242) can list all local users found on a targeted system.[^4]  |
| [[Service Stop\|T1489]] | Service Stop | [Qilin](https://attack.mitre.org/software/S1242) can terminate specific services on compromised hosts.[^4] [^6] [^9] [^7]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Qilin](https://attack.mitre.org/software/S1242) has been delivered via malicious links in spearphishing emails.[^11] [^10] <br> |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Qilin](https://attack.mitre.org/software/S1242) can use WMIC to change the Volume Shadow Copy Service (VSS) startup type to manual.[^7]  |
| [[Native API\|T1106]] | Native API | [Qilin](https://attack.mitre.org/software/S1242) can attempt to log on to the local computer via `LogonUserW` and use `GetLogicalDrives()` and `EnumResourceW()` for discovery.[^4] [^6]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Qilin](https://attack.mitre.org/software/S1242) has created a scheduled task named TVInstallRestore to mimic TeamViewer. [^7]  |
| [[Virtual Machine Discovery\|T1673]] | Virtual Machine Discovery | [Qilin](https://attack.mitre.org/software/S1242) can detect virtual machine environments including ESXi hosts, datacenters, and clusters within vCenter environments.[^6] [^7]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Qilin](https://attack.mitre.org/software/S1242) can bypass standard user access controls by using stolen tokens to launch processes at an elevated security context.[^1]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [Qilin](https://attack.mitre.org/software/S1242) can require a specific password to be passed by command-line argument during execution which must match a pre-defined value in the configuration in order for it to continue execution.[^1] [^5]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Qilin](https://attack.mitre.org/software/S1242) can embed a copy of [PsExec](https://attack.mitre.org/software/S0029) within its payload and place it in the %Temp% directory under a randomly generated filename.[^1] [^7]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Qilin](https://attack.mitre.org/software/S1242) has named its payload file TeamViewer_Host_Setup to disguise itself as a legitimate TeamViewer file.[^7]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Qilin](https://attack.mitre.org/software/S1242) can define specific processes to be terminated or left alone at execution.[^4] [^11] [^6] [^9] [^5] [^7]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Qilin](https://attack.mitre.org/software/S1242) has pushed scheduled tasks via Group Policy Objects (GPOs) for execution.[^3] [^4]  [Qilin](https://attack.mitre.org/software/S1242) has also created a scheduled task named TVInstallRestore, configured to run at logon using the `/SC ONLOGON` argument.[^7] <br> |
| [[Modify Registry\|T1112]] | Modify Registry | [Qilin](https://attack.mitre.org/software/S1242) can make Registry modifications to share networked drives between elevated and non-elevated processes and to increase the number of outstanding network requests per client.[^6] [^1]  [Qilin](https://attack.mitre.org/software/S1242) can also modify `HKEY_CURRENT_USER\Control Panel\Desktop\Wallpaper` to enable posting of ransom messages.[^7] <br> |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Qilin](https://attack.mitre.org/software/S1242) has the ability to list network drives.[^4] [^6]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [Qilin](https://attack.mitre.org/software/S1242) has the ability to clear Windows Event Logs.[^6] [^10]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Qilin](https://attack.mitre.org/software/S1242) can identify specific services for termination or to be left running at execution.[^4] [^11] [^9] [^7]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Qilin](https://attack.mitre.org/software/S1242) has used [PsExec](https://attack.mitre.org/software/S0029) to distribute a second encryptor, named encryptor_1.exe, across the targeted environment.[^7]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Qilin](https://attack.mitre.org/software/S1242) can inject pwndll.dll, a patched DLL from the legitimate DLL WICloader.dll, into svchost.exe for continuous execution.[^4]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Qilin](https://attack.mitre.org/software/S1242) has run `cmd /C [PsExec] -accepteula \\IP Address -c -f -h -d -i<br>C:\Users\xxx\<encryptor_1>.exe --password [PASSWORD] --spread --spread-process` to execute its encryptor to target multiple network shares.[^7]  |
| [[Query Registry\|T1012]] | Query Registry | [Qilin](https://attack.mitre.org/software/S1242) can check `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control SystemStartOptions` to determine if a machine is running in safe mode.[^4]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [Qilin](https://attack.mitre.org/software/S1242) can run PowerShell cmdlets to discover domain groups.[^7]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Qilin](https://attack.mitre.org/software/S1242) can accept a command line argument identifying specific IPs.[^4]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Qilin](https://attack.mitre.org/software/S1242) has used `GetLogicalDrives()` and `EnumResourceW()` to locate mounted drives and shares.[^6] <br> |
| [[File and Directory Permissions Modification\|T1222]] | File and Directory Permissions Modification | [Qilin](https://attack.mitre.org/software/S1242) can use symbolic links to redirect file paths for remote and local objects and can use  `chmod +x` to make its payload binary executable.[^1] [^7]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Qilin](https://attack.mitre.org/software/S1242) can use AES-256 or ChaCha20 for domain-wide encryption of victim servers and workstations and RSA-4096 or RSA-2048 to secure generated encryption keys.[^4] [^11] [^1] [^3] [^6] [^9] [^5] [^7]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Qilin](https://attack.mitre.org/software/S1242) has been executed by luring victims into clicking links in spearphishing emails.[^11] [^10] <br> |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Qilin](https://attack.mitre.org/software/S1242) has been delivered through exploitation of exposed applications and interfaces including Citrix and RDP.[^11]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Qilin](https://attack.mitre.org/software/S1242) has created a RunOnce autostart entry at `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce*aster = %Public%\enc.exe` pointing to a dropped copy of itself in the Public folder.[^4] [^6] [^7] <br> |
| [[Group Policy Modification\|T1484.001]] | Group Policy Modification | [Qilin](https://attack.mitre.org/software/S1242) has pushed a scheduled task via a Group Policy Object for payload execution.[^4] [^3]  |
| [[SSH\|T1021.004]] | SSH | [Qilin](https://attack.mitre.org/software/S1242) can enable SSH access on ESXi hosts.[^7]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Qilin](https://attack.mitre.org/software/S1242) can employ an embedded [Mimikatz](https://attack.mitre.org/software/S0002) module to dump LSASS memory.[^1]  |
| [[Delay Execution\|T1678]] | Delay Execution | [Qilin](https://attack.mitre.org/software/S1242) has the ability to delay execution.[^5]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Qilin](https://attack.mitre.org/software/S1242) has been delivered to victims through spearphishing emails with malicious attachments.[^11]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Qilin](https://attack.mitre.org/software/S1242) can exclude specific directories and files from encryption.[^4] [^5]  |
| [[Safe Mode Boot\|T1688]] | Safe Mode Boot | [Qilin](https://attack.mitre.org/software/S1242) can reboot targeted systems in safe mode to avoid detection.[^4] [^3]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Qilin](https://attack.mitre.org/software/S1242) can terminate antivirus-related processes and services.[^4] [^11] [^6] [^1] <br><br> |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Qilin](https://attack.mitre.org/software/S1242) can enumerate domain-connected hosts during its discovery phase.[^1] [^10] [^7]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Qilin](https://attack.mitre.org/software/S1242) has been delivered to victims through malicious email attachments.[^11]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Qilin](https://attack.mitre.org/software/S1242) can use PowerShell cmdlets to enumerate domain users.[^7]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Qilin](https://attack.mitre.org/software/S1242) can execute `vssadmin.exe delete shadows /all /quiet` to remove volume shadow copies and can disable High Availability (HA) and Distributed Resource Scheduler (DRS) in vCenter clusters.[^4] [^6] [^10] [^7]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Qilin](https://attack.mitre.org/software/S1242) can delete itself from infected hosts after execution.[^6] [^10]  |
| [[Internal Defacement\|T1491.001]] | Internal Defacement | [Qilin](https://attack.mitre.org/software/S1242) can set the wallpaper on compromised hosts to display a ransom message in each encrypted folder.[^10] [^5] [^7]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Qilin](https://attack.mitre.org/software/S1242) has been deployed on VMware vCenter and ESXi servers via custom PowerShell script.[^3] [^1]  [Qilin](https://attack.mitre.org/software/S1242) has also used PowerShell for discovery in vCenter and Active Directory environments.[^7]  |
| [[Remote Desktop Software\|T1219.002]] | Remote Desktop Software | [Qilin](https://attack.mitre.org/software/S1242) can use the Splashtop remote management service (SRManager.exe) to execute the Linux ransomware binary directly on Windows systems.[^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Moonstone Sleet\|G1036]] | Moonstone Sleet |
| [[Water Galura\|G1050]] | Water Galura |



## References

[^1]: [Picus Qilin MAR 2025](https://www.picussecurity.com/resource/blog/qilin-ransomware)


[^2]: Agenda


[^3]: [BushidoToken Qilin RaaS JUN 2024](https://blog.bushidotoken.net/2024/06/tracking-adversaries-qilin-raas.html)


[^4]: [Trend Micro Agenda Ransomware AUG 2022](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)


[^5]: [Trend Micro Agenda Ransomware OCT 2025](https://www.trendmicro.com/en_us/research/25/j/agenda-ransomware-deploys-linux-variant-on-windows-systems.html)


[^6]: [Halcyon Qilin.B OCT 2024](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)


[^7]: [Cisco Talos Qilin Ransomware OCT 2025](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)


[^8]: [MIcrosoft Moonstone Sleet Qilin MAR 2025](https://x.com/MsftSecIntel/status/1897738961348374621)


[^9]: [HC3 Qilin Threat Profile JUN 2024](https://www.aha.org/system/files/media/file/2024/06/tlp-clear-hc3-threat-profile-qilin-aka-agenda-ransomware-6-18-2024.pdf)


[^10]: [Sophos Qilin MSP APR 2025](https://news.sophos.com/en-us/2025/04/01/sophos-mdr-tracks-ongoing-campaign-by-qilin-affiliates-targeting-screenconnect/)


[^11]: [SentinelOne Qilin NOV 2022](https://www.sentinelone.com/anthology/agenda-qilin/)


