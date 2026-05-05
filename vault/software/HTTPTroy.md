---
aliases: 
    - S9007
    
mitre-attack: https://attack.mitre.org/software/S9007
---

## S9007

[HTTPTroy](https://attack.mitre.org/software/S9007) is a highly obfuscated backdoor that facilitates collection, command and control, defense evasion and exfiltration.  [HTTPTroy](https://attack.mitre.org/software/S9007) was first reported in October 2025. [HTTPTroy](https://attack.mitre.org/software/S9007) has been observed in operations attributed to DPRK-affiliated threat actors, including [Kimsuky](https://attack.mitre.org/groups/G0094).  [HTTPTroy](https://attack.mitre.org/software/S9007) has been delivered to victims through a separate loader leveraged by [Kimsuky](https://attack.mitre.org/groups/G0094).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [HTTPTroy](https://attack.mitre.org/software/S9007) has the ability to download files from C2 using the `down <FILENAME>` command.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [HTTPTroy](https://attack.mitre.org/software/S9007) has the ability to generate a reverse shell using the command `conn <IP_ADDRESS> <PORT>`.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [HTTPTroy](https://attack.mitre.org/software/S9007) has obfuscated request communications utilizing XOR encryption.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [HTTPTroy](https://attack.mitre.org/software/S9007) has obfuscated strings using Single Instruction Multiple Data (SIMD) instructions to hinder analysis and detection.[^1]  |
| [[Non-Standard Encoding\|T1132.002]] | Non-Standard Encoding | [HTTPTroy](https://attack.mitre.org/software/S9007) has obfuscated HTTP POST request communications utilizing XOR with a designated key of 0x56, followed by Base64 encoding.[^1]  |
| [[Dynamic API Resolution\|T1027.007]] | Dynamic API Resolution | [HTTPTroy](https://attack.mitre.org/software/S9007) has utilized dynamic API resolution by reconstructing API calls during runtime using combinations of arithmetic and logical operations to complicate static analysis.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [HTTPTroy](https://attack.mitre.org/software/S9007) has exfiltrated encrypted data over the C2 channel using the `up <FILENAME>` command.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [HTTPTroy](https://attack.mitre.org/software/S9007) has obtained screen captures leveraging the `screen` command which captures, encrypts and uploads the stolen image to the adversary controlled C2 server.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [HTTPTroy](https://attack.mitre.org/software/S9007) has used HTTP POST requests to communicate with C2.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [HTTPTroy](https://attack.mitre.org/software/S9007) has decoded strings encoded with Base64 and XOR prior to execution.[^1]  |
| [[Native API\|T1106]] | Native API | [HTTPTroy](https://attack.mitre.org/software/S9007) has leveraged Windows Native API calls, including `GetProcAddress` to execute functions in memory.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [HTTPTroy](https://attack.mitre.org/software/S9007) can terminate its running process and then remove traces of itself through the `die <COMMAND>` command.[^1]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [HTTPTroy](https://attack.mitre.org/software/S9007) has leveraged the ability to execute commands with system privileges using the `srun <EXECUTABLE> <ARGS>` command.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Kimsuky\|G0094]] | Kimsuky |



## References

[^1]: [Gen Digital Kimsuky HTTPTroy October 2025](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis)


