---
aliases: 
    - S1049
    
mitre-attack: https://attack.mitre.org/software/S1049
---

## S1049

[SUGARUSH](https://attack.mitre.org/software/S1049) is a small custom backdoor that can establish a reverse shell over TCP to a hard coded C2 address. [SUGARUSH](https://attack.mitre.org/software/S1049) was first identified during analysis of UNC3890's [C0010](https://attack.mitre.org/campaigns/C0010) campaign targeting Israeli companies, which began in late 2020.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [MoonWind](https://attack.mitre.org/software/S0149) can obtain the number of drives on the victim machine.[^1]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [SUGARUSH](https://attack.mitre.org/software/S1049) has used port 4585 for a TCP connection to its C2.[^2]  |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [SUGARUSH](https://attack.mitre.org/software/S1049) has checked for internet connectivity from an infected host before attempting to establish a new TCP connection.[^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | [SUGARUSH](https://attack.mitre.org/software/S1049) has created a service named `Service1` for persistence.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [SUGARUSH](https://attack.mitre.org/software/S1049) has used `cmd` for execution on an infected host.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [SUGARUSH](https://attack.mitre.org/software/S1049) has used TCP for C2.[^2]  |




## References

[^1]: [Palo Alto MoonWind March 2017](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)


[^2]: [Mandiant UNC3890 Aug 2022](https://www.mandiant.com/resources/blog/suspected-iranian-actor-targeting-israeli-shipping)


