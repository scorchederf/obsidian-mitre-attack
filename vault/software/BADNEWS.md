---
aliases: 
    - S0128
    
mitre-attack: https://attack.mitre.org/software/S0128
---

## S0128

[BADNEWS](https://attack.mitre.org/software/S0128) is malware that has been used by the actors responsible for the [Patchwork](https://attack.mitre.org/groups/G0040) campaign. Its name was given due to its use of RSS feeds, forums, and blogs for command and control. [^3]  [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | [BADNEWS](https://attack.mitre.org/software/S0128) collects C2 information via a dead drop resolver.[^3] [^1] [^4]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [BADNEWS](https://attack.mitre.org/software/S0128) establishes a backdoor over HTTP.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [BADNEWS](https://attack.mitre.org/software/S0128) has a command to take a screenshot and send it to the C2 server.[^3] [^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | When it first starts, [BADNEWS](https://attack.mitre.org/software/S0128) crawls the victim's local drives and collects documents with the following extensions: .doc, .docx, .pdf, .ppt, .pptx, and .txt.[^3] [^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [BADNEWS](https://attack.mitre.org/software/S0128) encrypts C2 data with a ROR by 3 and an XOR by 0x23.[^3] [^4]  |
| [[DLL\|T1574.001]] | DLL | [BADNEWS](https://attack.mitre.org/software/S0128) typically loads its DLL file into a legitimate signed Java or VMware executable.[^3] [^1]  |
| [[Data Encoding\|T1132]] | Data Encoding | After encrypting C2 data, [BADNEWS](https://attack.mitre.org/software/S0128) converts it into a hexadecimal representation and then encodes it into base64.[^3]  |
| [[Keylogging\|T1056.001]] | Keylogging | When it first starts, [BADNEWS](https://attack.mitre.org/software/S0128) spawns a new thread to log keystrokes.[^3] [^1] [^4]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [BADNEWS](https://attack.mitre.org/software/S0128) can use multiple C2 channels, including RSS feeds, Github, forums, and blogs.[^3] [^1] [^4]  |
| [[Invalid Code Signature\|T1036.001]] | Invalid Code Signature | [BADNEWS](https://attack.mitre.org/software/S0128) is sometimes signed with an invalid Authenticode certificate in an apparent effort to make it look more legitimate.[^4]  |
| [[Automated Collection\|T1119]] | Automated Collection | [BADNEWS](https://attack.mitre.org/software/S0128) monitors USB devices and copies files with certain extensions to a predefined directory.[^4]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [BADNEWS](https://attack.mitre.org/software/S0128) creates a scheduled task to establish by executing a malicious payload every subsequent minute.[^1]  |
| [[Data from Network Shared Drive\|T1039]] | Data from Network Shared Drive | When it first starts, [BADNEWS](https://attack.mitre.org/software/S0128) crawls the victim's mapped drives and collects documents with the following extensions: .doc, .docx, .pdf, .ppt, .pptx, and .txt.[^3]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [BADNEWS](https://attack.mitre.org/software/S0128) encodes C2 traffic with base64.[^3] [^1] [^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [BADNEWS](https://attack.mitre.org/software/S0128) installs a registry Run key to establish persistence.[^3]  |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | [BADNEWS](https://attack.mitre.org/software/S0128) copies files with certain extensions from USB devices to<br>a predefined directory.[^4]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [BADNEWS](https://attack.mitre.org/software/S0128) is capable of executing commands via cmd.exe.[^3] [^4]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [BADNEWS](https://attack.mitre.org/software/S0128) has a command to download an .exe and use process hollowing to inject it into a new process.[^3] [^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BADNEWS](https://attack.mitre.org/software/S0128) is capable of downloading additional files through C2 channels, including a new version of itself.[^3] [^1] [^4]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [BADNEWS](https://attack.mitre.org/software/S0128) attempts to hide its payloads using legitimate filenames.[^1]  |
| [[Native API\|T1106]] | Native API | [BADNEWS](https://attack.mitre.org/software/S0128) has a command to download an .exe and execute it via CreateProcess API. It can also run with ShellExecute.[^3] [^4]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [BADNEWS](https://attack.mitre.org/software/S0128) copies documents under 15MB found on the victim system to is the user's `%temp%\SMB\` folder. It also copies files from USB devices to a predefined directory.[^3] [^4]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [BADNEWS](https://attack.mitre.org/software/S0128) identifies files with certain extensions from USB devices, then copies them to a predefined directory.[^4]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [BADNEWS](https://attack.mitre.org/software/S0128) checks for new hard drives on the victim, such as USB devices, by listening for the WM_DEVICECHANGE window message.[^3] [^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Patchwork\|G0040]] | Patchwork |



## References

[^1]: [PaloAlto Patchwork Mar 2018](https://researchcenter.paloaltonetworks.com/2018/03/unit42-patchwork-continues-deliver-badnews-indian-subcontinent/)


[^2]: BADNEWS


[^3]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)


[^4]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)


