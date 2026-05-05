---
aliases: 
    - S0670
    
mitre-attack: https://attack.mitre.org/software/S0670
---

## S0670

[WarzoneRAT](https://attack.mitre.org/software/S0670) is a malware-as-a-service remote access tool (RAT) written in C++ that has been publicly available for purchase since at least late 2018.[^3] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [WarzoneRAT](https://attack.mitre.org/software/S0670) can obtain a list of processes on a compromised host.[^3]  |
| [[Keylogging\|T1056.001]] | Keylogging | [WarzoneRAT](https://attack.mitre.org/software/S0670) has the capability to install a live and offline keylogger, including through the use of the `GetAsyncKeyState` Windows API.[^3] [^2]   |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [WarzoneRAT](https://attack.mitre.org/software/S0670) can add itself to the `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` and `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UIF2IS20VK` Registry keys.[^3]  |
| [[Malicious File\|T1204.002]] | Malicious File | [WarzoneRAT](https://attack.mitre.org/software/S0670) has relied on a victim to open a malicious attachment within an email for execution.[^3] [^5]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [WarzoneRAT](https://attack.mitre.org/software/S0670) can disarm Windows Defender during the UAC process to evade detection.[^3]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [WarzoneRAT](https://attack.mitre.org/software/S0670) can send collected victim data to its C2 server.[^3]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [WarzoneRAT](https://attack.mitre.org/software/S0670) has the capability to grab passwords from numerous web browsers as well as from Outlook and Thunderbird email clients.[^3] [^2]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [WarzoneRAT](https://attack.mitre.org/software/S0670) can use `sdclt.exe` to bypass UAC in Windows 10 to escalate privileges; for older Windows versions [WarzoneRAT](https://attack.mitre.org/software/S0670) can use the IFileOperation exploit to bypass the UAC module.[^3] [^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [WarzoneRAT](https://attack.mitre.org/software/S0670) can collect data from a compromised host.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [WarzoneRAT](https://attack.mitre.org/software/S0670) can download and execute additional files.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [WarzoneRAT](https://attack.mitre.org/software/S0670) can collect compromised host information, including OS version, PC name, RAM size, and CPU details.[^3]  |
| [[Proxy\|T1090]] | Proxy | [WarzoneRAT](https://attack.mitre.org/software/S0670) has the capability to act as a reverse proxy.[^3]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [WarzoneRAT](https://attack.mitre.org/software/S0670) can encrypt its C2 with RC4 with the password `warzone160\x00`.[^3]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [WarzoneRAT](https://attack.mitre.org/software/S0670) has the ability to control an infected PC using RDP.[^3]  |
| [[Modify Registry\|T1112]] | Modify Registry | [WarzoneRAT](https://attack.mitre.org/software/S0670) can create `HKCU\Software\Classes\Folder\shell\open\command` as a new registry key during privilege escalation.[^2] [^3]   |
| [[Component Object Model Hijacking\|T1546.015]] | Component Object Model Hijacking | [WarzoneRAT](https://attack.mitre.org/software/S0670)  can perform COM hijacking by setting the path to itself to the `HKCU\Software\Classes\Folder\shell\open\command` key with a `DelegateExecute` parameter.[^3]  |
| [[Hide Artifacts\|T1564]] | Hide Artifacts | [WarzoneRAT](https://attack.mitre.org/software/S0670) can masquerade the Process Environment Block on a compromised host to hide its attempts to elevate privileges through `IFileOperation`.[^3]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [WarzoneRAT](https://attack.mitre.org/software/S0670) has been distributed as a malicious attachment within an email.[^3] [^5]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [WarzoneRAT](https://attack.mitre.org/software/S0670) can use XOR 0x45 to decrypt obfuscated code.[^3]  |
| [[PowerShell\|T1059.001]] | PowerShell | [WarzoneRAT](https://attack.mitre.org/software/S0670) can use PowerShell to download files and execute commands.[^3] [^2]  |
| [[Native API\|T1106]] | Native API | [WarzoneRAT](https://attack.mitre.org/software/S0670) can use a variety of API calls on a compromised host.[^2]  |
| [[Video Capture\|T1125]] | Video Capture | [WarzoneRAT](https://attack.mitre.org/software/S0670) can access the webcam on a victim's machine.[^3] [^2]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | WarzoneRAT has the ability of performing remote desktop access via a hVNC window for decreased visibility.[^4]  |
| [[Process Injection\|T1055]] | Process Injection | [WarzoneRAT](https://attack.mitre.org/software/S0670) has the ability to inject malicious DLLs into a specific process for privilege escalation.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [WarzoneRAT](https://attack.mitre.org/software/S0670) can use `cmd.exe` to execute malicious code.[^3]  |
| [[VNC\|T1021.005]] | VNC | [WarzoneRAT](https://attack.mitre.org/software/S0670) has the ability of performing remote desktop access via a VNC console.[^3]  |
| [[Template Injection\|T1221]] | Template Injection | [WarzoneRAT](https://attack.mitre.org/software/S0670) has been install via template injection through a malicious DLL embedded within a template RTF in a Word document.[^5]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [WarzoneRAT](https://attack.mitre.org/software/S0670) can communicate with its C2 server via TCP over port 5200.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [WarzoneRAT](https://attack.mitre.org/software/S0670) can enumerate directories on a compromise host.[^3]  |
| [[Rootkit\|T1014]] | Rootkit | [WarzoneRAT](https://attack.mitre.org/software/S0670) can include a rootkit to hide processes, files, and startup.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA2541\|G1018]] | TA2541 |
| [[Scattered Spider\|G1015]] | Scattered Spider |
| [[Confucius\|G0142]] | Confucius |



## References

[^1]: Ave Maria


[^2]: [Uptycs Warzone UAC Bypass November 2020](https://www.uptycs.com/blog/warzone-rat-comes-with-uac-bypass-technique)


[^3]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)


[^4]: [Bitdefender Trickbot VNC module Whitepaper 2021](https://www.bitdefender.com/files/News/CaseStudies/study/399/Bitdefender-PR-Whitepaper-Trickbot-creat5515-en-EN.pdf)


[^5]: [Uptycs Confucius APT Jan 2021](https://www.uptycs.com/blog/confucius-apt-deploys-warzone-rat)


[^6]: [Check Point Scattered Spider JUL 2025](https://blog.checkpoint.com/research/exposing-scattered-spider-new-indicators-highlight-growing-threat-to-enterprises-and-aviation/)


[^7]: [CISA Scattered Spider Advisory November 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)


[^8]: [Proofpoint TA2541 February 2022](https://www.proofpoint.com/us/blog/threat-insight/charting-ta2541s-flight)


