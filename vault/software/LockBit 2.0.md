---
aliases: 
    - S1199
    
mitre-attack: https://attack.mitre.org/software/S1199
---

## S1199

[LockBit 2.0](https://attack.mitre.org/software/S1199) is an affiliate-based Ransomware-as-a-Service (RaaS) that has been in use since at least June 2021 as the successor to LockBit Ransomware. [LockBit 2.0](https://attack.mitre.org/software/S1199) has versions capable of infecting Windows and VMware ESXi virtual machines, and has been observed targeting multiple industry verticals globally.[^3] [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Hidden Window\|T1564.003]] | Hidden Window | [LockBit 2.0](https://attack.mitre.org/software/S1199) can execute command line arguments in a hidden window.[^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [LockBit 2.0](https://attack.mitre.org/software/S1199) can use a Registry Run key to establish persistence at startup.[^3]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [LockBit 2.0](https://attack.mitre.org/software/S1199) can be executed via scheduled task.[^4]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [LockBit 2.0](https://attack.mitre.org/software/S1199) can use the Windows command shell for multiple post-compromise actions on objective.[^3] [^4] [^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [LockBit 2.0](https://attack.mitre.org/software/S1199) can disable firewall rules and anti-malware and monitoring software including Windows Defender.[^3] [^4]  |
| [[Service Stop\|T1489]] | Service Stop | [LockBit 2.0](https://attack.mitre.org/software/S1199) can automatically terminate processes that may interfere with the encryption or file extraction processes.[^2]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [LockBit 2.0](https://attack.mitre.org/software/S1199) can bypass UAC through creating the Registry key  `HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\ICM\Calibration`.[^3] [^4]  |
| [[Create Account\|T1136]] | Create Account | [LockBit 2.0](https://attack.mitre.org/software/S1199) has been observed creating accounts for persistence using simple names like "a".[^4]  |
| [[Modify Registry\|T1112]] | Modify Registry | [LockBit 2.0](https://attack.mitre.org/software/S1199) can create Registry keys to bypass UAC and for persistence.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [LockBit 2.0](https://attack.mitre.org/software/S1199) can enumerate system information including hostname and domain information.[^3] [^4]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [LockBit 2.0](https://attack.mitre.org/software/S1199) can decode scripts and strings in loaded modules.[^3] [^4]  |
| [[Process Discovery\|T1057]] | Process Discovery | [LockBit 2.0](https://attack.mitre.org/software/S1199) can determine if a running process has administrative privileges and terminate processes that interfere with encryption or exfiltration.[^3] [^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [LockBit 2.0](https://attack.mitre.org/software/S1199) can exclude files associated with core system functions from encryption.[^3]  |
| [[Group Policy Modification\|T1484.001]] | Group Policy Modification | [LockBit 2.0](https://attack.mitre.org/software/S1199) can modify Group Policy to disable Windows Defender and to automatically infect devices in Windows domains.[^3] [^4]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [LockBit 2.0](https://attack.mitre.org/software/S1199) has the ability to identify mounted external storage devices.[^3]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [LockBit 2.0](https://attack.mitre.org/software/S1199) can discover remote shares.[^3]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [LockBit 2.0](https://attack.mitre.org/software/S1199) can enumerate local drive configuration.[^3] [^4]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [LockBit 2.0](https://attack.mitre.org/software/S1199) can delete log files through the use of wevtutil.[^3] [^4] [^1] [^2]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [LockBit 2.0](https://attack.mitre.org/software/S1199) can use wmic.exe to delete volume shadow copies.[^1]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [LockBit 2.0](https://attack.mitre.org/software/S1199) will not execute on hosts where the system language is set to a language spoken in the Commonwealth of Independent States region.[^3] [^4]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [LockBit 2.0](https://attack.mitre.org/software/S1199) can check if a targeted machine is using a set of Eastern European languages and exit without infection if so.[^3] [^4]  |
| [[File Deletion\|T1070.004]] | File Deletion | [LockBit 2.0](https://attack.mitre.org/software/S1199) can delete itself from disk after execution.[^3] [^4] [^1]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [LockBit 2.0](https://attack.mitre.org/software/S1199) has the ability to move laterally via SMB.[^4] [^2]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [LockBit 2.0](https://attack.mitre.org/software/S1199) can use standard AES and elliptic-curve cryptography algorithms to encrypt victim data.[^4] [^2] <br> |
| [[PowerShell\|T1059.001]] | PowerShell | [LockBit 2.0](https://attack.mitre.org/software/S1199) can use the PowerShell module `InvokeGPUpdate` to modify Group Policy.[^3] [^4]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [LockBit 2.0](https://attack.mitre.org/software/S1199) has the ability to delete volume shadow copies on targeted hosts.[^3] [^1]  |




## References

[^1]: [Cybereason Lockbit 2.0](https://www.cybereason.com/blog/threat-analysis-report-lockbit-2.0-all-paths-lead-to-ransom)


[^2]: [SentinelOne LockBit 2.0](https://www.sentinelone.com/anthology/lockbit-2-0/)


[^3]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)


[^4]: [Palo Alto Lockbit 2.0 JUN 2022](https://unit42.paloaltonetworks.com/lockbit-2-ransomware/)


