---
aliases: 
    - S1223
    
mitre-attack: https://attack.mitre.org/software/S1223
---

## S1223

[THINCRUST](https://attack.mitre.org/software/S1223) is a Python-based backdoor tool that has been used by [UNC3886](https://attack.mitre.org/groups/G1048) since at least 2023.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [THINCRUST](https://attack.mitre.org/software/S1223) can use the Django python module "django.views.decorators.csrf” along with the decorator “csrf_exempt” within victim firewalls to disable cross-site request forgery protections.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [THINCRUST](https://attack.mitre.org/software/S1223) can use HTTP POST requests in C2 communications.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [THINCRUST](https://attack.mitre.org/software/S1223) can process RSA encryted C2 commands.[^1]  |
| [[Python\|T1059.006]] | Python | [THINCRUST](https://attack.mitre.org/software/S1223) can use Python scripts for command execution.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [THINCRUST](https://attack.mitre.org/software/S1223) can deobfuscate RSA encrypted C2 commands received through the DEVICEID cookie.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[UNC3886\|G1048]] | UNC3886 |



## References

[^1]: [Mandiant Fortinet Zero Day](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)


