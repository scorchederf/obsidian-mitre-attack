---
aliases: 
    - S0624
    
mitre-attack: https://attack.mitre.org/software/S0624
---

## S0624

[Ecipekac](https://attack.mitre.org/software/S0624) is a multi-layer loader that has been used by [menuPass](https://attack.mitre.org/groups/G0045) since at least 2019 including use as a loader for [P8RAT](https://attack.mitre.org/software/S0626), [SodaMaster](https://attack.mitre.org/software/S0627), and [FYAnti](https://attack.mitre.org/software/S0628).[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Ecipekac](https://attack.mitre.org/software/S0624) can use XOR, AES, and DES to encrypt loader shellcode.[^2]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Ecipekac](https://attack.mitre.org/software/S0624) has used a valid, legitimate digital signature to evade detection.[^2]  |
| [[DLL\|T1574.001]] | DLL | [Ecipekac](https://attack.mitre.org/software/S0624) can abuse the legitimate application policytool.exe to load a malicious DLL.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Ecipekac](https://attack.mitre.org/software/S0624) can download additional payloads to a compromised host.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Ecipekac](https://attack.mitre.org/software/S0624) has the ability to decrypt fileless loader modules.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[menuPass\|G0045]] | menuPass |



## References

[^1]: SigLoader


[^2]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)


[^3]: DESLoader


[^4]: HEAVYHAND


