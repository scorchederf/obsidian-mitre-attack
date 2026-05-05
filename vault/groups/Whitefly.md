---
aliases: 
    - Whitefly
mitre-attack: https://attack.mitre.org/groups/G0107
---

## G0107

[Whitefly](https://attack.mitre.org/groups/G0107) is a cyber espionage group that has been operating since at least 2017. The group has targeted organizations based mostly in Singapore across a wide variety of sectors, and is primarily interested in stealing large amounts of sensitive information. The group has been linked to an attack against Singapore’s largest public health organization, SingHealth.[^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Whitefly](https://attack.mitre.org/groups/G0107) has the ability to download additional tools from the C2.[^1]  |
| [[DLL\|T1574.001]] | DLL | [Whitefly](https://attack.mitre.org/groups/G0107) has used search order hijacking to run the loader Vcrodat.[^1] 	 |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Whitefly](https://attack.mitre.org/groups/G0107) has used [Mimikatz](https://attack.mitre.org/software/S0002) to obtain credentials.[^1]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [Whitefly](https://attack.mitre.org/groups/G0107) has used an open-source tool to exploit a known Windows privilege escalation vulnerability (CVE-2016-0051) on unpatched computers.[^1] 	 |
| [[Tool\|T1588.002]] | Tool | [Whitefly](https://attack.mitre.org/groups/G0107) has obtained and used tools such as [Mimikatz](https://attack.mitre.org/software/S0002).[^1]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [Whitefly](https://attack.mitre.org/groups/G0107) has used a simple remote shell tool that will call back to the C2 server and wait for commands.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Whitefly](https://attack.mitre.org/groups/G0107) has encrypted the payload used for C2.[^1] 	 |
| [[Malicious File\|T1204.002]] | Malicious File | [Whitefly](https://attack.mitre.org/groups/G0107) has used malicious .exe or .dll files disguised as documents or images.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Whitefly](https://attack.mitre.org/groups/G0107) has named the malicious DLL the same name as DLLs belonging to legitimate software from various security vendors.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Mimikatz\|S0002]] | Mimikatz | [^1]  |



## References

[^1]: [Symantec Whitefly March 2019](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/whitefly-espionage-singapore)


