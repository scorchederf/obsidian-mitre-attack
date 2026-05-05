---
aliases: 
    - S0371
    
mitre-attack: https://attack.mitre.org/software/S0371
---

## S0371

[POWERTON](https://attack.mitre.org/software/S0371) is a custom PowerShell backdoor first observed in 2018. It has typically been deployed as a late-stage backdoor by [APT33](https://attack.mitre.org/groups/G0064). At least two variants of the backdoor have been identified, with the later version containing improved functionality.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [POWERTON](https://attack.mitre.org/software/S0371) has used AES for encrypting C2 traffic.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [POWERTON](https://attack.mitre.org/software/S0371) has used HTTP/HTTPS for C2 traffic.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [POWERTON](https://attack.mitre.org/software/S0371) is written in PowerShell.[^1]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [POWERTON](https://attack.mitre.org/software/S0371) has the ability to dump password hashes.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [POWERTON](https://attack.mitre.org/software/S0371) can install a Registry Run key for persistence.[^1]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [POWERTON](https://attack.mitre.org/software/S0371) can use WMI for persistence.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT33\|G0064]] | APT33 |



## References

[^1]: [FireEye APT33 Guardrail](https://www.fireeye.com/blog/threat-research/2018/12/overruled-containing-a-potentially-destructive-adversary.html)


[^2]: [Microsoft Holmium June 2020](https://www.microsoft.com/security/blog/2020/06/18/inside-microsoft-threat-protection-mapping-attack-chains-from-cloud-to-endpoint/)


