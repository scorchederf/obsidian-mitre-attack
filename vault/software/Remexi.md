---
aliases: 
    - S0375
    
mitre-attack: https://attack.mitre.org/software/S0375
---

## S0375

[Remexi](https://attack.mitre.org/software/S0375) is a Windows-based Trojan that was developed in the C programming language.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Remexi](https://attack.mitre.org/software/S0375) utilizes scheduled tasks as a persistence mechanism.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Remexi](https://attack.mitre.org/software/S0375) silently executes received commands with cmd.exe.[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Remexi](https://attack.mitre.org/software/S0375) gathers and exfiltrates keystrokes from the machine.[^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Remexi](https://attack.mitre.org/software/S0375) performs exfiltration over [BITSAdmin](https://attack.mitre.org/software/S0190), which is also used for the C2 channel.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Remexi](https://attack.mitre.org/software/S0375) obfuscates its configuration data with XOR.[^2]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [Remexi](https://attack.mitre.org/software/S0375) collects text from the clipboard.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Remexi](https://attack.mitre.org/software/S0375) utilizes Run Registry keys in the HKLM hive as a persistence mechanism.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Remexi](https://attack.mitre.org/software/S0375) uses [BITSAdmin](https://attack.mitre.org/software/S0190) to communicate with the C2 server over HTTP.[^2]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Remexi](https://attack.mitre.org/software/S0375) executes received commands with wmic.exe (for WMI commands). [^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Remexi](https://attack.mitre.org/software/S0375) decrypts the configuration data using XOR with 25-character keys.[^2]  |
| [[Winlogon Helper DLL\|T1547.004]] | Winlogon Helper DLL | [Remexi](https://attack.mitre.org/software/S0375) achieves persistence using Userinit by adding the Registry key `HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit`.[^2]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [Remexi](https://attack.mitre.org/software/S0375) has a command to capture active windows on the machine and retrieve window titles.[^2]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Remexi](https://attack.mitre.org/software/S0375) encrypts and adds all gathered browser data into files for upload to C2.[^2]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Remexi](https://attack.mitre.org/software/S0375) uses AutoIt and VBS scripts throughout its execution process.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Remexi](https://attack.mitre.org/software/S0375) takes screenshots of windows of interest.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Remexi](https://attack.mitre.org/software/S0375) searches for files on the system. [^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT39\|G0087]] | APT39 |



## References

[^1]: [Symantec Chafer Dec 2015](https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets)


[^2]: [Securelist Remexi Jan 2019](https://securelist.com/chafer-used-remexi-malware/89538/)


[^3]: [Symantec Chafer February 2018](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/chafer-latest-attacks-reveal-heightened-ambitions)


