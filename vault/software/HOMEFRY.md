---
aliases: 
    - S0232
    
mitre-attack: https://attack.mitre.org/software/S0232
---

## S0232

[HOMEFRY](https://attack.mitre.org/software/S0232) is a 64-bit Windows password dumper/cracker that has previously been used in conjunction with other [Leviathan](https://attack.mitre.org/groups/G0065) backdoors. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | [HOMEFRY](https://attack.mitre.org/software/S0232) can perform credential dumping.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | Some strings in [HOMEFRY](https://attack.mitre.org/software/S0232) are obfuscated with XOR x56.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [HOMEFRY](https://attack.mitre.org/software/S0232) uses a command-line interface.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Leviathan\|G0065]] | Leviathan |



## References

[^1]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)


[^2]: HOMEFRY


