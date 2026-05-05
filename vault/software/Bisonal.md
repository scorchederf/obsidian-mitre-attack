---
aliases: 
    - S0268
    
mitre-attack: https://attack.mitre.org/software/S0268
---

## S0268

[Bisonal](https://attack.mitre.org/software/S0268) is a remote access tool (RAT) that has been used by [Tonto Team](https://attack.mitre.org/groups/G0131) against public and private sector organizations in Russia, South Korea, and Japan since at least December 2010.[^3] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Native API\|T1106]] | Native API | [Bisonal](https://attack.mitre.org/software/S0268) has used the Windows API to communicate with the Service Control Manager to execute a thread.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Bisonal](https://attack.mitre.org/software/S0268) will delete its dropper and VBS scripts from the victim’s machine.[^3] [^4] [^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Bisonal](https://attack.mitre.org/software/S0268) variants reported on in 2014 and 2015 used a simple XOR cipher for C2. Some [Bisonal](https://attack.mitre.org/software/S0268) samples encrypt C2 communications with RC4.[^3] [^4] [^2]   |
| [[Process Discovery\|T1057]] | Process Discovery | [Bisonal](https://attack.mitre.org/software/S0268) can obtain a list of running processes on the victim’s machine.[^3] [^4] [^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Bisonal](https://attack.mitre.org/software/S0268) has the capability to download files to execute on the victim’s machine.[^3] [^4] [^2]   |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [Bisonal](https://attack.mitre.org/software/S0268) can check to determine if the compromised system is running on VMware.[^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Bisonal](https://attack.mitre.org/software/S0268) has been modified to be used as a Windows service.[^2]   |
| [[Add-ins\|T1137.006]] | Add-ins | [Bisonal](https://attack.mitre.org/software/S0268) has been loaded through a `.wll` extension added to the ` %APPDATA%\microsoft\word\startup\` repository.[^2]   |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Bisonal](https://attack.mitre.org/software/S0268)'s dropper creates VBS scripts on the victim’s machine.[^3] [^2]   |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Bisonal](https://attack.mitre.org/software/S0268) has decoded strings in the malware using XOR and RC4.[^3] [^2]   |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Bisonal](https://attack.mitre.org/software/S0268)'s DLL file and non-malicious decoy file are encrypted with RC4 and some function name strings are obfuscated.[^3] [^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Bisonal](https://attack.mitre.org/software/S0268) can retrieve a file listing from the system.[^4] [^2]   |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Bisonal](https://attack.mitre.org/software/S0268) has added itself to the Registry key `HKEY_CURRENT_USER\Software\Microsoft\CurrentVersion\Run\` for persistence.[^3] [^2]   |
| [[Data from Local System\|T1005]] | Data from Local System | [Bisonal](https://attack.mitre.org/software/S0268) has collected information from a compromised host.[^2]   |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [Bisonal](https://attack.mitre.org/software/S0268) has checked if the malware is running in a virtual environment with the anti-debug function GetTickCount() to compare the timing.[^4] [^2]   |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Bisonal](https://attack.mitre.org/software/S0268) has used HTTP for C2 communications.[^3] [^4]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Bisonal](https://attack.mitre.org/software/S0268) has deleted Registry keys to clean up its prior activity.[^2]   |
| [[Rundll32\|T1218.011]] | Rundll32 | [Bisonal](https://attack.mitre.org/software/S0268) has used rundll32.exe to execute as part of the Registry Run key it adds: `HKEY_CURRENT_USER \Software\Microsoft\Windows\CurrentVersion\Run\”vert” = “rundll32.exe c:\windows\temp\pvcu.dll , Qszdez”`.[^3]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Bisonal](https://attack.mitre.org/software/S0268) has relied on users to execute malicious file attachments delivered via spearphishing emails.[^2]   |
| [[Binary Padding\|T1027.001]] | Binary Padding | [Bisonal](https://attack.mitre.org/software/S0268) has appended random binary data to the end of itself to generate a large binary.[^2]   |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Bisonal](https://attack.mitre.org/software/S0268) has been delivered as malicious email attachments.[^2]   |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Bisonal](https://attack.mitre.org/software/S0268) has encoded binary data with Base64 and ASCII.[^4] [^2]   |
| [[Query Registry\|T1012]] | Query Registry | [Bisonal](https://attack.mitre.org/software/S0268) has used the RegQueryValueExA function to retrieve proxy information in the Registry.[^2]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Bisonal](https://attack.mitre.org/software/S0268) has used the MPRESS packer and similar tools for obfuscation.[^2]   |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel |  [Bisonal](https://attack.mitre.org/software/S0268) has added the exfiltrated data to the URL over the C2 channel.[^2]   |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Bisonal](https://attack.mitre.org/software/S0268) has used raw sockets for network communication.[^2]  |
| [[Proxy\|T1090]] | Proxy | [Bisonal](https://attack.mitre.org/software/S0268) has supported use of a proxy server.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Bisonal](https://attack.mitre.org/software/S0268) has launched cmd.exe and used the ShellExecuteW() API function to execute commands on the system.[^3] [^4] [^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Bisonal](https://attack.mitre.org/software/S0268) has used commands and API calls to gather system information.[^3] [^4] [^2]  |
| [[Dynamic Resolution\|T1568]] | Dynamic Resolution | [Bisonal](https://attack.mitre.org/software/S0268) has used a dynamic DNS service for C2.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Bisonal](https://attack.mitre.org/software/S0268) can execute `ipconfig` on the victim’s machine.[^3] [^4] [^2]   |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Bisonal](https://attack.mitre.org/software/S0268) can check the system time set on the infected host.[^4]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Bisonal](https://attack.mitre.org/software/S0268) has renamed malicious code to `msacm32.dll` to hide within a legitimate library; earlier versions were disguised as `winhelp`.[^2]   |
| [[Masquerading\|T1036]] | Masquerading |  [Bisonal](https://attack.mitre.org/software/S0268) dropped a decoy payload with a .jpg extension that contained a malicious Visual Basic script.[^2]   |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Tonto Team\|G0131]] | Tonto Team |



## References

[^1]: [Secureworks BRONZE HUNTLEY ](https://www.secureworks.com/research/threat-profiles/bronze-huntley)


[^2]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)


[^3]: [Unit 42 Bisonal July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-bisonal-malware-used-attacks-russia-south-korea/)


[^4]: [Kaspersky CactusPete Aug 2020](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)


[^5]: Bisonal


