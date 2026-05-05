---
aliases: 
    - S0253
    
mitre-attack: https://attack.mitre.org/software/S0253
---

## S0253

[RunningRAT](https://attack.mitre.org/software/S0253) is a remote access tool that appeared in operations surrounding the 2018 Pyeongchang Winter Olympics along with [Gold Dragon](https://attack.mitre.org/software/S0249) and [Brave Prince](https://attack.mitre.org/software/S0252). [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [RunningRAT](https://attack.mitre.org/software/S0253) gathers logical drives information and volume information.[^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [RunningRAT](https://attack.mitre.org/software/S0253) kills antimalware running process.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [RunningRAT](https://attack.mitre.org/software/S0253) uses a batch file to kill a security program task and then attempts to remove itself.[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [RunningRAT](https://attack.mitre.org/software/S0253) captures keystrokes and sends them back to the C2 server.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [RunningRAT](https://attack.mitre.org/software/S0253) adds itself to the Registry key `Software\Microsoft\Windows\CurrentVersion\Run` to establish persistence upon reboot.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [RunningRAT](https://attack.mitre.org/software/S0253) contains code to delete files from the victim’s machine.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [RunningRAT](https://attack.mitre.org/software/S0253) gathers the OS version and processor information.[^2]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [RunningRAT](https://attack.mitre.org/software/S0253) contains code to compress files.[^2]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [RunningRAT](https://attack.mitre.org/software/S0253) contains code to clear event logs.[^2]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [RunningRAT](https://attack.mitre.org/software/S0253) contains code to open and copy data from the clipboard.[^2]  |




## References

[^1]: RunningRAT


[^2]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)


