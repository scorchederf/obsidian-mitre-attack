---
aliases: 
    - S1193
    
mitre-attack: https://attack.mitre.org/software/S1193
---

## S1193

[TAMECAT](https://attack.mitre.org/software/S1193) is a malware that is used by [APT42](https://attack.mitre.org/groups/G1044) to execute PowerShell or C# content.[^1]  

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [TAMECAT](https://attack.mitre.org/software/S1193) has used `cmd.exe` to run the `curl` command.[^1]   |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [TAMECAT](https://attack.mitre.org/software/S1193) has used `wget` and `curl` to download additional content.[^1]   |
| [[Visual Basic\|T1059.005]] | Visual Basic | [TAMECAT](https://attack.mitre.org/software/S1193) has used VBScript to query anti-virus products.[^1]   |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [TAMECAT](https://attack.mitre.org/software/S1193) has encoded C2 traffic with Base64.[^1]   |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [TAMECAT](https://attack.mitre.org/software/S1193) has used Windows Management Instrumentation (WMI) to query anti-virus products.[^1]   |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [TAMECAT](https://attack.mitre.org/software/S1193) has used AES to encrypt C2 traffic.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [TAMECAT](https://attack.mitre.org/software/S1193) has used Windows Management Instrumentation (WMI) to check for anti-virus products.[^1]   |
| [[PowerShell\|T1059.001]] | PowerShell | [TAMECAT](https://attack.mitre.org/software/S1193) has used PowerShell to download and run additional content.[^1]   |
| [[Web Protocols\|T1071.001]] | Web Protocols | [TAMECAT](https://attack.mitre.org/software/S1193) has used HTTP for C2 communications.[^1]   |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT42\|G1044]] | APT42 |



## References

[^1]: [Mandiant APT42-untangling](https://cloud.google.com/blog/topics/threat-intelligence/untangling-iran-apt42-operations)


