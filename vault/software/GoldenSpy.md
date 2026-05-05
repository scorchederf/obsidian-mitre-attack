---
aliases: 
    - S0493
    
mitre-attack: https://attack.mitre.org/software/S0493
---

## S0493

[GoldenSpy](https://attack.mitre.org/software/S0493) is a backdoor malware which has been packaged with legitimate tax preparation software. [GoldenSpy](https://attack.mitre.org/software/S0493) was discovered targeting organizations in China, being delivered with the "Intelligent Tax" software suite which is produced by the Golden Tax Department of Aisino Credit Information Co. and required to pay local taxes.[^1]  

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Service\|T1543.003]] | Windows Service | [GoldenSpy](https://attack.mitre.org/software/S0493) has established persistence by running in the background as an autostart service.[^1] 	 |
| [[System Information Discovery\|T1082]] | System Information Discovery | [GoldenSpy](https://attack.mitre.org/software/S0493) has gathered operating system information.[^1] 	 |
| [[Local Account\|T1136.001]] | Local Account | [GoldenSpy](https://attack.mitre.org/software/S0493) can create new users on an infected system.[^1] 	 |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [GoldenSpy](https://attack.mitre.org/software/S0493) has used HTTP over ports 9005 and 9006 for network traffic, 9002 for C2 requests, 33666 as a WebSocket, and 8090 to download files.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [GoldenSpy](https://attack.mitre.org/software/S0493) has exfiltrated host environment information to an external C2 domain via port 9006.[^1] 	 |
| [[Compromise Software Supply Chain\|T1195.002]] | Compromise Software Supply Chain | [GoldenSpy](https://attack.mitre.org/software/S0493) has been packaged with a legitimate tax preparation software.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [GoldenSpy](https://attack.mitre.org/software/S0493)'s setup file installs initial executables under the folder `%WinDir%\System32\PluginManager`.[^1] 	 |
| [[Native API\|T1106]] | Native API | [GoldenSpy](https://attack.mitre.org/software/S0493) can execute remote commands in the Windows command shell using the `WinExec()` API.[^1] 	 |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [GoldenSpy](https://attack.mitre.org/software/S0493) can execute remote commands via the command-line interface.[^1] 	 |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [GoldenSpy](https://attack.mitre.org/software/S0493) has included a program "ExeProtector", which monitors for the existence of [GoldenSpy](https://attack.mitre.org/software/S0493) on the infected system and redownloads if necessary.[^1] 	 |
| [[File Deletion\|T1070.004]] | File Deletion | [GoldenSpy](https://attack.mitre.org/software/S0493)'s uninstaller can delete registry entries, files and folders, and finally itself once these tasks have been completed.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [GoldenSpy](https://attack.mitre.org/software/S0493) has used the Ryeol HTTP Client to facilitate HTTP internet communication.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [GoldenSpy](https://attack.mitre.org/software/S0493) constantly attempts to download and execute files from the remote C2, including [GoldenSpy](https://attack.mitre.org/software/S0493) itself if not found on the system.[^1] 	 |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [GoldenSpy](https://attack.mitre.org/software/S0493)'s installer has delayed installation of [GoldenSpy](https://attack.mitre.org/software/S0493) for two hours after it reaches a victim system.[^1] 	 |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [GoldenSpy](https://attack.mitre.org/software/S0493)'s uninstaller has base64-encoded its variables. [^2]  |




## References

[^1]: [Trustwave GoldenSpy June 2020](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)


[^2]: [Trustwave GoldenSpy2 June 2020](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/goldenspy-chapter-two-the-uninstaller/)


