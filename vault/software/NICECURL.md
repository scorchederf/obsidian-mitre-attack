---
aliases: 
    - S1192
    
mitre-attack: https://attack.mitre.org/software/S1192
---

## S1192

[NICECURL](https://attack.mitre.org/software/S1192) is a VBScript-based backdoor used by [APT42](https://attack.mitre.org/groups/G1044) to download additional modules.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File Deletion\|T1070.004]] | File Deletion | [NICECURL](https://attack.mitre.org/software/S1192) has a function to remove artifacts.[^1]   |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [NICECURL](https://attack.mitre.org/software/S1192) has provided an arbitrary command execution interface.[^1]   |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [NICECURL](https://attack.mitre.org/software/S1192) has used HTTPS for C2 communications.[^1]   |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [NICECURL](https://attack.mitre.org/software/S1192) has the ability to download additional content onto an infected machine, e.g. by using `curl`.[^1]   |
| [[Web Protocols\|T1071.001]] | Web Protocols | [NICECURL](https://attack.mitre.org/software/S1192) has used HTTPS for C2 communications.[^1]   |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT42\|G1044]] | APT42 |



## References

[^1]: [Mandiant APT42-untangling](https://cloud.google.com/blog/topics/threat-intelligence/untangling-iran-apt42-operations)


