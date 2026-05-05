---
aliases: 
    - S0613
    
mitre-attack: https://attack.mitre.org/software/S0613
---

## S0613

[PS1](https://attack.mitre.org/software/S0613) is a loader that was used to deploy 64-bit backdoors in the [CostaRicto](https://attack.mitre.org/groups/G0132) campaign.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [CostaBricks](https://attack.mitre.org/software/S0614) can download additional payloads onto a compromised host.[^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [PS1](https://attack.mitre.org/software/S0613) can inject its payload DLL Into memory.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [PS1](https://attack.mitre.org/software/S0613) can utilize a PowerShell loader.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [PS1](https://attack.mitre.org/software/S0613) is distributed as a set of encrypted files and scripts.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [PS1](https://attack.mitre.org/software/S0613) can use an XOR key to decrypt a PowerShell loader and payload binary.[^1]  |




## References

[^1]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)


