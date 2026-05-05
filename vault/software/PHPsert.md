---
aliases: 
    - S9028
    
mitre-attack: https://attack.mitre.org/software/S9028
---

## S9028

[PHPsert](https://attack.mitre.org/software/S9028) is a webshell used to execute PHP code that has been in use since at least 2023 against targets in Japan, Singapore, Peru, Taiwan, Iran, Republic of Korea, and the Philippines. [PHPsert](https://attack.mitre.org/software/S9028) is not typically deployed as a standalone but integrated into web content such as text editors and content management systems.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [PHPsert](https://attack.mitre.org/software/S9028) has the ability to decode and decrypt obfuscated strings prior to execution.[^1]  |
| [[Web Shell\|T1505.003]] | Web Shell | [PHPsert](https://attack.mitre.org/software/S9028) can use the .php assert function to execute attacker-provided code and maintain persistence on targeted web servers.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [PHPsert](https://attack.mitre.org/software/S9028) has the ability to retrieve remote payloads.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols |  [PHPsert](https://attack.mitre.org/software/S9028) can retrieve remote files using HTTP POST.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [PHPsert](https://attack.mitre.org/software/S9028) can use multiple obfuscation techniques including XOR encoding, hexadecimal character representation, string concatenation, and randomized variable names.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [PHPsert](https://attack.mitre.org/software/S9028) can use Base64-encoded values in C2 communications.[^1]  |




## References

[^1]: [sentinelone operationDigitalEye Dec 2024](https://www.sentinelone.com/labs/operation-digital-eye-chinese-apt-compromises-critical-digital-infrastructure-via-visual-studio-code-tunnels/)


