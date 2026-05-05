---
aliases: 
    - S0230
    
mitre-attack: https://attack.mitre.org/software/S0230
---

## S0230

[ZeroT](https://attack.mitre.org/software/S0230) is a Trojan used by [TA459](https://attack.mitre.org/groups/G0062), often in conjunction with [PlugX](https://attack.mitre.org/software/S0013). [^2]  [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [ZeroT](https://attack.mitre.org/software/S0230) shellcode decrypts and decompresses its RC4-encrypted payload.[^1]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | Many [ZeroT](https://attack.mitre.org/software/S0230) samples can perform UAC bypass by using eventvwr.exe to execute a malicious file.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [ZeroT](https://attack.mitre.org/software/S0230) can add a new service to ensure [PlugX](https://attack.mitre.org/software/S0013) persists on the system when delivered as another payload onto the system.[^1]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [ZeroT](https://attack.mitre.org/software/S0230) has obfuscated DLLs and functions using dummy API calls inserted between real instructions.[^1]  |
| [[DLL\|T1574.001]] | DLL | [ZeroT](https://attack.mitre.org/software/S0230) has used DLL side-loading to load malicious payloads.[^2] [^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [ZeroT](https://attack.mitre.org/software/S0230) gathers the victim's IP address and domain information, and then sends it to its C2 server.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [ZeroT](https://attack.mitre.org/software/S0230) gathers the victim's computer name, Windows version, and system language, and then sends it to its C2 server.[^1]  |
| [[Steganography\|T1001.002]] | Steganography | [ZeroT](https://attack.mitre.org/software/S0230) has retrieved stage 2 payloads as Bitmap images that use Least Significant Bit (LSB) steganography.[^2] [^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [ZeroT](https://attack.mitre.org/software/S0230) has used HTTP for C2.[^2] [^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | Some [ZeroT](https://attack.mitre.org/software/S0230) DLL files have been packed with UPX.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [ZeroT](https://attack.mitre.org/software/S0230) can download additional payloads onto the victim.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [ZeroT](https://attack.mitre.org/software/S0230) has used RC4 to encrypt C2 traffic.[^2] [^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [ZeroT](https://attack.mitre.org/software/S0230) has encrypted its payload with RC4.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA459\|G0062]] | TA459 |



## References

[^1]: [Proofpoint ZeroT Feb 2017](https://www.proofpoint.com/us/threat-insight/post/APT-targets-russia-belarus-zerot-plugx)


[^2]: [Proofpoint TA459 April 2017](https://www.proofpoint.com/us/threat-insight/post/apt-targets-financial-analysts)


[^3]: ZeroT


