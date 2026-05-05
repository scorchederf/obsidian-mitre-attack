---
aliases: 
    - S0339
    
mitre-attack: https://attack.mitre.org/software/S0339
---

## S0339

[Micropsia](https://attack.mitre.org/software/S0339) is a remote access tool written in Delphi.[^2] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Micropsia](https://attack.mitre.org/software/S0339) gathers the hostname and OS version from the victim’s machine.[^2] [^3]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Micropsia](https://attack.mitre.org/software/S0339) executes an RAR tool to recursively archive files based on a predefined list of file extensions (*.xls, *.xlsx, *.csv, *.odt, *.doc, *.docx, *.ppt, *.pptx, *.pdf, *.mdb, *.accdb, *.accde, *.txt).[^3]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Micropsia](https://attack.mitre.org/software/S0339) searches for anti-virus software and firewall products installed on the victim’s machine using WMI.[^2] [^3]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Micropsia](https://attack.mitre.org/software/S0339) has keylogging capabilities.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Micropsia](https://attack.mitre.org/software/S0339) can perform a recursive directory listing for all volume drives available on the victim's machine and can also fetch specific files by their paths.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Micropsia](https://attack.mitre.org/software/S0339) creates a command-line shell using cmd.exe.[^3]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [Micropsia](https://attack.mitre.org/software/S0339) creates a shortcut to maintain persistence.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Micropsia](https://attack.mitre.org/software/S0339) collects the username from the victim’s machine.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Micropsia](https://attack.mitre.org/software/S0339) can download and execute an executable from the C2 server.[^2] [^3]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Micropsia](https://attack.mitre.org/software/S0339) creates a RAR archive based on collected files on the victim's machine.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Micropsia](https://attack.mitre.org/software/S0339) uses HTTP and HTTPS for C2 network communications.[^2] [^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Micropsia](https://attack.mitre.org/software/S0339) obfuscates the configuration with a custom Base64 and XOR.[^2] [^3]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Micropsia](https://attack.mitre.org/software/S0339) takes screenshots every 90 seconds by calling the Gdi32.BitBlt API.[^3]  |
| [[Audio Capture\|T1123]] | Audio Capture | [Micropsia](https://attack.mitre.org/software/S0339) can perform microphone recording.[^3]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [Micropsia](https://attack.mitre.org/software/S0339) creates a new hidden directory to store all components' outputs in a dedicated sub-folder for each.[^3]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Micropsia](https://attack.mitre.org/software/S0339) searches for anti-virus software and firewall products installed on the victim’s machine using WMI.[^2] [^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT-C-23\|G1028]] | APT-C-23 |



## References

[^1]: Micropsia


[^2]: [Talos Micropsia June 2017](https://blog.talosintelligence.com/2017/06/palestine-delphi.html)


[^3]: [Radware Micropsia July 2018](https://www.radware.com/blog/security/2018/07/micropsia-malware/)


