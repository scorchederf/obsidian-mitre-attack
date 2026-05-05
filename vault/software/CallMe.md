---
aliases: 
    - S0077
    
mitre-attack: https://attack.mitre.org/software/S0077
---

## S0077

[CallMe](https://attack.mitre.org/software/S0077) is a Trojan designed to run on Apple OSX. It is based on a publicly available tool called Tiny SHell. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [CallMe](https://attack.mitre.org/software/S0077) has the capability to download a file to the victim from the C2 server.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [CallMe](https://attack.mitre.org/software/S0077) uses AES to encrypt C2 traffic.[^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [CallMe](https://attack.mitre.org/software/S0077) has the capability to create a reverse shell on victims.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [CallMe](https://attack.mitre.org/software/S0077) exfiltrates data to its C2 server over the same protocol as C2 communications.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Scarlet Mimic\|G0029]] | Scarlet Mimic |



## References

[^1]: [Scarlet Mimic Jan 2016](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)


