---
aliases: 
    - Tonto Team
    - Earth Akhlut
    - BRONZE HUNTLEY
    - CactusPete
    - Karma Panda
mitre-attack: https://attack.mitre.org/groups/G0131
---

## G0131

[Tonto Team](https://attack.mitre.org/groups/G0131) is a suspected Chinese state-sponsored cyber espionage threat group that has primarily targeted South Korea, Japan, Taiwan, and the United States since at least 2009; by 2020 they expanded operations to include other Asian as well as Eastern European countries. [Tonto Team](https://attack.mitre.org/groups/G0131) has targeted government, military, energy, mining, financial, education, healthcare, and technology organizations, including through the Heartbeat Campaign (2009-2012) and Operation Bitter Biscuit (2017).[^11] [^1] [^10] [^3] [^13] [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Tonto Team](https://attack.mitre.org/groups/G0131) has used tools such as [NBTscan](https://attack.mitre.org/software/S0590) to enumerate network shares.[^15]  |
| [[DLL\|T1574.001]] | DLL | [Tonto Team](https://attack.mitre.org/groups/G0131) abuses a legitimate and signed Microsoft executable to launch a malicious DLL.[^1]  |
| [[External Proxy\|T1090.002]] | External Proxy | [Tonto Team](https://attack.mitre.org/groups/G0131) has routed their traffic through an external server in order to obfuscate their location.[^15]  |
| [[Python\|T1059.006]] | Python | [Tonto Team](https://attack.mitre.org/groups/G0131) has used Python-based tools for execution.[^15]   |
| [[Local Groups\|T1069.001]] | Local Groups | [Tonto Team](https://attack.mitre.org/groups/G0131) has used the `ShowLocalGroupDetails` command to identify administrator, user, and guest accounts on a compromised host.[^15]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Tonto Team](https://attack.mitre.org/groups/G0131) has used keylogging tools in their operations.[^15]  |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | [Tonto Team](https://attack.mitre.org/groups/G0131) has used a variety of credential dumping tools.[^15]   |
| [[Web Shell\|T1505.003]] | Web Shell | [Tonto Team](https://attack.mitre.org/groups/G0131) has used a first stage web shell after compromising a vulnerable Exchange server.[^1]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Tonto Team](https://attack.mitre.org/groups/G0131) has exploited Microsoft vulnerabilities, including CVE-2018-0798, CVE-2018-8174, CVE-2018-0802, CVE-2017-11882, CVE-2019-9489 CVE-2020-8468, and CVE-2018-0798 to enable execution of their delivered malicious payloads.[^11] [^15] [^9] [^2]   |
| [[Malicious File\|T1204.002]] | Malicious File | [Tonto Team](https://attack.mitre.org/groups/G0131) has relied on user interaction to open their malicious RTF documents.[^15] [^9]   |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Tonto Team](https://attack.mitre.org/groups/G0131) has delivered payloads via spearphishing attachments.[^15]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [Tonto Team](https://attack.mitre.org/groups/G0131) has used EternalBlue exploits for lateral movement.[^15]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Tonto Team](https://attack.mitre.org/groups/G0131) has used PowerShell to download additional payloads.[^1]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [Tonto Team](https://attack.mitre.org/groups/G0131) has exploited CVE-2019-0803 and MS16-032 to escalate privileges.[^15]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Tonto Team](https://attack.mitre.org/groups/G0131) has downloaded malicious DLLs which served as a [ShadowPad](https://attack.mitre.org/software/S0596) loader.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Mimikatz\|S0002]] | Mimikatz | [^11]  |
| [[gsecdump\|S0008]] | gsecdump | [^15]  |
| [[NBTscan\|S0590]] | NBTscan | [^15]  |
| [[LaZagne\|S0349]] | LaZagne | [^15]  |
| [[Bisonal\|S0268]] | Bisonal | [^11] [^7] [^9]   |
| [[ShadowPad\|S0596]] | ShadowPad | [^11]  |



## References

[^1]: [ESET Exchange Mar 2021](https://www.welivesecurity.com/2021/03/10/exchange-servers-under-siege-10-apt-groups/)


[^2]: [Talos Bisonal 10 Years March 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)


[^3]: [ARS Technica China Hack SK April 2017](https://arstechnica.com/information-technology/2017/04/researchers-claim-china-trying-to-hack-south-korea-missile-defense-efforts/)


[^4]: [CrowdStrike Manufacturing Threat July 2020](https://www.crowdstrike.com/blog/adversaries-targeting-the-manufacturing-industry/)


[^5]: CactusPete


[^6]: BRONZE HUNTLEY


[^7]: [Secureworks BRONZE HUNTLEY ](https://www.secureworks.com/research/threat-profiles/bronze-huntley)


[^8]: Karma Panda


[^9]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)


[^10]: [FireEye Chinese Espionage October 2019](https://web.archive.org/web/20210308054208/https://www.fireeye.com/content/dam/fireeye-www/summit/cds-2019/presentations/cds19-executive-s08-achievement-unlocked.pdf)


[^11]: [Kaspersky CactusPete Aug 2020](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)


[^12]: Earth Akhlut


[^13]: [Trend Micro HeartBeat Campaign January 2013](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_the-heartbeat-apt-campaign.pdf?)


[^14]: Tonto Team


[^15]: [TrendMicro Tonto Team October 2020](https://vb2020.vblocalhost.com/uploads/VB2020-06.pdf)


