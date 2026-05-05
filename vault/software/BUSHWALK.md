---
aliases: 
    - S1118
    
mitre-attack: https://attack.mitre.org/software/S1118
---

## S1118

[BUSHWALK](https://attack.mitre.org/software/S1118) is a web shell written in Perl that was inserted into the legitimate querymanifest.cgi file on compromised Ivanti Connect Secure VPNs during [Cutting Edge](https://attack.mitre.org/campaigns/C0029).[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BUSHWALK](https://attack.mitre.org/software/S1118) can write malicious payloads sent through a web request’s command parameter.[^2] [^1]  |
| [[Traffic Signaling\|T1205]] | Traffic Signaling | [BUSHWALK](https://attack.mitre.org/software/S1118) can modify the `DSUserAgentCap.pm` Perl module on Ivanti Connect Secure VPNs and either activate or deactivate depending on the value of the user agent in incoming HTTP requests.[^1]  |
| [[Web Shell\|T1505.003]] | Web Shell | [BUSHWALK](https://attack.mitre.org/software/S1118) is a web shell that has the ability to execute arbitrary commands or write files.[^2]  |
| [[Compromise Host Software Binary\|T1554]] | Compromise Host Software Binary | [BUSHWALK](https://attack.mitre.org/software/S1118) can embed into the legitimate `querymanifest.cgi` file on compromised Ivanti Connect Secure VPNs.[^2] [^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [BUSHWALK](https://attack.mitre.org/software/S1118) can Base64 decode and RC4 decrypt malicious payloads sent through a web request’s command parameter.[^2] [^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [BUSHWALK](https://attack.mitre.org/software/S1118) can encrypt the resulting data generated from C2 commands with RC4.[^2]  |




## References

[^1]: [Mandiant Cutting Edge Part 3 February 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)


[^2]: [Mandiant Cutting Edge Part 2 January 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)


