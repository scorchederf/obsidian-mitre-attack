---
aliases: 
    - S0141
    
mitre-attack: https://attack.mitre.org/software/S0141
---

## S0141

[Winnti for Windows](https://attack.mitre.org/software/S0141) is a modular remote access Trojan (RAT) that has been used likely by multiple groups to carry out intrusions in various regions since at least 2010, including by one group referred to as the same name, [Winnti Group](https://attack.mitre.org/groups/G0044).[^2] [^3] [^4] [^6] . The Linux variant is tracked separately under [Winnti for Linux](https://attack.mitre.org/software/S0430).[^7] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Native API\|T1106]] | Native API | [Winnti for Windows](https://attack.mitre.org/software/S0141) can use Native API to create a new process and to start services.[^4]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Winnti for Windows](https://attack.mitre.org/software/S0141) sets its DLL file as a new service in the Registry to establish persistence.[^3]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Winnti for Windows](https://attack.mitre.org/software/S0141) can XOR encrypt C2 traffic.[^4]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Winnti for Windows](https://attack.mitre.org/software/S0141) can check for the presence of specific files prior to moving to the next phase of execution.[^4]  |
| [[External Proxy\|T1090.002]] | External Proxy | The [Winnti for Windows](https://attack.mitre.org/software/S0141) HTTP/S C2 mode can make use of an external proxy.[^4]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Winnti for Windows](https://attack.mitre.org/software/S0141) can communicate using custom TCP.[^4]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Winnti for Windows](https://attack.mitre.org/software/S0141) can check if the explorer.exe process is responsible for calling its install function.[^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Winnti for Windows](https://attack.mitre.org/software/S0141) can add a service named `wind0ws` to the Registry to achieve persistence after reboot.[^4]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | The [Winnti for Windows](https://attack.mitre.org/software/S0141) HTTP/S C2 mode can make use of a local proxy.[^4]  |
| [[Rundll32\|T1218.011]] | Rundll32 | The [Winnti for Windows](https://attack.mitre.org/software/S0141) installer loads a DLL using rundll32.[^3] [^4]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Winnti for Windows](https://attack.mitre.org/software/S0141) can use a variant of the sysprep UAC bypass.[^4]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Winnti for Windows](https://attack.mitre.org/software/S0141) can determine if the OS on a compromised host is newer than Windows XP.[^4]  |
| [[Compression\|T1027.015]] | Compression | [Winnti for Windows](https://attack.mitre.org/software/S0141) has the ability to encrypt and compress its payload.[^4]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Winnti for Windows](https://attack.mitre.org/software/S0141) can run as a service using svchost.exe.[^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | The [Winnti for Windows](https://attack.mitre.org/software/S0141) dropper can place malicious payloads on targeted systems.[^4]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Winnti for Windows](https://attack.mitre.org/software/S0141) can delete the DLLs for its various components from a compromised host.[^4]  |
| [[Timestomp\|T1070.006]] | Timestomp | [Winnti for Windows](https://attack.mitre.org/software/S0141) can set the timestamps for its worker and service components to match that of cmd.exe.[^4]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Winnti for Windows](https://attack.mitre.org/software/S0141) has the ability to encrypt and compress its payload.[^4]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | The [Winnti for Windows](https://attack.mitre.org/software/S0141) dropper can decrypt and decompresses a data blob.[^4]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Winnti for Windows](https://attack.mitre.org/software/S0141) has the ability to use encapsulated HTTP/S in C2 communications.[^4]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | A [Winnti for Windows](https://attack.mitre.org/software/S0141) implant file was named ASPNET_FILTER.DLL, mimicking the legitimate ASP.NET ISAPI filter DLL with the same name.[^3]  |
| [[Environmental Keying\|T1480.001]] | Environmental Keying | The [Winnti for Windows](https://attack.mitre.org/software/S0141) dropper component can verify the existence of a single command line parameter and either terminate if it is not found or later use it as a decryption key.[^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Aquatic Panda\|G0143]] | Aquatic Panda |
| [[Winnti Group\|G0044]] | Winnti Group |



## References

[^1]: [Kaspersky Winnti June 2015](https://securelist.com/games-are-over/70991/)


[^2]: [Kaspersky Winnti April 2013](https://securelist.com/winnti-more-than-just-a-game/37029/)


[^3]: [Microsoft Winnti Jan 2017](https://blogs.technet.microsoft.com/mmpc/2017/01/25/detecting-threat-actors-in-recent-german-industrial-attacks-with-windows-defender-atp/)


[^4]: [Novetta Winnti April 2015](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)


[^5]: [Crowdstrike HuntReport 2022](https://go.crowdstrike.com/rs/281-OBQ-266/images/2022OverWatchThreatHuntingReport.pdf)


[^6]: [401 TRG Winnti Umbrella May 2018](https://401trg.github.io/pages/burning-umbrella.html)


[^7]: [Chronicle Winnti for Linux May 2019](https://medium.com/chronicle-blog/winnti-more-than-just-windows-and-gates-e4f03436031a)


