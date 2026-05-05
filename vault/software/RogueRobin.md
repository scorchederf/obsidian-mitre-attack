---
aliases: 
    - S0270
    
mitre-attack: https://attack.mitre.org/software/S0270
---

## S0270

[RogueRobin](https://attack.mitre.org/software/S0270) is a payload used by [DarkHydrus](https://attack.mitre.org/groups/G0079) that has been developed in PowerShell and C#. [^3] [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [RogueRobin](https://attack.mitre.org/software/S0270) establishes persistence by creating a shortcut (.LNK file) in the Windows startup folder to run a script each time the user logs in.[^3] [^4]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [RogueRobin](https://attack.mitre.org/software/S0270) uses various WMI queries to check if the sample is running in a sandbox.[^3] [^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [RogueRobin](https://attack.mitre.org/software/S0270) can save a new file to the system from the C2 server.[^3] [^4]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [RogueRobin](https://attack.mitre.org/software/S0270) gathers the IP address and domain from the victim’s machine.[^3]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [RogueRobin](https://attack.mitre.org/software/S0270) uses regsvr32.exe to run a .sct file for execution.[^4]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [RogueRobin](https://attack.mitre.org/software/S0270) collects the victim’s username and whether that user is an admin.[^3]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | The PowerShell script with the [RogueRobin](https://attack.mitre.org/software/S0270) payload was obfuscated using the COMPRESS technique in `Invoke-Obfuscation`.[^3] [^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [RogueRobin](https://attack.mitre.org/software/S0270) base64 encodes strings that are sent to the C2 over its DNS tunnel.[^3]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [RogueRobin](https://attack.mitre.org/software/S0270) has used Google Drive as a Command and Control channel. [^4]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [RogueRobin](https://attack.mitre.org/software/S0270) uses Windows Script Components.[^4] [^3]  |
| [[System Checks\|T1497.001]] | System Checks | [RogueRobin](https://attack.mitre.org/software/S0270) uses WMI to check BIOS version for VBOX, bochs, qemu, virtualbox, and vm to check for evidence that the script might be executing within an analysis environment. [^3] [^4]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [RogueRobin](https://attack.mitre.org/software/S0270) enumerates running processes to search for Wireshark and Windows Sysinternals suite.[^3] [^4]  |
| [[Process Discovery\|T1057]] | Process Discovery | [RogueRobin](https://attack.mitre.org/software/S0270) checks the running processes for evidence it may be running in a sandbox environment. It specifically enumerates processes for Wireshark and Sysinternals.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [RogueRobin](https://attack.mitre.org/software/S0270) gathers BIOS versions and manufacturers, the number of CPU cores, the total physical memory, and the computer name.[^3]  |
| [[PowerShell\|T1059.001]] | PowerShell | [RogueRobin](https://attack.mitre.org/software/S0270) uses a command prompt to run a PowerShell script from Excel.[^3]  To assist in establishing persistence, [RogueRobin](https://attack.mitre.org/software/S0270) creates `%APPDATA%\OneDrive.bat` and saves the following string to it:`powershell.exe -WindowStyle Hidden -exec bypass -File “%APPDATA%\OneDrive.ps1”`.[^4] [^3]  |
| [[Screen Capture\|T1113]] | Screen Capture | [RogueRobin](https://attack.mitre.org/software/S0270) has a command named `$screenshot` that may be responsible for taking screenshots of the victim machine.[^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [RogueRobin](https://attack.mitre.org/software/S0270) decodes an embedded executable using base64 and decompresses it.[^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [RogueRobin](https://attack.mitre.org/software/S0270) created a shortcut in the Windows startup folder to launch a PowerShell script each time the user logs in to establish persistence.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[DarkHydrus\|G0079]] | DarkHydrus |



## References

[^1]: [GitHub Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation)


[^2]: RogueRobin


[^3]: [Unit 42 DarkHydrus July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)


[^4]: [Unit42 DarkHydrus Jan 2019](https://unit42.paloaltonetworks.com/darkhydrus-delivers-new-trojan-that-can-use-google-drive-for-c2-communications/)


