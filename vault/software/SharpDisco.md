---
aliases: 
    - S1089
    
mitre-attack: https://attack.mitre.org/software/S1089
---

## S1089

[SharpDisco](https://attack.mitre.org/software/S1089) is a dropper developed in C# that has been used by [MoustachedBouncer](https://attack.mitre.org/groups/G1019) since at least 2020 to load malicious plugins.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [SharpDisco](https://attack.mitre.org/software/S1089) can create scheduled tasks to execute reverse shells that read and write data to and from specified SMB shares.[^1]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [SharpDisco](https://attack.mitre.org/software/S1089) can hide windows using `ProcessWindowStyle.Hidden`.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [SharpDisco](https://attack.mitre.org/software/S1089) has dropped a recent-files stealer plugin to `C:\Users\Public\WinSrcNT\It11.exe`.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [SharpDisco](https://attack.mitre.org/software/S1089) can load a plugin to exfiltrate stolen files to SMB shares also used in C2.[^1]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [SharpDisco](https://attack.mitre.org/software/S1089) has the ability to transfer data between SMB shares.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [SharpDisco](https://attack.mitre.org/software/S1089) can use a plugin to enumerate system drives.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [SharpDisco](https://attack.mitre.org/software/S1089) can use `cmd.exe` to execute plugins and to send command output to  specified SMB shares.[^1]  |
| [[Native API\|T1106]] | Native API | [SharpDisco](https://attack.mitre.org/software/S1089) can leverage Native APIs through plugins including `GetLogicalDrives`.[^1]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [SharpDisco](https://attack.mitre.org/software/S1089) has dropped a plugin to monitor external drives to `C:\Users\Public\It3.exe`.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SharpDisco](https://attack.mitre.org/software/S1089) has been used to download a Python interpreter to `C:\Users\Public\WinTN\WinTN.exe` as well as other plugins from external sources.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [SharpDisco](https://attack.mitre.org/software/S1089) can identify recently opened files by using an LNK format parser to extract the original file path from LNK files found in either `%USERPROFILE%\Recent` (Windows XP) or `%APPDATA%\Microsoft\Windows\Recent` (newer Windows versions) .[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MoustachedBouncer\|G1019]] | MoustachedBouncer |



## References

[^1]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)


