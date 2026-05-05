---
aliases: 
    - S1137
    
mitre-attack: https://attack.mitre.org/software/S1137
---

## S1137

[Moneybird](https://attack.mitre.org/software/S1137) is a ransomware variant written in C++ associated with [Agrius](https://attack.mitre.org/groups/G1030) operations. The name "Moneybird" is contained in the malware's ransom note and as strings in the executable.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Embedded Payloads\|T1027.009]] | Embedded Payloads | [Moneybird](https://attack.mitre.org/software/S1137) contains a configuration blob embedded in the malware itself.[^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Moneybird](https://attack.mitre.org/software/S1137) targets a common set of file types such as documents, certificates, and database files for encryption while avoiding executable, dynamic linked libraries, and similar items.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Agrius\|G1030]] | Agrius |



## References

[^1]: [CheckPoint Agrius 2023](https://research.checkpoint.com/2023/agrius-deploys-moneybird-in-targeted-attacks-against-israeli-organizations/)


