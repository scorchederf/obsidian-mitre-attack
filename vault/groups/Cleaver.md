---
aliases: 
    - Cleaver
    - Threat Group 2889
    - TG-2889
mitre-attack: https://attack.mitre.org/groups/G0003
---

## G0003

[Cleaver](https://attack.mitre.org/groups/G0003) is a threat group that has been attributed to Iranian actors and is responsible for activity tracked as Operation Cleaver. [^5]  Strong circumstantial evidence suggests Cleaver is linked to Threat Group 2889 (TG-2889). [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Cleaver](https://attack.mitre.org/groups/G0003) has been known to dump credentials using Mimikatz and Windows Credential Editor.[^5]  |
| [[ARP Cache Poisoning\|T1557.002]] | ARP Cache Poisoning | [Cleaver](https://attack.mitre.org/groups/G0003) has used custom tools to facilitate ARP cache poisoning.[^5]  |
| [[Tool\|T1588.002]] | Tool | [Cleaver](https://attack.mitre.org/groups/G0003) has obtained and used open-source tools such as [PsExec](https://attack.mitre.org/software/S0029), [Windows Credential Editor](https://attack.mitre.org/software/S0005), and [Mimikatz](https://attack.mitre.org/software/S0002).[^5]  |
| [[Malware\|T1587.001]] | Malware | [Cleaver](https://attack.mitre.org/groups/G0003) has created customized tools and payloads for functions including ARP poisoning, encryption, credential dumping, ASP.NET shells, web backdoors, process enumeration, WMI querying, HTTP and SMB communications, network interface sniffing, and keystroke logging.[^5]  |
| [[Social Media Accounts\|T1585.001]] | Social Media Accounts | [Cleaver](https://attack.mitre.org/groups/G0003) has created fake LinkedIn profiles that included profile photos, details, and connections.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Mimikatz\|S0002]] | Mimikatz | [^5]  |
| [[PsExec\|S0029]] | PsExec | [^5]  |
| [[TinyZBot\|S0004]] | TinyZBot | [^5]  |
| [[Net Crawler\|S0056]] | Net Crawler | [^5]  |



## References

[^1]: TG-2889


[^2]: [Dell Threat Group 2889](http://www.secureworks.com/cyber-threat-intelligence/threats/suspected-iran-based-hacker-group-creates-network-of-fake-linkedin-profiles/)


[^3]: Cleaver


[^4]: Threat Group 2889


[^5]: [Cylance Cleaver](https://web.archive.org/web/20200302085133/https://www.cylance.com/content/dam/cylance/pages/operation-cleaver/Cylance_Operation_Cleaver_Report.pdf)


