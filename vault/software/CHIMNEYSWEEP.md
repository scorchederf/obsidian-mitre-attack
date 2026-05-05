---
aliases: 
    - S1149
    
mitre-attack: https://attack.mitre.org/software/S1149
---

## S1149

[CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) is a backdoor malware that was deployed during [HomeLand Justice](https://attack.mitre.org/campaigns/C0038) along with [ROADSWEEP](https://attack.mitre.org/software/S1150) ransomware, and has been used to target Farsi and Arabic speakers since at least 2012.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can store captured screenshots to disk including to a covert store named `APPX.%x%x%x%x%x.tmp` where `%x` is a random value.[^1]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can execute a task which leads to execution if it finds a process name containing “creensaver.”[^1]  |
| [[CMSTP\|T1218.003]] | CMSTP | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can use CMSTP.exe to install a malicious Microsoft Connection Manager Profile.[^1]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) has executed a script named cln.vbs on compromised hosts.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can use a custom Base64 alphabet to encode an API decryption key.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can download additional files from C2.[^1]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can monitor for removable drives.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can send `HTTP GET` requests to  C2.[^1]  |
| [[Native API\|T1106]] | Native API | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can use Windows APIs including `LoadLibrary` and `GetProcAddress`.[^1]  |
| [[Embedded Payloads\|T1027.009]] | Embedded Payloads | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can extract RC4 encrypted embedded payloads for privilege escalation.[^1]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | The [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) installer has been padded with null bytes to inflate its size.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) has the ability to enumerate directories for files that match a set list.[^1]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can capture content from the clipboard.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can collect files from compromised hosts.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can use an embedded RC4 key to decrypt Windows API function strings.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can use the Windows `SilentCleanup` scheduled task to enable payload execution.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149)  can upload collected files to the command-and-control server.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can invoke the PowerShell command             `[Reflection.Assembly]::LoadFile(\"%s\")\n$i=\"\"\n$r=[%s]::%s(\"%s\",[ref] $i)\necho $r,$i\n` to execute secondary payloads.[^1]  |
| [[Non-Standard Encoding\|T1132.002]] | Non-Standard Encoding | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can use a custom Base64 alphabet for encoding C2.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) has included the victim's computer name and username in C2 messages sent to actor-owned infrastructure.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can check if a process name contains “creensaver.”[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) has the ability to support keylogging.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) is capable of checking whether a compromised device is running DeepFreeze by Faronics.[^1]  |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can reboot or shutdown the targeted system or logoff the current user.[^1]  |
| [[Dynamic API Resolution\|T1027.007]] | Dynamic API Resolution | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can use `LoadLibrary` and `GetProcAddress` to resolve Windows API function strings at run time.[^1]  |
| [[Web Service\|T1102]] | Web Service | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) has the ability to use use Telegram channels to return a list of commands to be executed, to download additional payloads, or to create a reverse shell.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can capture screenshots on targeted systems using a timer and either upload them or store them to disk.[^1]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can make use of the Windows `SilentCleanup` scheduled task to execute its payload with elevated privileges.[^1]  |
| [[Timestomp\|T1070.006]] | Timestomp | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can time stomp its executable, previously dating it between 2010 to 2021.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can use the Windows Registry Environment key to change the `%windir%` variable to point to `c:\Windows` to enable payload execution.[^1] <br> |
| [[Code Signing\|T1553.002]] | Code Signing | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) has been dropped by a self-extracting archive signed with a valid digital certificate.[^1]  |




## References

[^1]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)


