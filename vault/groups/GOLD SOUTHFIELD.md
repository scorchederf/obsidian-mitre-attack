---
aliases: 
    - GOLD SOUTHFIELD
    - Pinchy Spider
mitre-attack: https://attack.mitre.org/groups/G0115
---

## G0115

[GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) is a financially motivated threat group active since at least 2018 that operates the [REvil](https://attack.mitre.org/software/S0496) Ransomware-as-a Service (RaaS). [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) provides backend infrastructure for affiliates recruited on underground forums to perpetrate high value deployments. By early 2020, [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) started capitalizing on the new trend of stealing data and further extorting the victim to pay for their data to not get publicly leaked.[^3] [^1] [^7] [^6] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Trusted Relationship\|T1199]] | Trusted Relationship | [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) has breached Managed Service Providers (MSP's) to deliver malware to MSP customers.[^3]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) has exploited Oracle WebLogic vulnerabilities for initial compromise.[^3]  |
| [[Screen Capture\|T1113]] | Screen Capture | [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) has used the remote monitoring and management tool ConnectWise to obtain screen captures from victim's machines.[^5]  |
| [[Remote Access Tools\|T1219]] | Remote Access Tools | [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) has used the cloud-based remote management and monitoring tool "ConnectWise Control" to deploy [REvil](https://attack.mitre.org/software/S0496).[^5]  |
| [[Compromise Software Supply Chain\|T1195.002]] | Compromise Software Supply Chain | [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) has distributed ransomware by backdooring software installers via a strategic web compromise of the site hosting Italian WinRAR.[^3] [^1] [^7]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) has executed base64 encoded PowerShell scripts on compromised hosts.[^5]  |
| [[External Remote Services\|T1133]] | External Remote Services | [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) has used publicly-accessible RDP and remote management and monitoring (RMM) servers to gain access to victim machines.[^3] 	 |
| [[PowerShell\|T1059.001]] | PowerShell | [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) has staged and executed PowerShell scripts on compromised hosts.[^5]  |
| [[Phishing\|T1566]] | Phishing | [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) has conducted malicious spam (malspam) campaigns to gain access to victim's machines.[^3]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[ConnectWise\|S0591]] | ConnectWise | [^4] [^5]  |
| [[REvil\|S0496]] | REvil | [^3] [^1]  |



## References

[^1]: [Secureworks GandCrab and REvil September 2019](https://www.secureworks.com/blog/revil-the-gandcrab-connection)


[^2]: Pinchy Spider


[^3]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)


[^4]: [Anomali Static Kitten February 2021](https://www.anomali.com/blog/probable-iranian-cyber-actors-static-kitten-conducting-cyberespionage-campaign-targeting-uae-and-kuwait-government-agencies)


[^5]: [Tetra Defense Sodinokibi March 2020](https://web.archive.org/web/20210414101816/https://tetradefense.com/incident-response-services/cause-and-effect-sodinokibi-ransomware-analysis/)


[^6]: [CrowdStrike Evolution of Pinchy Spider July 2021](https://www.crowdstrike.com/blog/the-evolution-of-revil-ransomware-and-pinchy-spider/)


[^7]: [Secureworks GOLD SOUTHFIELD](https://www.secureworks.com/research/threat-profiles/gold-southfield)


