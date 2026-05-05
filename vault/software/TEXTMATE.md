---
aliases: 
    - S0146
    
mitre-attack: https://attack.mitre.org/software/S0146
---

## S0146

[TEXTMATE](https://attack.mitre.org/software/S0146) is a second-stage PowerShell backdoor that is memory-resident. It was observed being used along with [POWERSOURCE](https://attack.mitre.org/software/S0145) in February 2017. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[DNS\|T1071.004]] | DNS | [TEXTMATE](https://attack.mitre.org/software/S0146) uses DNS TXT records for C2.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [TEXTMATE](https://attack.mitre.org/software/S0146) executes cmd.exe to provide a reverse shell to adversaries.[^2] [^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN7\|G0046]] | FIN7 |



## References

[^1]: TEXTMATE


[^2]: [FireEye FIN7 March 2017](https://web.archive.org/web/20180808125108/https:/www.fireeye.com/blog/threat-research/2017/03/fin7_spear_phishing.html)


[^3]: DNSMessenger


[^4]: [Cisco DNSMessenger March 2017](http://blog.talosintelligence.com/2017/03/dnsmessenger.html)


