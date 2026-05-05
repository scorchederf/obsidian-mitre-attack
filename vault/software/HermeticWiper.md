---
aliases: 
    - S0697
    
mitre-attack: https://attack.mitre.org/software/S0697
---

## S0697

[HermeticWiper](https://attack.mitre.org/software/S0697) is a data wiper that has been used since at least early 2022, primarily against Ukraine with additional activity observed in Latvia and Lithuania. Some sectors targeted include government, financial, defense, aviation, and IT services.[^5] [^3] [^6] [^7] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [HermeticWiper](https://attack.mitre.org/software/S0697) has the ability to use scheduled tasks for execution.[^3]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [HermeticWiper](https://attack.mitre.org/software/S0697) has the ability to set the `HKLM:\SYSTEM\\CurrentControlSet\\Control\\CrashControl\CrashDumpEnabled` Registry key to `0` in order to disable crash dumps.[^5] [^6] [^1]  |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [HermeticWiper](https://attack.mitre.org/software/S0697) can use `AdjustTokenPrivileges` to grant itself privileges for debugging with `SeDebugPrivilege`, creating backups with `SeBackupPrivilege`, loading drivers with `SeLoadDriverPrivilege`, and shutting down a local system with `SeShutdownPrivilege`.[^1] [^6]  |
| [[Group Policy Modification\|T1484.001]] | Group Policy Modification | [HermeticWiper](https://attack.mitre.org/software/S0697) has the ability to deploy through an infected system's default domain policy.[^4]  |
| [[Data Destruction\|T1485]] | Data Destruction | [HermeticWiper](https://attack.mitre.org/software/S0697) can recursively wipe folders and files in `Windows`, `Program Files`, `Program Files(x86)`, `PerfLogs`, `Boot, System`, `Volume Information`, and `AppData` folders using `FSCTL_MOVE_FILE`. [HermeticWiper](https://attack.mitre.org/software/S0697) can also overwrite symbolic links and big files in `My Documents` and on the Desktop with random bytes.[^4]  |
| [[Code Signing\|T1553.002]] | Code Signing | The [HermeticWiper](https://attack.mitre.org/software/S0697) executable has been signed with a legitimate certificate issued to Hermetica Digital Ltd.[^3] [^6] [^7] [^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [HermeticWiper](https://attack.mitre.org/software/S0697) has the ability to modify Registry keys to disable crash dumps, colors for compressed files, and pop-up information about folders and desktop items.[^5] [^6] [^1]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [HermeticWiper](https://attack.mitre.org/software/S0697) can disable pop-up information about folders and desktop items and delete Registry keys to hide malicious services.[^6] [^4]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [HermeticWiper](https://attack.mitre.org/software/S0697) can enumerate common folders such as My Documents, Desktop, and AppData.[^5] [^1]  |
| [[Disk Structure Wipe\|T1561.002]] | Disk Structure Wipe | [HermeticWiper](https://attack.mitre.org/software/S0697) has the ability to corrupt disk partitions, damage the Master Boot Record (MBR), and overwrite the Master File Table (MFT) of all available physical drives.[^5] [^3] [^6] [^1]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [HermeticWiper](https://attack.mitre.org/software/S0697) can disable the VSS service on a compromised host using the service control manager.[^6] [^4] [^1]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [HermeticWiper](https://attack.mitre.org/software/S0697) has the ability to receive a command parameter to sleep prior to carrying out destructive actions on a targeted host.[^6]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [HermeticWiper](https://attack.mitre.org/software/S0697) can decompress and copy driver files using `LZCopy`.[^6]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [HermeticWiper](https://attack.mitre.org/software/S0697) can use `cmd.exe /Q/c move CSIDL_SYSTEM_DRIVE\temp\sys.tmp1 CSIDL_WINDOWS\policydefinitions\postgresql.exe 1> \\127.0.0.1\ADMIN$\_1636727589.6007507 2>&1` to deploy on an infected system.[^4]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [HermeticWiper](https://attack.mitre.org/software/S0697) can determine the OS version and bitness on a targeted host.[^5] [^6] [^4] [^1]  |
| [[Native API\|T1106]] | Native API | [HermeticWiper](https://attack.mitre.org/software/S0697) can call multiple Windows API functions used for privilege escalation, service execution, and to overwrite random bites of data.[^5] [^6] [^4] [^1]  |
| [[Compression\|T1027.015]] | Compression | [HermeticWiper](https://attack.mitre.org/software/S0697) can compress 32-bit and 64-bit driver files with the Lempel-Ziv algorithm.[^3] [^6] [^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [HermeticWiper](https://attack.mitre.org/software/S0697) can enumerate physical drives on a targeted host.[^5] [^6] [^4] [^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [HermeticWiper](https://attack.mitre.org/software/S0697) has used the name `postgressql.exe` to mask a malicious payload.[^4]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [HermeticWiper](https://attack.mitre.org/software/S0697) can overwrite the `C:\Windows\System32\winevt\Logs` file on a targeted system.[^4]  |
| [[Windows Service\|T1543.003]] | Windows Service | [HermeticWiper](https://attack.mitre.org/software/S0697) can load drivers by creating a new service using the `CreateServiceW` API.[^6]  |
| [[File Deletion\|T1070.004]] | File Deletion | [HermeticWiper](https://attack.mitre.org/software/S0697) has the ability to overwrite its own file with random bites.[^6] [^4]  |
| [[Service Stop\|T1489]] | Service Stop | [HermeticWiper](https://attack.mitre.org/software/S0697) has the ability to stop the Volume Shadow Copy service.[^1]  |
| [[Disk Content Wipe\|T1561.001]] | Disk Content Wipe | [HermeticWiper](https://attack.mitre.org/software/S0697) has the ability to corrupt disk partitions and obtain raw disk access to destroy data.[^6] [^5]  |
| [[Service Execution\|T1569.002]] | Service Execution | [HermeticWiper](https://attack.mitre.org/software/S0697) can create system services to aid in executing the payload.[^5] [^6] [^1]  |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [HermeticWiper](https://attack.mitre.org/software/S0697) can initiate a system shutdown.[^5] [^1]  |




## References

[^1]: [Qualys Hermetic Wiper March 2022](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)


[^2]: Trojan.Killdisk


[^3]: [Symantec Ukraine Wipers February 2022](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/ukraine-wiper-malware-russia)


[^4]: [ESET Hermetic Wizard March 2022](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)


[^5]: [SentinelOne Hermetic Wiper February 2022](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack)


[^6]: [Crowdstrike DriveSlayer February 2022](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)


[^7]: [ESET Hermetic Wiper February 2022](https://www.welivesecurity.com/2022/02/24/hermeticwiper-new-data-wiping-malware-hits-ukraine)


[^8]: DriveSlayer


[^9]: [Crowdstrike PartyTicket March 2022](https://www.crowdstrike.com/blog/how-to-decrypt-the-partyticket-ransomware-targeting-ukraine)


[^10]: [CISA AA22-057A Destructive Malware February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-057a)


