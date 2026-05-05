---
aliases: 
    - Andariel
    - Silent Chollima
    - PLUTONIUM
    - Onyx Sleet
mitre-attack: https://attack.mitre.org/groups/G0138
---

## G0138

[Andariel](https://attack.mitre.org/groups/G0138) is a North Korean state-sponsored threat group that has been active since at least 2009. [Andariel](https://attack.mitre.org/groups/G0138) has primarily focused its operations--which have included destructive attacks--against South Korean government agencies, military organizations, and a variety of domestic companies; they have also conducted cyber financial operations against ATMs, banks, and cryptocurrency exchanges. [Andariel](https://attack.mitre.org/groups/G0138)'s notable activity includes Operation Black Mine, Operation GoldenAxe, and Campaign Rifle.[^10] [^7] [^13] [^9] [^4] <br><br>[Andariel](https://attack.mitre.org/groups/G0138) is considered a sub-set of [Lazarus Group](https://attack.mitre.org/groups/G0032), and has been attributed to North Korea's Reconnaissance General Bureau.[^6] <br><br>North Korean group definitions are known to have significant overlap, and some security researchers report all North Korean state-sponsored cyber activity under the name [Lazarus Group](https://attack.mitre.org/groups/G0032) instead of tracking clusters or subgroups.

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Andariel](https://attack.mitre.org/groups/G0138) has used the `netstat -naop tcp` command to display TCP connections on a victim's machine.[^2]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Andariel](https://attack.mitre.org/groups/G0138) has exploited numerous ActiveX vulnerabilities, including zero-days.[^10] [^7] [^9]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Andariel](https://attack.mitre.org/groups/G0138) has collected large numbers of files from compromised network systems for later extraction.[^10]  |
| [[IP Addresses\|T1590.005]] | IP Addresses | [Andariel](https://attack.mitre.org/groups/G0138) has limited its watering hole attacks to specific IP address ranges.[^13]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Andariel](https://attack.mitre.org/groups/G0138) has used watering hole attacks, often with zero-day exploits, to gain initial access to victims within a specific IP range.[^13] [^9]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Andariel](https://attack.mitre.org/groups/G0138) has used `tasklist` to enumerate processes and find a specific string.[^2]  |
| [[Software\|T1592.002]] | Software | [Andariel](https://attack.mitre.org/groups/G0138) has inserted a malicious script within compromised websites to collect potential victim information such as browser type, system language, Flash Player version, and other data.[^9]  |
| [[Malware\|T1588.001]] | Malware | [Andariel](https://attack.mitre.org/groups/G0138) has used a variety of publicly-available remote access Trojans (RATs) for its operations.[^10]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Andariel](https://attack.mitre.org/groups/G0138) has attempted to lure victims into enabling malicious macros within email attachments.[^13]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Andariel](https://attack.mitre.org/groups/G0138) has conducted spearphishing campaigns that included malicious Word or Excel attachments.[^13] [^3]  |
| [[Steganography\|T1027.003]] | Steganography | [Andariel](https://attack.mitre.org/groups/G0138) has hidden malicious executables within PNG files.[^3] [^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Andariel](https://attack.mitre.org/groups/G0138) has downloaded additional tools and malware onto compromised hosts.[^13]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Rifdoor\|S0433]] | Rifdoor | [^13]  |
| [[gh0st RAT\|S0032]] | gh0st RAT | [^13]  |



## References

[^1]: PLUTONIUM


[^2]: [Kaspersky Andariel Ransomware June 2021](https://securelist.com/andariel-evolves-to-target-south-korea-with-ransomware/102811/)


[^3]: [MalwareBytes Lazarus-Andariel Conceals Code April 2021](https://blog.malwarebytes.com/threat-intelligence/2021/04/lazarus-apt-conceals-malicious-code-within-bmp-file-to-drop-its-rat/)


[^4]: [CrowdStrike Silent Chollima Adversary September 2021](https://adversary.crowdstrike.com/en-US/adversary/silent-chollima/)


[^5]: Andariel


[^6]: [Treasury North Korean Cyber Groups September 2019](https://home.treasury.gov/news/press-releases/sm774)


[^7]: [IssueMakersLab Andariel GoldenAxe May 2017](http://www.issuemakerslab.com/research3/)


[^8]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^9]: [TrendMicro New Andariel Tactics July 2018](https://www.trendmicro.com/en_us/research/18/g/new-andariel-reconnaissance-tactics-hint-at-next-targets.html)


[^10]: [FSI Andariel Campaign Rifle July 2017](https://fsiceat.tistory.com/2)


[^11]: Silent Chollima


[^12]: Onyx Sleet


[^13]: [AhnLab Andariel Subgroup of Lazarus June 2018](https://web.archive.org/web/20230213154832/http://download.ahnlab.com/global/brochure/%5BAnalysis%5DAndariel_Group.pdf)


