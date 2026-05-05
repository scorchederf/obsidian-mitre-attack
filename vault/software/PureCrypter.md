---
aliases: 
    - S9019
    
mitre-attack: https://attack.mitre.org/software/S9019
---

## S9019

PureCrypter is a fully-featured malware loader, developed by a threat actor called “PureCoder," that has been in use since at least 2021 to distribute a variety of remote access trojans and information stealers.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [PureCrypter](https://attack.mitre.org/software/S9019) can enumerate processes on compromised hosts.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [PureCrypter](https://attack.mitre.org/software/S9019) can enumerate a targeted system's SerialNumber and Version.[^2] [^1]  |
| [[Mutual Exclusion\|T1480.002]] | Mutual Exclusion | [PureCrypter](https://attack.mitre.org/software/S9019) code contains a global mutex.[^2]  |
| [[Virtual Machine Discovery\|T1673]] | Virtual Machine Discovery | [PureCrypter](https://attack.mitre.org/software/S9019) can identify virtual machines by querying the WMI object Win32_ComputerSystem for manufacturer and model and check it against the regular expression Microsoft|VMWare|Virtual.[^2]  |
| [[Web Service\|T1102]] | Web Service | [PureCrypter](https://attack.mitre.org/software/S9019) can use Telegram or Discord to send infection status messages.[^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [PureCrypter](https://attack.mitre.org/software/S9019) has executed `Set-MpPreference -ExclusionPath` to exclude files or folders from Windows Defender scans.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [PureCrypter](https://attack.mitre.org/software/S9019) can retrieve the username from targeted machines.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [PureCrypter](https://attack.mitre.org/software/S9019) has used multiple file names to appear legitimate such as firefox\firefox.exe, Google\chrome.exe, and Taskmgr.exe.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [PureCrypter](https://attack.mitre.org/software/S9019) can decrypt downloaded resources and parse internal files to determine its settings.[^2] [^1]  |
| [[System Location Discovery\|T1614]] | System Location Discovery | [PureCrypter](https://attack.mitre.org/software/S9019) can use `kernel32!GetGeoInfo` to determine system location.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [PureCrypter](https://attack.mitre.org/software/S9019) can identify installed antivirus solutions.[^1]  |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [PureCrypter](https://attack.mitre.org/software/S9019) has the ability to call `CheckRemoteDebuggerPresent`.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [PureCrypter](https://attack.mitre.org/software/S9019) can maintain persistence with scheduled tasks.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [PureCrypter](https://attack.mitre.org/software/S9019) can send a TLS 1.2 encrypted infection message via Discord webhook.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [PureCrypter](https://attack.mitre.org/software/S9019) can set multiple Registry Run keys to establish persistence.[^2]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [PureCrypter](https://attack.mitre.org/software/S9019) code contains an ExclusionRegionNames option where it can compare the results of `kernel32!GetGeoInfo` with a list of regions.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [PureCrypter](https://attack.mitre.org/software/S9019) can download additional payloads for execution on the compromised host.[^2] [^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [PureCrypter](https://attack.mitre.org/software/S9019) can execute PowerShell commands to exclude files from EDR and to self-delete.[^2] [^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [PureCrypter](https://attack.mitre.org/software/S9019) can use AES to encrypt system information sent to the C2.[^1]  |
| [[Masquerade File Type\|T1036.008]] | Masquerade File Type | [PureCrypter](https://attack.mitre.org/software/S9019) has used a .NET downloader named 63342221.BAT and has used .jpg, .png, and .log as false extensions for malicious files.[^2]  |
| [[Process Injection\|T1055]] | Process Injection | [PureCrypter](https://attack.mitre.org/software/S9019) can inject its final stage into another process on the targeted system.[^2]  |
| [[Hidden Window\|T1564.003]] | Hidden Window |  [PureCrypter](https://attack.mitre.org/software/S9019) can set `ProcessWindowStyle.Hidden` to hide windows on victim machines.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [PureCrypter](https://attack.mitre.org/software/S9019) can execute a PowerShell command to self-delete.[^2]  |
| [[Delay Execution\|T1678]] | Delay Execution | [PureCrypter](https://attack.mitre.org/software/S9019) has the ability to delay for a specified number of seconds before execution.[^2]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [PureCrypter](https://attack.mitre.org/software/S9019) can insert junk code to avoid detection.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [PureCrypter](https://attack.mitre.org/software/S9019) has used SmartAssembly and NET-Reactor for string encryption and control flow obfuscation.[^2] [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT-C-36\|G0099]] | APT-C-36 |



## References

[^1]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)


[^2]: [Zscaler PureCrypter JUN 2022](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)


