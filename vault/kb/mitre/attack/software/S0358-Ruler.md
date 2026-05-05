---
aliases: 
    - S0358
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0358-Ruler
---

## Description

[[kb/mitre/attack/software/S0358-Ruler\|Ruler]] is a tool to abuse Microsoft Exchange services. It is publicly available on GitHub and the tool is executed via the command line. The creators of [[kb/mitre/attack/software/S0358-Ruler\|Ruler]] have also released a defensive tool, NotRuler, to detect its usage.[^2] [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1087.003-Email_Account\|T1087.003]] | Email Account | [[kb/mitre/attack/software/S0358-Ruler\|Ruler]] can be used to enumerate Exchange users and dump the GAL.[^2]  |
| [[kb/mitre/attack/techniques/T1137.003-Outlook_Forms\|T1137.003]] | Outlook Forms | [[kb/mitre/attack/software/S0358-Ruler\|Ruler]] can be used to automate the abuse of Outlook Forms to establish persistence.[^2]  |
| [[kb/mitre/attack/techniques/T1137.004-Outlook_Home_Page\|T1137.004]] | Outlook Home Page | [[kb/mitre/attack/software/S0358-Ruler\|Ruler]] can be used to automate the abuse of Outlook Home Pages to establish persistence.[^2]   |
| [[kb/mitre/attack/techniques/T1137.005-Outlook_Rules\|T1137.005]] | Outlook Rules | [[kb/mitre/attack/software/S0358-Ruler\|Ruler]] can be used to automate the abuse of Outlook Rules to establish persistence.[^2]   |





> [!info]- References
> [^1]: [SensePost NotRuler](https://github.com/sensepost/notruler)

> [^2]: [SensePost Ruler GitHub](https://github.com/sensepost/ruler)


