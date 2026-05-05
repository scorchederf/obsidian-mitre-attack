---
aliases: 
    - S0379
    
mitre-attack: https://attack.mitre.org/software/S0379
---

## S0379

[Revenge RAT](https://attack.mitre.org/software/S0379) is a freely available remote access tool written in .NET (C#).[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Revenge RAT](https://attack.mitre.org/software/S0379) gathers the username from the system.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Revenge RAT](https://attack.mitre.org/software/S0379) has a plugin for keylogging.[^1] [^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Revenge RAT](https://attack.mitre.org/software/S0379) has the ability to upload and download files.[^1]  |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | [Revenge RAT](https://attack.mitre.org/software/S0379) has a plugin for credential harvesting.[^1]  |
| [[Video Capture\|T1125]] | Video Capture | [Revenge RAT](https://attack.mitre.org/software/S0379) has the ability to access the webcam.[^1] [^2]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Revenge RAT](https://attack.mitre.org/software/S0379) has a plugin to perform RDP access.[^1] <br> |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Revenge RAT](https://attack.mitre.org/software/S0379) collects the CPU information, OS information, and system language.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Revenge RAT](https://attack.mitre.org/software/S0379) uses Base64 to encode information sent to the C2 server.[^1]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [Revenge RAT](https://attack.mitre.org/software/S0379) used blogpost.com as its primary command and control server during a campaign.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Revenge RAT](https://attack.mitre.org/software/S0379) collects the IP address and MAC address from the system.[^1]  |
| [[Mshta\|T1218.005]] | Mshta | [Revenge RAT](https://attack.mitre.org/software/S0379) uses mshta.exe to run malicious scripts on the system.[^2]  |
| [[Winlogon Helper DLL\|T1547.004]] | Winlogon Helper DLL | [Revenge RAT](https://attack.mitre.org/software/S0379) creates a Registry key at `HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell` to survive a system reboot.[^1]  |
| [[Audio Capture\|T1123]] | Audio Capture | [Revenge RAT](https://attack.mitre.org/software/S0379) has a plugin for microphone interception.[^1] [^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Revenge RAT](https://attack.mitre.org/software/S0379) uses cmd.exe to execute commands and run scripts on the victim's machine.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Revenge RAT](https://attack.mitre.org/software/S0379) uses the PowerShell command `Reflection.Assembly` to load itself into memory to aid in execution.[^2]  |
| [[Indirect Command Execution\|T1202]] | Indirect Command Execution | [Revenge RAT](https://attack.mitre.org/software/S0379) uses the [Forfiles](https://attack.mitre.org/software/S0193) utility to execute commands on the system.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Revenge RAT](https://attack.mitre.org/software/S0379) has a plugin for screen capture.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Revenge RAT](https://attack.mitre.org/software/S0379) schedules tasks to run malicious scripts at different intervals.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA2541\|G1018]] | TA2541 |
| [[The White Company\|G0089]] | The White Company |



## References

[^1]: [Cylance Shaheen Nov 2018](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)


[^2]: [Cofense RevengeRAT Feb 2019](https://web.archive.org/web/20200428173819/https://cofense.com/upgrades-delivery-support-infrastructure-revenge-rat-malware-bigger-threat/)


[^3]: [Proofpoint TA2541 February 2022](https://www.proofpoint.com/us/blog/threat-insight/charting-ta2541s-flight)


