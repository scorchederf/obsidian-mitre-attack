---
aliases: 
    - S1144
    
mitre-attack: https://attack.mitre.org/software/S1144
---

## S1144

[FRP](https://attack.mitre.org/software/S1144), which stands for Fast Reverse Proxy, is an openly available tool that is capable of exposing a server located behind a firewall or Network Address Translation (NAT) to the Internet. [FRP](https://attack.mitre.org/software/S1144) can support multiple protocols including TCP, UDP, and HTTP(S) and has been abused by threat actors to proxy command and control communications.[^5] [^3] [^4] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [FRP](https://attack.mitre.org/software/S1144) can communicate over TCP, TCP stream multiplexing, KERN Communications Protocol (KCP), QUIC, and UDP.[^5]  |
| [[JavaScript\|T1059.007]] | JavaScript | [FRP](https://attack.mitre.org/software/S1144) can support the use of a JSON configuration file.[^5]  |
| [[Proxy\|T1090]] | Proxy | [FRP](https://attack.mitre.org/software/S1144) can proxy communications through a server in public IP space to local servers located behind a NAT or firewall.[^5]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [FRP](https://attack.mitre.org/software/S1144) can tunnel SSH and Unix Domain Socket communications over TCP between external nodes and exposed resources behind firewalls or NAT.[^5]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [FRP](https://attack.mitre.org/software/S1144) can be configured to only accept TLS connections.[^5]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | As part of load balancing [FRP](https://attack.mitre.org/software/S1144) can set `healthCheck.type = "tcp"` or `healthCheck.type = "http"` to check service status on specific hosts with TCPing or an HTTP request.[^5]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [FRP](https://attack.mitre.org/software/S1144) can use a dashboard and U/I to display the status of connections from the FRP client and server.[^5]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | The [FRP](https://attack.mitre.org/software/S1144) client can be configured to connect to the server through a proxy.[^5]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [FRP](https://attack.mitre.org/software/S1144) can use STCP (Secret TCP) with a preshared key to encrypt services exposed to public networks.[^5]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [FRP](https://attack.mitre.org/software/S1144) has the ability to use HTTP and HTTPS to enable the forwarding of requests for internal services via domain name.[^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Blue Mockingbird\|G0108]] | Blue Mockingbird |
| [[Magic Hound\|G0059]] | Magic Hound |
| [[Volt Typhoon\|G1017]] | Volt Typhoon |



## References

[^1]: [Microsoft Volt Typhoon May 2023](https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/)


[^2]: [DFIR Phosphorus November 2021](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)


[^3]: [Joint Cybersecurity Advisory Volt Typhoon June 2023](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)


[^4]: [RedCanary Mockingbird May 2020](https://redcanary.com/blog/blue-mockingbird-cryptominer/)


[^5]: [FRP GitHub](https://github.com/fatedier/frp)


