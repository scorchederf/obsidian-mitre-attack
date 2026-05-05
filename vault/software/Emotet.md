---
aliases: 
    - S0367
    
mitre-attack: https://attack.mitre.org/software/S0367
---

## S0367

[Emotet](https://attack.mitre.org/software/S0367) is a modular malware variant which is primarily used as a downloader for other malware variants such as [TrickBot](https://attack.mitre.org/software/S0266) and [IcedID](https://attack.mitre.org/software/S0483). Emotet first emerged in June 2014, initially targeting the financial sector, and has expanded to multiple verticals over time.[^25] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Emotet](https://attack.mitre.org/software/S0367) has enumerated all users connected to network shares. |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Emotet](https://attack.mitre.org/software/S0367) has copied itself to remote systems using the `service.exe` filename.[^20]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Emotet](https://attack.mitre.org/software/S0367) is known to use RSA keys for encrypting C2 traffic. [^15]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [Emotet](https://attack.mitre.org/software/S0367) has been observed leveraging a module that retrieves passwords stored on a system for the current logged-on user. [^16] [^26]  |
| [[Password Guessing\|T1110.001]] | Password Guessing | [Emotet](https://attack.mitre.org/software/S0367) has been observed using a hard coded list of passwords to brute force user accounts. [^22] [^13] [^16] [^24] [^26] [^20]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Emotet](https://attack.mitre.org/software/S0367) has used WMI to execute powershell.exe.[^10]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [Emotet](https://attack.mitre.org/software/S0367) has used HTTP over ports such as 20, 22, 443, 7080, and 50000, in addition to using ports commonly associated with HTTP/S.[^6] [^20]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [Emotet](https://attack.mitre.org/software/S0367) inflates malicious files and malware as an evasion technique.[^5]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Emotet](https://attack.mitre.org/software/S0367) uses RegSvr32 to execute the DLL payload.[^5]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Emotet](https://attack.mitre.org/software/S0367) has leveraged the Admin$, C$, and IPC$ shares for lateral movement. [^22] [^20]   |
| [[Malicious File\|T1204.002]] | Malicious File | [Emotet](https://attack.mitre.org/software/S0367) has relied upon users clicking on a malicious attachment delivered through spearphishing.[^25] [^10] [^14]  |
| [[Token Impersonation／Theft\|T1134.001]] | Token Impersonation／Theft | [Emotet](https://attack.mitre.org/software/S0367) has the ability to duplicate the user’s token.[^20]  For example, [Emotet](https://attack.mitre.org/software/S0367) may use a variant of Google’s ProtoBuf to send messages that specify how code will be executed.[^1]  |
| [[Local Accounts\|T1078.003]] | Local Accounts | [Emotet](https://attack.mitre.org/software/S0367) can brute force a local admin password, then use it to facilitate lateral movement.[^22]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Emotet](https://attack.mitre.org/software/S0367) has been observed adding the downloaded payload to the `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run` key to maintain persistence.[^13] [^16] [^12]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Emotet](https://attack.mitre.org/software/S0367) has been delivered by phishing emails containing links. [^25] [^9] [^3] [^22] [^13] [^16] [^6] [^6] [^12]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Emotet](https://attack.mitre.org/software/S0367) has used Google’s Protobufs to serialize data sent to and from the C2 server.[^20]  Additionally, [Emotet](https://attack.mitre.org/software/S0367) has used Base64 to encode data before sending to the C2 server.[^4]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Emotet](https://attack.mitre.org/software/S0367) has enumerated non-hidden network shares using `WNetEnumResourceW`. [^20]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Emotet](https://attack.mitre.org/software/S0367) has used HTTP for command and control.[^20]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Emotet](https://attack.mitre.org/software/S0367) has exfiltrated data over its C2 channel.[^15] [^20]  |
| [[Embedded Payloads\|T1027.009]] | Embedded Payloads | [Emotet](https://attack.mitre.org/software/S0367) has dropped an embedded executable at `%Temp%\setup.exe`.[^20]  Additionally, [Emotet](https://attack.mitre.org/software/S0367) may embed entire code into other files.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Emotet](https://attack.mitre.org/software/S0367) can download follow-on payloads and items via malicious `url` parameters in obfuscated PowerShell code.[^8]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [Emotet](https://attack.mitre.org/software/S0367) has been seen exploiting SMB via a vulnerability exploit like EternalBlue (MS17-010) to achieve lateral movement and propagation.[^13] [^16] [^24] [^23]   |
| [[Email Collection\|T1114]] | Email Collection | [Emotet](https://attack.mitre.org/software/S0367) has been observed leveraging a module that can scrape email addresses from Outlook.[^26] [^14] [^20]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Emotet](https://attack.mitre.org/software/S0367) has maintained persistence through a scheduled task, e.g. though a .dll file in the Registry.[^16] [^1]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Emotet](https://attack.mitre.org/software/S0367) has been observed dropping browser password grabber modules. [^15] [^14]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Emotet](https://attack.mitre.org/software/S0367) has used Powershell to retrieve the malicious payload and download additional resources like [Mimikatz](https://attack.mitre.org/software/S0002). [^13] [^15] [^12] [^23] [^10]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Emotet](https://attack.mitre.org/software/S0367) has used a self-extracting RAR file to deliver modules to victims. Emotet has also extracted embedded executables from files using hard-coded buffer offsets.[^20]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Emotet](https://attack.mitre.org/software/S0367) has sent Microsoft Word documents with embedded macros that will invoke scripts to download additional payloads. [^13] [^6] [^15] [^12] [^10]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Emotet](https://attack.mitre.org/software/S0367) has relied upon users clicking on a malicious link delivered through spearphishing.[^25] [^10]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Emotet](https://attack.mitre.org/software/S0367) has installed itself as a new service with the service name `Windows Defender System Service` and display name `WinDefService`.[^20]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Emotet](https://attack.mitre.org/software/S0367) has obfuscated macros within malicious documents to hide the URLs hosting the malware,  CMD.exe arguments, and PowerShell scripts. [^6] [^15] [^12] [^2]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Emotet](https://attack.mitre.org/software/S0367) has been observed dropping and executing password grabber modules including [Mimikatz](https://attack.mitre.org/software/S0002).[^15] [^1]  |
| [[Network Sniffing\|T1040]] | Network Sniffing | [Emotet](https://attack.mitre.org/software/S0367) has been observed to hook network APIs to monitor network traffic. [^25]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [Emotet](https://attack.mitre.org/software/S0367) has reflectively loaded payloads into memory.[^20]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Emotet](https://attack.mitre.org/software/S0367) uses obfuscated URLs to download a ZIP file.[^5]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Emotet](https://attack.mitre.org/software/S0367) has used cmd.exe to run a PowerShell script. [^12]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Emotet](https://attack.mitre.org/software/S0367) has been delivered by phishing emails containing attachments. [^3] [^22] [^13] [^16] [^6] [^15] [^12] [^10] [^14]  |
| [[Email Account\|T1087.003]] | Email Account | [Emotet](https://attack.mitre.org/software/S0367) has been observed leveraging a module that can scrape email addresses from Outlook.[^26] [^14] [^20]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Emotet](https://attack.mitre.org/software/S0367) has used custom packers to protect its payloads.[^15]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Emotet](https://attack.mitre.org/software/S0367) uses a copy of `certutil.exe` stored in a temporary directory for process hollowing, starting the program in a suspended state before loading malicious code.[^5]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Emotet](https://attack.mitre.org/software/S0367) has been observed enumerating local processes.[^18]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Emotet](https://attack.mitre.org/software/S0367) has been observed injecting in to Explorer.exe and other processes. [^12] [^25] [^16]  |
| [[Local Email Collection\|T1114.001]] | Local Email Collection | [Emotet](https://attack.mitre.org/software/S0367) has been observed leveraging a module that scrapes email data from Outlook.[^26]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Emotet](https://attack.mitre.org/software/S0367) has been observed creating new services to maintain persistence.[^16] [^24] [^20]   |
| [[Encrypted Channel\|T1573]] | Encrypted Channel | [Emotet](https://attack.mitre.org/software/S0367) has encrypted data before sending to the C2 server.[^4]  |
| [[Native API\|T1106]] | Native API | [Emotet](https://attack.mitre.org/software/S0367) has used `CreateProcess` to create a new process to run its executable and `WNetEnumResourceW` to enumerate non-hidden shares.[^20]  |
| [[Wi-Fi Discovery\|T1016.002]] | Wi-Fi Discovery | [Emotet](https://attack.mitre.org/software/S0367) can extract names of all locally reachable Wi-Fi networks and then perform a brute-force attack to spread to new networks.[^20]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Wizard Spider\|G0102]] | Wizard Spider |



## References

[^1]: [emotet_hc3_nov2023](https://www.hhs.gov/sites/default/files/emotet-the-enduring-and-persistent-threat-to-the-hph-tlpclear.pdf)


[^2]: [ESET Emotet Dec 2018](https://www.welivesecurity.com/2018/12/28/analysis-latest-emotet-propagation-campaign/)


[^3]: [CIS Emotet Apr 2017](https://www.cisecurity.org/blog/emotet-changes-ttp-and-arrives-in-united-states/)


[^4]: [Fortinet Emotet May 2017](https://www.fortinet.com/blog/threat-research/deep-analysis-of-new-emotet-variant-part-1.html)


[^5]: [emotet_trendmicro_mar2023](https://www.trendmicro.com/en_us/research/23/c/emotet-returns-now-adopts-binary-padding-for-evasion.html)


[^6]: [Talos Emotet Jan 2019](https://blog.talosintelligence.com/2019/01/return-of-emotet.html)


[^7]: [ESET Emotet Nov 2018](https://www.welivesecurity.com/2018/11/09/emotet-launches-major-new-spam-campaign/)


[^8]: [Pincus Emotet 2020](https://medium.com/picus-security/an-analysis-of-emotet-malware-powershell-unobfuscation-4f46b50dcf2b)


[^9]: [Kaspersky Emotet Jan 2019](https://securelist.com/the-banking-trojan-emotet-detailed-analysis/69560/)


[^10]: [Carbon Black Emotet Apr 2019](https://www.carbonblack.com/2019/04/24/cb-tau-threat-intelligence-notification-emotet-utilizing-wmi-to-launch-powershell-encoded-code/)


[^11]: [CrowdStrike Grim Spider May 2019](https://www.crowdstrike.com/blog/timelining-grim-spiders-big-game-hunting-tactics/)


[^12]: [Picus Emotet Dec 2018](https://www.picussecurity.com/blog/the-christmas-card-you-never-wanted-a-new-wave-of-emotet-is-back-to-wreak-havoc.html)


[^13]: [Symantec Emotet Jul 2018](https://www.symantec.com/blogs/threat-intelligence/evolution-emotet-trojan-distributor)


[^14]: [IBM IcedID November 2017](https://securityintelligence.com/new-banking-trojan-icedid-discovered-by-ibm-x-force-research/)


[^15]: [Trend Micro Emotet Jan 2019](https://documents.trendmicro.com/assets/white_papers/ExploringEmotetsActivities_Final.pdf)


[^16]: [US-CERT Emotet Jul 2018](https://www.us-cert.gov/ncas/alerts/TA18-201A)


[^17]: [Sophos New Ryuk Attack October 2020](https://news.sophos.com/en-us/2020/10/14/inside-a-new-ryuk-ransomware-attack/)


[^18]: [ASEC Emotet 2017](https://global.ahnlab.com/global/upload/download/asecreport/ASEC%20REPORT_vol.88_ENG.pdf)


[^19]: Geodo


[^20]: [Binary Defense Emotes Wi-Fi Spreader](https://www.binarydefense.com/resources/blog/emotet-evolves-with-new-wi-fi-spreader/)


[^21]: Emotet


[^22]: [Malwarebytes Emotet Dec 2017](https://support.malwarebytes.com/docs/DOC-2295)


[^23]: [Red Canary Emotet Feb 2019](https://redcanary.com/blog/stopping-emotet-before-it-moves-laterally/)


[^24]: [Secureworks Emotet Nov 2018](https://www.secureworks.com/blog/lazy-passwords-become-rocket-fuel-for-emotet-smb-spreader)


[^25]: [Trend Micro Banking Malware Jan 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/new-banking-malware-uses-network-sniffing-for-data-theft/)


[^26]: [CIS Emotet Dec 2018](https://www.cisecurity.org/white-papers/ms-isac-security-primer-emotet/)


