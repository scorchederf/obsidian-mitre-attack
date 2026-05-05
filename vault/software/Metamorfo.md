---
aliases: 
    - S0455
    
mitre-attack: https://attack.mitre.org/software/S0455
---

## S0455

[Metamorfo](https://attack.mitre.org/software/S0455) is a Latin-American banking trojan operated by a Brazilian cybercrime group that has been active since at least April 2018. The group focuses on targeting banks and cryptocurrency services in Brazil and Mexico.[^6] [^1]  

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[JavaScript\|T1059.007]] | JavaScript | [Metamorfo](https://attack.mitre.org/software/S0455) includes payloads written in JavaScript.[^6]   |
| [[Software Discovery\|T1518]] | Software Discovery | [Metamorfo](https://attack.mitre.org/software/S0455) has searched the compromised system for banking applications.[^3] [^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Metamorfo](https://attack.mitre.org/software/S0455) has a command to launch a keylogger and capture keystrokes on the victim’s machine.[^4] [^1]   |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Metamorfo](https://attack.mitre.org/software/S0455) collects a list of installed antivirus software from the victim’s system.[^4] [^1]   |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Metamorfo](https://attack.mitre.org/software/S0455)'s C2 communication has been encrypted using OpenSSL.[^6]   |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Metamorfo](https://attack.mitre.org/software/S0455) has used HTTP for C2.[^6] [^1]   |
| [[Msiexec\|T1218.007]] | Msiexec | [Metamorfo](https://attack.mitre.org/software/S0455) has used MsiExec.exe to automatically execute files.[^4] [^1]   |
| [[Malicious File\|T1204.002]] | Malicious File | [Metamorfo](https://attack.mitre.org/software/S0455) requires the user to double-click the executable to run the malicious HTA file or to download a malicious installer.[^3] [^1]   |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Metamorfo](https://attack.mitre.org/software/S0455) has injected a malicious DLL into the Windows Media Player process (wmplayer.exe).[^6]  |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | [Metamorfo](https://attack.mitre.org/software/S0455) has used YouTube to store and hide C&C server domains.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Metamorfo](https://attack.mitre.org/software/S0455) has encrypted payloads and strings.[^6] [^1]  |
| [[Native API\|T1106]] | Native API | [Metamorfo](https://attack.mitre.org/software/S0455) has used native WINAPI calls.[^6] [^4]  |
| [[DLL\|T1574.001]] | DLL | [Metamorfo](https://attack.mitre.org/software/S0455) has side-loaded its malicious DLL file.[^6] [^3] [^1]   |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Metamorfo](https://attack.mitre.org/software/S0455) has been delivered to victims via emails with malicious HTML attachments.[^3] [^1]   |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Metamorfo](https://attack.mitre.org/software/S0455) uses JavaScript to get the system time.[^6]   |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Metamorfo](https://attack.mitre.org/software/S0455) has used raw TCP for C2.[^3]   |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Metamorfo](https://attack.mitre.org/software/S0455) has configured persistence to the Registry key `HKCU\Software\Microsoft\Windows\CurrentVersion\Run, Spotify =% APPDATA%\Spotify\Spotify.exe` and used .LNK files in the startup folder to achieve persistence.[^6] [^3] [^4] [^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Metamorfo](https://attack.mitre.org/software/S0455) can send the data it collects to the C2 server.[^1]   |
| [[Indicator Removal\|T1070]] | Indicator Removal | [Metamorfo](https://attack.mitre.org/software/S0455) has a command to delete a Registry key it uses, `\Software\Microsoft\Internet Explorer\notes`.[^3]  |
| [[GUI Input Capture\|T1056.002]] | GUI Input Capture | [Metamorfo](https://attack.mitre.org/software/S0455) has displayed fake forms on top of banking sites to intercept credentials from victims.[^3]   |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [Metamorfo](https://attack.mitre.org/software/S0455) has embedded a "vmdetect.exe" executable to identify virtual machines at the beginning of execution.[^6]   |
| [[File Deletion\|T1070.004]] | File Deletion | [Metamorfo](https://attack.mitre.org/software/S0455) has deleted itself from the system after execution.[^6] [^4]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Metamorfo](https://attack.mitre.org/software/S0455) has written process names to the Registry, disabled IE browser features, deleted Registry keys, and changed the ExtendedUIHoverTime key.[^6] [^4] [^3] [^1]  |
| [[One-Way Communication\|T1102.003]] | One-Way Communication | [Metamorfo](https://attack.mitre.org/software/S0455) has downloaded a zip file for execution on the system.[^6] [^3] [^4]   |
| [[Automated Collection\|T1119]] | Automated Collection | [Metamorfo](https://attack.mitre.org/software/S0455) has automatically collected mouse clicks, continuous screenshots on the machine, and set timers to collect the contents of the clipboard and website browsing.[^3]   |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [Metamorfo](https://attack.mitre.org/software/S0455) has communicated with hosts over raw TCP on port 9999.[^3]   |
| [[Mshta\|T1218.005]] | Mshta | [Metamorfo](https://attack.mitre.org/software/S0455) has used mshta.exe to execute a HTA payload.[^3]   |
| [[Clipboard Data\|T1115]] | Clipboard Data | [Metamorfo](https://attack.mitre.org/software/S0455) has a function to hijack data from the clipboard by monitoring the contents of the clipboard and replacing the cryptocurrency wallet with the attacker's.[^4] [^1]  |
| [[Shared Modules\|T1129]] | Shared Modules | [Metamorfo](https://attack.mitre.org/software/S0455) had used AutoIt to load and execute the DLL payload.[^4]   |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Metamorfo](https://attack.mitre.org/software/S0455) has collected the hostname and operating system version from the compromised host.[^3] [^4] [^1]  |
| [[Transmitted Data Manipulation\|T1565.002]] | Transmitted Data Manipulation | [Metamorfo](https://attack.mitre.org/software/S0455) has a function that can watch the contents of the system clipboard for valid bitcoin addresses, which it then overwrites with the attacker's address.[^4] [^1]   |
| [[Screen Capture\|T1113]] | Screen Capture | [Metamorfo](https://attack.mitre.org/software/S0455) can collect screenshots of the victim’s machine.[^3] [^1]   |
| [[Code Signing\|T1553.002]] | Code Signing | [Metamorfo](https://attack.mitre.org/software/S0455) has digitally signed executables using AVAST Software certificates.[^6]   |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Metamorfo](https://attack.mitre.org/software/S0455) has used `cmd.exe /c` to execute files.[^6]   |
| [[Software Packing\|T1027.002]] | Software Packing | [Metamorfo](https://attack.mitre.org/software/S0455) has used VMProtect to pack and protect files.[^4]   |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Metamorfo](https://attack.mitre.org/software/S0455) has a function to kill processes associated with defenses and can prevent certain processes from launching.[^6] [^3]   |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [Metamorfo](https://attack.mitre.org/software/S0455) can enumerate all windows on the victim’s machine.[^3] [^4]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Metamorfo](https://attack.mitre.org/software/S0455) has collected the username from the victim's machine.[^1]   |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Metamorfo](https://attack.mitre.org/software/S0455) has disguised an MSI file as the Adobe Acrobat Reader Installer and has masqueraded payloads as OneDrive, WhatsApp, or Spotify, for example.[^6] [^1]   |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Metamorfo](https://attack.mitre.org/software/S0455) has used MSI files to download additional files to execute.[^6] [^3] [^4] [^1]   |
| [[Process Discovery\|T1057]] | Process Discovery | [Metamorfo](https://attack.mitre.org/software/S0455) has performed process name checks and has monitored applications.[^6]   |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Metamorfo](https://attack.mitre.org/software/S0455) has encrypted C2 commands with AES-256.[^1]   |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Metamorfo](https://attack.mitre.org/software/S0455) has used VBS code on victims’ systems.[^3]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [Metamorfo](https://attack.mitre.org/software/S0455) has hidden its GUI using the ShowWindow() WINAPI call.[^6]   |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | Upon execution, [Metamorfo](https://attack.mitre.org/software/S0455) has unzipped itself after being downloaded to the system and has performed string decryption.[^6] [^3] [^1]   |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Metamorfo](https://attack.mitre.org/software/S0455) has searched the Program Files directories for specific folders and has searched for strings related to its mutexes.[^6] [^4] [^3]   |




## References

[^1]: [ESET Casbaneiro Oct 2019](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)


[^2]: Casbaneiro


[^3]: [FireEye Metamorfo Apr 2018](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)


[^4]: [Fortinet Metamorfo Feb 2020](https://www.fortinet.com/blog/threat-research/another-metamorfo-variant-targeting-customers-of-financial-institutions)


[^5]: Metamorfo


[^6]: [Medium Metamorfo Apr 2020](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)


