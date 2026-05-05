---
aliases: 
    - S0109
    
mitre-attack: https://attack.mitre.org/software/S0109
---

## S0109

[WEBC2](https://attack.mitre.org/software/S0109) is a family of backdoor malware used by [APT1](https://attack.mitre.org/groups/G0006) as early as July 2006. [WEBC2](https://attack.mitre.org/software/S0109) backdoors are designed to retrieve a webpage, with commands hidden in HTML comments or special tags, from a predetermined C2 server. [^2] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[DLL\|T1574.001]] | DLL | Variants of [WEBC2](https://attack.mitre.org/software/S0109) achieve persistence by using DLL search order hijacking, usually by copying the DLL file to `%SYSTEMROOT%` (`C:\WINDOWS\ntshrui.dll`).[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [WEBC2](https://attack.mitre.org/software/S0109) can download and execute a file.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [WEBC2](https://attack.mitre.org/software/S0109) can open an interactive command shell.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT1\|G0006]] | APT1 |



## References

[^1]: WEBC2


[^2]: [Mandiant APT1 Appendix](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)


[^3]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)


