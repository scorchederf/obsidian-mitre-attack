---
aliases: 
    - S0013
    
mitre-attack: https://attack.mitre.org/software/S0013
---

## S0013

[PlugX](https://attack.mitre.org/software/S0013) is a remote access tool (RAT) with modular plugins that has been used by multiple threat groups.[^38] [^19] [^44] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [PlugX](https://attack.mitre.org/software/S0013) has made calls to Windows API `CheckRemoteDebuggerPresent` and exits if it detects a debugger.[^29]  |
| [[Modify Registry\|T1112]] | Modify Registry | [PlugX](https://attack.mitre.org/software/S0013) has a module to create, delete, or modify Registry keys.[^47] [^23] [^9]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [PlugX](https://attack.mitre.org/software/S0013) has a module to enumerate drives and find files recursively.[^47] [^33] [^23] [^37]  [PlugX](https://attack.mitre.org/software/S0013) has also checked the path from which it is running for specific parameters prior to execution. [^47] [^9] [^29]  |
| [[System Location Discovery\|T1614]] | System Location Discovery | [PlugX](https://attack.mitre.org/software/S0013) has obtained the location of the victim device by leveraging `GetSystemDefaultLCID`.[^47]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | In one instance, [menuPass](https://attack.mitre.org/groups/G0045) added [PlugX](https://attack.mitre.org/software/S0013) as a service with a display name of "Corel Writing Tools Utility."[^17]  |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [PlugX](https://attack.mitre.org/software/S0013) has copied itself to infected removable drives for propagation to other victim devices.[^9]  |
| [[Mutual Exclusion\|T1480.002]] | Mutual Exclusion | [PlugX](https://attack.mitre.org/software/S0013) has leveraged a mutex in its infection process.[^47] [^29]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [PlugX](https://attack.mitre.org/software/S0013) has captured victim IP address details of the targeted machine.[^47] [^9]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [PlugX](https://attack.mitre.org/software/S0013) can modify the characteristics of folders to hide them from the compromised user.[^37]  [PlugX](https://attack.mitre.org/software/S0013) has also modified file attributes to hidden and system.[^47] [^29]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [PlugX](https://attack.mitre.org/software/S0013) can be configured to use raw TCP or UDP for command and control.[^47] [^3]  |
| [[Malicious File\|T1204.002]] | Malicious File | [PlugX](https://attack.mitre.org/software/S0013) has leveraged an initial executable disguised as a legitimate document to trick the target into opening it.[^33] [^48]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [PlugX](https://attack.mitre.org/software/S0013) has collected a list of all mapped drives on the infected host.[^47]  |
| [[Keylogging\|T1056.001]] | Keylogging | [PlugX](https://attack.mitre.org/software/S0013) has a module for capturing keystrokes per process including window titles.[^23]  |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | [PlugX](https://attack.mitre.org/software/S0013) uses Pastebin to store C2 addresses.[^5]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [PlugX](https://attack.mitre.org/software/S0013) has identified system time through its GetSystemInfo command.[^47]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [PlugX](https://attack.mitre.org/software/S0013) has loaded its payload into memory.[^47] [^48] [^21] [^7] [^29]  |
| [[Process Discovery\|T1057]] | Process Discovery | [PlugX](https://attack.mitre.org/software/S0013) has a module to list the processes running on a machine.[^23]  |
| [[Query Registry\|T1012]] | Query Registry | [PlugX](https://attack.mitre.org/software/S0013) can enumerate and query for information contained within the Windows Registry.[^47] [^23] [^38]  |
| [[DLL\|T1574.001]] | DLL | [PlugX](https://attack.mitre.org/software/S0013) has the ability to use DLL search order hijacking for installation on targeted systems.[^37] [^7]   [PlugX](https://attack.mitre.org/software/S0013) has also used DLL side-loading to evade anti-virus.[^19] [^3] [^8] [^22] [^5] [^6] [^36]  [PlugX](https://attack.mitre.org/software/S0013) has also used a legitimately signed executable to side-load a malicious payload within a DLL file.[^47] [^33] [^48] [^7] [^29]  |
| [[Clear Persistence\|T1070.009]] | Clear Persistence | [PlugX](https://attack.mitre.org/software/S0013) has deleted registry keys that store data and maintained persistence.[^47]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [PlugX](https://attack.mitre.org/software/S0013) has a module to enumerate network shares.[^47] [^23]  |
| [[MSBuild\|T1127.001]] | MSBuild | A version of [PlugX](https://attack.mitre.org/software/S0013) loads as shellcode within a .NET Framework project using msbuild.exe, presumably to bypass application control techniques.[^5]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [PlugX](https://attack.mitre.org/software/S0013) can be configured to use HTTP for command and control.[^47] [^3] [^48] [^37]  [PlugX](https://attack.mitre.org/software/S0013) has also used HTTPS for C2.[^21]  |
| [[Windows Service\|T1543.003]] | Windows Service | [PlugX](https://attack.mitre.org/software/S0013) can be added as a service to establish persistence. [PlugX](https://attack.mitre.org/software/S0013) also has a module to change service configurations as well as start, control, and delete services.[^23] [^38] [^22] [^17] [^42]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [PlugX](https://attack.mitre.org/software/S0013) allows actors to spawn a reverse shell on a victim.[^47] [^23] [^3] [^48] [^21] [^7]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [PlugX](https://attack.mitre.org/software/S0013) has a module to download and execute files on the compromised machine.[^23] [^9] [^21] [^37]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [PlugX](https://attack.mitre.org/software/S0013) has modified local firewall rules on victim machines to enable a random, high-number listening port for subsequent access and C2 activity.[^39]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [PlugX](https://attack.mitre.org/software/S0013) has collected system information including OS version, processor information, RAM size, location, host name, IP, and screen size of the infected host.[^47]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [PlugX](https://attack.mitre.org/software/S0013) has collected and staged the victim’s computer files for exfiltration.[^9]  |
| [[System Checks\|T1497.001]] | System Checks | [PlugX](https://attack.mitre.org/software/S0013) checks if VMware tools is running in the background by searching for any process named "vmtoolsd".[^40]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [PlugX](https://attack.mitre.org/software/S0013) has a module for enumerating TCP and UDP network connections and associated processes using the `netstat` command.[^23]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [PlugX](https://attack.mitre.org/software/S0013) has been disguised as legitimate Adobe and PotPlayer files.[^37]  [PlugX](https://attack.mitre.org/software/S0013) has also imitated legitimate software directories and file names through the creation and storage of a legitimate EXE and the malicious DLLs.[^47] [^48] [^7] [^29]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [PlugX](https://attack.mitre.org/software/S0013) adds Run key entries in the Registry to establish persistence.[^47] [^23] [^9] [^48] [^22] [^29] [^38]  [PlugX](https://attack.mitre.org/software/S0013) has established persistence via the registry keys `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` and `HKLM\Software\Microsoft\Windows\CurrentVersion\Run`.[^47]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [PlugX](https://attack.mitre.org/software/S0013) has utilized junk code and opaque predicates in payloads to hinder analysis.[^47]  |
| [[DNS\|T1071.004]] | DNS | [PlugX](https://attack.mitre.org/software/S0013) can be configured to use DNS for command and control.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [PlugX](https://attack.mitre.org/software/S0013) has the remove itself and other artifacts.[^47] [^9]  |
| [[Screen Capture\|T1113]] | Screen Capture | [PlugX](https://attack.mitre.org/software/S0013) allows the operator to capture screenshots.[^23]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [PlugX](https://attack.mitre.org/software/S0013) has created a scheduled task to execute additional malicious software, as well as maintain persistence.[^47]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [PlugX](https://attack.mitre.org/software/S0013) can use RC4 encryption in C2 communications.[^47] [^37]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [PlugX](https://attack.mitre.org/software/S0013) has used random, high-number, non-standard ports to listen for subsequent actions and C2 activities.[^39]  |
| [[Dynamic API Resolution\|T1027.007]] | Dynamic API Resolution | [PlugX](https://attack.mitre.org/software/S0013) has leveraged obfuscated Windows API function calls that were concealed as unique names, or hashes of the Windows API.[^47]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [PlugX](https://attack.mitre.org/software/S0013) decompresses and decrypts itself using the Microsoft API call RtlDecompressBuffer.[^23] [^6] [^37]  [PlugX](https://attack.mitre.org/software/S0013) has also decrypted its payloads in memory.[^47] [^33] [^48] [^29]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [PlugX](https://attack.mitre.org/software/S0013) has the ability to execute a command on a hidden desktop.[^47]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [PlugX](https://attack.mitre.org/software/S0013) can identify removable media attached to compromised hosts.[^9]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [PlugX](https://attack.mitre.org/software/S0013) has exfiltrated stolen data and files to its C2 server.[^9] [^7]  |
| [[Native API\|T1106]] | Native API | [PlugX](https://attack.mitre.org/software/S0013) can use the Windows API functions `GetProcAddress`, `LoadLibrary`, and `CreateProcess` to execute another process.[^47] [^37] [^38]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [PlugX](https://attack.mitre.org/software/S0013) can use API hashing and modify the names of strings to evade detection.[^6] [^37]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [PlugX](https://attack.mitre.org/software/S0013) has the ability to gather the username from the victim’s machine.[^47]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [PlugX](https://attack.mitre.org/software/S0013) has leveraged XOR encryption with the key of 123456789.[^47]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Velvet Ant\|G1047]] | Velvet Ant |
| [[Daggerfly\|G1034]] | Daggerfly |
| [[APT41\|G0096]] | APT41 |
| [[APT3\|G0022]] | APT3 |
| [[Higaisa\|G0126]] | Higaisa |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 |
| [[Cinnamon Tempest\|G1021]] | Cinnamon Tempest |
| [[GALLIUM\|G0093]] | GALLIUM |
| [[Axiom\|G0001]] | Axiom |
| [[menuPass\|G0045]] | menuPass |
| [[TA459\|G0062]] | TA459 |
| [[LuminousMoth\|G1014]] | LuminousMoth |
| [[DragonOK\|G0017]] | DragonOK |
| [[Winnti Group\|G0044]] | Winnti Group |
| [[Mustang Panda\|G0129]] | Mustang Panda |



## References

[^1]: [DOJ APT10 Dec 2018](https://www.justice.gov/opa/pr/two-chinese-hackers-associated-ministry-state-security-charged-global-computer-intrusion)


[^2]: [Secureworks BRONZE PRESIDENT December 2019](https://www.secureworks.com/research/bronze-president-targets-ngos)


[^3]: [Dell TG-3390](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)


[^4]: PlugX


[^5]: [Palo Alto PlugX June 2017](https://researchcenter.paloaltonetworks.com/2017/06/unit42-paranoid-plugx/)


[^6]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^7]: [Sophos PlugX September 2022](https://www.secureworks.com/blog/bronze-president-targets-russian-speakers-with-updated-plugx)


[^8]: [Stewart 2014](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^9]: [DOJ Affidavit Search and Seizure PlugX December 2024](https://www.justice.gov/archives/opa/media/1384136/dl)


[^10]: Korplug


[^11]: Kaba


[^12]: [Malwarebytes Higaisa 2020](https://blog.malwarebytes.com/threat-analysis/2020/06/higaisa/)


[^13]: [Symantec Daggerfly 2023](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)


[^14]: [Nccgroup Emissary Panda May 2018](https://research.nccgroup.com/2018/05/18/emissary-panda-a-potential-new-malicious-tool/)


[^15]: [Recorded Future REDDELTA July 2020](https://go.recordedfuture.com/hubfs/reports/cta-2020-0728.pdf)


[^16]: [Cybereason Soft Cell June 2019](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)


[^17]: [FireEye APT10 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/apt10_menupass_grou.html)


[^18]: [Kaspersky LuminousMoth July 2021](https://securelist.com/apt-luminousmoth/103332/)


[^19]: [FireEye Clandestine Fox Part 2](https://www.fireeye.com/blog/threat-research/2014/06/clandestine-fox-part-deux.html)


[^20]: TVT


[^21]: [Google Threat Intelligence Group MUSTANG PANDA PLUGX August 2025](https://cloud.google.com/blog/topics/threat-intelligence/prc-nexus-espionage-targets-diplomats)


[^22]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^23]: [CIRCL PlugX March 2013](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)


[^24]: [Cisco Group 72](http://blogs.cisco.com/security/talos/threat-spotlight-group-72)


[^25]: Thoper


[^26]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)


[^27]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^28]: [Crowdstrike MUSTANG PANDA June 2018](https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-june-mustang-panda/)


[^29]: [Sophos Mustang Panda PLUGX](https://www.secureworks.com/blog/bronze-president-targets-government-officials)


[^30]: [Bitdefender LuminousMoth July 2021](https://www.bitdefender.com/blog/labs/luminousmoth-plugx-file-exfiltration-and-persistence-revisited)


[^31]: [Anomali MUSTANG PANDA October 2019](https://www.anomali.com/blog/china-based-apt-mustang-panda-targets-minority-groups-public-and-private-sector-organizations)


[^32]: [Dell SecureWorks BRONZE STARLIGHT Profile](https://www.secureworks.com/research/threat-profiles/bronze-starlight)


[^33]: [Cisco Talos MUSTANG PANDA PLUGX PUBLOAD MAY 2022](https://blog.talosintelligence.com/mustang-panda-targets-europe/)


[^34]: [Proofpoint TA459 April 2017](https://www.proofpoint.com/us/threat-insight/post/apt-targets-financial-analysts)


[^35]: [Kaspersky Winnti April 2013](https://securelist.com/winnti-more-than-just-a-game/37029/)


[^36]: [Profero APT27 December 2020](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)


[^37]: [Proofpoint TA416 Europe March 2022](https://www.proofpoint.com/us/blog/threat-insight/good-bad-and-web-bug-ta416-increases-operational-tempo-against-european)


[^38]: [Lastline PlugX Analysis](https://lastline3.rssing.com/chan-29044929/all_p1.html#c29044929a2)


[^39]: [Sygnia VelvetAnt 2024A](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)


[^40]: [Unit42 PlugX June 2017](https://unit42.paloaltonetworks.com/unit42-paranoid-plugx/)


[^41]: [Avira Mustang Panda January 2020](https://www.avira.com/en/blog/new-wave-of-plugx-targets-hong-kong)


[^42]: [Proofpoint ZeroT Feb 2017](https://www.proofpoint.com/us/threat-insight/post/APT-targets-russia-belarus-zerot-plugx)


[^43]: Sogu


[^44]: [New DragonOK](http://researchcenter.paloaltonetworks.com/2015/04/unit-42-identifies-new-dragonok-backdoor-malware-deployed-against-japanese-targets/)


[^45]: DestroyRAT


[^46]: [apt41_mandiant](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^47]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)


[^48]: [EclecticIQ Mustang Panda PlugX](https://blog.eclecticiq.com/mustang-panda-apt-group-uses-european-commission-themed-lure-to-deliver-plugx-malware)


[^49]: [SecureWorks BRONZE UNION June 2017](https://www.secureworks.com/research/bronze-union)


