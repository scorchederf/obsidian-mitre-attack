---
aliases: 
    - S0048
    
mitre-attack: https://attack.mitre.org/software/S0048
---

## S0048

[PinchDuke](https://attack.mitre.org/software/S0048) is malware that was used by [APT29](https://attack.mitre.org/groups/G0016) from 2008 to 2010. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [PinchDuke](https://attack.mitre.org/software/S0048) searches for files created within a certain timeframe and whose file extension matches a predefined list.[^1]  |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | [PinchDuke](https://attack.mitre.org/software/S0048) steals credentials from compromised hosts. [PinchDuke](https://attack.mitre.org/software/S0048)'s credential stealing functionality is believed to be based on the source code of the Pinch credential stealing malware (also known as LdPinch). Credentials targeted by [PinchDuke](https://attack.mitre.org/software/S0048) include ones associated many sources such as WinInet Credential Cache, and Lightweight Directory Access Protocol (LDAP).[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [PinchDuke](https://attack.mitre.org/software/S0048) transfers files from the compromised host via HTTP or HTTPS to a C2 server.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [PinchDuke](https://attack.mitre.org/software/S0048) gathers system configuration information.[^1]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [PinchDuke](https://attack.mitre.org/software/S0048) steals credentials from compromised hosts. [PinchDuke](https://attack.mitre.org/software/S0048)'s credential stealing functionality is believed to be based on the source code of the Pinch credential stealing malware (also known as LdPinch). Credentials targeted by [PinchDuke](https://attack.mitre.org/software/S0048) include ones associated with many sources such as The Bat!, Yahoo!, Mail.ru, Passport.Net, Google Talk, and Microsoft Outlook.[^1]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [PinchDuke](https://attack.mitre.org/software/S0048) steals credentials from compromised hosts. [PinchDuke](https://attack.mitre.org/software/S0048)'s credential stealing functionality is believed to be based on the source code of the Pinch credential stealing malware (also known as LdPinch). Credentials targeted by [PinchDuke](https://attack.mitre.org/software/S0048) include ones associated with many sources such as Netscape Navigator, Mozilla Firefox, Mozilla Thunderbird, and Internet Explorer. [^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [PinchDuke](https://attack.mitre.org/software/S0048) collects user files from the compromised host based on predefined file extensions.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)


