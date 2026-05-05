---
aliases: 
    - S0475
    
mitre-attack: https://attack.mitre.org/software/S0475
---

## S0475

[BackConfig](https://attack.mitre.org/software/S0475) is a custom Trojan with a flexible plugin architecture that has been used by [Patchwork](https://attack.mitre.org/groups/G0040).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Code Signing\|T1553.002]] | Code Signing | [BackConfig](https://attack.mitre.org/software/S0475) has been signed with self signed digital certificates mimicking a legitimate software company.[^1]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [BackConfig](https://attack.mitre.org/software/S0475) has used VBS to install its downloader component and malicious documents with VBA macro code.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [BackConfig](https://attack.mitre.org/software/S0475) can download and run batch files to execute commands on a compromised host.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BackConfig](https://attack.mitre.org/software/S0475) can download and execute additional payloads on a compromised host.[^1]  |
| [[Native API\|T1106]] | Native API | [BackConfig](https://attack.mitre.org/software/S0475) can leverage API functions such as `ShellExecuteA` and `HttpOpenRequestA` in the process of downloading and executing files.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [BackConfig](https://attack.mitre.org/software/S0475) has the ability to identify folders and files related to previous infections.[^1] 	 |
| [[Office Template Macros\|T1137.001]] | Office Template Macros | [BackConfig](https://attack.mitre.org/software/S0475) has the ability to use hidden columns in Excel spreadsheets to store executable files or commands for VBA macros.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [BackConfig](https://attack.mitre.org/software/S0475) has the ability to remove files and folders related to previous infections.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [BackConfig](https://attack.mitre.org/software/S0475) has the ability to gather the victim's computer name.[^1]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [BackConfig](https://attack.mitre.org/software/S0475) has used compressed and decimal encoded VBS scripts.[^1]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [BackConfig](https://attack.mitre.org/software/S0475) has the ability to set folders or files to be hidden from the Windows Explorer default view.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [BackConfig](https://attack.mitre.org/software/S0475) has the ability to use scheduled tasks to repeatedly execute malicious payloads on a compromised host.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [BackConfig](https://attack.mitre.org/software/S0475) has the ability to use HTTPS for C2 communiations.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [BackConfig](https://attack.mitre.org/software/S0475) has used a custom routine to decrypt strings.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [BackConfig](https://attack.mitre.org/software/S0475) has hidden malicious payloads in `%USERPROFILE%\Adobe\Driver\dwg\` and mimicked the legitimate DHCP service binary.[^1]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [BackConfig](https://attack.mitre.org/software/S0475) has compromised victims via links to URLs hosting malicious content.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Patchwork\|G0040]] | Patchwork |



## References

[^1]: [Unit 42 BackConfig May 2020](https://unit42.paloaltonetworks.com/updated-backconfig-malware-targeting-government-and-military-organizations/)


