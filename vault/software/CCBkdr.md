---
aliases: 
    - S0222
    
mitre-attack: https://attack.mitre.org/software/S0222
---

## S0222

[CCBkdr](https://attack.mitre.org/software/S0222) is malware that was injected into a signed version of CCleaner and distributed from CCleaner's distribution website. [^3]  [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Compromise Software Supply Chain\|T1195.002]] | Compromise Software Supply Chain | [CCBkdr](https://attack.mitre.org/software/S0222) was added to a legitimate, signed version 5.33 of the CCleaner software and distributed on CCleaner's distribution site.[^3] [^1] [^2]  |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [CCBkdr](https://attack.mitre.org/software/S0222) can use a DGA for [Fallback Channels](https://attack.mitre.org/techniques/T1008) if communications with the primary command and control server are lost.[^3]  |




## References

[^1]: [Intezer Aurora Sept 2017](http://www.intezer.com/evidence-aurora-operation-still-active-supply-chain-attack-through-ccleaner/)


[^2]: [Avast CCleaner3 2018](https://blog.avast.com/new-investigations-in-ccleaner-incident-point-to-a-possible-third-stage-that-had-keylogger-capacities)


[^3]: [Talos CCleanup 2017](http://blog.talosintelligence.com/2017/09/avast-distributes-malware.html)


