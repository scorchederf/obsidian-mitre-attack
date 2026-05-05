---
aliases: 
    - S1018
    
mitre-attack: https://attack.mitre.org/software/S1018
---

## S1018

[Saint Bot](https://attack.mitre.org/software/S1018) is a .NET downloader that has been used by [Saint Bear](https://attack.mitre.org/groups/G1031) since at least March 2021.[^1] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Saint Bot](https://attack.mitre.org/software/S1018) has used `regsvr32` to execute scripts.[^1] [^3]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Saint Bot](https://attack.mitre.org/software/S1018) has injected its DLL component into `EhStorAurhn.exe`.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Saint Bot](https://attack.mitre.org/software/S1018) can collect the IP address of a victim machine.[^1]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Saint Bot](https://attack.mitre.org/software/S1018) has attempted to bypass UAC using `fodhelper.exe` to escalate privileges.[^3]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Saint Bot](https://attack.mitre.org/software/S1018) has been obfuscated to help avoid detection.[^3]  |
| [[Masquerading\|T1036]] | Masquerading | [Saint Bot](https://attack.mitre.org/software/S1018) has renamed malicious binaries as `wallpaper.mp4` and `slideshow.mp4` to avoid detection.[^1] [^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Saint Bot](https://attack.mitre.org/software/S1018) can download additional files onto a compromised host.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Saint Bot](https://attack.mitre.org/software/S1018) has used HTTP for C2 communications.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Saint Bot](https://attack.mitre.org/software/S1018) can identify the OS version, CPU, and other details from a victim's machine.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Saint Bot](https://attack.mitre.org/software/S1018) has used `cmd.exe` and `.bat` scripts for execution.[^3]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [Saint Bot](https://attack.mitre.org/software/S1018) has used the command `timeout 20` to pause the execution of its initial loader.[^3]  |
| [[Query Registry\|T1012]] | Query Registry | [Saint Bot](https://attack.mitre.org/software/S1018) has used `check_registry_keys` as part of its environmental checks.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Saint Bot](https://attack.mitre.org/software/S1018) has created a scheduled task named "Maintenance" to establish persistence.[^1]  |
| [[Native API\|T1106]] | Native API | [Saint Bot](https://attack.mitre.org/software/S1018) has used different API calls, including `GetProcAddress`, `VirtualAllocEx`, `WriteProcessMemory`, `CreateProcessA`, and `SetThreadContext`.[^1] [^3]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Saint Bot](https://attack.mitre.org/software/S1018) has relied on users to execute a malicious attachment delivered via spearphishing.[^1] [^3]  |
| [[Asynchronous Procedure Call\|T1055.004]] | Asynchronous Procedure Call | [Saint Bot](https://attack.mitre.org/software/S1018) has written its payload into a newly-created `EhStorAuthn.exe` process using `ZwWriteVirtualMemory` and executed it using `NtQueueApcThread` and `ZwAlertResumeThread`.[^1]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Saint Bot](https://attack.mitre.org/software/S1018) has been distributed through malicious links contained within spearphishing emails.[^3]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Saint Bot](https://attack.mitre.org/software/S1018) has been packed using a dark market crypter.[^1]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Saint Bot](https://attack.mitre.org/software/S1018) has used `.vbs` scripts for execution.[^3]  |
| [[System Checks\|T1497.001]] | System Checks | [Saint Bot](https://attack.mitre.org/software/S1018) has run several virtual machine and sandbox checks, including checking if `Sbiedll.dll` is present in a list of loaded modules, comparing the machine name to `HAL9TH` and the user name to `JohnDoe`, and checking the BIOS version for known virtual machine identifiers.[^3]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Saint Bot](https://attack.mitre.org/software/S1018) has used PowerShell for execution.[^3]  |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [Saint Bot](https://attack.mitre.org/software/S1018) has used `is_debugger_present` as part of its environmental checks.[^1]  |
| [[System Location Discovery\|T1614]] | System Location Discovery | [Saint Bot](https://attack.mitre.org/software/S1018) has conducted system locale checks to see if the compromised host is in Russia, Ukraine, Belarus, Armenia, Kazakhstan, or Moldova.[^1] [^3]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Saint Bot](https://attack.mitre.org/software/S1018) has established persistence by being copied to the Startup directory or through the `\Software\Microsoft\Windows\CurrentVersion\Run` registry key.[^1] [^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Saint Bot](https://attack.mitre.org/software/S1018) can deobfuscate strings and files for execution.[^1]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | The [Saint Bot](https://attack.mitre.org/software/S1018) loader has used API calls to spawn `MSBuild.exe` in a suspended state before injecting the decrypted [Saint Bot](https://attack.mitre.org/software/S1018) binary into it.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Saint Bot](https://attack.mitre.org/software/S1018) has enumerated running processes on a compromised host to determine if it is running under the process name `dfrgui.exe`.[^3]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Saint Bot](https://attack.mitre.org/software/S1018) has been distributed as malicious attachments within spearphishing emails.[^1] [^3]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Saint Bot](https://attack.mitre.org/software/S1018) has been disguised as a legitimate executable, including as Windows SDK.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Saint Bot](https://attack.mitre.org/software/S1018) can search a compromised host for specific files.[^3]  |
| [[Hijack Execution Flow\|T1574]] | Hijack Execution Flow | [Saint Bot](https://attack.mitre.org/software/S1018) will use the malicious file `slideshow.mp4` if present to load the core API provided by `ntdll.dll` to avoid any hooks placed on calls to the original `ntdll.dll` file by endpoint detection and response or antimalware software.[^3]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Saint Bot](https://attack.mitre.org/software/S1018) can collect the username from a compromised host.[^1]  |
| [[InstallUtil\|T1218.004]] | InstallUtil | [Saint Bot](https://attack.mitre.org/software/S1018) had used `InstallUtil.exe` to download and deploy executables.[^1]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Saint Bot](https://attack.mitre.org/software/S1018) has relied on users to click on a malicious link delivered via a spearphishing.[^3]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Saint Bot](https://attack.mitre.org/software/S1018) has used Base64 to encode its C2 communications.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Saint Bot](https://attack.mitre.org/software/S1018) can run a batch script named `del.bat` to remove any [Saint Bot](https://attack.mitre.org/software/S1018) payload-linked files from a compromise system if anti-analysis or locale checks fail.[^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Saint Bot](https://attack.mitre.org/software/S1018) can collect files and information from a compromised host.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Ember Bear\|G1003]] | Ember Bear |
| [[Saint Bear\|G1031]] | Saint Bear |



## References

[^1]: [Malwarebytes Saint Bot April 2021](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)


[^2]: [CISA GRU29155 2024](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)


[^3]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)


