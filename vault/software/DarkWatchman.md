---
aliases: 
    - S0673
    
mitre-attack: https://attack.mitre.org/software/S0673
---

## S0673

[DarkWatchman](https://attack.mitre.org/software/S0673) is a lightweight JavaScript-based remote access tool (RAT) that avoids file operations; it was first observed in November 2021.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Location Discovery\|T1614]] | System Location Discovery | [DarkWatchman](https://attack.mitre.org/software/S0673) can identity the OS locale of a compromised host.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [DarkWatchman](https://attack.mitre.org/software/S0673) has been observed deleting its original launcher after installation.[^1]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [DarkWatchman](https://attack.mitre.org/software/S0673) can store configuration strings, keylogger, and output of components in the Registry.[^1]  |
| [[Compression\|T1027.015]] | Compression | [DarkWatchman](https://attack.mitre.org/software/S0673) has been delivered as compressed RAR payloads in ZIP files to victims.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [DarkWatchman](https://attack.mitre.org/software/S0673) can modify Registry values to store configuration strings, keylogger, and output of components.[^1]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [DarkWatchman](https://attack.mitre.org/software/S0673) can delete shadow volumes using `vssadmin.exe`.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [DarkWatchman](https://attack.mitre.org/software/S0673) can stage local data in the Windows Registry.[^1]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [DarkWatchman](https://attack.mitre.org/software/S0673) reports window names along with keylogger information to provide application context.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [DarkWatchman](https://attack.mitre.org/software/S0673) can execute PowerShell commands and has used PowerShell to execute a keylogger.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [DarkWatchman](https://attack.mitre.org/software/S0673) can collect time zone information and system `UPTIME`.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [DarkWatchman](https://attack.mitre.org/software/S0673) has the ability to enumerate file and folder names.[^1]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [DarkWatchman](https://attack.mitre.org/software/S0673) has used Base64 to encode PowerShell commands.[^1]  |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [DarkWatchman](https://attack.mitre.org/software/S0673) has used a DGA to generate a domain name for C2.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [DarkWatchman](https://attack.mitre.org/software/S0673) can query the Registry to determine if it has already been installed on the system.[^1]  |
| [[Shared Modules\|T1129]] | Shared Modules | [DarkWatchman](https://attack.mitre.org/software/S0673) can load DLLs.[^1]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [DarkWatchman](https://attack.mitre.org/software/S0673) can retrieve browser history.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [DarkWatchman](https://attack.mitre.org/software/S0673) encodes data using hexadecimal representation before sending it to the C2 server.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [DarkWatchman](https://attack.mitre.org/software/S0673) can use `cmd.exe` to execute commands.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [DarkWatchman](https://attack.mitre.org/software/S0673) can use TLS to encrypt its C2 channel.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [DarkWatchman](https://attack.mitre.org/software/S0673) uses HTTPS for command and control.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [DarkWatchman](https://attack.mitre.org/software/S0673) can collect files from a compromised host.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [DarkWatchman](https://attack.mitre.org/software/S0673) has the ability to self-extract as a RAR archive.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [DarkWatchman](https://attack.mitre.org/software/S0673) can use WMI to execute commands.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [DarkWatchman](https://attack.mitre.org/software/S0673) has been delivered via spearphishing emails that contain a malicious zip file.[^1]  |
| [[Compile After Delivery\|T1027.004]] | Compile After Delivery | [DarkWatchman](https://attack.mitre.org/software/S0673) has used the `csc.exe` tool to compile a C# executable.[^1]   |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [DarkWatchman](https://attack.mitre.org/software/S0673) has created a scheduled task for persistence.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [DarkWatchman](https://attack.mitre.org/software/S0673) can search for anti-virus products on the system.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [DarkWatchman](https://attack.mitre.org/software/S0673) can track key presses with a keylogger module.[^1]  |
| [[Masquerading\|T1036]] | Masquerading | [DarkWatchman](https://attack.mitre.org/software/S0673) has used an icon mimicking a text file to mask a malicious executable.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [DarkWatchman](https://attack.mitre.org/software/S0673) can collect the OS version, system architecture, and computer name.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [DarkWatchman](https://attack.mitre.org/software/S0673) has collected the username from a victim machine.[^1]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [DarkWatchman](https://attack.mitre.org/software/S0673) can uninstall malicious components from the Registry, stop processes, and clear the browser history.[^1]  |
| [[JavaScript\|T1059.007]] | JavaScript | [DarkWatchman](https://attack.mitre.org/software/S0673) uses JavaScript to perform its core functionalities.[^1]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [DarkWatchman](https://attack.mitre.org/software/S0673) can list signed PnP drivers for smartcard readers.[^1]  |




## References

[^1]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)


