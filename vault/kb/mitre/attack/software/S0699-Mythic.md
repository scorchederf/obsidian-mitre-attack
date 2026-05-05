---
aliases: 
    - S0699
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0699-Mythic
---

## Description

[[kb/mitre/attack/software/S0699-Mythic\|Mythic]] is an open source, cross-platform post-exploitation/command and control platform. [[kb/mitre/attack/software/S0699-Mythic\|Mythic]] is designed to "plug-n-play" with various agents and communication channels.[^4] [^1] [^3]  Deployed [[kb/mitre/attack/software/S0699-Mythic\|Mythic]] C2 servers have been observed as part of potentially malicious infrastructure.[^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1008-Fallback_Channels\|T1008]] | Fallback Channels | [[kb/mitre/attack/software/S0699-Mythic\|Mythic]] can use a list of C2 URLs as fallback mechanisms in case one IP or domain gets blocked.[^3] 	 |
| [[kb/mitre/attack/techniques/T1030-Data_Transfer_Size_Limits\|T1030]] | Data Transfer Size Limits | [[kb/mitre/attack/software/S0699-Mythic\|Mythic]] supports custom chunk sizes used to upload/download files.[^3] 	 |
| [[kb/mitre/attack/techniques/T1071.001-Web_Protocols\|T1071.001]] | Web Protocols | [[kb/mitre/attack/software/S0699-Mythic\|Mythic]] supports HTTP-based C2 profiles.[^3] 	 |
| [[kb/mitre/attack/techniques/T1071.002-File_Transfer_Protocols\|T1071.002]] | File Transfer Protocols | [[kb/mitre/attack/software/S0699-Mythic\|Mythic]] supports SMB-based peer-to-peer C2 profiles.[^3] 	 |
| [[kb/mitre/attack/techniques/T1071.004-DNS\|T1071.004]] | DNS | [[kb/mitre/attack/software/S0699-Mythic\|Mythic]] supports DNS-based C2 profiles.[^3] 	 |
| [[kb/mitre/attack/techniques/T1090.001-Internal_Proxy\|T1090.001]] | Internal Proxy | [[kb/mitre/attack/software/S0699-Mythic\|Mythic]] can leverage a peer-to-peer C2 profile between agents.[^3] 		 |
| [[kb/mitre/attack/techniques/T1090.002-External_Proxy\|T1090.002]] | External Proxy | [[kb/mitre/attack/software/S0699-Mythic\|Mythic]] can leverage a modified SOCKS5 proxy to tunnel egress C2 traffic.[^3]  |
| [[kb/mitre/attack/techniques/T1090.004-Domain_Fronting\|T1090.004]] | Domain Fronting | [[kb/mitre/attack/software/S0699-Mythic\|Mythic]] supports domain fronting via custom request headers.[^3] 	 |
| [[kb/mitre/attack/techniques/T1095-Non-Application_Layer_Protocol\|T1095]] | Non-Application Layer Protocol | [[kb/mitre/attack/software/S0699-Mythic\|Mythic]] supports WebSocket and TCP-based C2 profiles.[^3] 	 |
| [[kb/mitre/attack/techniques/T1119-Automated_Collection\|T1119]] | Automated Collection | [[kb/mitre/attack/software/S0699-Mythic\|Mythic]] supports scripting of file downloads from agents.[^3] 	 |
| [[kb/mitre/attack/techniques/T1132-Data_Encoding\|T1132]] | Data Encoding | [[kb/mitre/attack/software/S0699-Mythic\|Mythic]] provides various transform functions to encode and/or randomize C2 data.[^3] 	 |
| [[kb/mitre/attack/techniques/T1572-Protocol_Tunneling\|T1572]] | Protocol Tunneling | [[kb/mitre/attack/software/S0699-Mythic\|Mythic]] can use SOCKS proxies to tunnel traffic through another protocol.[^3]  |
| [[kb/mitre/attack/techniques/T1573.002-Asymmetric_Cryptography\|T1573.002]] | Asymmetric Cryptography | [[kb/mitre/attack/software/S0699-Mythic\|Mythic]] supports SSL encrypted C2.[^3] 	 |





> [!info]- References
> [^1]: [Mythic SpecterOps](https://posts.specterops.io/a-change-of-mythic-proportions-21debeb03617)

> [^2]: [RecordedFuture 2021 Ad Infra](https://go.recordedfuture.com/hubfs/reports/cta-2022-0118.pdf)

> [^3]: [Mythc Documentation](https://docs.mythic-c2.net/)

> [^4]: [Mythic Github](https://github.com/its-a-feature/Mythic)


