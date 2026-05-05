---
aliases: 
    - S0187
    
mitre-attack: https://attack.mitre.org/software/S0187
---

## S0187

[Daserf](https://attack.mitre.org/software/S0187) is a backdoor that has been used to spy on and steal from Japanese, South Korean, Russian, Singaporean, and Chinese victims. Researchers have identified versions written in both Visual C and Delphi. [^2]  [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Daserf](https://attack.mitre.org/software/S0187) can execute shell commands.[^2] [^1]  |
| [[Code Signing\|T1553.002]] | Code Signing | Some [Daserf](https://attack.mitre.org/software/S0187) samples were signed with a stolen digital certificate.[^6]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Daserf](https://attack.mitre.org/software/S0187) can download remote files.[^2] [^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | A version of [Daserf](https://attack.mitre.org/software/S0187) uses the MPRESS packer.[^2]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Daserf](https://attack.mitre.org/software/S0187) uses custom base64 encoding to obfuscate HTTP traffic.[^1]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Daserf](https://attack.mitre.org/software/S0187) hides collected data in password-protected .rar archives.[^6]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Daserf](https://attack.mitre.org/software/S0187) can take screenshots.[^2] [^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Daserf](https://attack.mitre.org/software/S0187) uses encrypted Windows APIs and also encrypts data using the alternative base64+RC4 or the Caesar cipher.[^2]  |
| [[Steganography\|T1001.002]] | Steganography | [Daserf](https://attack.mitre.org/software/S0187) can use steganography to hide malicious code downloaded to the victim.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Daserf](https://attack.mitre.org/software/S0187) uses RC4 encryption to obfuscate HTTP traffic.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Daserf](https://attack.mitre.org/software/S0187) uses file and folder names related to legitimate programs in order to blend in, such as HP, Intel, Adobe, and perflogs.[^6]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Daserf](https://attack.mitre.org/software/S0187) can log keystrokes.[^2] [^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Daserf](https://attack.mitre.org/software/S0187) uses HTTP for C2.[^1]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Daserf](https://attack.mitre.org/software/S0187) leverages [Mimikatz](https://attack.mitre.org/software/S0002) and [Windows Credential Editor](https://attack.mitre.org/software/S0005) to steal credentials.[^6]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Daserf](https://attack.mitre.org/software/S0187) hides collected data in password-protected .rar archives.[^6]  |
| [[Indicator Removal from Tools\|T1027.005]] | Indicator Removal from Tools | Analysis of [Daserf](https://attack.mitre.org/software/S0187) has shown that it regularly undergoes technical improvements to evade anti-virus detection.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[BRONZE BUTLER\|G0060]] | BRONZE BUTLER |



## References

[^1]: [Secureworks BRONZE BUTLER Oct 2017](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)


[^2]: [Trend Micro Daserf Nov 2017](http://blog.trendmicro.com/trendlabs-security-intelligence/redbaldknight-bronze-butler-daserf-backdoor-now-using-steganography/)


[^3]: Muirim


[^4]: Daserf


[^5]: Nioupale


[^6]: [Symantec Tick Apr 2016](https://www.symantec.com/connect/blogs/tick-cyberespionage-group-zeros-japan)


