---
aliases: 
    - S0596
    
mitre-attack: https://attack.mitre.org/software/S0596
---

## S0596

[ShadowPad](https://attack.mitre.org/software/S0596) is a modular backdoor that was first identified in a supply chain compromise of the NetSarang software in mid-July 2017. The malware was originally thought to be exclusively used by [APT41](https://attack.mitre.org/groups/G0096), but has since been observed to be used by various Chinese threat activity groups. [^10] [^3] [^2]  

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [ShadowPad](https://attack.mitre.org/software/S0596) has collected the username of the victim system.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [ShadowPad](https://attack.mitre.org/software/S0596) can modify the Registry to store and maintain a configuration block and virtual file system.[^2] [^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [ShadowPad](https://attack.mitre.org/software/S0596) has collected the current date and time of the victim system.[^2]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [ShadowPad](https://attack.mitre.org/software/S0596) has deleted arbitrary Registry values.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [ShadowPad](https://attack.mitre.org/software/S0596) has decrypted a binary blob to start execution.[^2]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [ShadowPad](https://attack.mitre.org/software/S0596) maintains a configuration block and virtual file system in the Registry.[^2] [^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [ShadowPad](https://attack.mitre.org/software/S0596) has collected the domain name of the victim system.[^2]  |
| [[Scheduled Transfer\|T1029]] | Scheduled Transfer | [ShadowPad](https://attack.mitre.org/software/S0596) has sent data back to C2 every 8 hours.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [ShadowPad](https://attack.mitre.org/software/S0596) has collected the PID of a malicious process.[^2]  |
| [[DNS\|T1071.004]] | DNS | [ShadowPad](https://attack.mitre.org/software/S0596) has used DNS tunneling for C2 communications.[^2]  |
| [[Non-Standard Encoding\|T1132.002]] | Non-Standard Encoding | [ShadowPad](https://attack.mitre.org/software/S0596) has encoded data as readable Latin characters.[^3]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [ShadowPad](https://attack.mitre.org/software/S0596) has used FTP for C2 communications.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [ShadowPad](https://attack.mitre.org/software/S0596) has used UDP for C2 communications.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [ShadowPad](https://attack.mitre.org/software/S0596) has encrypted its payload, a virtual file system, and various files.[^3] [^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [ShadowPad](https://attack.mitre.org/software/S0596) communicates over HTTP to retrieve a string that is decoded into a C2 server URL.[^2]  |
| [[Process Injection\|T1055]] | Process Injection | [ShadowPad](https://attack.mitre.org/software/S0596) has injected an install module into a newly created process.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [ShadowPad](https://attack.mitre.org/software/S0596) has discovered system information including memory status, CPU frequency, and OS versions.[^2]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [ShadowPad](https://attack.mitre.org/software/S0596) has discovered system information including volume serial numbers.[^2]  |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [ShadowPad](https://attack.mitre.org/software/S0596) uses a DGA that is based on the day of the month for C2 servers.[^3] [^2] [^5]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [ShadowPad](https://attack.mitre.org/software/S0596) has downloaded code from a C2 server.[^3]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [ShadowPad](https://attack.mitre.org/software/S0596) has injected a DLL into svchost.exe.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Mustang Panda\|G0129]] | Mustang Panda |
| [[RedEcho\|G1042]] | RedEcho |
| [[Tropic Trooper\|G0081]] | Tropic Trooper |
| [[Tonto Team\|G0131]] | Tonto Team |
| [[APT41\|G0096]] | APT41 |
| [[Aquatic Panda\|G0143]] | Aquatic Panda |
| [[Earth Lusca\|G1006]] | Earth Lusca |
| [[BRONZE BUTLER\|G0060]] | BRONZE BUTLER |



## References

[^1]: [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)


[^2]: [Kaspersky ShadowPad Aug 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)


[^3]: [Securelist ShadowPad Aug 2017](https://securelist.com/shadowpad-in-corporate-networks/81432/)


[^4]: [RecordedFuture RedEcho 2021](https://go.recordedfuture.com/hubfs/reports/cta-2021-0228.pdf)


[^5]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^6]: [Crowdstrike HuntReport 2022](https://go.crowdstrike.com/rs/281-OBQ-266/images/2022OverWatchThreatHuntingReport.pdf)


[^7]: POISONPLUG.SHADOW


[^8]: [RecordedFuture RedEcho 2022](https://go.recordedfuture.com/hubfs/reports/ta-2022-0406.pdf)


[^9]: [Kaspersky CactusPete Aug 2020](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)


[^10]: [Recorded Future RedEcho Feb 2021](https://go.recordedfuture.com/hubfs/reports/cta-2021-0228.pdf)


[^11]: [Palo Alto Unit42 STATELY TAURUS TONESHELL September 2023](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)


