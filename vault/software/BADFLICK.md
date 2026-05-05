---
aliases: 
    - S0642
    
mitre-attack: https://attack.mitre.org/software/S0642
---

## S0642

[BADFLICK](https://attack.mitre.org/software/S0642) is a backdoor used by [Leviathan](https://attack.mitre.org/groups/G0065) in spearphishing campaigns first reported in 2018 that targeted the U.S. engineering and maritime industries.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [BADFLICK](https://attack.mitre.org/software/S0642) has captured victim computer name, memory space, and CPU details.[^2]  |
| [[Archive via Library\|T1560.002]] | Archive via Library | [BADFLICK](https://attack.mitre.org/software/S0642) has compressed data using the aPLib compression library.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [BADFLICK](https://attack.mitre.org/software/S0642) has searched for files on the infected host.[^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [BADFLICK](https://attack.mitre.org/software/S0642) has relied upon users clicking on a malicious attachment delivered through spearphishing.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [BADFLICK](https://attack.mitre.org/software/S0642) has uploaded files from victims' machines.[^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [BADFLICK](https://attack.mitre.org/software/S0642) has been distributed via spearphishing campaigns containing malicious Microsoft Word documents.[^2]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [BADFLICK](https://attack.mitre.org/software/S0642) has delayed communication to the actor-controlled IP address by 5 minutes.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [BADFLICK](https://attack.mitre.org/software/S0642) has captured victim IP address details.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BADFLICK](https://attack.mitre.org/software/S0642) has download files from its C2 server.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [BADFLICK](https://attack.mitre.org/software/S0642) can decode shellcode using a custom rotating XOR cipher.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Leviathan\|G0065]] | Leviathan |



## References

[^1]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)


[^2]: [Accenture MUDCARP March 2019](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)


