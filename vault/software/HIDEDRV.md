---
aliases: 
    - S0135
    
mitre-attack: https://attack.mitre.org/software/S0135
---

## S0135

[HIDEDRV](https://attack.mitre.org/software/S0135) is a rootkit used by [APT28](https://attack.mitre.org/groups/G0007). It has been deployed along with [Downdelph](https://attack.mitre.org/software/S0134) to execute and hide that malware. [^1]  [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Rootkit\|T1014]] | Rootkit | [HIDEDRV](https://attack.mitre.org/software/S0135) is a rootkit that hides certain operating system artifacts.[^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [HIDEDRV](https://attack.mitre.org/software/S0135) injects a DLL for [Downdelph](https://attack.mitre.org/software/S0134) into the explorer.exe process.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT28\|G0007]] | APT28 |



## References

[^1]: [ESET Sednit Part 3](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part3.pdf)


[^2]: [Sekoia HideDRV Oct 2016](https://web.archive.org/web/20180202163754/http://www.sekoia.fr/blog/wp-content/uploads/2016/10/Rootkit-analysis-Use-case-on-HIDEDRV-v1.6.pdf)


