---
aliases: 
    - S0415
    
mitre-attack: https://attack.mitre.org/software/S0415
---

## S0415

[BOOSTWRITE](https://attack.mitre.org/software/S0415) is a loader crafted to be launched via abuse of the DLL search order of applications used by [FIN7](https://attack.mitre.org/groups/G0046).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [BOOSTWRITE](https://attack.mitre.org/software/S0415) has used a a 32-byte long multi-XOR key to decode data inside its payload.[^1] 	 |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [BOOSTWRITE](https://attack.mitre.org/software/S0415) has encoded its payloads using a ChaCha stream cipher with a 256-bit key and 64-bit Initialization vector (IV) to evade detection.[^1]  |
| [[Code Signing\|T1553.002]] | Code Signing | [BOOSTWRITE](https://attack.mitre.org/software/S0415) has been signed by a valid CA.[^1]  |
| [[Shared Modules\|T1129]] | Shared Modules | [BOOSTWRITE](https://attack.mitre.org/software/S0415) has used the DWriteCreateFactory() function to load additional modules.[^1]  |
| [[DLL\|T1574.001]] | DLL | [BOOSTWRITE](https://attack.mitre.org/software/S0415) has exploited the loading of the legitimate Dwrite.dll file by actually loading the gdi library, which then loads the gdiplus library and ultimately loads the local Dwrite dll.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN7\|G0046]] | FIN7 |



## References

[^1]: [FireEye FIN7 Oct 2019](https://www.fireeye.com/blog/threat-research/2019/10/mahalo-fin7-responding-to-new-tools-and-techniques.html)


