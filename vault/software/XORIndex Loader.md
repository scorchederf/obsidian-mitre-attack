---
aliases: 
    - S1248
    
mitre-attack: https://attack.mitre.org/software/S1248
---

## S1248

[XORIndex Loader](https://attack.mitre.org/software/S1248) is a XOR-encoded loader that collects host data, decodes follow-on scripts and acts as a downloader for the [BeaverTail](https://attack.mitre.org/software/S1246) malware.  [XORIndex Loader](https://attack.mitre.org/software/S1248) was first reported in June 2025.  [XORIndex Loader](https://attack.mitre.org/software/S1248) has been leveraged by North Korea-affiliated threat actors identified as [Contagious Interview](https://attack.mitre.org/groups/G1052).  [XORIndex Loader](https://attack.mitre.org/software/S1248) has been delivered to victims through code repository sites utilizing typo squatting naming conventions of various npm packages.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [XORIndex Loader](https://attack.mitre.org/software/S1248) has the ability to collect the hostname, OS Username, Geolocation, and OS version of an infected host.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [XORIndex Loader](https://attack.mitre.org/software/S1248) can decode its payload prior to execution.[^1]  |
| [[System Location Discovery\|T1614]] | System Location Discovery | [XORIndex Loader](https://attack.mitre.org/software/S1248) can identify the geographical location of a victim host.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [XORIndex Loader](https://attack.mitre.org/software/S1248) has leveraged webservices to identify the public IP of the victim host.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [XORIndex Loader](https://attack.mitre.org/software/S1248) has exfiltrated victim data using HTTPS POST requests to its C2 servers.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [XORIndex Loader](https://attack.mitre.org/software/S1248) has been used to download a malicious payload to include [BeaverTail](https://attack.mitre.org/software/S1246).[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [XORIndex Loader](https://attack.mitre.org/software/S1248) has encoded module names and C2 URLs as hexadecimal strings in attempts to evade analysis.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [XORIndex Loader](https://attack.mitre.org/software/S1248) has used HTTPS POST to communicate with C2.[^1]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [XORIndex Loader](https://attack.mitre.org/software/S1248) has obfuscated strings using ASCII buffers and TextDecoder.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [XORIndex Loader](https://attack.mitre.org/software/S1248) has leveraged legitimate package names to mimic frequently utilized tools to entice victims to download and execute malicious payloads.[^1]  |
| [[JavaScript\|T1059.007]] | JavaScript | [XORIndex Loader](https://attack.mitre.org/software/S1248) has executed malicious JavaScript code.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [XORIndex Loader](https://attack.mitre.org/software/S1248) has collected the username from the victim host.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Contagious Interview\|G1052]] | Contagious Interview |



## References

[^1]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)


