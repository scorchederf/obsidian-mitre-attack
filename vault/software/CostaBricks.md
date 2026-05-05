---
aliases: 
    - S0614
    
mitre-attack: https://attack.mitre.org/software/S0614
---

## S0614

[CostaBricks](https://attack.mitre.org/software/S0614) is a loader that was used to deploy 32-bit backdoors in the [CostaRicto](https://attack.mitre.org/groups/G0132) campaign.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [CostaBricks](https://attack.mitre.org/software/S0614) has been used to load [SombRAT](https://attack.mitre.org/software/S0615) onto a compromised host.[^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [CostaBricks](https://attack.mitre.org/software/S0614) can implement a custom-built virtual machine mechanism to obfuscate its code.[^1]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [CostaBricks](https://attack.mitre.org/software/S0614) has added the entire unobfuscated code of the legitimate open source application Blink to its code.[^1]  |
| [[Process Injection\|T1055]] | Process Injection | [CostaBricks](https://attack.mitre.org/software/S0614) can inject a payload into the memory of a compromised host.[^1]  |
| [[Native API\|T1106]] | Native API | [CostaBricks](https://attack.mitre.org/software/S0614) has used a number of API calls, including `VirtualAlloc`, `VirtualFree`, `LoadLibraryA`, `GetProcAddress`, and `ExitProcess`.[^1]   |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [CostaBricks](https://attack.mitre.org/software/S0614) has the ability to use bytecode to decrypt embedded payloads.[^1]  |




## References

[^1]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)


