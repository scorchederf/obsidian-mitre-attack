---
aliases: 
    - S0650
    
mitre-attack: https://attack.mitre.org/software/S0650
---

## S0650

[QakBot](https://attack.mitre.org/software/S0650) is a modular banking trojan that has been used primarily by financially-motivated actors since at least 2007. [QakBot](https://attack.mitre.org/software/S0650) is continuously maintained and developed and has evolved from an information stealer into a delivery agent for ransomware, most notably [ProLock](https://attack.mitre.org/software/S0654) and [Egregor](https://attack.mitre.org/software/S0554).[^10] [^8] [^13] [^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [QakBot](https://attack.mitre.org/software/S0650) can use Regsvr32 to execute malicious DLLs.[^8] [^6] [^5] [^17] [^18] [^2]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [QakBot](https://attack.mitre.org/software/S0650) has placed its payload in hidden subdirectories.[^17]  |
| [[System Checks\|T1497.001]] | System Checks | [QakBot](https://attack.mitre.org/software/S0650) can check the compromised host for the presence of multiple executables associated with analysis tools and halt execution if any are found.[^1] [^5]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [QakBot](https://attack.mitre.org/software/S0650) can identify remote systems through the `net view` command.[^14] [^13] [^17]  |
| [[Data from Local System\|T1005]] | Data from Local System | [QakBot](https://attack.mitre.org/software/S0650) can use a variety of commands, including esentutl.exe to steal sensitive data from Internet Explorer and Microsoft Edge, to acquire information that is subsequently exfiltrated.[^8] [^13]  |
| [[External Proxy\|T1090.002]] | External Proxy | [QakBot](https://attack.mitre.org/software/S0650) has a module that can proxy C2 communications.[^13]  |
| [[PowerShell\|T1059.001]] | PowerShell | [QakBot](https://attack.mitre.org/software/S0650) can use PowerShell to download and execute payloads.[^15]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [QakBot](https://attack.mitre.org/software/S0650) can use cmd.exe to launch itself and to execute multiple C2 commands.[^14] [^5] [^13] [^17]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [QakBot](https://attack.mitre.org/software/S0650) can identify the installed antivirus product on a targeted system.[^14] [^5] [^5] [^13]  |
| [[Native API\|T1106]] | Native API | [QakBot](https://attack.mitre.org/software/S0650) can use `GetProcAddress` to help delete malicious strings from memory.[^5]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [QakBot](https://attack.mitre.org/software/S0650) can use large file sizes to evade detection.[^1] [^15]  |
| [[Windows Service\|T1543.003]] | Windows Service | [QakBot](https://attack.mitre.org/software/S0650) can remotely create a temporary service on a target host.[^18]  |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [QakBot](https://attack.mitre.org/software/S0650) can use domain generation algorithms in C2 communication.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [QakBot](https://attack.mitre.org/software/S0650) has the ability to modify the Registry to add its binaries to the Windows Defender exclusion list.[^15]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [QakBot](https://attack.mitre.org/software/S0650) can identify whether it has been run previously on a host by checking for a specified folder.[^5]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [QakBot](https://attack.mitre.org/software/S0650) can maintain persistence by creating an auto-run Registry key.[^1] [^14] [^10] [^15]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [QakBot](https://attack.mitre.org/software/S0650) can store its configuration information in a randomly named subkey under `HKCU\Software\Microsoft`.[^8] [^15]  |
| [[Masquerade File Type\|T1036.008]] | Masquerade File Type | The [QakBot](https://attack.mitre.org/software/S0650) payload has been disguised as a PNG file and hidden within LNK files using a Microsoft File Explorer icon.[^15] [^17]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [QakBot](https://attack.mitre.org/software/S0650) can use `net share` to identify network shares for use in lateral movement.[^1] [^13]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [QakBot](https://attack.mitre.org/software/S0650) can use process hollowing to execute its main payload.[^5]  |
| [[JavaScript\|T1059.007]] | JavaScript | The [QakBot](https://attack.mitre.org/software/S0650) web inject module can inject Java Script into web banking pages visited by the victim.[^13] [^17]  |
| [[Msiexec\|T1218.007]] | Msiexec | [QakBot](https://attack.mitre.org/software/S0650) can use MSIExec to spawn multiple cmd.exe processes.[^14]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [QakBot](https://attack.mitre.org/software/S0650) can deobfuscate and re-assemble code strings for execution.[^6] [^5] [^13]  |
| [[Local Email Collection\|T1114.001]] | Local Email Collection | [QakBot](https://attack.mitre.org/software/S0650) can target and steal locally stored emails to support thread hijacking phishing campaigns.[^4] [^10] [^13]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [QakBot](https://attack.mitre.org/software/S0650) has gained execution through users opening malicious links.[^1] [^4] [^10] [^5] [^13] [^15] [^17] <br> |
| [[System Time Discovery\|T1124]] | System Time Discovery | [QakBot](https://attack.mitre.org/software/S0650) can identify the system time on a targeted host.[^13]  |
| [[Malicious File\|T1204.002]] | Malicious File | [QakBot](https://attack.mitre.org/software/S0650) has gained execution through users opening malicious attachments.[^1] [^4] [^14] [^10] [^6] [^5] [^13] [^15] [^2] [^11]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [QakBot](https://attack.mitre.org/software/S0650) can send stolen information to C2 nodes including passwords, accounts, and emails.[^13]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [QakBot](https://attack.mitre.org/software/S0650) can identify the user name on a compromised system.[^13] [^17]  |
| [[HTML Smuggling\|T1027.006]] | HTML Smuggling | [QakBot](https://attack.mitre.org/software/S0650) has been delivered in ZIP files via HTML smuggling.[^17] [^2]  |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [QakBot](https://attack.mitre.org/software/S0650) can measure the download speed on a targeted host.[^13]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [QakBot](https://attack.mitre.org/software/S0650) can RC4 encrypt strings in C2 communication.[^13]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [QakBot](https://attack.mitre.org/software/S0650) can use obfuscated and encoded scripts.[^6] [^17]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [QakBot](https://attack.mitre.org/software/S0650) has the ability to use HTTP and HTTPS in communication with C2 servers.[^1] [^14] [^13]  |
| [[Code Signing\|T1553.002]] | Code Signing | [QakBot](https://attack.mitre.org/software/S0650) can use signed loaders to evade detection.[^5] [^2] <br> |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [QakBot](https://attack.mitre.org/software/S0650) has hidden code within Excel spreadsheets by turning the font color to white and splitting it across multiple cells.[^6]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [QakBot](https://attack.mitre.org/software/S0650) can move laterally using worm-like functionality through exploitation of SMB.[^14]  |
| [[Process Discovery\|T1057]] | Process Discovery | [QakBot](https://attack.mitre.org/software/S0650) has the ability to check running processes.[^5]  |
| [[Local Groups\|T1069.001]] | Local Groups | [QakBot](https://attack.mitre.org/software/S0650) can use `net localgroup` to enable discovery of local groups.[^13] [^17]  |
| [[DLL\|T1574.001]] | DLL | [QakBot](https://attack.mitre.org/software/S0650) has the ability to use DLL side-loading for execution.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [QakBot](https://attack.mitre.org/software/S0650) can use `net config workstation`, `arp -a`, `nslookup`, and `ipconfig /all` to gather network configuration information.[^14] [^13] [^15] [^17] [^11]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [QakBot](https://attack.mitre.org/software/S0650) has the ability to capture web session cookies.[^4] [^13]  |
| [[Process Injection\|T1055]] | Process Injection | [QakBot](https://attack.mitre.org/software/S0650) can inject itself into processes including explore.exe, Iexplore.exe, Mobsync.exe., and wermgr.exe.[^1] [^4] [^10] [^13] [^17]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [QakBot](https://attack.mitre.org/software/S0650) can run `nltest /domain_trusts /all_trusts` for domain trust discovery.[^13]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [QakBot](https://attack.mitre.org/software/S0650) has stored stolen emails and other data into new folders prior to exfiltration.[^4]  |
| [[Brute Force\|T1110]] | Brute Force | [QakBot](https://attack.mitre.org/software/S0650) can conduct brute force attacks to capture credentials.[^4] [^14] [^13]  |
| [[Mark-of-the-Web Bypass\|T1553.005]] | Mark-of-the-Web Bypass | [QakBot](https://attack.mitre.org/software/S0650) has been packaged in ISO files in order to bypass Mark of the Web (MOTW) security measures.[^17]  |
| [[Browser Session Hijacking\|T1185]] | Browser Session Hijacking | [QakBot](https://attack.mitre.org/software/S0650) can use advanced web injects to steal web banking credentials.[^6] [^13]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | The [QakBot](https://attack.mitre.org/software/S0650) dropper can delay dropping the payload to evade detection.[^6] [^13]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [QakBot](https://attack.mitre.org/software/S0650) has the ability to download additional components and malware.[^1] [^14] [^10] [^6] [^13] [^15]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [QakBot](https://attack.mitre.org/software/S0650) can identify peripheral devices on targeted systems.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [QakBot](https://attack.mitre.org/software/S0650) has the ability use TCP to send or receive C2 packets.[^13]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [QakBot](https://attack.mitre.org/software/S0650) has spread through emails with malicious links.[^1] [^4] [^10] [^5] [^13] [^15] [^17] <br> |
| [[Indicator Removal from Tools\|T1027.005]] | Indicator Removal from Tools | [QakBot](https://attack.mitre.org/software/S0650) can make small changes to itself in order to change its checksum and hash value.[^14] [^6]  |
| [[Modify Registry\|T1112]] | Modify Registry | [QakBot](https://attack.mitre.org/software/S0650) can modify the Registry to store its configuration information in a randomly named subkey under `HKCU\Software\Microsoft`.[^8] [^15]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [QakBot](https://attack.mitre.org/software/S0650) has spread through emails with malicious attachments.[^1] [^4] [^10] [^6] [^5] [^13] [^15] [^2] [^11]  |
| [[Keylogging\|T1056.001]] | Keylogging | [QakBot](https://attack.mitre.org/software/S0650) can capture keystrokes on a compromised host.[^4] [^10] [^13]  |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [QakBot](https://attack.mitre.org/software/S0650) has the ability to use removable drives to spread through compromised networks.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [QakBot](https://attack.mitre.org/software/S0650) can Base64 encode system information sent to C2.[^14] [^13]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [QakBot](https://attack.mitre.org/software/S0650) can use VBS to download and execute malicious files.[^1] <br>[^4] [^14] [^10] [^6] [^15] [^17]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [QakBot](https://attack.mitre.org/software/S0650) can collect system information including the OS version and domain on a compromised host.[^14] [^5] [^15] [^11]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [QakBot](https://attack.mitre.org/software/S0650) can execute WMI queries to gather information.[^13]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [QakBot](https://attack.mitre.org/software/S0650) has the ability to enumerate windows on a compromised host.[^5] <br> |
| [[Software Discovery\|T1518]] | Software Discovery | [QakBot](https://attack.mitre.org/software/S0650) can enumerate a list of installed programs.[^15]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [QakBot](https://attack.mitre.org/software/S0650) can use `netstat` to enumerate current network connections.[^13] [^17]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [QakBot](https://attack.mitre.org/software/S0650) has the ability to create scheduled tasks for persistence.[^1] [^4] [^14] [^10] [^8] [^6] [^13] [^15]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [QakBot](https://attack.mitre.org/software/S0650) has used Rundll32.exe to drop malicious DLLs including [Brute Ratel C4](https://attack.mitre.org/software/S1063) and to enable C2 communication.[^14] [^8] [^6] [^5] [^17]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | The [QakBot](https://attack.mitre.org/software/S0650) proxy module can encapsulate SOCKS5 protocol within its own proxy protocol.[^13]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [QakBot](https://attack.mitre.org/software/S0650) has collected usernames and passwords from Firefox and Chrome.[^13]  |
| [[Software Packing\|T1027.002]] | Software Packing | [QakBot](https://attack.mitre.org/software/S0650) can encrypt and pack malicious payloads.[^6]  |
| [[File Deletion\|T1070.004]] | File Deletion | [QakBot](https://attack.mitre.org/software/S0650) can delete folders and files including overwriting its executable with legitimate programs.[^4] [^14] [^5] [^15]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA551\|G0127]] | TA551 |
| [[TA577\|G1037]] | TA577 |
| [[Storm-1811\|G1046]] | Storm-1811 |



## References

[^1]: [Trend Micro Qakbot May 2020](https://www.trendmicro.com/vinfo/ph/security/news/cybercrime-and-digital-threats/qakbot-resurges-spreads-through-vbs-files)


[^2]: [Deep Instinct Black Basta August 2022](https://www.deepinstinct.com/blog/black-basta-ransomware-threat-emergence)


[^3]: QBot


[^4]: [Kroll Qakbot June 2020](https://www.kroll.com/en/insights/publications/cyber/qakbot-malware-exfiltrating-emails-thread-hijacking-attacks)


[^5]: [ATT QakBot April 2021](https://cybersecurity.att.com/blogs/labs-research/the-rise-of-qakbot)


[^6]: [Cyberint Qakbot May 2021](https://blog.cyberint.com/qakbot-banking-trojan)


[^7]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)


[^8]: [Red Canary Qbot](https://redcanary.com/threat-detection-report/threats/qbot/)


[^9]: [Microsoft Storm-1811 2024](https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/)


[^10]: [Trend Micro Qakbot December 2020](https://success.trendmicro.com/en-US/solution/KA-0011282)


[^11]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^12]: Pinkslipbot


[^13]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)


[^14]: [Crowdstrike Qakbot October 2020](https://www.crowdstrike.com/blog/duck-hunting-with-falcon-complete-qakbot-zip-based-campaign/)


[^15]: [Group IB Ransomware September 2020](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)


[^16]: QuackBot


[^17]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)


[^18]: [NCC Group Black Basta June 2022](https://research.nccgroup.com/2022/06/06/shining-the-light-on-black-basta/)


