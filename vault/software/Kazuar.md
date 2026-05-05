---
aliases: 
    - S0265
    
mitre-attack: https://attack.mitre.org/software/S0265
---

## S0265

[Kazuar](https://attack.mitre.org/software/S0265) is a fully featured, multi-platform backdoor Trojan written using the Microsoft .NET framework. [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Kazuar](https://attack.mitre.org/software/S0265) adds a sub-key under several Registry run keys.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Kazuar](https://attack.mitre.org/software/S0265) downloads additional plug-ins to load on the victim’s machine, including the ability to upgrade and replace its own binary.[^3]  |
| [[Data Destruction\|T1485]] | Data Destruction | [Kazuar](https://attack.mitre.org/software/S0265) can overwrite files with random data before deleting them.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Kazuar](https://attack.mitre.org/software/S0265) can delete files.[^3]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Kazuar](https://attack.mitre.org/software/S0265) is obfuscated using the open source ConfuserEx protector. [Kazuar](https://attack.mitre.org/software/S0265) also obfuscates the name of created files/folders/mutexes and encrypts debug messages written to log files using the Rijndael cipher.[^3]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Kazuar](https://attack.mitre.org/software/S0265) encodes communications to the C2 server in Base64.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Kazuar](https://attack.mitre.org/software/S0265) obtains a list of running processes through WMI querying and the `ps` command.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Kazuar](https://attack.mitre.org/software/S0265) finds a specified directory, lists the files and metadata about those files.[^3]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Kazuar](https://attack.mitre.org/software/S0265) gathers information on users.[^3]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [Kazuar](https://attack.mitre.org/software/S0265) has used internal nodes on the compromised network for C2 communications.[^2]  |
| [[Local Groups\|T1069.001]] | Local Groups | [Kazuar](https://attack.mitre.org/software/S0265) gathers information about local groups and members.[^3]  |
| [[Video Capture\|T1125]] | Video Capture | [Kazuar](https://attack.mitre.org/software/S0265) captures images from the webcam.[^3]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Kazuar](https://attack.mitre.org/software/S0265) uses /bin/bash to execute commands on the victim’s machine.[^3]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | If running in a Windows environment, [Kazuar](https://attack.mitre.org/software/S0265) saves a DLL to disk that is injected into the explorer.exe process to execute the payload. [Kazuar](https://attack.mitre.org/software/S0265) can also be configured to inject and execute within specific processes.[^3]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [Kazuar](https://attack.mitre.org/software/S0265) uses FTP and FTPS to communicate with the C2 server.[^3]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Kazuar](https://attack.mitre.org/software/S0265) can install itself as a new service.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Kazuar](https://attack.mitre.org/software/S0265) gathers information on the system.[^3]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [Kazuar](https://attack.mitre.org/software/S0265) has used compromised WordPress blogs as C2 servers.[^3]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Kazuar](https://attack.mitre.org/software/S0265) can accept multiple URLs for C2 servers.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Kazuar](https://attack.mitre.org/software/S0265) uses HTTP and HTTPS to communicate with the C2 server. [Kazuar](https://attack.mitre.org/software/S0265) can also act as a webserver and listen for inbound HTTP requests through an exposed API.[^3]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [Kazuar](https://attack.mitre.org/software/S0265) gathers information about opened windows.[^3]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Kazuar](https://attack.mitre.org/software/S0265) captures screenshots of the victim’s screen.[^3]  |
| [[Scheduled Transfer\|T1029]] | Scheduled Transfer | [Kazuar](https://attack.mitre.org/software/S0265) can sleep for a specific time and be set to communicate at specific intervals.[^3]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Kazuar](https://attack.mitre.org/software/S0265) gathers information on local drives.[^3]  |
| [[Local Account\|T1087.001]] | Local Account | [Kazuar](https://attack.mitre.org/software/S0265) gathers information on local groups and members on the victim’s machine.[^3]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Kazuar](https://attack.mitre.org/software/S0265) stages command output and collected data in files before exfiltration.[^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Kazuar](https://attack.mitre.org/software/S0265) uploads files from a specified directory to the C2 server.[^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Kazuar](https://attack.mitre.org/software/S0265) gathers information about network adapters.[^3]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Kazuar](https://attack.mitre.org/software/S0265) obtains a list of running processes through WMI querying.[^3]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [Kazuar](https://attack.mitre.org/software/S0265) adds a .lnk file to the Windows startup folder.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Kazuar](https://attack.mitre.org/software/S0265) uses cmd.exe to execute commands on the victim’s machine.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Turla\|G0010]] | Turla |



## References

[^1]: Kazuar


[^2]: [Accenture HyperStack October 2020](https://web.archive.org/web/20201101015247/https://www.accenture.com/us-en/blogs/cyber-defense/turla-belugasturgeon-compromises-government-entity)


[^3]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)


[^4]: [Talos TinyTurla September 2021](https://blog.talosintelligence.com/2021/09/tinyturla.html)


