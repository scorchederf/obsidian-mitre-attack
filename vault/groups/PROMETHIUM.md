---
aliases: 
    - PROMETHIUM
    - StrongPity
mitre-attack: https://attack.mitre.org/groups/G0056
---

## G0056

[PROMETHIUM](https://attack.mitre.org/groups/G0056) is an activity group focused on espionage that has been active since at least 2012. The group has conducted operations globally with a heavy emphasis on Turkish targets. [PROMETHIUM](https://attack.mitre.org/groups/G0056) has demonstrated similarity to another activity group called [NEODYMIUM](https://attack.mitre.org/groups/G0055) due to overlapping victim and campaign characteristics.[^3] [^2] [^4] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Malicious File\|T1204.002]] | Malicious File | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has attempted to get users to execute compromised installation files for legitimate software including compression applications, security software, browsers, file recovery applications, and other tools and utilities.[^4] [^1]  |
| [[Code Signing Certificates\|T1587.002]] | Code Signing Certificates | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has created self-signed certificates to sign malicious installers.[^1]  |
| [[Local Accounts\|T1078.003]] | Local Accounts | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has created admin accounts on a compromised host.[^1]  |
| [[Digital Certificates\|T1587.003]] | Digital Certificates | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has created self-signed digital certificates for use in HTTPS C2 traffic.[^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has used Registry run keys to establish persistence.[^4]  |
| [[Windows Service\|T1543.003]] | Windows Service | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has created new services and modified existing services for persistence.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has disguised malicious installer files by bundling them with legitimate software installers.[^4] [^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has named services to appear legitimate.[^4] [^1]  |
| [[Code Signing\|T1553.002]] | Code Signing | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has signed code with self-signed certificates.[^1]  |
| [[Port Knocking\|T1205.001]] | Port Knocking | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has used a script that configures the knockd service and firewall to only accept C2 connections from systems that use a specified sequence of knock ports.[^1]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has used watering hole attacks to deliver malicious versions of legitimate installers.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[StrongPity\|S0491]] | StrongPity | [^1] [^4]  |
| [[Truvasys\|S0178]] | Truvasys | [^3] [^2]  |



## References

[^1]: [Bitdefender StrongPity June 2020](https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf)


[^2]: [Microsoft SIR Vol 21](http://download.microsoft.com/download/E/B/0/EB0F50CC-989C-4B66-B7F6-68CD3DC90DE3/Microsoft_Security_Intelligence_Report_Volume_21_English.pdf)


[^3]: [Microsoft NEODYMIUM Dec 2016](https://blogs.technet.microsoft.com/mmpc/2016/12/14/twin-zero-day-attacks-promethium-and-neodymium-target-individuals-in-europe/)


[^4]: [Talos Promethium June 2020](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)


[^5]: StrongPity


[^6]: PROMETHIUM


