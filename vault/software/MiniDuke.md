---
aliases: 
    - S0051
    
mitre-attack: https://attack.mitre.org/software/S0051
---

## S0051

[MiniDuke](https://attack.mitre.org/software/S0051) is malware that was used by [APT29](https://attack.mitre.org/groups/G0016) from 2010 to 2015. The [MiniDuke](https://attack.mitre.org/software/S0051) toolset consists of multiple downloader and backdoor components. The loader has been used with other [MiniDuke](https://attack.mitre.org/software/S0051) components as well as in conjunction with [CosmicDuke](https://attack.mitre.org/software/S0050) and [PinchDuke](https://attack.mitre.org/software/S0048). [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | Some [MiniDuke](https://attack.mitre.org/software/S0051) components use Twitter to initially obtain the address of a C2 server or as a backup if no hard-coded C2 server responds.[^4] [^2] [^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [MiniDuke](https://attack.mitre.org/software/S0051) can gather the hostname on a compromised machine.[^1]  |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [MiniDuke](https://attack.mitre.org/software/S0051) can use DGA to generate new Twitter URLs for C2.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [MiniDuke](https://attack.mitre.org/software/S0051) can use control flow flattening to obscure code.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [MiniDuke](https://attack.mitre.org/software/S0051) uses Google Search to identify C2 servers if its primary C2 method via Twitter is not working.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [MiniDuke](https://attack.mitre.org/software/S0051) can download additional encrypted backdoors onto the victim via GIF files.[^2] [^1]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [MiniDuke](https://attack.mitre.org/software/S0051) can can use a named pipe to forward communications from one compromised machine with internet access to other compromised machines.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [MiniDuke](https://attack.mitre.org/software/S0051) can enumerate local drives.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [MiniDuke](https://attack.mitre.org/software/S0051) uses HTTP and HTTPS for command and control.[^4] [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)


[^2]: [Securelist MiniDuke Feb 2013](https://web.archive.org/web/20170630181406/https://cdn.securelist.com/files/2014/07/themysteryofthepdf0-dayassemblermicrobackdoor.pdf)


[^3]: [Secureworks IRON HEMLOCK Profile](http://www.secureworks.com/research/threat-profiles/iron-hemlock)


[^4]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)


