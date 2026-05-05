---
aliases: 
    - BITTER
    - T-APT-17
mitre-attack: https://attack.mitre.org/groups/G1002
---

## G1002

[BITTER](https://attack.mitre.org/groups/G1002) is a suspected South Asian cyber espionage threat group that has been active since at least 2013. [BITTER](https://attack.mitre.org/groups/G1002) has targeted government, energy, and engineering organizations in Pakistan, China, Bangladesh, and Saudi Arabia.[^1] [^3] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BITTER](https://attack.mitre.org/groups/G1002) has downloaded additional malware and tools onto a compromised host.[^1] [^3]   |
| [[Web Protocols\|T1071.001]] | Web Protocols | [BITTER](https://attack.mitre.org/groups/G1002) has used HTTP POST requests for C2.[^1] [^3]  |
| [[Tool\|T1588.002]] | Tool | [BITTER](https://attack.mitre.org/groups/G1002) has obtained tools such as PuTTY for use in their operations.[^3]  |
| [[Dynamic Resolution\|T1568]] | Dynamic Resolution | [BITTER](https://attack.mitre.org/groups/G1002) has used DDNS for C2 communications.[^3]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [BITTER](https://attack.mitre.org/groups/G1002) has sent spearphishing emails with a malicious RTF document or Excel spreadsheet.[^1] [^3]  |
| [[Malicious File\|T1204.002]] | Malicious File | [BITTER](https://attack.mitre.org/groups/G1002) has attempted to lure victims into opening malicious attachments delivered via spearphishing.[^1] [^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [BITTER](https://attack.mitre.org/groups/G1002) has used a RAR SFX dropper to deliver malware.[^3]  |
| [[Encrypted Channel\|T1573]] | Encrypted Channel | [BITTER](https://attack.mitre.org/groups/G1002) has encrypted their C2 communications.[^3]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [BITTER](https://attack.mitre.org/groups/G1002) has exploited CVE-2021-1732 for privilege escalation.[^4] [^2]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [BITTER](https://attack.mitre.org/groups/G1002) has disguised malware as a Windows Security update service.[^1]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [BITTER](https://attack.mitre.org/groups/G1002) has registered domains to stage payloads.[^3]  |
| [[Dynamic Data Exchange\|T1559.002]] | Dynamic Data Exchange | [BITTER](https://attack.mitre.org/groups/G1002) has executed OLE objects using Microsoft Equation Editor to download and run malicious payloads.[^1]   |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [BITTER](https://attack.mitre.org/groups/G1002) has exploited Microsoft Office vulnerabilities CVE-2012-0158, CVE-2017-11882, CVE-2018-0798, and CVE-2018-0802.[^1] [^3]  |
| [[Domains\|T1583.001]] | Domains | [BITTER](https://attack.mitre.org/groups/G1002) has registered a variety of domains to host malicious payloads and for C2.[^3]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [BITTER](https://attack.mitre.org/groups/G1002) has used scheduled tasks for persistence and execution.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [BITTER](https://attack.mitre.org/groups/G1002) has used TCP for C2 communications.[^3]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[ZxxZ\|S1013]] | ZxxZ | [^1]  |



## References

[^1]: [Cisco Talos Bitter Bangladesh May 2022](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)


[^2]: [Microsoft CVE-2021-1732 Feb 2021](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-1732)


[^3]: [Forcepoint BITTER Pakistan Oct 2016](https://www.forcepoint.com/blog/x-labs/bitter-targeted-attack-against-pakistan)


[^4]: [DBAPPSecurity BITTER zero-day Feb 2021](https://ti.dbappsecurity.com.cn/blog/articles/2021/02/10/windows-kernel-zero-day-exploit-is-used-by-bitter-apt-in-targeted-attack/)


[^5]: T-APT-17


