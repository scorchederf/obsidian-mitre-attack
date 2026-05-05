---
aliases: 
    - S0078
    
mitre-attack: https://attack.mitre.org/software/S0078
---

## S0078

[Psylo](https://attack.mitre.org/software/S0078) is a shellcode-based Trojan that has been used by [Scarlet Mimic](https://attack.mitre.org/groups/G0029). It has similar characteristics as [FakeM](https://attack.mitre.org/software/S0076). [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Psylo](https://attack.mitre.org/software/S0078) uses HTTPS for C2.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Psylo](https://attack.mitre.org/software/S0078) has commands to enumerate all storage devices and to find all files that start with a particular string.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Psylo](https://attack.mitre.org/software/S0078) has a command to download a file to the system from its C2 server.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Psylo](https://attack.mitre.org/software/S0078) exfiltrates data to its C2 server over the same protocol as C2 communications.[^1]  |
| [[Timestomp\|T1070.006]] | Timestomp | [Psylo](https://attack.mitre.org/software/S0078) has a command to conduct timestomping by setting a specified file’s timestamps to match those of a system file in the System32 directory.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Scarlet Mimic\|G0029]] | Scarlet Mimic |



## References

[^1]: [Scarlet Mimic Jan 2016](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)


