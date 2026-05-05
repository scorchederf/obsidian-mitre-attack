---
aliases: 
    - S1122
    
mitre-attack: https://attack.mitre.org/software/S1122
---

## S1122

[Mispadu](https://attack.mitre.org/software/S1122) is a banking trojan written in Delphi that was first observed in 2019 and uses a Malware-as-a-Service (MaaS) business model.[^4] [^3]  This malware is operated, managed, and sold by the [Malteiro](https://attack.mitre.org/groups/G1026) cybercriminal group.[^3]  [Mispadu](https://attack.mitre.org/software/S1122) has mainly been used to target victims in Brazil and Mexico, and has also had confirmed operations throughout Latin America and Europe.[^3] [^1] [^2]  

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Mispadu](https://attack.mitre.org/software/S1122) decrypts its encrypted configuration files prior to execution.[^3] [^4]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Mispadu](https://attack.mitre.org/software/S1122) can steal credentials from Google Chrome.[^3] [^4] [^6]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Mispadu](https://attack.mitre.org/software/S1122) has the ability to capture screenshots on compromised hosts.[^3] [^1] [^4] [^6]   |
| [[Msiexec\|T1218.007]] | Msiexec | [Mispadu](https://attack.mitre.org/software/S1122) has been installed via MSI installer.[^3] [^4]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [Mispadu](https://attack.mitre.org/software/S1122) checks and will terminate execution if the compromised system’s language ID is not Spanish or Portuguese.[^2] [^3]  |
| [[Browser Extensions\|T1176.001]] | Browser Extensions | [Mispadu](https://attack.mitre.org/software/S1122) utilizes malicious Google Chrome browser extensions to steal financial data.[^4]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [Mispadu](https://attack.mitre.org/software/S1122) can monitor browser activity for online banking actions and display full-screen overlay images to block user access to the intended site or present additional data fields.[^2] [^3]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Mispadu](https://attack.mitre.org/software/S1122) has been spread via malicious links embedded in emails.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Mispadu](https://attack.mitre.org/software/S1122) collects the OS version, computer name, and language ID.[^4]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Mispadu](https://attack.mitre.org/software/S1122) has relied on users to execute malicious files in order to gain execution on victim machines.[^4] [^6] [^3]  |
| [[Native API\|T1106]] | Native API | [Mispadu](https://attack.mitre.org/software/S1122) has used a variety of Windows API calls, including ShellExecute and WriteProcessMemory.[^2] [^3]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Mispadu](https://attack.mitre.org/software/S1122) uses RunDLL32 for execution via its injector DLL.[^4]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Mispadu](https://attack.mitre.org/software/S1122) can log keystrokes on the victim's machine.[^4] [^6] [^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Mispadu](https://attack.mitre.org/software/S1122) creates a link in the startup folder for persistence.[^4]  [Mispadu](https://attack.mitre.org/software/S1122) adds persistence via the registry key `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`.[^6]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Mispadu](https://attack.mitre.org/software/S1122) uses a custom algorithm to obfuscate its internal strings and uses hardcoded keys.[^4] <br><br>[Mispadu](https://attack.mitre.org/software/S1122) also uses encoded configuration files and has encoded payloads using Base64.[^4] [^3] [^5]  |
| [[Process Injection\|T1055]] | Process Injection | [Mispadu](https://attack.mitre.org/software/S1122)'s binary is injected into memory via `WriteProcessMemory`.[^2] [^3]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Mispadu](https://attack.mitre.org/software/S1122) can list installed security products in the victim’s environment.[^4] [^6]  |
| [[GUI Input Capture\|T1056.002]] | GUI Input Capture | [Mispadu](https://attack.mitre.org/software/S1122) can monitor browser activity for online banking actions and display full-screen overlay images to block user access to the intended site or present additional data fields.[^2] [^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Mispadu](https://attack.mitre.org/software/S1122) can enumerate the running processes on a compromised host.[^4]  |
| [[System Checks\|T1497.001]] | System Checks | [Mispadu](https://attack.mitre.org/software/S1122) can run checks to verify if it is running within a virtualized environments including Hyper-V, VirtualBox or VMWare and will terminate execution if the computer name is “JOHN-PC.”[^4] [^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Mispadu](https://attack.mitre.org/software/S1122) searches for various filesystem paths to determine what banking applications are installed on the victim’s machine.[^4]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Mispadu](https://attack.mitre.org/software/S1122) can sends the collected financial data to the C2 server.[^4] [^3]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Mispadu](https://attack.mitre.org/software/S1122) contains a copy of the OpenSSL library to encrypt C2 traffic.[^2]   |
| [[Clipboard Data\|T1115]] | Clipboard Data | [Mispadu](https://attack.mitre.org/software/S1122) has the ability to capture and replace Bitcoin wallet data in the clipboard on a compromised host.[^4]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [Mispadu](https://attack.mitre.org/software/S1122) has obtained credentials from mail clients via NirSoft MailPassView.[^3] [^2] [^4]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Mispadu](https://attack.mitre.org/software/S1122)’s dropper uses VBS files to install payloads and perform execution.[^3] [^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Malteiro\|G1026]] | Malteiro |



## References

[^1]: [SCILabs URSA/Mispadu Evolution 2023](https://blog.scilabs.mx/en/evolution-of-banking-trojan-ursa-mispadu/)


[^2]: [Segurança Informática URSA Sophisticated Loader 2020](https://seguranca-informatica.pt/threat-analysis-the-emergent-ursa-trojan-impacts-many-countries-using-a-sophisticated-loader/)


[^3]: [SCILabs Malteiro 2021](https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/)


[^4]: [ESET Security Mispadu Facebook Ads 2019](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/)


[^5]: [SCILabs Malteiro Threat Overlap 2023](https://blog.scilabs.mx/en/ursa-mispadu-overlap-analysis-with-other-threats/)


[^6]: [Metabase Q Mispadu Trojan 2023](https://www.metabaseq.com/mispadu-banking-trojan/)


