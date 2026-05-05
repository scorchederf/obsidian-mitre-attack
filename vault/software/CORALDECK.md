---
aliases: 
    - S0212
    
mitre-attack: https://attack.mitre.org/software/S0212
---

## S0212

[CORALDECK](https://attack.mitre.org/software/S0212) is an exfiltration tool used by [APT37](https://attack.mitre.org/groups/G0067). [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [CORALDECK](https://attack.mitre.org/software/S0212) has exfiltrated data in HTTP POST headers.[^1]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [CORALDECK](https://attack.mitre.org/software/S0212) has created password-protected RAR, WinImage, and zip archives to be exfiltrated.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [CORALDECK](https://attack.mitre.org/software/S0212) searches for specified files.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT37\|G0067]] | APT37 |



## References

[^1]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)


[^2]: CORALDECK


