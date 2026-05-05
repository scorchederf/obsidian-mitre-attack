---
aliases: 
    - S0174
    
mitre-attack: https://attack.mitre.org/software/S0174
---

## S0174

Responder is an open source tool used for LLMNR, NBT-NS and MDNS poisoning, with built-in HTTP/SMB/MSSQL/FTP/LDAP rogue authentication server supporting NTLMv1/NTLMv2/LMv2, Extended Security NTLMSSP and Basic HTTP authentication. [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Network Sniffing\|T1040]] | Network Sniffing | [Responder](https://attack.mitre.org/software/S0174) captures hashes and credentials that are sent to the system after the name services have been poisoned.[^4]  |
| [[Name Resolution Poisoning and SMB Relay\|T1557.001]] | Name Resolution Poisoning and SMB Relay | [Responder](https://attack.mitre.org/software/S0174) is used to poison name services to gather hashes and credentials from systems within a local network.[^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Ember Bear\|G1003]] | Ember Bear |
| [[APT28\|G0007]] | APT28 |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: [US District Court Indictment GRU Oct 2018](https://www.justice.gov/opa/page/file/1098481/download)


[^2]: [ClearSky Lazarus Aug 2020](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)


[^3]: [FireEye APT28 Hospitality Aug 2017](https://web.archive.org/web/20171202185937/https://www.fireeye.com/blog/threat-research/2017/08/apt28-targets-hospitality-sector.html)


[^4]: [GitHub Responder](https://github.com/SpiderLabs/Responder)


[^5]: [CISA GRU29155 2024](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)


