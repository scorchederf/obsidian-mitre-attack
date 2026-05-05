---
aliases: 
    - S0259
    
mitre-attack: https://attack.mitre.org/software/S0259
---

## S0259

[InnaputRAT](https://attack.mitre.org/software/S0259) is a remote access tool that can exfiltrate files from a victim’s machine. [InnaputRAT](https://attack.mitre.org/software/S0259) has been seen out in the wild since 2016. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [InnaputRAT](https://attack.mitre.org/software/S0259) launches a shell to execute commands on the victim’s machine.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [InnaputRAT](https://attack.mitre.org/software/S0259) gathers system information.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [InnaputRAT](https://attack.mitre.org/software/S0259) uses an 8-byte XOR key to obfuscate API names and other strings contained in the payload.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [InnaputRAT](https://attack.mitre.org/software/S0259) has a command to delete files.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [InnaputRAT](https://attack.mitre.org/software/S0259) enumerates directories and obtains file attributes on a system.[^1]  |
| [[Native API\|T1106]] | Native API | [InnaputRAT](https://attack.mitre.org/software/S0259) uses the API call ShellExecuteW for execution.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [InnaputRAT](https://attack.mitre.org/software/S0259) variants have attempted to appear legitimate by adding a new service named OfficeUpdateService.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | Some [InnaputRAT](https://attack.mitre.org/software/S0259) variants establish persistence by modifying the Registry key `HKU\<SID>\Software\Microsoft\Windows\CurrentVersion\Run:%appdata%\NeutralApp\NeutralApp.exe`.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | Some [InnaputRAT](https://attack.mitre.org/software/S0259) variants create a new Windows service to establish persistence.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [InnaputRAT](https://attack.mitre.org/software/S0259) gathers volume drive information.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [InnaputRAT](https://attack.mitre.org/software/S0259) variants have attempted to appear legitimate by using the file names SafeApp.exe and NeutralApp.exe.[^1]  |




## References

[^1]: [ASERT InnaputRAT April 2018](https://asert.arbornetworks.com/innaput-actors-utilize-remote-access-trojan-since-2016-presumably-targeting-victim-files/)


[^2]: InnaputRAT


