---
aliases: 
    - S9017
    
mitre-attack: https://attack.mitre.org/software/S9017
---

## S9017

[DCRAT](https://attack.mitre.org/software/S9017) is a variant of the open-source [AsyncRAT](https://attack.mitre.org/software/S1087) developed in C# with additional capabilities such as patching Microsoft’s Antimalware Scan Interface (AMSI).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [DCRAT](https://attack.mitre.org/software/S9017) can use certificate-based authentication for C2 servers.[^1] <br> |
| [[Keylogging\|T1056.001]] | Keylogging | [DCRAT](https://attack.mitre.org/software/S9017) can log keystrokes on targeted systems.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | The [DCRAT](https://attack.mitre.org/software/S9017) configuration file is encrypted using AES-256.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [DCRAT](https://attack.mitre.org/software/S9017) can patch Microsoft’s Antimalware Scan Interface (AMSI) to evade detection.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT-C-36\|G0099]] | APT-C-36 |



## References

[^1]: [Zscaler BlindEagle DEC 2025](https://www.zscaler.com/blogs/security-research/blindeagle-targets-colombian-government-agency-caminho-and-dcrat)


