---
aliases: 
    - S1213
    
mitre-attack: https://attack.mitre.org/software/S1213
---

## S1213

[Lumma Stealer](https://attack.mitre.org/software/S1213) is an information stealer malware family in use since at least 2022. [Lumma Stealer](https://attack.mitre.org/software/S1213) is a Malware as a Service (MaaS) where captured data has been sold in criminal markets to Initial Access Brokers.[^4] [^1] [^2] [^6] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [Lumma Stealer](https://attack.mitre.org/software/S1213) has checked for debugger strings by invoking `GetForegroundWindow` and looks for strings containing “x32dbg”, “x64dbg”, “windbg”, “ollydbg”, “dnspy”, “immunity debugger”, “hyperdbg”, “debug”, “debugger”, “cheat engine”, “cheatengine” and “ida”.[^6]  |
| [[AutoHotKey & AutoIT\|T1059.010]] | AutoHotKey & AutoIT | [Lumma Stealer](https://attack.mitre.org/software/S1213) has utilized AutoIt malware scripts and AutoIt executables.[^2] [^4]  |
| [[Supply Chain Compromise\|T1195]] | Supply Chain Compromise | [Lumma Stealer](https://attack.mitre.org/software/S1213) has been delivered through cracked software downloads.[^4] [^6] [^3]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Lumma Stealer](https://attack.mitre.org/software/S1213) has taken screenshots of victim machines.[^4]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Lumma Stealer](https://attack.mitre.org/software/S1213) has gathered credential and other information from multiple browsers.[^4] [^6] [^3]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Lumma Stealer](https://attack.mitre.org/software/S1213) has detected antivirus processes using commands such as “tasklist” and “findstr.”[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Lumma Stealer](https://attack.mitre.org/software/S1213) has used Base64-encoded content during execution, decoded via PowerShell.[^1]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Lumma Stealer](https://attack.mitre.org/software/S1213) has used process hollowing leveraging a legitimate program such as “BitLockerToGo.exe” to inject a malicious payload.[^2]  |
| [[Electron Applications\|T1218.015]] | Electron Applications | [Lumma Stealer](https://attack.mitre.org/software/S1213) as leveraged Electron Applications to disable GPU sandboxing to avoid detection by security software.[^3]  |
| [[System Checks\|T1497.001]] | System Checks | [Lumma Stealer](https://attack.mitre.org/software/S1213) has queried system resources on the victim device to identify if it is executing in a sandbox or virtualized environments, checking usernames, conducting WMI queries for system details, checking for files commonly found in virtualized environments, searching system services, and inspecting process names.[^6]  [Lumma Stealer](https://attack.mitre.org/software/S1213) has checked system GPU configurations for sandbox detection.[^3]  |
| [[Mshta\|T1218.005]] | Mshta | [Lumma Stealer](https://attack.mitre.org/software/S1213) has used mshta.exe to execute additional content.[^2] [^1]  |
| [[DLL\|T1574.001]] | DLL | [Lumma Stealer](https://attack.mitre.org/software/S1213) has leveraged legitimate applications to then side-load malicious DLLs during execution.[^4]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Lumma Stealer](https://attack.mitre.org/software/S1213) has attempted to bypass Windows Antimalware Scan Interface (AMSI) by removing the string “AmsiScanBuffer” from the “clr.dll” module in memory to prevent it from being called.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Lumma Stealer](https://attack.mitre.org/software/S1213) has created registry keys to maintain persistence using `HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`.[^4] [^1]  |
| [[Browser Extensions\|T1176.001]] | Browser Extensions | [Lumma Stealer](https://attack.mitre.org/software/S1213) has installed a malicious browser extension to target Google Chrome, Microsoft Edge, Opera and Brave browsers for the purpose of stealing data.[^4]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Lumma Stealer](https://attack.mitre.org/software/S1213) has configured a custom user data directory such as a folder within `%USERPROFILE%\AppData\Roaming` for staging data.[^3]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Lumma Stealer](https://attack.mitre.org/software/S1213) has exfiltrated collected data over existing HTTP and HTTPS C2 channels.[^2] [^6]  |
| [[User Execution\|T1204]] | User Execution | [Lumma Stealer](https://attack.mitre.org/software/S1213) has been distributed through a fake CAPTCHA that presents instructions to the victim to open Windows Run window (“Windows Button + R”) and paste clipboard contents (“CTRL + V”) and press “Enter” to execute a Base64-encoded PowerShell.[^2] [^4] [^1]  |
| [[Masquerade File Type\|T1036.008]] | Masquerade File Type | [Lumma Stealer](https://attack.mitre.org/software/S1213) has used payloads that resemble benign file extensions such as .mp3, .accdb, and .pub, though the files contained malicious JavaScript content.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Lumma Stealer](https://attack.mitre.org/software/S1213) has used SmartAssembly to obfuscate .NET payloads.[^6]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Lumma Stealer](https://attack.mitre.org/software/S1213) has used PowerShell for initial user execution and other fuctions.[^2] [^4] [^1] [^6]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Lumma Stealer](https://attack.mitre.org/software/S1213) has automated collection of various information including cryptocurrency wallet details.[^4]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [Lumma Stealer](https://attack.mitre.org/software/S1213) has used reflective loading techniques to load content into memory during execution.[^1] [^6]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Lumma Stealer](https://attack.mitre.org/software/S1213) has gained initial execution through victims opening malicious executable files embedded in zip archives, and MSI files within RAR files.[^4]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Lumma Stealer](https://attack.mitre.org/software/S1213) has used AES-encrypted payloads contained within PowerShell scripts.[^2]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Lumma Stealer](https://attack.mitre.org/software/S1213) has used valid code signing digital certificates from ConsolHQ LTD and Verandah Green Limited to appear legitimate.[^3]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [Lumma Stealer](https://attack.mitre.org/software/S1213) has identified and gathered information from two-factor authentication extensions for multiple browsers.[^4]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [Lumma Stealer](https://attack.mitre.org/software/S1213) has harvested cookies from various browsers.[^4] [^6] [^3]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Lumma Stealer](https://attack.mitre.org/software/S1213) has used HTTPS for command and control purposes.[^6]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Lumma Stealer](https://attack.mitre.org/software/S1213) has used HTTP and HTTP for command and control communication.[^2] [^6]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Lumma Stealer](https://attack.mitre.org/software/S1213)  has been delivered through phishing emails with malicious attachments.[^4]  |
| [[Python\|T1059.006]] | Python | [Lumma Stealer](https://attack.mitre.org/software/S1213) has used malicious Python scripts to execute payloads.[^4]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [Lumma Stealer](https://attack.mitre.org/software/S1213) has utilized the .NET `ProcessStartInfo` class features to prevent the process from creating a visible window through setting the `CreateNoWindow` setting to “True,” which allows the executed command or script to run without displaying a command prompt window.[^6]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Lumma Stealer](https://attack.mitre.org/software/S1213) has been delivered through phishing emails containing malicious links.[^4]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Lumma Stealer](https://attack.mitre.org/software/S1213) has gathered various system information from victim machines.[^4] [^6] [^3]  |




## References

[^1]: [Netskope LummaStealer 2025](https://www.netskope.com/blog/lumma-stealer-fake-captchas-new-techniques-to-evade-detection)


[^2]: [Qualys LummaStealer 2024](https://blog.qualys.com/vulnerabilities-threat-research/2024/10/20/unmasking-lumma-stealer-analyzing-deceptive-tactics-with-fake-captcha)


[^3]: [TrendMicro LummaStealer 2025](https://www.trendmicro.com/en_us/research/25/a/lumma-stealers-github-based-delivery-via-mdr.html)


[^4]: [Cybereason LumaStealer Undated](https://www.cybereason.com/blog/threat-analysis-rise-of-lummastealer)


[^5]: LummaStealer


[^6]: [Fortinet LummaStealer 2024](https://www.fortinet.com/blog/threat-research/lumma-variant-on-youtube)


