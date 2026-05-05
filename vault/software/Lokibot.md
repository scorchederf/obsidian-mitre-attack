---
aliases: 
    - S0447
    
mitre-attack: https://attack.mitre.org/software/S0447
---

## S0447

[Lokibot](https://attack.mitre.org/software/S0447) is a widely distributed information stealer that was first reported in 2015. It is designed to steal sensitive information such as usernames, passwords, cryptocurrency wallets, and other credentials. [Lokibot](https://attack.mitre.org/software/S0447) can also create a backdoor into infected systems to allow an attacker to install additional payloads.[^2] [^8] [^6] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Lokibot](https://attack.mitre.org/software/S0447) has used VBS scripts and XLS macros for execution.[^4]   |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Lokibot](https://attack.mitre.org/software/S0447) is delivered via a malicious XLS attachment contained within a spearhpishing email.[^4]   |
| [[Software Packing\|T1027.002]] | Software Packing | [Lokibot](https://attack.mitre.org/software/S0447) has used several packing methods for obfuscation.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Lokibot](https://attack.mitre.org/software/S0447) has obfuscated strings with base64 encoding.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Lokibot](https://attack.mitre.org/software/S0447) has decoded and decrypted its stages multiple times using hard-coded keys to deliver the final payload, and has decoded its server response hex string using XOR.[^4]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [Lokibot](https://attack.mitre.org/software/S0447) has stolen credentials from multiple applications and data sources including Windows OS credentials, email clients, FTP, and SFTP clients.[^2]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [Lokibot](https://attack.mitre.org/software/S0447) has reflectively loaded the decoded DLL into memory.[^4]   |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Lokibot](https://attack.mitre.org/software/S0447) has used process hollowing to inject itself into legitimate Windows process.[^2] [^4]   |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Lokibot](https://attack.mitre.org/software/S0447) has the ability to discover the username on the infected host.[^5]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Lokibot](https://attack.mitre.org/software/S0447) can search for specific files on an infected host.[^4]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Lokibot](https://attack.mitre.org/software/S0447) has the ability to capture input on the compromised host via keylogging.[^5]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Lokibot](https://attack.mitre.org/software/S0447) has used `cmd /c` commands embedded within batch scripts.[^4]   |
| [[Modify Registry\|T1112]] | Modify Registry | [Lokibot](https://attack.mitre.org/software/S0447) has modified the Registry as part of its UAC bypass process.[^4]   |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Lokibot](https://attack.mitre.org/software/S0447) embedded the commands `schtasks /Run /TN \Microsoft\Windows\DiskCleanup\SilentCleanup /I` inside a batch script.[^4]   |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [Lokibot](https://attack.mitre.org/software/S0447) has performed a time-based anti-debug check before downloading its third stage.[^4]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Lokibot](https://attack.mitre.org/software/S0447) has the ability to initiate contact with command and control (C2) to exfiltrate stolen data.[^5]  |
| [[Scheduled Task／Job\|T1053]] | Scheduled Task／Job | [Lokibot](https://attack.mitre.org/software/S0447)'s second stage DLL has set a timer using “timeSetEvent” to schedule its next execution.[^4]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | <br>[Lokibot](https://attack.mitre.org/software/S0447) has utilized multiple techniques to bypass UAC.[^4]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Lokibot](https://attack.mitre.org/software/S0447) has the ability to discover the computer name and Windows product name/version.[^5]  |
| [[Native API\|T1106]] | Native API | [Lokibot](https://attack.mitre.org/software/S0447) has used LoadLibrary(), GetProcAddress() and CreateRemoteThread() API functions to execute its shellcode.[^4]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [Lokibot](https://attack.mitre.org/software/S0447) has the ability to copy itself to a hidden file and directory.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Lokibot](https://attack.mitre.org/software/S0447) has used PowerShell commands embedded inside batch scripts.[^4]   |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Lokibot](https://attack.mitre.org/software/S0447) has the ability to discover the domain name of the infected host.[^5]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Lokibot](https://attack.mitre.org/software/S0447) will delete its dropped files after bypassing UAC.[^4]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Lokibot](https://attack.mitre.org/software/S0447) has tricked recipients into enabling malicious macros by getting victims to click "enable content" in email attachments.[^7] [^4]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Lokibot](https://attack.mitre.org/software/S0447) has used HTTP for C2 communications.[^2] [^4]   |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Lokibot](https://attack.mitre.org/software/S0447) downloaded several staged items onto the victim's machine.[^4]   |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Lokibot](https://attack.mitre.org/software/S0447) has demonstrated the ability to steal credentials from multiple applications and data sources including Safari and the Chromium and Mozilla Firefox-based web browsers.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[SilverTerrier\|G0083]] | SilverTerrier |



## References

[^1]: Lokibot


[^2]: [Infoblox Lokibot January 2019](https://insights.infoblox.com/threat-intelligence-reports/threat-intelligence--22)


[^3]: [Unit42 SilverTerrier 2018](https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/whitepapers/unit42-silverterrier-rise-of-nigerian-business-email-compromise)


[^4]: [Talos Lokibot Jan 2021](https://blog.talosintelligence.com/2021/01/a-deep-dive-into-lokibot-infection-chain.html)


[^5]: [FSecure Lokibot November 2019](https://www.f-secure.com/v-descs/trojan_w32_lokibot.shtml)


[^6]: [CISA Lokibot September 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-266a)


[^7]: [TrendMicro Msiexec Feb 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/attack-using-windows-installer-msiexec-exe-leads-lokibot/)


[^8]: [Morphisec Lokibot April 2020](https://blog.morphisec.com/lokibot-with-autoit-obfuscator-frenchy-shellcode)


