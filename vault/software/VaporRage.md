---
aliases: 
    - S0636
    
mitre-attack: https://attack.mitre.org/software/S0636
---

## S0636

[VaporRage](https://attack.mitre.org/software/S0636) is a shellcode downloader that has been used by [APT29](https://attack.mitre.org/groups/G0016) since at least 2021.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [VaporRage](https://attack.mitre.org/software/S0636) can deobfuscate XOR-encoded shellcode prior to execution.[^1]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [VaporRage](https://attack.mitre.org/software/S0636) has the ability to check for the presence of a specific DLL and terminate if it is not found.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [VaporRage](https://attack.mitre.org/software/S0636) has the ability to download malicious shellcode to compromised systems.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [VaporRage](https://attack.mitre.org/software/S0636) can use HTTP to download shellcode from compromised websites.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)


