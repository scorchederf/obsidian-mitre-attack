---
aliases: 
    - S1064
    
mitre-attack: https://attack.mitre.org/software/S1064
---

## S1064

[SVCReady](https://attack.mitre.org/software/S1064) is a loader that has been used since at least April 2022 in malicious spam campaigns. Security researchers have noted overlaps between [TA551](https://attack.mitre.org/groups/G0127) activity and [SVCReady](https://attack.mitre.org/software/S1064) distribution, including similarities in file names, lure images, and identical grammatical errors.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Query Registry\|T1012]] | Query Registry | [SVCReady](https://attack.mitre.org/software/S1064) can search for the `HKEY_LOCAL_MACHINE\HARDWARE\DESCRIPTION\System` Registry key to gather system information.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [SVCReady](https://attack.mitre.org/software/S1064) can encrypt victim data with an RC4 cipher.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [SVCReady](https://attack.mitre.org/software/S1064) has relied on users clicking a malicious attachment delivered through spearphishing.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [SVCReady](https://attack.mitre.org/software/S1064) can collect data from an infected host.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [SVCReady](https://attack.mitre.org/software/S1064) has been distributed via spearphishing campaigns containing malicious Mircrosoft Word documents.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [SVCReady](https://attack.mitre.org/software/S1064) has named a task `RecoveryExTask` as part of its persistence activity.[^1]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [SVCReady](https://attack.mitre.org/software/S1064) has used VBA macros to execute shellcode.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [SVCReady](https://attack.mitre.org/software/S1064) has used `rundll32.exe` for execution.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [SVCReady](https://attack.mitre.org/software/S1064) can create a scheduled task named `RecoveryExTask` to gain persistence.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SVCReady](https://attack.mitre.org/software/S1064) has the ability to download additional tools such as the RedLine Stealer to an infected host.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [SVCReady](https://attack.mitre.org/software/S1064) can send collected data in JSON format to its C2 server.[^1]   |
| [[Web Protocols\|T1071.001]] | Web Protocols | [SVCReady](https://attack.mitre.org/software/S1064) can communicate with its C2 servers via HTTP.[^1]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [SVCReady](https://attack.mitre.org/software/S1064) can check for the number of devices plugged into an infected host.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [SVCReady](https://attack.mitre.org/software/S1064) can collect the username from an infected host.[^1]  |
| [[Component Object Model Hijacking\|T1546.015]] | Component Object Model Hijacking | [SVCReady](https://attack.mitre.org/software/S1064) has created the `HKEY_CURRENT_USER\Software\Classes\CLSID\{E6D34FFC-AD32-4d6a-934C-D387FA873A19}` Registry key for persistence.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [SVCReady](https://attack.mitre.org/software/S1064) can take a screenshot from an infected host.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [SVCReady](https://attack.mitre.org/software/S1064) can collect time zone information.[^1]  |
| [[Native API\|T1106]] | Native API | [SVCReady](https://attack.mitre.org/software/S1064) can use Windows API calls to gather information from an infected host.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [SVCReady](https://attack.mitre.org/software/S1064) can use `WMI` queries to detect the presence of a virtual machine environment.[^1]   |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SVCReady](https://attack.mitre.org/software/S1064) has the ability to collect information such as computer name, computer manufacturer, BIOS, operating system, and firmware, including through the use of `systeminfo.exe`.[^1]  |
| [[System Checks\|T1497.001]] | System Checks | [SVCReady](https://attack.mitre.org/software/S1064) has the ability to determine if its runtime environment is virtualized.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [SVCReady](https://attack.mitre.org/software/S1064) can collect a list of running processes from an infected host.[^1]  |
| [[Software Discovery\|T1518]] | Software Discovery | [SVCReady](https://attack.mitre.org/software/S1064) can collect a list of installed software from an infected host.[^1]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [SVCReady](https://attack.mitre.org/software/S1064) can enter a sleep stage for 30 minutes to evade detection.[^1]  |




## References

[^1]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)


