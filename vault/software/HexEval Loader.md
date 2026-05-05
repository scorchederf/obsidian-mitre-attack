---
aliases: 
    - S1249
    
mitre-attack: https://attack.mitre.org/software/S1249
---

## S1249

[HexEval Loader](https://attack.mitre.org/software/S1249) is a hex-encoded loader that collects host data, decodes follow-on scripts and acts as a downloader for the [BeaverTail](https://attack.mitre.org/software/S1246) malware.  [HexEval Loader](https://attack.mitre.org/software/S1249) was first reported in April 2025.  [HexEval Loader](https://attack.mitre.org/software/S1249) has previously been leveraged by North Korea-affiliated threat actors identified as [Contagious Interview](https://attack.mitre.org/groups/G1052).  [HexEval Loader](https://attack.mitre.org/software/S1249) has been delivered to victims through code repository sites utilizing typosquatting naming conventions of various npm packages.[^3] [^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [HexEval Loader](https://attack.mitre.org/software/S1249) has identified the OS and MAC address of victim device through host fingerprinting scripting.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [HexEval Loader](https://attack.mitre.org/software/S1249) has utilized a cross-platform keylogger that has the capability to capture keystrokes on Windows, macOS and Linux systems.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [HexEval Loader](https://attack.mitre.org/software/S1249) has been used to download a malicious payload to include [BeaverTail](https://attack.mitre.org/software/S1246).[^3] [^2] [^1]  |
| [[JavaScript\|T1059.007]] | JavaScript | [HexEval Loader](https://attack.mitre.org/software/S1249) has executed malicious JavaScript code.[^3] [^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [HexEval Loader](https://attack.mitre.org/software/S1249) has encoded module names and C2 URLs as hexadecimal strings in attempts to evade analysis.[^3] [^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [HexEval Loader](https://attack.mitre.org/software/S1249) has leveraged server-side client configurations to identify the public IP of the victim host.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [HexEval Loader](https://attack.mitre.org/software/S1249) has exfiltrated victim data using HTTPS POST requests to its C2 servers.[^3] [^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [HexEval Loader](https://attack.mitre.org/software/S1249) has masqueraded and typosquatted as legitimate code repository packages and projects.[^3] [^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [HexEval Loader](https://attack.mitre.org/software/S1249) has collected the username from the victim host.[^1]  |
| [[System Location Discovery\|T1614]] | System Location Discovery | [HexEval Loader](https://attack.mitre.org/software/S1249) has a function where the C2 endpoint can identify the geographical location of a victim host based on request headers, execution environment and runtime conditions.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [HexEval Loader](https://attack.mitre.org/software/S1249) has used HTTP and HTTPS POST requests to communicate with C2.[^3] [^2] [^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [HexEval Loader](https://attack.mitre.org/software/S1249) has decoded its payload prior to execution.[^3] [^2] [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Contagious Interview\|G1052]] | Contagious Interview |



## References

[^1]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)


[^2]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)


[^3]: [Socket Contagious Interview NPM April 2025](https://socket.dev/blog/lazarus-expands-malicious-npm-campaign-11-new-packages-add-malware-loaders-and-bitbucket)


