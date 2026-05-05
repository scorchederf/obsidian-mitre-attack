---
aliases: 
    - S0434
    
mitre-attack: https://attack.mitre.org/software/S0434
---

## S0434

[Imminent Monitor](https://attack.mitre.org/software/S0434) was a commodity remote access tool (RAT) offered for sale from 2012 until 2019, when an operation was conducted to take down the Imminent Monitor infrastructure. Various cracked versions and variations of this RAT are still in circulation.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Native API\|T1106]] | Native API | [Imminent Monitor](https://attack.mitre.org/software/S0434) has leveraged CreateProcessW() call to execute the debugger.[^2]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a PasswordRecoveryPacket module for recovering browser passwords.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Imminent Monitor](https://attack.mitre.org/software/S0434) has decoded malware components that are then dropped to the system.[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a keylogging module.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Imminent Monitor](https://attack.mitre.org/software/S0434) has deleted files related to its dynamic debugger feature.[^2]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a module for performing remote desktop access.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a "Process Watcher" feature to monitor processes in case the client ever crashes or gets closed.[^1]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a CommandPromptPacket and ScriptPacket module(s) for creating a remote shell and executing scripts.[^2]  |
| [[Video Capture\|T1125]] | Video Capture | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a remote webcam monitoring capability.[^1] [^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a feature to disable Windows Task Manager.[^1] 	 |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a dynamic debugging feature to set the file attribute to hidden.[^2]  |
| [[Compute Hijacking\|T1496.001]] | Compute Hijacking | [Imminent Monitor](https://attack.mitre.org/software/S0434) has the capability to run a cryptocurrency miner on the victim machine.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Imminent Monitor](https://attack.mitre.org/software/S0434) has uploaded a file containing debugger logs, network information and system information to the C2.[^2]  |
| [[Audio Capture\|T1123]] | Audio Capture | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a remote microphone monitoring capability.[^1] [^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Imminent Monitor](https://attack.mitre.org/software/S0434) has encrypted the spearphish attachments to avoid detection from email gateways; the debugger also encrypts information before sending to the C2.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a dynamic debugging feature to check whether it is located in the %TEMP% directory, otherwise it copies itself there.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT-C-36\|G0099]] | APT-C-36 |
| [[TA2541\|G1018]] | TA2541 |



## References

[^1]: [Imminent Unit42 Dec2019](https://unit42.paloaltonetworks.com/imminent-monitor-a-rat-down-under/)


[^2]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)


[^3]: [Proofpoint TA2541 February 2022](https://www.proofpoint.com/us/blog/threat-insight/charting-ta2541s-flight)


