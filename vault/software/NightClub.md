---
aliases: 
    - S1090
    
mitre-attack: https://attack.mitre.org/software/S1090
---

## S1090

[NightClub](https://attack.mitre.org/software/S1090) is a modular implant written in C++ that has been used by [MoustachedBouncer](https://attack.mitre.org/groups/G1019) since at least 2014.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Service\|T1543.003]] | Windows Service | [NightClub](https://attack.mitre.org/software/S1090) has created a Windows service named `WmdmPmSp` to establish persistence.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [NightClub](https://attack.mitre.org/software/S1090) can use SMTP and DNS for file exfiltration and C2.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [NightClub](https://attack.mitre.org/software/S1090) has chosen file names to appear legitimate including EsetUpdate-0117583943.exe for its dropper.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [NightClub](https://attack.mitre.org/software/S1090) can use a file monitor to steal specific files from targeted systems.[^1]  |
| [[Native API\|T1106]] | Native API | [NightClub](https://attack.mitre.org/software/S1090) can use multiple native APIs including `GetKeyState`, `GetForegroundWindow`, `GetWindowThreadProcessId`, and `GetKeyboardLayout`.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [NightClub](https://attack.mitre.org/software/S1090) can use a file monitor to identify .lnk, .doc, .docx, .xls, .xslx, and .pdf files.[^1]  |
| [[DNS\|T1071.004]] | DNS | [NightClub](https://attack.mitre.org/software/S1090) can use a DNS tunneling plugin to exfiltrate data by adding it to the subdomain portion of a DNS request.[^1]  |
| [[Timestomp\|T1070.006]] | Timestomp | [NightClub](https://attack.mitre.org/software/S1090) can modify the Creation, Access, and Write timestamps for malicious DLLs to match those of the genuine Windows DLL user32.dll.[^1]  |
| [[Non-Standard Encoding\|T1132.002]] | Non-Standard Encoding | [NightClub](https://attack.mitre.org/software/S1090) has used a non-standard encoding in DNS tunneling removing any `=` from the result of base64 encoding, and replacing `/` characters with `-s` and `+` characters with `-p`.[^1]  |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [NightClub](https://attack.mitre.org/software/S1090) can use emails for C2 communications.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [NightClub](https://attack.mitre.org/software/S1090) has created a service named `WmdmPmSp` to spoof a Windows Media service.[^1]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [NightClub](https://attack.mitre.org/software/S1090) can use `GetForegroundWindow` to enumerate the active window.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [NightClub](https://attack.mitre.org/software/S1090) can use a plugin for keylogging.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [NightClub](https://attack.mitre.org/software/S1090) can load a module to call `CreateCompatibleDC` and `GdipSaveImageToStream` for screen capture.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [NightClub](https://attack.mitre.org/software/S1090) can load multiple additional plugins on an infected host.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [NightClub](https://attack.mitre.org/software/S1090) can obfuscate strings using the congruential generator `(LCG): staten+1 = (690069 × staten + 1) mod 232`.[^1] <br> |
| [[Process Discovery\|T1057]] | Process Discovery | [NightClub](https://attack.mitre.org/software/S1090) has the ability to use `GetWindowThreadProcessId` to identify the process behind a specified window.[^1]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [NightClub](https://attack.mitre.org/software/S1090) has the ability to monitor removable drives.[^1]  |
| [[Audio Capture\|T1123]] | Audio Capture | [NightClub](https://attack.mitre.org/software/S1090) can load a module to leverage the LAME encoder and `mciSendStringW` to control and capture audio.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [NightClub](https://attack.mitre.org/software/S1090) has copied captured files and keystrokes to the `%TEMP%` directory of compromised hosts.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [NightClub](https://attack.mitre.org/software/S1090) can modify the Registry to set the ServiceDLL for a service created by the malware for persistence.[^1] <br> |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MoustachedBouncer\|G1019]] | MoustachedBouncer |



## References

[^1]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)


