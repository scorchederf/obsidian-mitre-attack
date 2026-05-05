---
aliases: 
    - S0243
    
mitre-attack: https://attack.mitre.org/software/S0243
---

## S0243

[DealersChoice](https://attack.mitre.org/software/S0243) is a Flash exploitation framework used by [APT28](https://attack.mitre.org/groups/G0007). [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [DealersChoice](https://attack.mitre.org/software/S0243) makes modifications to open-source scripts from GitHub and executes them on the victim’s machine.[^3]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [DealersChoice](https://attack.mitre.org/software/S0243) leverages vulnerable versions of Flash to perform execution.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [DealersChoice](https://attack.mitre.org/software/S0243) uses HTTP for communication with the C2 server.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT28\|G0007]] | APT28 |



## References

[^1]: DealersChoice


[^2]: [Secureworks IRON TWILIGHT Active Measures March 2017](https://www.secureworks.com/research/iron-twilight-supports-active-measures)


[^3]: [Sofacy DealersChoice](https://researchcenter.paloaltonetworks.com/2018/03/unit42-sofacy-uses-dealerschoice-target-european-government-agency/)


