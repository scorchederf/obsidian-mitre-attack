---
aliases: 
    - S1123
    
mitre-attack: https://attack.mitre.org/software/S1123
---

## S1123

[PITSTOP](https://attack.mitre.org/software/S1123) is a backdoor that was deployed on compromised Ivanti Connect Secure VPNs during [Cutting Edge](https://attack.mitre.org/campaigns/C0029) to enable command execution and file read/write.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [PITSTOP](https://attack.mitre.org/software/S1123) has the ability to communicate over TLS.[^1]  |
| [[Inter-Process Communication\|T1559]] | Inter-Process Communication | [PITSTOP](https://attack.mitre.org/software/S1123) can listen over the Unix domain socket located at `/data/runtime/cockpit/wd.fd`.[^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [PITSTOP](https://attack.mitre.org/software/S1123) has the ability to receive shell commands over a Unix domain socket.[^1]  |
| [[Socket Filters\|T1205.002]] | Socket Filters | [PITSTOP](https://attack.mitre.org/software/S1123) can listen and evaluate incoming commands on the domain socket, created by PITHOOK malware, located at `/data/runtime/cockpit/wd.fd` for a predefined magic byte sequence. [PITSTOP](https://attack.mitre.org/software/S1123) can then duplicate the socket for further communication over TLS.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [PITSTOP](https://attack.mitre.org/software/S1123) can deobfuscate base64 encoded and AES encrypted commands.[^1]  |




## References

[^1]: [Mandiant Cutting Edge Part 3 February 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)


