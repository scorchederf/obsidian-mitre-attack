---
aliases: 
    - S0594
    
mitre-attack: https://attack.mitre.org/software/S0594
---

## S0594

[Out1](https://attack.mitre.org/software/S0594) is a remote access tool written in python and used by [MuddyWater](https://attack.mitre.org/groups/G0069) since at least 2021.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Out1](https://attack.mitre.org/software/S0594) can use HTTP and HTTPS in communications with remote hosts.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Out1](https://attack.mitre.org/software/S0594) has the ability to encode data.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Out1](https://attack.mitre.org/software/S0594) can use native command line for execution.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Out1](https://attack.mitre.org/software/S0594) can copy files and Registry data from compromised hosts.[^1]  |
| [[Local Email Collection\|T1114.001]] | Local Email Collection | [Out1](https://attack.mitre.org/software/S0594) can parse e-mails on a target machine.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MuddyWater\|G0069]] | MuddyWater |



## References

[^1]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)


