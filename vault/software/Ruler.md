---
aliases: 
    - S0358
    
mitre-attack: https://attack.mitre.org/software/S0358
---

## S0358

[Ruler](https://attack.mitre.org/software/S0358) is a tool to abuse Microsoft Exchange services. It is publicly available on GitHub and the tool is executed via the command line. The creators of [Ruler](https://attack.mitre.org/software/S0358) have also released a defensive tool, NotRuler, to detect its usage.[^2] [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Outlook Rules\|T1137.005]] | Outlook Rules | [Ruler](https://attack.mitre.org/software/S0358) can be used to automate the abuse of Outlook Rules to establish persistence.[^2]   |
| [[Outlook Forms\|T1137.003]] | Outlook Forms | [Ruler](https://attack.mitre.org/software/S0358) can be used to automate the abuse of Outlook Forms to establish persistence.[^2]  |
| [[Outlook Home Page\|T1137.004]] | Outlook Home Page | [Ruler](https://attack.mitre.org/software/S0358) can be used to automate the abuse of Outlook Home Pages to establish persistence.[^2]   |
| [[Email Account\|T1087.003]] | Email Account | [Ruler](https://attack.mitre.org/software/S0358) can be used to enumerate Exchange users and dump the GAL.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT33\|G0064]] | APT33 |



## References

[^1]: [Microsoft Holmium June 2020](https://www.microsoft.com/security/blog/2020/06/18/inside-microsoft-threat-protection-mapping-attack-chains-from-cloud-to-endpoint/)


[^2]: [SensePost Ruler GitHub](https://github.com/sensepost/ruler)


[^3]: [FireEye APT33 Guardrail](https://www.fireeye.com/blog/threat-research/2018/12/overruled-containing-a-potentially-destructive-adversary.html)


[^4]: [SensePost NotRuler](https://github.com/sensepost/notruler)


