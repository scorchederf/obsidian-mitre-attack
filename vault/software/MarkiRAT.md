---
aliases: 
    - S0652
    
mitre-attack: https://attack.mitre.org/software/S0652
---

## S0652

[MarkiRAT](https://attack.mitre.org/software/S0652) is a remote access Trojan (RAT) compiled with Visual Studio that has been used by [Ferocious Kitten](https://attack.mitre.org/groups/G0137) since at least 2015.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[BITS Jobs\|T1197]] | BITS Jobs | [MarkiRAT](https://attack.mitre.org/software/S0652) can use BITS Utility to connect with the C2 server.[^1]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [MarkiRAT](https://attack.mitre.org/software/S0652) can use the `GetKeyboardLayout` API to check if a compromised host's keyboard is set to Persian.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [MarkiRAT](https://attack.mitre.org/software/S0652) can retrieve the victim’s username.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [MarkiRAT](https://attack.mitre.org/software/S0652) can look for files carrying specific extensions such as: .rtf, .doc, .docx, .xls, .xlsx, .ppt, .pptx, .pps, .ppsx, .txt, .gpg, .pkr, .kdbx, .key, and .jpb.[^1]  |
| [[Native API\|T1106]] | Native API | [MarkiRAT](https://attack.mitre.org/software/S0652) can run the ShellExecuteW API via the Windows Command Shell.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [MarkiRAT](https://attack.mitre.org/software/S0652) can download additional files and tools from its C2 server, including through the use of [BITSAdmin](https://attack.mitre.org/software/S0190).[^1]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [MarkiRAT](https://attack.mitre.org/software/S0652) can modify the shortcut that launches Telegram by replacing its path with the malicious payload to launch with the legitimate executable.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [MarkiRAT](https://attack.mitre.org/software/S0652) can upload data from the victim's machine to the C2 server.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [MarkiRAT](https://attack.mitre.org/software/S0652) can capture all keystrokes on a compromised host.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [MarkiRAT](https://attack.mitre.org/software/S0652) can drop its payload into the Startup directory to ensure it automatically runs when the compromised system is started.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [MarkiRAT](https://attack.mitre.org/software/S0652) can utilize cmd.exe to execute commands in a victim's environment.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [MarkiRAT](https://attack.mitre.org/software/S0652) can check for running processes on the victim’s machine to look for Kaspersky and Bitdefender antivirus products.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [MarkiRAT](https://attack.mitre.org/software/S0652) can obtain the computer name from a compromised host.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [MarkiRAT](https://attack.mitre.org/software/S0652) can exfiltrate locally stored data via its C2.[^1]  |
| [[Password Managers\|T1555.005]] | Password Managers | [MarkiRAT](https://attack.mitre.org/software/S0652) can gather information from the Keepass password manager.[^1]   |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [MarkiRAT](https://attack.mitre.org/software/S0652) can masquerade as `update.exe` and `svehost.exe`; it has also mimicked legitimate Telegram and Chrome files.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [MarkiRAT](https://attack.mitre.org/software/S0652) can search for different processes on a system.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [MarkiRAT](https://attack.mitre.org/software/S0652) can store collected data locally in a created .nfo file.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [MarkiRAT](https://attack.mitre.org/software/S0652) can initiate communication over HTTP/HTTPS for its C2 server.[^1]  |
| [[Software Discovery\|T1518]] | Software Discovery | [MarkiRAT](https://attack.mitre.org/software/S0652) can check for the Telegram installation directory by enumerating the files on disk.[^1]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [MarkiRAT](https://attack.mitre.org/software/S0652) can capture clipboard content.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [MarkiRAT](https://attack.mitre.org/software/S0652) can capture screenshots that are initially saved as ‘scr.jpg’.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Ferocious Kitten\|G0137]] | Ferocious Kitten |



## References

[^1]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)


