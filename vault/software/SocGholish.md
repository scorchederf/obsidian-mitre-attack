---
aliases: 
    - S1124
    
mitre-attack: https://attack.mitre.org/software/S1124
---

## S1124

[SocGholish](https://attack.mitre.org/software/S1124) is a JavaScript-based loader malware that has been used since at least 2017. It has been observed in use against multiple sectors globally for initial access, primarily through drive-by-downloads masquerading as software updates. SocGholish is operated by [Mustard Tempest](https://attack.mitre.org/groups/G1020) and its access has been sold to groups including [Indrik Spider](https://attack.mitre.org/groups/G0119) for downloading secondary RAT and ransomware payloads.[^5] [^6] [^1] [^3]  

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SocGholish](https://attack.mitre.org/software/S1124) has the ability to enumerate system information including the victim computer name.[^6] [^1] [^3]  |
| [[System Location Discovery\|T1614]] | System Location Discovery | [SocGholish](https://attack.mitre.org/software/S1124) can use IP-based geolocation to limit infections to victims in North America, Europe, and a small number of Asian-Pacific nations.[^3]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [SocGholish](https://attack.mitre.org/software/S1124) has used WMI calls for script execution and system profiling.[^6]   |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SocGholish](https://attack.mitre.org/software/S1124) can download additional malware to infected hosts.[^1] [^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [SocGholish](https://attack.mitre.org/software/S1124) has single or double Base-64 encoded references to its second-stage server URLs.[^5]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [SocGholish](https://attack.mitre.org/software/S1124) can profile compromised systems to identify domain trust relationships.[^6] [^1]  |
| [[JavaScript\|T1059.007]] | JavaScript | The [SocGholish](https://attack.mitre.org/software/S1124) payload is executed as JavaScript.[^6] [^5] [^1] [^3]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [SocGholish](https://attack.mitre.org/software/S1124) has been named `AutoUpdater.js` to mimic legitimate update files.[^6]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [SocGholish](https://attack.mitre.org/software/S1124) has been spread via emails containing malicious links.[^6]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [SocGholish](https://attack.mitre.org/software/S1124) can use `whoami` to obtain the username from a compromised host.[^6] [^1] [^3]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [SocGholish](https://attack.mitre.org/software/S1124) has been distributed through compromised websites with malicious content often masquerading as browser updates.[^6]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [SocGholish](https://attack.mitre.org/software/S1124) has lured victims into interacting with malicious links on compromised websites for execution.[^6]  |
| [[Software Discovery\|T1518]] | Software Discovery | [SocGholish](https://attack.mitre.org/software/S1124) can identify the victim's browser in order to serve the correct fake update page.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [SocGholish](https://attack.mitre.org/software/S1124) can list processes on targeted hosts.[^3]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [SocGholish](https://attack.mitre.org/software/S1124) can send output from `whoami` to a local temp file using the naming convention `rad<5-hex-chars>.tmp`.[^1]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [SocGholish](https://attack.mitre.org/software/S1124) can exfiltrate data directly to its C2 domain via HTTP.[^1]  |
| [[Web Service\|T1102]] | Web Service | [SocGholish](https://attack.mitre.org/software/S1124) has used Amazon Web Services to host second-stage servers.[^5]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [SocGholish](https://attack.mitre.org/software/S1124) has the ability to enumerate the domain name of a victim, as well as if the host is a member of an Active Directory domain.[^6] [^1] [^3]  |
| [[Compression\|T1027.015]] | Compression | The [SocGholish](https://attack.mitre.org/software/S1124) JavaScript payload has been delivered within a compressed ZIP archive.[^1] [^3]   |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Mustard Tempest\|G1020]] | Mustard Tempest |



## References

[^1]: [Red Canary SocGholish March 2024](https://redcanary.com/threat-detection-report/threats/socgholish/)


[^2]: FakeUpdates


[^3]: [Secureworks Gold Prelude Profile](https://www.secureworks.com/research/threat-profiles/gold-prelude)


[^4]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^5]: [SentinelOne SocGholish Infrastructure November 2022](https://www.sentinelone.com/labs/socgholish-diversifies-and-expands-its-malware-staging-infrastructure-to-counter-defenders/)


[^6]: [SocGholish-update](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)


