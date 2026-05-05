---
aliases: 
    - S0679
    
mitre-attack: https://attack.mitre.org/software/S0679
---

## S0679

[Ferocious](https://attack.mitre.org/software/S0679) is a first stage implant composed of VBS and PowerShell scripts that has been used by [WIRTE](https://attack.mitre.org/groups/G0090) since at least 2021.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Ferocious](https://attack.mitre.org/software/S0679) has the ability to use Visual Basic scripts for execution.[^1]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [Ferocious](https://attack.mitre.org/software/S0679) can run `GET.WORKSPACE` in Microsoft Excel to check if a mouse is present.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Ferocious](https://attack.mitre.org/software/S0679) has checked for AV software as part of its persistence process.[^1]  |
| [[Component Object Model Hijacking\|T1546.015]] | Component Object Model Hijacking | [Ferocious](https://attack.mitre.org/software/S0679) can use COM hijacking to establish persistence.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Ferocious](https://attack.mitre.org/software/S0679) can use PowerShell scripts for execution.[^1]  |
| [[System Checks\|T1497.001]] | System Checks | [Ferocious](https://attack.mitre.org/software/S0679) can run anti-sandbox checks using the Microsoft Excel 4.0 function `GET.WORKSPACE` to determine the OS version, if there is a mouse present, and if the host is capable of playing sounds.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Ferocious](https://attack.mitre.org/software/S0679) can use `GET.WORKSPACE` in Microsoft Excel to determine the OS version of the compromised host.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Ferocious](https://attack.mitre.org/software/S0679) can delete files from a compromised host.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Ferocious](https://attack.mitre.org/software/S0679) has the ability to add a Class ID in the current user Registry hive to enable persistence mechanisms.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[WIRTE\|G0090]] | WIRTE |



## References

[^1]: [Kaspersky WIRTE November 2021](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)


