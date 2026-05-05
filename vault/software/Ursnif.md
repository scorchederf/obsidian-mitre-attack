---
aliases: 
    - S0386
    
mitre-attack: https://attack.mitre.org/software/S0386
---

## S0386

[Ursnif](https://attack.mitre.org/software/S0386) is a banking trojan and variant of the Gozi malware observed being spread through various automated exploit kits, [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001)s, and malicious links.[^8] [^3]  [Ursnif](https://attack.mitre.org/software/S0386) is associated primarily with data theft, but variants also include components (backdoors, spyware, file injectors, etc.) capable of a wide variety of behaviors.[^11] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Ursnif](https://attack.mitre.org/software/S0386) has gathered information about running services.[^11]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Ursnif](https://attack.mitre.org/software/S0386) has used Registry Run keys to establish automatic execution at system startup.[^2] [^15]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Ursnif](https://attack.mitre.org/software/S0386) has dropped payload and configuration files to disk. [Ursnif](https://attack.mitre.org/software/S0386) has also been used to download and execute additional payloads.[^2] [^15]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Ursnif](https://attack.mitre.org/software/S0386) has used an XOR-based algorithm to encrypt Tor clients dropped to disk.[^3] 	[Ursnif](https://attack.mitre.org/software/S0386) droppers have also been delivered as password-protected zip files that execute base64 encoded [PowerShell](https://attack.mitre.org/techniques/T1059/001) commands.[^16]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [Ursnif](https://attack.mitre.org/software/S0386) has used [Tor](https://attack.mitre.org/software/S0183) for C2.[^8] [^3]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Ursnif](https://attack.mitre.org/software/S0386) has used tmp files to stage gathered information.[^11]  |
| [[Native API\|T1106]] | Native API | [Ursnif](https://attack.mitre.org/software/S0386) has used `CreateProcessW` to create child processes.[^14]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [Ursnif](https://attack.mitre.org/software/S0386) has used a 30 minute delay after execution to evade sandbox monitoring tools.[^4]  |
| [[Component Object Model\|T1559.001]] | Component Object Model | [Ursnif](https://attack.mitre.org/software/S0386) droppers have used COM objects to execute the malware's full executable payload.[^16]  |
| [[Credential API Hooking\|T1056.004]] | Credential API Hooking | [Ursnif](https://attack.mitre.org/software/S0386) has hooked APIs to perform a wide variety of information theft, such as monitoring traffic from browsers.[^11]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Ursnif](https://attack.mitre.org/software/S0386) has gathered information about running processes.[^11] [^15]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Ursnif](https://attack.mitre.org/software/S0386) has used HTTP POSTs to exfil gathered information.[^11] [^14] [^3]  |
| [[Data Encoding\|T1132]] | Data Encoding | [Ursnif](https://attack.mitre.org/software/S0386) has used encoded data in HTTP URLs for C2.[^3] 	 |
| [[Thread Local Storage\|T1055.005]] | Thread Local Storage | [Ursnif](https://attack.mitre.org/software/S0386) has injected code into target processes via thread local storage callbacks.[^11] [^2] [^14]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Ursnif](https://attack.mitre.org/software/S0386) has used crypto key information stored in the Registry to decrypt Tor clients dropped to disk.[^3]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Ursnif](https://attack.mitre.org/software/S0386) has used strings from legitimate system files and existing folders for its file, folder, and Registry entry names.[^11]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Ursnif](https://attack.mitre.org/software/S0386) has collected files from victim machines, including certificates and cookies.[^15]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Ursnif](https://attack.mitre.org/software/S0386) droppers execute base64 encoded [PowerShell](https://attack.mitre.org/techniques/T1059/001) commands.[^16]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Ursnif](https://attack.mitre.org/software/S0386) has used hooked APIs to take screenshots.[^11] [^15]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Ursnif](https://attack.mitre.org/software/S0386) has registered itself as a system service in the Registry for automatic execution at system startup.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Ursnif](https://attack.mitre.org/software/S0386) droppers have used PowerShell in download cradles to download and execute the malware's full executable payload.[^16]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Ursnif](https://attack.mitre.org/software/S0386) has used HTTPS for C2.[^11] [^14] [^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Ursnif](https://attack.mitre.org/software/S0386) has deleted data staged in tmp files after exfiltration.[^11]  |
| [[Query Registry\|T1012]] | Query Registry | [Ursnif](https://attack.mitre.org/software/S0386) has used [Reg](https://attack.mitre.org/software/S0075) to query the Registry for installed programs.[^11] [^15]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Ursnif](https://attack.mitre.org/software/S0386) has used Registry modifications as part of its installation routine.[^15] [^3]  |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [Ursnif](https://attack.mitre.org/software/S0386) has used a DGA to generate domain names for C2.[^3]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Ursnif](https://attack.mitre.org/software/S0386) droppers have used VBA macros to download and execute the malware's full executable payload.[^16]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Ursnif](https://attack.mitre.org/software/S0386) has used [Systeminfo](https://attack.mitre.org/software/S0096) to gather system information.[^11]  |
| [[Proxy\|T1090]] | Proxy | [Ursnif](https://attack.mitre.org/software/S0386) has used a peer-to-peer (P2P) network for C2.[^8] [^3]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Ursnif](https://attack.mitre.org/software/S0386) droppers have used WMI classes to execute [PowerShell](https://attack.mitre.org/techniques/T1059/001) commands.[^16]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Ursnif](https://attack.mitre.org/software/S0386) has used process hollowing to inject into child processes.[^14]  |
| [[Browser Session Hijacking\|T1185]] | Browser Session Hijacking | [Ursnif](https://attack.mitre.org/software/S0386) has injected HTML codes into banking sites to steal sensitive online banking information (ex: usernames and passwords).[^15]  |
| [[Taint Shared Content\|T1080]] | Taint Shared Content | [Ursnif](https://attack.mitre.org/software/S0386) has copied itself to and infected files in network drives for propagation.[^11] [^4]  |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [Ursnif](https://attack.mitre.org/software/S0386) has copied itself to and infected removable drives for propagation.[^11] [^4]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [Ursnif](https://attack.mitre.org/software/S0386) droppers have used COM properties to execute malware in hidden windows.[^16]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA551\|G0127]] | TA551 |



## References

[^1]: [Unit 42 Valak July 2020](https://unit42.paloaltonetworks.com/valak-evolution/)


[^2]: [TrendMicro PE_URSNIF.A2](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/PE_URSNIF.A2?_ga=2.131425807.1462021705.1559742358-1202584019.1549394279)


[^3]: [ProofPoint Ursnif Aug 2016](https://www.proofpoint.com/us/threat-insight/post/ursnif-variant-dreambot-adds-tor-functionality)


[^4]: [TrendMicro Ursnif File Dec 2014](https://blog.trendmicro.com/trendlabs-security-intelligence/info-stealing-file-infector-hits-us-uk/)


[^5]: Dreambot


[^6]: PE_URSNIF


[^7]: Ursnif


[^8]: [NJCCIC Ursnif Sept 2016](https://www.cyber.nj.gov/threat-landscape/malware/trojans/ursnif)


[^9]: [Cybereason Valak May 2020](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)


[^10]: [Secureworks GOLD CABIN](https://www.secureworks.com/research/threat-profiles/gold-cabin)


[^11]: [TrendMicro Ursnif Mar 2015](https://web.archive.org/web/20210719165945/https://www.trendmicro.com/en_us/research/15/c/ursnif-the-multifaceted-malware.html?_ga=2.165628854.808042651.1508120821-744063452.1505819992)


[^12]: [Unit 42 TA551 Jan 2021](https://unit42.paloaltonetworks.com/ta551-shathak-icedid/)


[^13]: Gozi-ISFB


[^14]: [FireEye Ursnif Nov 2017](https://www.fireeye.com/blog/threat-research/2017/11/ursnif-variant-malicious-tls-callback-technique.html)


[^15]: [TrendMicro BKDR_URSNIF.SM](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/BKDR_URSNIF.SM?_ga=2.129468940.1462021705.1559742358-1202584019.1549394279)


[^16]: [Bromium Ursnif Mar 2017](https://www.bromium.com/how-ursnif-evades-detection/)


