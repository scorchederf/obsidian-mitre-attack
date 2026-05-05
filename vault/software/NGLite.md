---
aliases: 
    - S1106
    
mitre-attack: https://attack.mitre.org/software/S1106
---

## S1106

[NGLite](https://attack.mitre.org/software/S1106) is a backdoor Trojan that is only capable of running commands received through its C2 channel. While the capabilities are standard for a backdoor, NGLite uses a novel C2 channel that leverages a decentralized network based on the legitimate NKN to communicate between the backdoor and the actors.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [NGLite](https://attack.mitre.org/software/S1106) will initially beacon out to the NKN network via an HTTP POST over TCP 30003.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [NGLite](https://attack.mitre.org/software/S1106) will run the `whoami` command to gather system information and return this to the command and control server.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [NGLite](https://attack.mitre.org/software/S1106) will use an AES encrypted channel for command and control purposes, in one case using the key `WHATswrongwithUu`.[^1]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [NGLite](https://attack.mitre.org/software/S1106) has abused NKN infrastructure for its C2 communication.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [NGLite](https://attack.mitre.org/software/S1106) identifies the victim system MAC and IPv4 addresses and uses these to establish a victim identifier.[^1]  |




## References

[^1]: [NGLite Trojan](https://unit42.paloaltonetworks.com/manageengine-godzilla-nglite-kdcsponge/)


