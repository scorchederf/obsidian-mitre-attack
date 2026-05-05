---
aliases: 
    - S0202
    
mitre-attack: https://attack.mitre.org/software/S0202
---

## S0202

[adbupd](https://attack.mitre.org/software/S0202) is a backdoor used by [PLATINUM](https://attack.mitre.org/groups/G0068) that is similar to [Dipsind](https://attack.mitre.org/software/S0200). [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [adbupd](https://attack.mitre.org/software/S0202) can use a WMI script to achieve persistence.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [adbupd](https://attack.mitre.org/software/S0202) can run a copy of cmd.exe.[^2]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [adbupd](https://attack.mitre.org/software/S0202) contains a copy of the OpenSSL library to encrypt C2 traffic.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[PLATINUM\|G0068]] | PLATINUM |



## References

[^1]: adbupd


[^2]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)


