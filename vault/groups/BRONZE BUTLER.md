---
aliases: 
    - BRONZE BUTLER
    - REDBALDKNIGHT
    - Tick
mitre-attack: https://attack.mitre.org/groups/G0060
---

## G0060

[BRONZE BUTLER](https://attack.mitre.org/groups/G0060) is a cyber espionage group with likely Chinese origins that has been active since at least 2008. The group primarily targets Japanese organizations, particularly those in government, biotechnology, electronics manufacturing, and industrial chemistry.[^2] [^1] [^8] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) downloads encoded payloads and decodes them on the victim.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has exfiltrated files stolen from local systems.[^1]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used TROJ_GETVERSION to discover system services.[^8]  |
| [[File Deletion\|T1070.004]] | File Deletion | The [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) uploader or malware the uploader uses `command` to delete the RAR archives after they have been exfiltrated.[^1]  |
| [[Python\|T1059.006]] | Python | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has made use of Python-based remote access tools.[^8]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) used spearphishing emails with malicious Microsoft Word attachments to infect victims.[^6] [^8]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has given malware the same name as an existing file on the file share server to cause users to unwittingly launch and install the malware on additional systems.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used a tool to capture screenshots.[^1] [^8]  |
| [[Masquerading\|T1036]] | Masquerading | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has masked executables with document file icons including Word and Adobe PDF.[^8]  |
| [[Tool\|T1588.002]] | Tool | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has obtained and used open-source tools such as [Mimikatz](https://attack.mitre.org/software/S0002), [gsecdump](https://attack.mitre.org/software/S0008), and [Windows Credential Editor](https://attack.mitre.org/software/S0005).[^6]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used a Windows 10 specific tool and xxmm to bypass UAC for privilege escalation.[^1] [^8]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used VBS and VBE scripts for execution.[^1] [^8]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | Several [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) tools encode data with base64 when posting it to a C2 server.[^1]  |
| [[Software Discovery\|T1518]] | Software Discovery | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used tools to enumerate software installed on an infected host.[^8]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) malware has used HTTP for C2.[^1]  |
| [[Data from Network Shared Drive\|T1039]] | Data from Network Shared Drive | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has exfiltrated files stolen from file shares.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has incorporated code into several tools that attempts to terminate anti-virus processes.[^8]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used `net time` to check the local time on a target system.[^1]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) compromised three Japanese websites using a Flash exploit to perform watering hole attacks.[^6]  |
| [[DLL\|T1574.001]] | DLL | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used legitimate applications to side-load malicious DLLs.[^8]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used various tools (such as Mimikatz and WCE) to perform credential dumping.[^1]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has exploited Microsoft Office vulnerabilities CVE-2014-4114, CVE-2018-0802, and CVE-2018-0798 for execution.[^6] [^8]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) typically use `ping` and [Net](https://attack.mitre.org/software/S0039) to enumerate systems.[^1]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has compressed data into password-protected RAR archives prior to exfiltration.[^1] [^8]  |
| [[At\|T1053.002]] | At | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used [at](https://attack.mitre.org/software/S0110) to register a scheduled task to execute malware during lateral movement.[^1]  |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060)'s MSGET downloader uses a dead drop resolver to access malicious payloads.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used [schtasks](https://attack.mitre.org/software/S0111) to register a scheduled task to execute malware during lateral movement.[^1]  |
| [[Taint Shared Content\|T1080]] | Taint Shared Content | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has placed malware on file shares and given it the same name as legitimate documents on the share.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has attempted to get users to launch malicious Microsoft Word attachments delivered via spearphishing emails.[^6] [^8]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) downloader code has included "0" characters at the end of the file to inflate the file size in a likely attempt to evade anti-virus detection.[^1] [^8]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used a batch script that adds a Registry Run key to establish malware persistence.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used PowerShell for execution.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used batch scripts and the command-line interface for execution.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used various tools to download files, including DGet (a similar tool to wget).[^1]  |
| [[Pass the Ticket\|T1550.003]] | Pass the Ticket | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has created forged Kerberos Ticket Granting Ticket (TGT) and Ticket Granting Service (TGS) tickets to maintain administrative access.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used RC4 encryption (for Datper malware) and AES (for xxmm malware) to obfuscate HTTP traffic. [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has also used a tool called RarStar that encodes data with a custom XOR algorithm when posting it to a C2 server.[^1]  |
| [[Steganography\|T1027.003]] | Steganography | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used steganography in multiple operations to conceal malicious payloads.[^8]  |
| [[Domain Account\|T1087.002]] | Domain Account | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used `net user /domain` to identify account information.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has collected a list of files from the victim and uploaded it to its C2 server, and then created a new list of specific files to steal.[^1]  |
| [[Right-to-Left Override\|T1036.002]] | Right-to-Left Override | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used Right-to-Left Override to deceive victims into executing several strains of malware.[^8]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^1]  |
| [[at\|S0110]] | at | [^1]  |
| [[Windows Credential Editor\|S0005]] | Windows Credential Editor | [^1] [^6]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^1] [^6] [^8]  |
| [[gsecdump\|S0008]] | gsecdump | [^1] [^6]  |
| [[cmd\|S0106]] | cmd | [^1]  |
| [[schtasks\|S0111]] | schtasks | [^1]  |
| [[Avenger\|S0473]] | Avenger | [^8]  |
| [[down_new\|S0472]] | down_new | [^8]  |
| [[ABK\|S0469]] | ABK | [^8]  |
| [[Daserf\|S0187]] | Daserf | [^2] [^6]  |
| [[build_downer\|S0471]] | build_downer | [^8]  |
| [[ShadowPad\|S0596]] | ShadowPad | [^7]  |
| [[BBK\|S0470]] | BBK | [^8]  |



## References

[^1]: [Secureworks BRONZE BUTLER Oct 2017](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)


[^2]: [Trend Micro Daserf Nov 2017](http://blog.trendmicro.com/trendlabs-security-intelligence/redbaldknight-bronze-butler-daserf-backdoor-now-using-steganography/)


[^3]: REDBALDKNIGHT


[^4]: Tick


[^5]: BRONZE BUTLER


[^6]: [Symantec Tick Apr 2016](https://www.symantec.com/connect/blogs/tick-cyberespionage-group-zeros-japan)


[^7]: [Recorded Future RedEcho Feb 2021](https://go.recordedfuture.com/hubfs/reports/cta-2021-0228.pdf)


[^8]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)


