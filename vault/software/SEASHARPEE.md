---
aliases: 
    - S0185
    
mitre-attack: https://attack.mitre.org/software/S0185
---

## S0185

[SEASHARPEE](https://attack.mitre.org/software/S0185) is a Web shell that has been used by [OilRig](https://attack.mitre.org/groups/G0049). [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SEASHARPEE](https://attack.mitre.org/software/S0185) can download remote files onto victims.[^1]  |
| [[Timestomp\|T1070.006]] | Timestomp | [SEASHARPEE](https://attack.mitre.org/software/S0185) can timestomp files on victims using a Web shell.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [SEASHARPEE](https://attack.mitre.org/software/S0185) can execute commands on victims.[^1]  |
| [[Web Shell\|T1505.003]] | Web Shell | [SEASHARPEE](https://attack.mitre.org/software/S0185) is a Web shell.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[OilRig\|G0049]] | OilRig |



## References

[^1]: [FireEye APT34 Webinar Dec 2017](https://www.brighttalk.com/webcast/10703/296317/apt34-new-targeted-attack-in-the-middle-east)


[^2]: SEASHARPEE


