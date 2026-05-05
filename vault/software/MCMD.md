---
aliases: 
    - S0500
    
mitre-attack: https://attack.mitre.org/software/S0500
---

## S0500

[MCMD](https://attack.mitre.org/software/S0500) is a remote access tool that provides remote command shell capability used by [Dragonfly](https://attack.mitre.org/groups/G0035).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Clear Persistence\|T1070.009]] | Clear Persistence | [MCMD](https://attack.mitre.org/software/S0500) has the ability to remove set Registry Keys, including those used for persistence.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [MCMD](https://attack.mitre.org/software/S0500) can launch a console process (cmd.exe) with redirected standard input and output.[^1]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [MCMD](https://attack.mitre.org/software/S0500) can modify processes to prevent them from being visible on the desktop.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [MCMD](https://attack.mitre.org/software/S0500) can use HTTPS in communication with C2 web servers.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [MCMD](https://attack.mitre.org/software/S0500) has been named Readme.txt to appear legitimate.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [MCMD](https://attack.mitre.org/software/S0500) can Base64 encode output strings prior to sending to C2.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [MCMD](https://attack.mitre.org/software/S0500) can use scheduled tasks for persistence.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [MCMD](https://attack.mitre.org/software/S0500) has the ability to upload files from an infected device.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [MCMD](https://attack.mitre.org/software/S0500) can upload additional files to a compromised host.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [MCMD](https://attack.mitre.org/software/S0500) can use Registry Run Keys for persistence.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Dragonfly\|G0035]] | Dragonfly |



## References

[^1]: [Secureworks MCMD July 2019](https://www.secureworks.com/research/mcmd-malware-analysis)


