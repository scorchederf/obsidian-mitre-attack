---
aliases: 
    - Axiom
    - Group 72
mitre-attack: https://attack.mitre.org/groups/G0001
---

## G0001

[Axiom](https://attack.mitre.org/groups/G0001) is a suspected Chinese cyber espionage group that has targeted the aerospace, defense, government, manufacturing, and media sectors since at least 2008. Some reporting suggests a degree of overlap between [Axiom](https://attack.mitre.org/groups/G0001) and [Winnti Group](https://attack.mitre.org/groups/G0044) but the two groups appear to be distinct based on differences in reporting on TTPs and targeting.[^4] [^2] [^7] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Steganography\|T1001.002]] | Steganography | [Axiom](https://attack.mitre.org/groups/G0001) has used steganography to hide its C2 communications.[^6]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Axiom](https://attack.mitre.org/groups/G0001) has collected data from a compromised network.[^6]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Axiom](https://attack.mitre.org/groups/G0001) has compressed and encrypted data prior to exfiltration.[^6]  |
| [[Botnet\|T1584.005]] | Botnet | [Axiom](https://attack.mitre.org/groups/G0001) has used large groups of compromised machines for use as proxy nodes.[^6]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Axiom](https://attack.mitre.org/groups/G0001) has used watering hole attacks to gain access.[^3]  |
| [[Subvert Trust Controls\|T1553]] | Subvert Trust Controls | [Axiom](https://attack.mitre.org/groups/G0001) has used digital certificates to deliver malware.[^6]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Axiom](https://attack.mitre.org/groups/G0001) has used RDP during operations.[^6]  |
| [[DNS Server\|T1583.002]] | DNS Server | [Axiom](https://attack.mitre.org/groups/G0001) has acquired dynamic DNS services for use in the targeting of intended victims.[^6]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Axiom](https://attack.mitre.org/groups/G0001) has used exploits for multiple vulnerabilities including CVE-2014-0322, CVE-2012-4792, CVE-2012-1889, and CVE-2013-3893.[^3]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Axiom](https://attack.mitre.org/groups/G0001) has used previously compromised administrative accounts to escalate privileges.[^6]  |
| [[Virtual Private Server\|T1583.003]] | Virtual Private Server | [Axiom](https://attack.mitre.org/groups/G0001) has used VPS hosting providers in targeting of intended victims.[^6]  |
| [[RDP Hijacking\|T1563.002]] | RDP Hijacking | [Axiom](https://attack.mitre.org/groups/G0001) has targeted victims with remote administration tools including RDP.[^6]  |
| [[Accessibility Features\|T1546.008]] | Accessibility Features | [Axiom](https://attack.mitre.org/groups/G0001) actors have been known to use the Sticky Keys replacement within RDP sessions to obtain persistence.[^6]  |
| [[Phishing\|T1566]] | Phishing | [Axiom](https://attack.mitre.org/groups/G0001) has used spear phishing to initially compromise victims.[^3] [^6]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Axiom](https://attack.mitre.org/groups/G0001) has been observed using SQL injection to gain access to systems.[^6] [^3]  |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | [Axiom](https://attack.mitre.org/groups/G0001) has been known to dump credentials.[^6]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[PlugX\|S0013]] | PlugX | [^3] [^6]  |
| [[Hydraq\|S0203]] | Hydraq | [^6] [^3]  |
| [[gh0st RAT\|S0032]] | gh0st RAT | [^3] [^6]  |
| [[Derusbi\|S0021]] | Derusbi | [^6] [^3]  |
| [[Hikit\|S0009]] | Hikit | [^6] [^3]  |
| [[PoisonIvy\|S0012]] | PoisonIvy | [^3] [^6]  |
| [[ZxShell\|S0412]] | ZxShell | [^5] [^3]  |
| [[Zox\|S0672]] | Zox | [^6]  |



## References

[^1]: Group 72


[^2]: [Kaspersky Winnti June 2015](https://securelist.com/games-are-over/70991/)


[^3]: [Cisco Group 72](http://blogs.cisco.com/security/talos/threat-spotlight-group-72)


[^4]: [Kaspersky Winnti April 2013](https://securelist.com/winnti-more-than-just-a-game/37029/)


[^5]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)


[^6]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)


[^7]: [Novetta Winnti April 2015](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)


[^8]: Axiom


