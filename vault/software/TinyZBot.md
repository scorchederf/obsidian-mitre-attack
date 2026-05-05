---
aliases: 
    - S0004
    
mitre-attack: https://attack.mitre.org/software/S0004
---

## S0004

[TinyZBot](https://attack.mitre.org/software/S0004) is a bot written in C# that was developed by [Cleaver](https://attack.mitre.org/groups/G0003). [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [TinyZBot](https://attack.mitre.org/software/S0004) can disable Avira anti-virus.[^1]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [TinyZBot](https://attack.mitre.org/software/S0004) contains functionality to collect information from the clipboard.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [TinyZBot](https://attack.mitre.org/software/S0004) contains screen capture functionality.[^1]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [TinyZBot](https://attack.mitre.org/software/S0004) can create a shortcut in the Windows startup folder for persistence.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [TinyZBot](https://attack.mitre.org/software/S0004) can install as a Windows service for persistence.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [TinyZBot](https://attack.mitre.org/software/S0004) can create a shortcut in the Windows startup folder for persistence.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [TinyZBot](https://attack.mitre.org/software/S0004) contains keylogger functionality.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [TinyZBot](https://attack.mitre.org/software/S0004) supports execution from the command-line.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Cleaver\|G0003]] | Cleaver |



## References

[^1]: [Cylance Cleaver](https://web.archive.org/web/20200302085133/https://www.cylance.com/content/dam/cylance/pages/operation-cleaver/Cylance_Operation_Cleaver_Report.pdf)


