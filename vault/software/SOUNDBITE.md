---
aliases: 
    - S0157
    
mitre-attack: https://attack.mitre.org/software/S0157
---

## S0157

[SOUNDBITE](https://attack.mitre.org/software/S0157) is a signature backdoor used by [APT32](https://attack.mitre.org/groups/G0050). [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SOUNDBITE](https://attack.mitre.org/software/S0157) is capable of gathering system information.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [SOUNDBITE](https://attack.mitre.org/software/S0157) is capable of modifying the Registry.[^2]  |
| [[DNS\|T1071.004]] | DNS | [SOUNDBITE](https://attack.mitre.org/software/S0157) communicates via DNS for C2.[^2]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [SOUNDBITE](https://attack.mitre.org/software/S0157) is capable of enumerating application windows.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [SOUNDBITE](https://attack.mitre.org/software/S0157) is capable of enumerating and manipulating files and directories.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT32\|G0050]] | APT32 |



## References

[^1]: SOUNDBITE


[^2]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)


