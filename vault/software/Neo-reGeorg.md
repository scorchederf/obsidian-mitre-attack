---
aliases: 
    - S1189
    
mitre-attack: https://attack.mitre.org/software/S1189
---

## S1189

[Neo-reGeorg](https://attack.mitre.org/software/S1189) is an open-source web shell designed as a restructuring of [reGeorg](https://attack.mitre.org/software/S1187) with improved usability, security, and fixes for exising [reGeorg](https://attack.mitre.org/software/S1187) bugs.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Neo-reGeorg](https://attack.mitre.org/software/S1189) can tunnel data in and out of targeted networks.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Neo-reGeorg](https://attack.mitre.org/software/S1189) has the ability to download files to targeted systems.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Neo-reGeorg](https://attack.mitre.org/software/S1189) can create multiple TCP connections for a single session.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Neo-reGeorg](https://attack.mitre.org/software/S1189) can use customized HTTP headers.[^1]  |
| [[Proxy\|T1090]] | Proxy | [Neo-reGeorg](https://attack.mitre.org/software/S1189) has the ability to establish a SOCKS5 proxy on a compromised web server.[^1]  |
| [[Python\|T1059.006]] | Python | [Neo-reGeorg](https://attack.mitre.org/software/S1189) is a Python-based web shell.[^1]  |
| [[Non-Standard Encoding\|T1132.002]] | Non-Standard Encoding | [Neo-reGeorg](https://attack.mitre.org/software/S1189) can use modified Base64 encoding to obfuscate communications.[^1]  |
| [[Web Shell\|T1505.003]] | Web Shell | [Neo-reGeorg](https://attack.mitre.org/software/S1189) can be installed on compromised web servers to tunnel C2 connections.[^1] [^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Sandworm Team\|G0034]] | Sandworm Team |



## References

[^1]: [GitHub Neo-reGeorg 2019](https://github.com/L-codes/Neo-reGeorg/blob/master/README-en.md)


[^2]: [Mandiant-Sandworm-Ukraine-2022](https://www.mandiant.com/resources/blog/sandworm-disrupts-power-ukraine-operational-technology)


