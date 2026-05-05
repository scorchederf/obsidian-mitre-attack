---
aliases: 
    - S1051
    
mitre-attack: https://attack.mitre.org/software/S1051
---

## S1051

[KEYPLUG](https://attack.mitre.org/software/S1051) is a modular backdoor written in C++, with Windows and Linux variants, that has been used by [APT41](https://attack.mitre.org/groups/G0096) since at least June 2021.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [KEYPLUG](https://attack.mitre.org/software/S1051) has the ability to communicate over HTTP and WebSocket Protocol (WSS) for C2.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [KEYPLUG](https://attack.mitre.org/software/S1051) can obtain the current tick count of an infected computer.[^1]  |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | The [KEYPLUG](https://attack.mitre.org/software/S1051) Windows variant has retrieved C2 addresses from encoded data in posts on tech community forums.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [KEYPLUG](https://attack.mitre.org/software/S1051) can use a hardcoded one-byte XOR encoded configuration file.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [KEYPLUG](https://attack.mitre.org/software/S1051) can decode its configuration file to determine C2 protocols.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [KEYPLUG](https://attack.mitre.org/software/S1051) can use TLS-encrypted WebSocket Protocol (WSS) for C2.[^1]  |
| [[Proxy\|T1090]] | Proxy | [KEYPLUG](https://attack.mitre.org/software/S1051) has used Cloudflare CDN associated infrastructure to redirect C2 communications to malicious domains.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | <br>[KEYPLUG](https://attack.mitre.org/software/S1051) can use TCP and KCP (KERN Communications Protocol) over UDP for C2 communication.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT41\|G0096]] | APT41 |



## References

[^1]: [Mandiant APT41](https://www.mandiant.com/resources/apt41-us-state-governments)


[^2]: KEYPLUG.LINUX


