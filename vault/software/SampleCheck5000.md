---
aliases: 
    - S1168
    
mitre-attack: https://attack.mitre.org/software/S1168
---

## S1168

[SampleCheck5000](https://attack.mitre.org/software/S1168) is a downloader with multiple variants that was used by [OilRig](https://attack.mitre.org/groups/G0049) including during the [Outer Space](https://attack.mitre.org/campaigns/C0042) campaign to download and execute additional payloads. [^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [SampleCheck5000](https://attack.mitre.org/software/S1168) can create unique victim identifiers by using the compromised system’s volume ID.[^2]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [SampleCheck5000](https://attack.mitre.org/software/S1168) can use the Microsoft Office Exchange Web Services API to access an actor-controlled account and retrieve C2 commands and payloads placed in Draft messages.[^1] [^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SampleCheck5000](https://attack.mitre.org/software/S1168) can download additional payloads to compromised hosts.[^1] [^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [SampleCheck5000](https://attack.mitre.org/software/S1168) can decode and decrypt command line strings and files received through C2.[^1] [^2]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [SampleCheck5000](https://attack.mitre.org/software/S1168) can gzip compress files uploaded to a shared mailbox used for C2 and exfiltration.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [SampleCheck5000](https://attack.mitre.org/software/S1168) can call cmd.exe to execute C2 command line strings.[^1] [^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [SampleCheck5000](https://attack.mitre.org/software/S1168) can use the Exchange Web Services API for C2 communication.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SampleCheck5000](https://attack.mitre.org/software/S1168) can create unique victim identifiers by using the compromised system’s computer name.[^2]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [SampleCheck5000](https://attack.mitre.org/software/S1168) can log the output from C2 commands in an encrypted and compressed format on disk prior to exfiltration.[^2]  |
| [[Exfiltration Over Web Service\|T1567]] | Exfiltration Over Web Service | [SampleCheck5000](https://attack.mitre.org/software/S1168) can use the Microsoft Office Exchange Web Services API to access an actor-controlled account and retrieve files for exfiltration.[^1] [^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[OilRig\|G0049]] | OilRig |



## References

[^1]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)


[^2]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)


[^3]: SC5k


