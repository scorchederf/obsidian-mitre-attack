---
aliases: 
    - S0216
    
mitre-attack: https://attack.mitre.org/software/S0216
---

## S0216

[POORAIM](https://attack.mitre.org/software/S0216) is a backdoor used by [APT37](https://attack.mitre.org/groups/G0067) in campaigns since at least 2014. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [POORAIM](https://attack.mitre.org/software/S0216) can conduct file browsing.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [POORAIM](https://attack.mitre.org/software/S0216) can perform screen capturing.[^1]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [POORAIM](https://attack.mitre.org/software/S0216) has used AOL Instant Messenger for C2.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [POORAIM](https://attack.mitre.org/software/S0216) can enumerate processes.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [POORAIM](https://attack.mitre.org/software/S0216) can identify system information, including battery status.[^1]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [POORAIM](https://attack.mitre.org/software/S0216) has been delivered through compromised sites acting as watering holes.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT37\|G0067]] | APT37 |



## References

[^1]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)


[^2]: POORAIM


