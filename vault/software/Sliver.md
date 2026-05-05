---
aliases: 
    - S0633
    
mitre-attack: https://attack.mitre.org/software/S0633
---

## S0633

[Sliver](https://attack.mitre.org/software/S0633) is an open source, cross-platform, red team command and control (C2) framework written in Golang. [Sliver](https://attack.mitre.org/software/S0633) includes its own package manager, "armory," for staging and downloading additional tools and payloads to the primary C2 framework.[^9] [^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Sliver](https://attack.mitre.org/software/S0633) obfuscates configuration and other static files using native Go libraries such as `garble` and `gobfuscate` to inhibit configuration analysis and static detection.[^3]  |
| [[Process Injection\|T1055]] | Process Injection | [Sliver](https://attack.mitre.org/software/S0633) includes multiple methods to perform process injection to migrate the framework into other, potentially privileged processes on the victim machine.[^3] [^5] [^9] [^13]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Sliver](https://attack.mitre.org/software/S0633) can enumerate files on a target system.[^2]  |
| [[Compile After Delivery\|T1027.004]] | Compile After Delivery | [Sliver](https://attack.mitre.org/software/S0633) includes functionality to retrieve source code and compile locally prior to execution in victim environments.[^5]  |
| [[Steganography\|T1001.002]] | Steganography | [Sliver](https://attack.mitre.org/software/S0633) can encode binary data into a .PNG file for C2 communication.[^15]  |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [Sliver](https://attack.mitre.org/software/S0633) has the ability to manipulate user tokens on targeted Windows systems.[^9] [^13]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Sliver](https://attack.mitre.org/software/S0633) has built-in functionality to launch a Powershell command prompt.[^5]  |
| [[DNS\|T1071.004]] | DNS | [Sliver](https://attack.mitre.org/software/S0633) can support C2 communications over DNS.[^4] [^9] [^14] [^5] [^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Sliver](https://attack.mitre.org/software/S0633) can encrypt strings at compile time.[^9] [^13]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Sliver](https://attack.mitre.org/software/S0633) can use mutual TLS and RSA  cryptography to exchange a session key.[^4] [^9] [^7] [^5] [^3]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [Sliver](https://attack.mitre.org/software/S0633) has a built-in SOCKS5 proxying capability allowing for [Sliver](https://attack.mitre.org/software/S0633) clients to proxy network traffic through other clients within a victim network.[^5]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Sliver](https://attack.mitre.org/software/S0633) has the ability to gather network configuration information.[^16]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Sliver](https://attack.mitre.org/software/S0633) can take screenshots of the victim’s active display.[^8]  |
| [[Web Protocols\|T1071.001]] | Web Protocols |  [Sliver](https://attack.mitre.org/software/S0633) has the ability to support C2 communications over HTTP and HTTPS.[^4] [^9] [^13] [^5] [^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Sliver](https://attack.mitre.org/software/S0633) can download additional content and files from the [Sliver](https://attack.mitre.org/software/S0633) server to the client residing on the victim machine using the `upload` command.[^1] [^5]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Sliver](https://attack.mitre.org/software/S0633) can use AES-GCM-256 to encrypt a session key for C2 message exchange.[^7]  |
| [[Application Layer Protocol\|T1071]] | Application Layer Protocol | [Sliver](https://attack.mitre.org/software/S0633) can utilize the Wireguard VPN protocol for command and control.[^5]  |
| [[Golden Ticket\|T1558.001]] | Golden Ticket | [Sliver](https://attack.mitre.org/software/S0633) incorporates the [Rubeus](https://attack.mitre.org/software/S1071) framework to allow for Kerberos ticket manipulation, specifically for forging Kerberos Golden Tickets.[^5]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Sliver](https://attack.mitre.org/software/S0633) can exfiltrate files from the victim using the `download` command.[^10]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Sliver](https://attack.mitre.org/software/S0633) can leverage multiple techniques to bypass User Account Control (UAC) on Windows systems.[^5]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Sliver](https://attack.mitre.org/software/S0633) can use standard encoding techniques like gzip and hex to ASCII to encode the C2 communication payload.[^15]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Sliver](https://attack.mitre.org/software/S0633) has a built-in `procdump` command allowing for retrieval of memory from processes such as `lsass.exe` for credential harvesting.[^5]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Sliver](https://attack.mitre.org/software/S0633) can collect network connection information.[^12]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Cinnamon Tempest\|G1021]] | Cinnamon Tempest |
| [[TA551\|G0127]] | TA551 |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [GitHub Sliver Upload](https://github.com/BishopFox/sliver/blob/ea329226636ab8e470086a17f13aa8d330baad22/client/command/filesystem/upload.go)


[^2]: [GitHub Sliver File System August 2021](https://github.com/BishopFox/sliver/tree/master/client/command/filesystem)


[^3]: [Microsoft Sliver 2022](https://www.microsoft.com/en-us/security/blog/2022/08/24/looking-for-the-sliver-lining-hunting-for-emerging-command-and-control-frameworks/)


[^4]: [Cybersecurity Advisory SVR TTP May 2021](https://www.ncsc.gov.uk/files/Advisory-further-TTPs-associated-with-SVR-cyber-actors.pdf)


[^5]: [Cybereason Sliver Undated](https://www.cybereason.com/blog/sliver-c2-leveraged-by-many-threat-actors)


[^6]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^7]: [GitHub Sliver Encryption](https://github.com/BishopFox/sliver/wiki/Transport-Encryption)


[^8]: [GitHub Sliver Screen](https://github.com/BishopFox/sliver/blob/master/implant/sliver/screen/screenshot_windows.go)


[^9]: [Bishop Fox Sliver Framework August 2019](https://labs.bishopfox.com/tech-blog/sliver)


[^10]: [GitHub Sliver Download](https://github.com/BishopFox/sliver/blob/7489c69962b52b09ed377d73d142266564845297/client/command/filesystem/download.go)


[^11]: [Secureworks IRON HEMLOCK Profile](http://www.secureworks.com/research/threat-profiles/iron-hemlock)


[^12]: [GitHub Sliver Netstat](https://github.com/BishopFox/sliver/tree/58a56a077f0813bb312f9fa4df7453b510c3a73b/implant/sliver/netstat)


[^13]: [GitHub Sliver C2](https://github.com/BishopFox/sliver/)


[^14]: [GitHub Sliver C2 DNS](https://github.com/BishopFox/sliver/wiki/DNS-C2)


[^15]: [GitHub Sliver HTTP](https://github.com/BishopFox/sliver/wiki/HTTP(S)-C2)


[^16]: [GitHub Sliver Ifconfig](https://github.com/BishopFox/sliver/blob/ea329226636ab8e470086a17f13aa8d330baad22/client/command/network/ifconfig.go)


