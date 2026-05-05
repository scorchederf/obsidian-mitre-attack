---
aliases: 
    - S0622
    
mitre-attack: https://attack.mitre.org/software/S0622
---

## S0622

[AppleSeed](https://attack.mitre.org/software/S0622) is a backdoor that has been used by [Kimsuky](https://attack.mitre.org/groups/G0094) to target South Korean government, academic, and commercial  targets since at least 2021.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[JavaScript\|T1059.007]] | JavaScript | [AppleSeed](https://attack.mitre.org/software/S0622) has the ability to use JavaScript to execute PowerShell.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [AppleSeed](https://attack.mitre.org/software/S0622) has the ability to execute its payload via PowerShell.[^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [AppleSeed](https://attack.mitre.org/software/S0622) has used UPX packers for its payload DLL.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [AppleSeed](https://attack.mitre.org/software/S0622) can identify the IP of a targeted system.[^1]  |
| [[Masquerading\|T1036]] | Masquerading | [AppleSeed](https://attack.mitre.org/software/S0622) can disguise JavaScript files as PDFs.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [AppleSeed](https://attack.mitre.org/software/S0622) has been distributed to victims through malicious e-mail attachments.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [AppleSeed](https://attack.mitre.org/software/S0622) can decode its payload prior to execution.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [AppleSeed](https://attack.mitre.org/software/S0622) can enumerate the current process on a compromised host.[^1]  |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [AppleSeed](https://attack.mitre.org/software/S0622) can gain system level privilege by passing `SeDebugPrivilege` to the `AdjustTokenPrivilege` API.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [AppleSeed](https://attack.mitre.org/software/S0622) can use `GetKeyState` and `GetKeyboardState` to capture keystrokes on the victim’s machine.[^1] [^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [AppleSeed](https://attack.mitre.org/software/S0622) can collect data on a compromised host.[^1] [^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [AppleSeed](https://attack.mitre.org/software/S0622) has the ability to rename its payload to ESTCommon.dll to masquerade as a DLL belonging to ESTsecurity.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [AppleSeed](https://attack.mitre.org/software/S0622) can identify the OS version of a targeted system.[^1]  |
| [[Automated Collection\|T1119]] | Automated Collection | [AppleSeed](https://attack.mitre.org/software/S0622) has automatically collected data from USB drives, keystrokes, and screen images before exfiltration.[^2]  |
| [[Exfiltration Over Web Service\|T1567]] | Exfiltration Over Web Service | [AppleSeed](https://attack.mitre.org/software/S0622) has exfiltrated files using web services.[^2]  |
| [[Data Transfer Size Limits\|T1030]] | Data Transfer Size Limits | [AppleSeed](https://attack.mitre.org/software/S0622) has divided files if the size is 0x1000000 bytes or more.[^2]  |
| [[Native API\|T1106]] | Native API | [AppleSeed](https://attack.mitre.org/software/S0622) has the ability to use multiple dynamically resolved API calls.[^1]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [AppleSeed](https://attack.mitre.org/software/S0622) has compressed collected data before exfiltration.[^2]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [AppleSeed](https://attack.mitre.org/software/S0622) can use a second channel for C2 when the primary channel is in upload mode.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [AppleSeed](https://attack.mitre.org/software/S0622) can exfiltrate files via the C2 channel.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [AppleSeed](https://attack.mitre.org/software/S0622) has the ability to search for .txt, .ppt, .hwp, .pdf, and .doc files in specified directories.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [AppleSeed](https://attack.mitre.org/software/S0622) has the ability to Base64 encode its payload and custom encrypt API calls.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [AppleSeed](https://attack.mitre.org/software/S0622) has the ability to communicate with C2 over HTTP.[^1] [^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [AppleSeed](https://attack.mitre.org/software/S0622) can delete files from a compromised host after they are exfiltrated.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [AppleSeed](https://attack.mitre.org/software/S0622) can take screenshots on a compromised host by calling a series of APIs.[^1] [^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [AppleSeed](https://attack.mitre.org/software/S0622) can achieve execution through users running malicious file attachments distributed via email.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [AppleSeed](https://attack.mitre.org/software/S0622) can stage files in a central location prior to exfiltration.[^1]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [AppleSeed](https://attack.mitre.org/software/S0622) can zip and encrypt data collected on a target system.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [AppleSeed](https://attack.mitre.org/software/S0622) has the ability to create the Registry key name `EstsoftAutoUpdate` at `HKCU\Software\Microsoft/Windows\CurrentVersion\RunOnce` to establish persistence.[^1]  |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | [AppleSeed](https://attack.mitre.org/software/S0622) can find and collect data from removable media devices.[^1] [^2]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [AppleSeed](https://attack.mitre.org/software/S0622) can pull a timestamp from the victim's machine.[^1]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [AppleSeed](https://attack.mitre.org/software/S0622) can call regsvr32.exe for execution.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Kimsuky\|G0094]] | Kimsuky |



## References

[^1]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)


[^2]: [KISA Operation Muzabi](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)


