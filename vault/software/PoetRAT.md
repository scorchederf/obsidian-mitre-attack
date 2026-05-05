---
aliases: 
    - S0428
    
mitre-attack: https://attack.mitre.org/software/S0428
---

## S0428

[PoetRAT](https://attack.mitre.org/software/S0428) is a remote access trojan (RAT) that was first identified in April 2020. [PoetRAT](https://attack.mitre.org/software/S0428) has been used in multiple campaigns against the private and public sectors in Azerbaijan, including ICS and SCADA systems in the energy sector. The STIBNITE activity group has been observed using the malware. [PoetRAT](https://attack.mitre.org/software/S0428) derived its name from references in the code to poet William Shakespeare. [^3] [^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [PoetRAT](https://attack.mitre.org/software/S0428) sent username, computer name, and the previously generated UUID in reply to a "who" command from C2.[^3]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [PoetRAT](https://attack.mitre.org/software/S0428) has exfiltrated data over the C2 channel.[^1]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [PoetRAT](https://attack.mitre.org/software/S0428) has used FTP for C2 communications.[^1]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [PoetRAT](https://attack.mitre.org/software/S0428) has `pyminifier` to obfuscate scripts.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [PoetRAT](https://attack.mitre.org/software/S0428) has called cmd through a Word document macro.[^1]  |
| [[Exfiltration Over Alternative Protocol\|T1048]] | Exfiltration Over Alternative Protocol | [PoetRAT](https://attack.mitre.org/software/S0428) has used a .NET tool named dog.exe to exiltrate information over an e-mail account.[^3]  |
| [[Malicious File\|T1204.002]] | Malicious File | [PoetRAT](https://attack.mitre.org/software/S0428) has used spearphishing attachments to infect victims.[^3]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [PoetRAT](https://attack.mitre.org/software/S0428) used TLS to encrypt communications over port 143[^3]  |
| [[Modify Registry\|T1112]] | Modify Registry | [PoetRAT](https://attack.mitre.org/software/S0428) has made registry modifications to alter its behavior upon execution.[^3]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [PoetRAT](https://attack.mitre.org/software/S0428) was distributed via malicious Word documents.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [PoetRAT](https://attack.mitre.org/software/S0428) has the ability to list files upon receiving the `ls` command from C2.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [PoetRAT](https://attack.mitre.org/software/S0428) has the ability to copy files and download/upload files into C2 channels using FTP and HTTPS.[^3] [^1]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [PoetRAT](https://attack.mitre.org/software/S0428) has the ability to hide and unhide files.[^3]  |
| [[Automated Collection\|T1119]] | Automated Collection | [PoetRAT](https://attack.mitre.org/software/S0428) used file system monitoring to track modification and enable automatic exfiltration.[^3]  |
| [[Video Capture\|T1125]] | Video Capture | [PoetRAT](https://attack.mitre.org/software/S0428) has used a Python tool named Bewmac to record the webcam on compromised hosts.[^3]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [PoetRAT](https://attack.mitre.org/software/S0428) has used [ftp](https://attack.mitre.org/software/S0095) for exfiltration.[^3]  |
| [[System Checks\|T1497.001]] | System Checks | [PoetRAT](https://attack.mitre.org/software/S0428) checked the size of the hard drive to determine if it was being run in a sandbox environment. In the event of sandbox detection, it would delete itself by overwriting the malware scripts with the contents of "License.txt" and exiting.[^3]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [PoetRAT](https://attack.mitre.org/software/S0428) used Nmap for remote system discovery.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [PoetRAT](https://attack.mitre.org/software/S0428) has used HTTP and HTTPs for C2 communications.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [PoetRAT](https://attack.mitre.org/software/S0428) has the ability to gather information about the compromised host.[^3]  |
| [[Dynamic Data Exchange\|T1559.002]] | Dynamic Data Exchange | [PoetRAT](https://attack.mitre.org/software/S0428) was delivered with documents using DDE to execute malicious code.[^3]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [PoetRAT](https://attack.mitre.org/software/S0428) used voStro.exe, a compiled pypykatz (Python version of [Mimikatz](https://attack.mitre.org/software/S0002)), to steal credentials.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [PoetRAT](https://attack.mitre.org/software/S0428) has the ability to list all running processes.[^3]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [PoetRAT](https://attack.mitre.org/software/S0428) has used Word documents with VBScripts to execute malicious activities.[^3] [^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [PoetRAT](https://attack.mitre.org/software/S0428) used TLS to encrypt command and control (C2) communications.[^3]  |
| [[Python\|T1059.006]] | Python | [PoetRAT](https://attack.mitre.org/software/S0428) was executed with a Python script and worked in conjunction with additional Python-based post-exploitation tools.[^3]  |
| [[Screen Capture\|T1113]] | Screen Capture | [PoetRAT](https://attack.mitre.org/software/S0428) has the ability to take screen captures.[^3] [^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [PoetRAT](https://attack.mitre.org/software/S0428) has used LZMA and base64 libraries to decode obfuscated scripts.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [PoetRAT](https://attack.mitre.org/software/S0428) has used a custom encryption scheme for communication between scripts.[^3]  |
| [[Lua\|T1059.011]] | Lua | [PoetRAT](https://attack.mitre.org/software/S0428) has executed a Lua script through a Lua interpreter for Windows.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [PoetRAT](https://attack.mitre.org/software/S0428) has added a registry key in the <RUN> hive for persistence.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [PoetRAT](https://attack.mitre.org/software/S0428) has the ability to overwrite scripts and delete itself if a sandbox environment is detected.[^3]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [PoetRAT](https://attack.mitre.org/software/S0428) has used a Python tool named Browdec.exe to steal browser credentials.[^3]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [PoetRAT](https://attack.mitre.org/software/S0428) has the ability to compress files with zip.[^3]  |
| [[Keylogging\|T1056.001]] | Keylogging | [PoetRAT](https://attack.mitre.org/software/S0428) has used a Python tool named klog.exe for keylogging.[^3]  |




## References

[^1]: [Talos PoetRAT October 2020](https://blog.talosintelligence.com/2020/10/poetrat-update.html)


[^2]: [Dragos Threat Report 2020](https://hub.dragos.com/hubfs/Year-in-Review/Dragos_2020_ICS_Cybersecurity_Year_In_Review.pdf?hsCtaTracking=159c0fc3-92d8-425d-aeb8-12824f2297e8%7Cf163726d-579b-4996-9a04-44e5a124d770)


[^3]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)


