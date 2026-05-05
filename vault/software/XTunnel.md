---
aliases: 
    - S0117
    
mitre-attack: https://attack.mitre.org/software/S0117
---

## S0117

[XTunnel](https://attack.mitre.org/software/S0117) a VPN-like network proxy tool that can relay traffic between a C2 server and a victim. It was first seen in May 2013 and reportedly used by [APT28](https://attack.mitre.org/groups/G0007) during the compromise of the Democratic National Committee. [^1]  [^6]  [^8] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [XTunnel](https://attack.mitre.org/software/S0117) is capable of accessing locally stored passwords on victims.[^6]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | A version of [XTunnel](https://attack.mitre.org/software/S0117) introduced in July 2015 inserted junk code into the binary in a likely attempt to obfuscate it and bypass security products.[^8]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [XTunnel](https://attack.mitre.org/software/S0117) has been used to execute remote commands.[^1]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [XTunnel](https://attack.mitre.org/software/S0117) is capable of probing the network for open ports.[^6]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [XTunnel](https://attack.mitre.org/software/S0117) uses SSL/TLS and RC4 to encrypt traffic.[^6] [^8]  |
| [[Proxy\|T1090]] | Proxy | [XTunnel](https://attack.mitre.org/software/S0117) relays traffic between a C2 server and a victim.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | A version of [XTunnel](https://attack.mitre.org/software/S0117) introduced in July 2015 obfuscated the binary using opaque predicates and other techniques in a likely attempt to obfuscate it and bypass security products.[^8]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | The C2 server used by [XTunnel](https://attack.mitre.org/software/S0117) provides a port number to the victim to use as a fallback in case the connection closes on the currently used port.[^8]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT28\|G0007]] | APT28 |



## References

[^1]: [Crowdstrike DNC June 2016](https://www.crowdstrike.com/blog/bears-midst-intrusion-democratic-national-committee/)


[^2]: [US District Court Indictment GRU Oct 2018](https://www.justice.gov/opa/page/file/1098481/download)


[^3]: XTunnel


[^4]: Trojan.Shunnael


[^5]: [Secureworks IRON TWILIGHT Active Measures March 2017](https://www.secureworks.com/research/iron-twilight-supports-active-measures)


[^6]: [Invincea XTunnel](https://www.invincea.com/2016/07/tunnel-of-gov-dnc-hack-and-the-russian-xtunnel/)


[^7]: [Symantec APT28 Oct 2018](https://www.symantec.com/blogs/election-security/apt28-espionage-military-government)


[^8]: [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)


[^9]: X-Tunnel


[^10]: [ESET Sednit Part 3](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part3.pdf)


[^11]: XAPS


