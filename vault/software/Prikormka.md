---
aliases: 
    - S0113
    
mitre-attack: https://attack.mitre.org/software/S0113
---

## S0113

[Prikormka](https://attack.mitre.org/software/S0113) is a malware family used in a campaign known as Operation Groundbait. It has predominantly been observed in Ukraine and was used as early as 2008. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Prikormka](https://attack.mitre.org/software/S0113) encrypts some C2 traffic with the Blowfish cipher.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Prikormka](https://attack.mitre.org/software/S0113) contains a keylogger module that collects keystrokes and the titles of foreground windows.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Prikormka](https://attack.mitre.org/software/S0113) uses rundll32.exe to load its DLL.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | Some resources in [Prikormka](https://attack.mitre.org/software/S0113) are encrypted with a simple XOR operation or encoded with Base64.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Prikormka](https://attack.mitre.org/software/S0113) contains a module that captures screenshots of the victim's desktop.[^1]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | A module in [Prikormka](https://attack.mitre.org/software/S0113) collects information on available printers and disk drives.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | A module in [Prikormka](https://attack.mitre.org/software/S0113) collects information from the victim about its IP addresses and MAC addresses.[^1]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | A module in [Prikormka](https://attack.mitre.org/software/S0113) gathers logins and passwords stored in applications on the victims, including Google Chrome, Mozilla Firefox, and several other browsers.[^1]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | A module in [Prikormka](https://attack.mitre.org/software/S0113) collects passwords stored in applications installed on the victim.[^1]  |
| [[DLL\|T1574.001]] | DLL | [Prikormka](https://attack.mitre.org/software/S0113) uses DLL search order hijacking for persistence by saving itself as ntshrui.dll to the Windows directory so it will load before the legitimate ntshrui.dll saved in the System32 subdirectory.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | A module in [Prikormka](https://attack.mitre.org/software/S0113) collects information from the victim about Windows OS version, computer name, battery info, and physical memory.[^1]  |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | [Prikormka](https://attack.mitre.org/software/S0113) contains a module that collects documents with certain extensions from removable media or fixed drives connected via USB.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | A module in [Prikormka](https://attack.mitre.org/software/S0113) collects information from the victim about installed anti-virus software.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Prikormka](https://attack.mitre.org/software/S0113) encodes C2 traffic with Base64.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | After encrypting its own log files, the log encryption module in [Prikormka](https://attack.mitre.org/software/S0113) deletes the original, unencrypted files from the host.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Prikormka](https://attack.mitre.org/software/S0113) adds itself to a Registry Run key with the name guidVGA or guidVSA.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Prikormka](https://attack.mitre.org/software/S0113) creates a directory, `%USERPROFILE%\AppData\Local\SKC\`, which is used to store collected log files.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | A module in [Prikormka](https://attack.mitre.org/software/S0113) collects information about the paths, size, and creation time of files with specific file extensions, but not the actual content of the file.[^1]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | After collecting documents from removable media, [Prikormka](https://attack.mitre.org/software/S0113) compresses the collected files, and encrypts it with Blowfish.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | A module in [Prikormka](https://attack.mitre.org/software/S0113) collects information from the victim about the current user name.[^1]  |




## References

[^1]: [ESET Operation Groundbait](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)


