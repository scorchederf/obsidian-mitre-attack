---
aliases: 
    - S9032
    
mitre-attack: https://attack.mitre.org/software/S9032
---

## S9032

[MuddyViper](https://attack.mitre.org/software/S9032) is custom backdoor written in C and C++ used by [MuddyWater](https://attack.mitre.org/groups/G0069) for command and control (C2) communications and persistence. [MuddyViper](https://attack.mitre.org/software/S9032) is loaded by [Fooder](https://attack.mitre.org/software/S9033) and sends frequent messages to the C2 server.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Delay Execution\|T1678]] | Delay Execution | [MuddyViper](https://attack.mitre.org/software/S9032) has the ability to sleep for a certain amount of time, with the default being one minute.[^1]       |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [MuddyViper](https://attack.mitre.org/software/S9032) has the ability to check for a specified list of security tools in the compromised environment.[^1]      |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [MuddyViper](https://attack.mitre.org/software/S9032) has the ability to download files from the C2 server. Additionally, [MuddyViper](https://attack.mitre.org/software/S9032) has the ability to download a file in chunks with sleep time between each chunk.[^1]       |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [MuddyViper](https://attack.mitre.org/software/S9032) has the ability to encrypt C2 communication using AES-CBC using the CNG API, the key `0608101047106453101617106423101013101012101083109710108585106969`, and the initialization vector `0`.[^1]       |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [MuddyViper](https://attack.mitre.org/software/S9032) has archived collected web browser data into a file named CacheDump.zip.[^1]         |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [MuddyViper](https://attack.mitre.org/software/S9032) has the ability to establish persistence by creating a scheduled task named ManageOnDriveUpdater to launch itself during system startup.[^1]       |
| [[Process Discovery\|T1057]] | Process Discovery | [MuddyViper](https://attack.mitre.org/software/S9032) has the ability to collect running processes.[^1]      |
| [[Web Protocols\|T1071.001]] | Web Protocols | [MuddyViper](https://attack.mitre.org/software/S9032) has used HTTP GET requests over port 443 and with the WINHTTP_FLAG_SECURE set to SSL/TLS via the WinHTTP API.[^1]       |
| [[Native API\|T1106]] | Native API | [MuddyViper](https://attack.mitre.org/software/S9032) has the ability to relaunch itself using the `CreateProcessW` API.[^1]       |
| [[Modify Registry\|T1112]] | Modify Registry | [MuddyViper](https://attack.mitre.org/software/S9032) has the ability to clear the Registry values in the Windows Startup folder that were previously set for persistence.[^1]       |
| [[GUI Input Capture\|T1056.002]] | GUI Input Capture | [MuddyViper](https://attack.mitre.org/software/S9032) has displayed a fake Windows Security dialog to gather credentials.[^1]       |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [MuddyViper](https://attack.mitre.org/software/S9032) has reflectively loaded the decrypted HackBrowserData tool in a new thread.[^1]        |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [MuddyViper](https://attack.mitre.org/software/S9032) has decrypted the embedded HackBrowserData tool prior to execution.[^1]      |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [MuddyViper](https://attack.mitre.org/software/S9032) has uploaded files to the C2 server. Additionally, [MuddyViper](https://attack.mitre.org/software/S9032) has the ability to upload the specified file in chunks with sleep time between each chunk.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [MuddyViper](https://attack.mitre.org/software/S9032) has used PowerShell.exe to launch a reverse shell.[^1]   |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [MuddyViper](https://attack.mitre.org/software/S9032) has launched a reverse shell using a provided command line.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [MuddyViper](https://attack.mitre.org/software/S9032) has used cmd.exe to launch a reverse shell.[^1]   |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [MuddyViper](https://attack.mitre.org/software/S9032) has the ability to establish persistence by configuring its installation directory as a Windows Startup folder by setting the following Registry values to `%APPDATALOCAL%\Microsoft\Windows\PPBCompatCache\ManagerCache`:  `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders\Startup` and `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders\Startup`.[^1]       |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MuddyWater\|G0069]] | MuddyWater |



## References

[^1]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)


