---
aliases: 
    - S0699
    
mitre-attack: https://attack.mitre.org/software/S0699
---

## S0699

[Mythic](https://attack.mitre.org/software/S0699) is an open source, cross-platform post-exploitation/command and control platform. [Mythic](https://attack.mitre.org/software/S0699) is designed to "plug-n-play" with various agents and communication channels.[^1] [^4] [^3]  Deployed [Mythic](https://attack.mitre.org/software/S0699) C2 servers have been observed as part of potentially malicious infrastructure.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[External Proxy\|T1090.002]] | External Proxy | [Mythic](https://attack.mitre.org/software/S0699) can leverage a modified SOCKS5 proxy to tunnel egress C2 traffic.[^3]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [Mythic](https://attack.mitre.org/software/S0699) supports SMB-based peer-to-peer C2 profiles.[^3] 	 |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Mythic](https://attack.mitre.org/software/S0699) supports SSL encrypted C2.[^3] 	 |
| [[DNS\|T1071.004]] | DNS | [Mythic](https://attack.mitre.org/software/S0699) supports DNS-based C2 profiles.[^3] 	 |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Mythic](https://attack.mitre.org/software/S0699) supports HTTP-based C2 profiles.[^3] 	 |
| [[Data Encoding\|T1132]] | Data Encoding | [Mythic](https://attack.mitre.org/software/S0699) provides various transform functions to encode and/or randomize C2 data.[^3] 	 |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [Mythic](https://attack.mitre.org/software/S0699) can leverage a peer-to-peer C2 profile between agents.[^3] 		 |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Mythic](https://attack.mitre.org/software/S0699) supports WebSocket and TCP-based C2 profiles.[^3] 	 |
| [[Data Transfer Size Limits\|T1030]] | Data Transfer Size Limits | [Mythic](https://attack.mitre.org/software/S0699) supports custom chunk sizes used to upload/download files.[^3] 	 |
| [[Automated Collection\|T1119]] | Automated Collection | [Mythic](https://attack.mitre.org/software/S0699) supports scripting of file downloads from agents.[^3] 	 |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Mythic](https://attack.mitre.org/software/S0699) can use SOCKS proxies to tunnel traffic through another protocol.[^3]  |
| [[Domain Fronting\|T1090.004]] | Domain Fronting | [Mythic](https://attack.mitre.org/software/S0699) supports domain fronting via custom request headers.[^3] 	 |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Mythic](https://attack.mitre.org/software/S0699) can use a list of C2 URLs as fallback mechanisms in case one IP or domain gets blocked.[^3] 	 |




## References

[^1]: [Mythic Github](https://github.com/its-a-feature/Mythic)


[^2]: [RecordedFuture 2021 Ad Infra](https://go.recordedfuture.com/hubfs/reports/cta-2022-0118.pdf)


[^3]: [Mythc Documentation](https://docs.mythic-c2.net/)


[^4]: [Mythic SpecterOps](https://posts.specterops.io/a-change-of-mythic-proportions-21debeb03617)


