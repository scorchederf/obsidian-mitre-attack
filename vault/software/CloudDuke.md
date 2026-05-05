---
aliases: 
    - S0054
    
mitre-attack: https://attack.mitre.org/software/S0054
---

## S0054

[CloudDuke](https://attack.mitre.org/software/S0054) is malware that was used by [APT29](https://attack.mitre.org/groups/G0016) in 2015. [^2]  [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | One variant of [CloudDuke](https://attack.mitre.org/software/S0054) uses HTTP and HTTPS for C2.[^2]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | One variant of [CloudDuke](https://attack.mitre.org/software/S0054) uses a Microsoft OneDrive account to exchange commands and stolen data with its operators.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [CloudDuke](https://attack.mitre.org/software/S0054) downloads and executes additional malware from either a Web address or a Microsoft OneDrive account.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [Securelist Minidionis July 2015](https://securelist.com/minidionis-one-more-apt-with-a-usage-of-cloud-drives/71443/)


[^2]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)


