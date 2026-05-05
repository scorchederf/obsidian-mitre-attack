---
aliases: 
    - S0219
    
mitre-attack: https://attack.mitre.org/software/S0219
---

## S0219

[WINERACK](https://attack.mitre.org/software/S0219) is a backdoor used by [APT37](https://attack.mitre.org/groups/G0067). [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [WINERACK](https://attack.mitre.org/software/S0219) can enumerate processes.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [WINERACK](https://attack.mitre.org/software/S0219) can gather information on the victim username.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [WINERACK](https://attack.mitre.org/software/S0219) can enumerate files and directories.[^1]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [WINERACK](https://attack.mitre.org/software/S0219) can enumerate active windows.[^1]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [WINERACK](https://attack.mitre.org/software/S0219) can create a reverse shell that utilizes statically-linked Wine cmd.exe code to emulate Windows command prompt commands.[^1]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [WINERACK](https://attack.mitre.org/software/S0219) can enumerate services.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [WINERACK](https://attack.mitre.org/software/S0219) can gather information about the host.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT37\|G0067]] | APT37 |



## References

[^1]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)


