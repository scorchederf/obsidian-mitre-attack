---
aliases: 
    - S0150
    
mitre-attack: https://attack.mitre.org/software/S0150
---

## S0150

[POSHSPY](https://attack.mitre.org/software/S0150) is a backdoor that has been used by [APT29](https://attack.mitre.org/groups/G0016) since at least 2015. It appears to be used as a secondary backdoor used if the actors lost access to their primary backdoors. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data Transfer Size Limits\|T1030]] | Data Transfer Size Limits | [POSHSPY](https://attack.mitre.org/software/S0150) uploads data in 2048-byte chunks.[^1]  |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [POSHSPY](https://attack.mitre.org/software/S0150) uses a DGA to derive command and control URLs from a word list.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [POSHSPY](https://attack.mitre.org/software/S0150) appends a file signature header (randomly selected from six file types) to encrypted data prior to upload or download.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [POSHSPY](https://attack.mitre.org/software/S0150) uses PowerShell to execute various commands, one to execute its payload.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [POSHSPY](https://attack.mitre.org/software/S0150) encrypts C2 traffic with AES and RSA.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [POSHSPY](https://attack.mitre.org/software/S0150) downloads and executes additional PowerShell code and Windows binaries.[^1]  |
| [[Timestomp\|T1070.006]] | Timestomp | [POSHSPY](https://attack.mitre.org/software/S0150) modifies timestamps of all downloaded executables to match a randomly selected file created prior to 2013.[^1]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [POSHSPY](https://attack.mitre.org/software/S0150) uses a WMI event subscription to establish persistence.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [FireEye POSHSPY April 2017](https://www.fireeye.com/blog/threat-research/2017/03/dissecting_one_ofap.html)


[^2]: POSHSPY


