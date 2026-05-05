---
aliases: 
    - S0266
    
mitre-attack: https://attack.mitre.org/software/S0266
---

## S0266

[TrickBot](https://attack.mitre.org/software/S0266) is a Trojan spyware program written in C++ that first emerged in September 2016 as a possible successor to [Dyre](https://attack.mitre.org/software/S0024). [TrickBot](https://attack.mitre.org/software/S0266) was developed and initially used by [Wizard Spider](https://attack.mitre.org/groups/G0102) for targeting banking sites in North America, Australia, and throughout Europe; it has since been used against all sectors worldwide as part of "big game hunting" ransomware campaigns.[^9] [^1] [^6] [^28] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [TrickBot](https://attack.mitre.org/software/S0266) gathers the OS version, machine name, CPU type, amount of RAM available, and UEFI/BIOS firmware information from the victim’s machine.[^9] [^1] [^8] [^21]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [TrickBot](https://attack.mitre.org/software/S0266) can identify the user and groups the user belongs to on a compromised host.[^8]  |
| [[Component Object Model\|T1559.001]] | Component Object Model | [TrickBot](https://attack.mitre.org/software/S0266) used COM to setup scheduled task for persistence.[^15]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [TrickBot](https://attack.mitre.org/software/S0266) creates a scheduled task on the system that provides persistence.[^9] [^14] [^23]  |
| [[Bootkit\|T1542.003]] | Bootkit | [TrickBot](https://attack.mitre.org/software/S0266) can implant malicious code into a compromised device's firmware.[^21]  |
| [[Browser Session Hijacking\|T1185]] | Browser Session Hijacking | [TrickBot](https://attack.mitre.org/software/S0266) uses web injects and browser redirection to trick the user into providing their login credentials on a fake or modified web page.[^1] [^6] [^23] [^27]  |
| [[Native API\|T1106]] | Native API | [TrickBot](https://attack.mitre.org/software/S0266) uses the Windows API call, CreateProcessW(), to manage execution flow.[^9]  [TrickBot](https://attack.mitre.org/software/S0266) has also used `Nt*` API functions to perform [Process Injection](https://attack.mitre.org/techniques/T1055).[^26]  |
| [[PowerShell\|T1059.001]] | PowerShell | [TrickBot](https://attack.mitre.org/software/S0266) has been known to use PowerShell to download new payloads, open documents, and upload data to command and control servers. <br> [^7]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [TrickBot](https://attack.mitre.org/software/S0266) can send information about the compromised host and upload data to a hardcoded C2 server.[^8] [^7]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [TrickBot](https://attack.mitre.org/software/S0266) can use secondary C2 servers for communication after establishing connectivity and relaying victim information to primary C2 servers.[^8]  |
| [[VNC\|T1021.005]] | VNC | [TrickBot](https://attack.mitre.org/software/S0266) has used a VNC module to monitor the victim and collect information to pivot to valuable systems on the network [^5] [^7]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [TrickBot](https://attack.mitre.org/software/S0266) uses non-descriptive names to hide functionality.[^9]  |
| [[Windows Service\|T1543.003]] | Windows Service | [TrickBot](https://attack.mitre.org/software/S0266) establishes persistence by creating an autostart service that allows it to run whenever the machine boots.[^27]  |
| [[Software Packing\|T1027.002]] | Software Packing | [TrickBot](https://attack.mitre.org/software/S0266) leverages a custom packer to obfuscate its functionality.[^9]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [TrickBot](https://attack.mitre.org/software/S0266) can obtain passwords stored in files from several applications such as Outlook, Filezilla, OpenSSH, OpenVPN and WinSCP.[^27] [^8]  Additionally, it searches for the ".vnc.lnk" affix to steal VNC credentials.[^3]  |
| [[Malicious File\|T1204.002]] | Malicious File | [TrickBot](https://attack.mitre.org/software/S0266) has attempted to get users to launch malicious documents to deliver its payload. [^3] [^8]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [TrickBot](https://attack.mitre.org/software/S0266) uses a custom crypter leveraging Microsoft’s CryptoAPI to encrypt C2 traffic.[^1] Newer versions of [TrickBot](https://attack.mitre.org/software/S0266) have been known to use `bcrypt` to encrypt and digitally sign responses to their C2 server. [^12]  |
| [[Local Account\|T1087.001]] | Local Account | [TrickBot](https://attack.mitre.org/software/S0266) collects the users of the system.[^9] [^27]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [TrickBot](https://attack.mitre.org/software/S0266) module shareDll/mshareDll discovers network shares via the WNetOpenEnumA API.[^15] [^25]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [TrickBot](https://attack.mitre.org/software/S0266) can Base64-encode C2 commands.[^8]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [TrickBot](https://attack.mitre.org/software/S0266) has been delivered via malicious links in phishing e-mails.[^8]  |
| [[Data from Local System\|T1005]] | Data from Local System | [TrickBot](https://attack.mitre.org/software/S0266) collects local files and information from the victim’s local machine.[^9]  |
| [[Permission Groups Discovery\|T1069]] | Permission Groups Discovery | [TrickBot](https://attack.mitre.org/software/S0266) can identify the groups the user on a compromised host belongs to.[^8]  |
| [[Credentials in Registry\|T1552.002]] | Credentials in Registry | [TrickBot](https://attack.mitre.org/software/S0266) has retrieved PuTTY credentials by querying the `Software\SimonTatham\Putty\Sessions` registry key [^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [TrickBot](https://attack.mitre.org/software/S0266) uses module networkDll for process list discovery.[^15] [^25]  |
| [[Email Account\|T1087.003]] | Email Account | [TrickBot](https://attack.mitre.org/software/S0266) collects email addresses from Outlook.[^27]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [TrickBot](https://attack.mitre.org/software/S0266) has used `printf` and file I/O loops to delay process execution as part of API hammering.[^26]  |
| [[Remote Access Tools\|T1219]] | Remote Access Tools | [TrickBot](https://attack.mitre.org/software/S0266) uses vncDll module to remote control the victim machine.[^15] [^25]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [TrickBot](https://attack.mitre.org/software/S0266) has used macros in Excel documents to download and deploy the malware on the user’s machine.[^3]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [TrickBot](https://attack.mitre.org/software/S0266) can disable Windows Defender.[^27]  |
| [[Masquerading\|T1036]] | Masquerading | The [TrickBot](https://attack.mitre.org/software/S0266) downloader has used an icon to appear as a Microsoft Word document.[^8]  |
| [[Firmware Corruption\|T1495]] | Firmware Corruption | [TrickBot](https://attack.mitre.org/software/S0266) module "Trickboot" can write or erase the UEFI/BIOS firmware of a compromised device.[^21]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [TrickBot](https://attack.mitre.org/software/S0266) decodes the configuration data and modules.[^1] [^8] [^26]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [TrickBot](https://attack.mitre.org/software/S0266) can enumerate computers and network devices.[^8]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | Some [TrickBot](https://attack.mitre.org/software/S0266) samples have used HTTP over ports 447 and 8082 for C2.[^9] [^1] [^14]  Newer versions of [TrickBot](https://attack.mitre.org/software/S0266) have been known to use a custom communication protocol which sends the data unencrypted over port 443. [^7]  |
| [[Password Managers\|T1555.005]] | Password Managers | [TrickBot](https://attack.mitre.org/software/S0266) can steal passwords from the KeePass open source password manager.[^8]  |
| [[Modify Registry\|T1112]] | Modify Registry | [TrickBot](https://attack.mitre.org/software/S0266) can modify registry entries.[^27]  |
| [[Code Signing\|T1553.002]] | Code Signing | [TrickBot](https://attack.mitre.org/software/S0266) has come with a signed downloader component.[^8]  |
| [[Credential Stuffing\|T1110.004]] | Credential Stuffing | [TrickBot](https://attack.mitre.org/software/S0266) uses brute-force attack against RDP with rdpscanDll module.[^15] [^25]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [TrickBot](https://attack.mitre.org/software/S0266) searches the system for all of the following file extensions: .avi, .mov, .mkv, .mpeg, .mpeg4, .mp4, .mp3, .wav, .ogg, .jpeg, .jpg, .png, .bmp, .gif, .tiff, .ico, .xlsx, and .zip. It can also obtain browsing history, cookies, and plug-in information.[^9] [^27]  |
| [[Credential API Hooking\|T1056.004]] | Credential API Hooking | [TrickBot](https://attack.mitre.org/software/S0266) has the ability to capture RDP credentials by capturing the `CredEnumerateA` API[^3]   |
| [[System Service Discovery\|T1007]] | System Service Discovery | [TrickBot](https://attack.mitre.org/software/S0266) collects a list of install programs and services on the system’s machine.[^9]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [TrickBot](https://attack.mitre.org/software/S0266) downloads several additional files and saves them to the victim's machine.[^14] [^7]  |
| [[Process Injection\|T1055]] | Process Injection | [TrickBot](https://attack.mitre.org/software/S0266) has used `Nt*` [Native API](https://attack.mitre.org/techniques/T1106) functions to inject code into legitimate processes such as `wermgr.exe`.[^26]  |
| [[External Proxy\|T1090.002]] | External Proxy | [TrickBot](https://attack.mitre.org/software/S0266) has been known to reach a command and control server via one of nine proxy IP addresses. [^12]  [^7]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [TrickBot](https://attack.mitre.org/software/S0266) injects into the svchost.exe process.[^9] [^14] [^23] [^8]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [TrickBot](https://attack.mitre.org/software/S0266) utilizes EternalBlue and EternalRomance exploits for lateral movement in the modules wormwinDll, wormDll, mwormDll, nwormDll, tabDll.[^15]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | TrickBot has used a hidden VNC (hVNC) window to monitor the victim and collect information stealthily.[^19]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [TrickBot](https://attack.mitre.org/software/S0266) establishes persistence in the Startup folder.[^15]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [TrickBot](https://attack.mitre.org/software/S0266) uses HTTPS to communicate with its C2 servers, to get malware updates, modules that perform most of the malware logic and various configuration files.[^9] [^8]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [TrickBot](https://attack.mitre.org/software/S0266) uses an AES CBC (256 bits) encryption algorithm for its loader and configuration files.[^9]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [TrickBot](https://attack.mitre.org/software/S0266) can obtain passwords stored in files from web browsers such as Chrome, Firefox, Internet Explorer, and Microsoft Edge, sometimes using [esentutl](https://attack.mitre.org/software/S0404).[^27] [^8] [^7]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [TrickBot](https://attack.mitre.org/software/S0266) can gather information about domain trusts by utilizing [Nltest](https://attack.mitre.org/software/S0359).[^22] [^8]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [TrickBot](https://attack.mitre.org/software/S0266) obtains the IP address, location, and other relevant network information from the victim’s machine.[^9] [^27] [^8]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [TrickBot](https://attack.mitre.org/software/S0266) has used an email with an Excel sheet containing a malicious macro to deploy the malware[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Wizard Spider\|G0102]] | Wizard Spider |
| [[TA505\|G0092]] | TA505 |



## References

[^1]: [Fidelis TrickBot Oct 2016](https://www.fidelissecurity.com/threatgeek/2016/10/trickbot-we-missed-you-dyre)


[^2]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^3]: [TrendMicro Trickbot Feb 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/trickbot-adds-remote-application-credential-grabbing-capabilities-to-its-repertoire/)


[^4]: [IBM TA505 April 2020](https://web.archive.org/web/20200420201624/https://securityintelligence.com/posts/ta505-continues-to-infect-networks-with-sdbbot-rat/)


[^5]: [Trickbot VNC module July 2021](https://www.bleepingcomputer.com/news/security/trickbot-updates-its-vnc-module-for-high-value-targets/)


[^6]: [IBM TrickBot Nov 2016](https://securityintelligence.com/tricks-of-the-trade-a-deeper-look-into-trickbots-machinations/)


[^7]: [Bitdefender Trickbot VNC module Whitepaper 2021](https://www.bitdefender.com/files/News/CaseStudies/study/399/Bitdefender-PR-Whitepaper-Trickbot-creat5515-en-EN.pdf)


[^8]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)


[^9]: [S2 Grupo TrickBot June 2017](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)


[^10]: [CrowdStrike Grim Spider May 2019](https://www.crowdstrike.com/blog/timelining-grim-spiders-big-game-hunting-tactics/)


[^11]: TrickBot


[^12]: [Bitdefender Trickbot C2 infra Nov 2020](https://www.bitdefender.com/blog/labs/trickbot-is-dead-long-live-trickbot/)


[^13]: Totbrick


[^14]: [Trend Micro Totbrick Oct 2016](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/tspy_trickload.n)


[^15]: [ESET Trickbot Oct 2020](https://www.welivesecurity.com/2020/10/12/eset-takes-part-global-operation-disrupt-trickbot/)


[^16]: [Sophos New Ryuk Attack October 2020](https://news.sophos.com/en-us/2020/10/14/inside-a-new-ryuk-ransomware-attack/)


[^17]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^18]: TSPY_TRICKLOAD


[^19]: [Emotet Deploys TrickBot](https://www.cybereason.com/blog/research/triple-threat-emotet-deploys-trickbot-to-steal-data-spread-ryuk-ransomware#:~:text=TrickBot%20uses%20a%20hidden%20VNC,desktop%20without%20the%20victim%20noticing)


[^20]: [Proofpoint TA505 Sep 2017](https://www.proofpoint.com/us/threat-insight/post/threat-actor-profile-ta505-dridex-globeimposter)


[^21]: [Eclypsium Trickboot December 2020](https://eclypsium.com/wp-content/uploads/2020/12/TrickBot-Now-Offers-TrickBoot-Persist-Brick-Profit.pdf)


[^22]: [Fortinet TrickBot](https://www.fortinet.com/blog/threat-research/trickbot-s-new-reconnaissance-plugin.html)


[^23]: [Microsoft Totbrick Oct 2017](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Trojan:Win32/Totbrick)


[^24]: [DHS/CISA Ransomware Targeting Healthcare October 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-302a)


[^25]: [Bitdefender Trickbot March 2020](https://www.bitdefender.com/files/News/CaseStudies/study/316/Bitdefender-Whitepaper-TrickBot-en-EN-interactive.pdf)


[^26]: [Joe Sec Trickbot](https://www.joesecurity.org/blog/498839998833561473)


[^27]: [Trend Micro Trickbot Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/trickbot-shows-off-new-trick-password-grabber-module/)


[^28]: [CrowdStrike Wizard Spider October 2020](https://www.crowdstrike.com/blog/wizard-spider-adversary-update/)


