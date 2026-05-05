---
aliases: 
    - S0200
    
mitre-attack: https://attack.mitre.org/software/S0200
---

## S0200

[Dipsind](https://attack.mitre.org/software/S0200) is a malware family of backdoors that appear to be used exclusively by [PLATINUM](https://attack.mitre.org/groups/G0068). [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Dipsind](https://attack.mitre.org/software/S0200) can download remote files.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Dipsind](https://attack.mitre.org/software/S0200) encrypts C2 data with AES256 in ECB mode.[^2]  |
| [[Winlogon Helper DLL\|T1547.004]] | Winlogon Helper DLL | A [Dipsind](https://attack.mitre.org/software/S0200) variant registers as a Winlogon Event Notify DLL to establish persistence.[^2]  |
| [[Scheduled Transfer\|T1029]] | Scheduled Transfer | [Dipsind](https://attack.mitre.org/software/S0200) can be configured to only run during normal working hours, which would make its communications harder to distinguish from normal traffic.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Dipsind](https://attack.mitre.org/software/S0200) can spawn remote shells.[^2]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Dipsind](https://attack.mitre.org/software/S0200) encodes C2 traffic with base64.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Dipsind](https://attack.mitre.org/software/S0200) uses HTTP for C2.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[PLATINUM\|G0068]] | PLATINUM |



## References

[^1]: Dipsind


[^2]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)


