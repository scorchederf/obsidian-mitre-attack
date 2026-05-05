---
aliases: 
    - S0628
    
mitre-attack: https://attack.mitre.org/software/S0628
---

## S0628

[FYAnti](https://attack.mitre.org/software/S0628) is a loader that has been used by [menuPass](https://attack.mitre.org/groups/G0045) since at least 2020, including to deploy [QuasarRAT](https://attack.mitre.org/software/S0262).[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [FYAnti](https://attack.mitre.org/software/S0628) can download additional payloads to a compromised host.[^2] 	  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [FYAnti](https://attack.mitre.org/software/S0628) can search the `C:\Windows\Microsoft.NET\` directory for files of a specified size.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [FYAnti](https://attack.mitre.org/software/S0628) has the ability to decrypt an embedded .NET module.[^2]  |
| [[Software Packing\|T1027.002]] | Software Packing | [FYAnti](https://attack.mitre.org/software/S0628) has used ConfuserEx to pack its .NET module.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[menuPass\|G0045]] | menuPass |



## References

[^1]: DILLJUICE stage2


[^2]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)


