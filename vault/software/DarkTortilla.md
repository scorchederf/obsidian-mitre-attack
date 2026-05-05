---
aliases: 
    - S1066
    
mitre-attack: https://attack.mitre.org/software/S1066
---

## S1066

[DarkTortilla](https://attack.mitre.org/software/S1066) is a highly configurable .NET-based crypter that has been possibly active since at least August 2015. [DarkTortilla](https://attack.mitre.org/software/S1066) has been used to deliver popular information stealers, RATs, and payloads such as [Agent Tesla](https://attack.mitre.org/software/S0331), AsyncRat, [NanoCore](https://attack.mitre.org/software/S0336), RedLine, [Cobalt Strike](https://attack.mitre.org/software/S0154), and Metasploit.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [DarkTortilla](https://attack.mitre.org/software/S1066) can download additional packages for keylogging, cryptocurrency mining, and other capabilities; it can also retrieve malicious payloads such as [Agent Tesla](https://attack.mitre.org/software/S0331), AsyncRat, [NanoCore](https://attack.mitre.org/software/S0336), RedLine, [Cobalt Strike](https://attack.mitre.org/software/S0154), and Metasploit.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [DarkTortilla](https://attack.mitre.org/software/S1066) can decrypt its payload and associated configuration elements using the Rijndael cipher.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [DarkTortilla](https://attack.mitre.org/software/S1066) has been obfuscated with the DeepSea .NET and ConfuserEx code obfuscators.[^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [DarkTortilla](https://attack.mitre.org/software/S1066) can use a .NET-based DLL named `RunPe6` for process injection.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [DarkTortilla](https://attack.mitre.org/software/S1066) has been distributed via spearphishing emails containing archive attachments, with file types such as .iso, .zip, .img, .dmg, and .tar, as well as through malicious documents.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [DarkTortilla](https://attack.mitre.org/software/S1066) has established persistence via the `Software\Microsoft\Windows NT\CurrentVersion\Run` registry key and by creating a .lnk shortcut file in the Windows startup folder.[^1]  |
| [[Winlogon Helper DLL\|T1547.004]] | Winlogon Helper DLL |  [DarkTortilla](https://attack.mitre.org/software/S1066) has established persistence via the `Software\Microsoft\Windows NT\CurrentVersion\Winlogon` registry key.[^1]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [DarkTortilla](https://attack.mitre.org/software/S1066) can implement the `kernel32.dll` Sleep function to delay execution for up to 300 seconds before implementing persistence or processing an addon package.[^1]  |
| [[COR_PROFILER\|T1574.012]] | COR_PROFILER | [DarkTortilla](https://attack.mitre.org/software/S1066) can detect profilers by verifying the `COR_ENABLE_PROFILING` environment variable is present and active.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [DarkTortilla](https://attack.mitre.org/software/S1066) can check for the Kaspersky Anti-Virus suite.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [DarkTortilla](https://attack.mitre.org/software/S1066) can use `cmd.exe` to add registry keys for persistence.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [DarkTortilla](https://attack.mitre.org/software/S1066) can obtain system information by querying the `Win32_ComputerSystem`, `Win32_BIOS`, `Win32_MotherboardDevice`, `Win32_PnPEntity`, and `Win32_DiskDrive` WMI objects.[^1]  |
| [[Masquerading\|T1036]] | Masquerading | [DarkTortilla](https://attack.mitre.org/software/S1066)'s payload has been renamed `PowerShellInfo.exe`.[^1]  |
| [[Hide Artifacts\|T1564]] | Hide Artifacts | [DarkTortilla](https://attack.mitre.org/software/S1066) has used `%HiddenReg%` and `%HiddenKey%` as part of its persistence via the Windows registry.[^1]  |
| [[System Checks\|T1497.001]] | System Checks | [DarkTortilla](https://attack.mitre.org/software/S1066) can search a compromised system's running processes and services to detect Hyper-V, QEMU, Virtual PC, Virtual Box, and VMware, as well as Sandboxie.[^1]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [DarkTortilla](https://attack.mitre.org/software/S1066) can download a clipboard information stealer module.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [DarkTortilla](https://attack.mitre.org/software/S1066) can download a keylogging module.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [DarkTortilla](https://attack.mitre.org/software/S1066) has relied on a user to open a malicious document or archived file delivered via email for initial execution.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [DarkTortilla](https://attack.mitre.org/software/S1066) can enumerate a list of running processes on a compromised system.[^1]  |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [DarkTortilla](https://attack.mitre.org/software/S1066) can check for internet connectivity by issuing HTTP GET requests.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [DarkTortilla](https://attack.mitre.org/software/S1066) can use WMI queries to obtain system information.[^1]  |
| [[Native API\|T1106]] | Native API | [DarkTortilla](https://attack.mitre.org/software/S1066) can use a variety of API calls for persistence and defense evasion.[^1]  |
| [[Web Service\|T1102]] | Web Service | [DarkTortilla](https://attack.mitre.org/software/S1066) can retrieve its primary payload from public sites such as Pastebin and Textbin.[^1]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [DarkTortilla](https://attack.mitre.org/software/S1066) can retrieve information about a compromised system's running services.[^1]  |
| [[Component Object Model\|T1559.001]] | Component Object Model | [DarkTortilla](https://attack.mitre.org/software/S1066) has used the `WshShortcut` COM object to create a .lnk shortcut file in the Windows startup folder.[^1]  |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [DarkTortilla](https://attack.mitre.org/software/S1066) can detect debuggers by using functions such as `DebuggerIsAttached` and `DebuggerIsLogging`. [DarkTortilla](https://attack.mitre.org/software/S1066) can also detect profilers by verifying the `COR_ENABLE_PROFILING` environment variable is present and active.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [DarkTortilla](https://attack.mitre.org/software/S1066) has modified registry keys for persistence.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [DarkTortilla](https://attack.mitre.org/software/S1066) has used HTTP and HTTPS for C2.[^1]  |




## References

[^1]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)


