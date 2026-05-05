---
aliases: 
    - S0633
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0633-Sliver
---

## Description

[[kb/mitre/attack/software/S0633-Sliver\|Sliver]] is an open source, cross-platform, red team command and control (C2) framework written in Golang. [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] includes its own package manager, "armory," for staging and downloading additional tools and payloads to the primary C2 framework.[^1] [^9] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1001.002-Steganography\|T1001.002]] | Steganography | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] can encode binary data into a .PNG file for C2 communication.[^2]  |
| [[kb/mitre/attack/techniques/T1003.001-LSASS_Memory\|T1003.001]] | LSASS Memory | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] has a built-in `procdump` command allowing for retrieval of memory from processes such as `lsass.exe` for credential harvesting.[^9]  |
| [[kb/mitre/attack/techniques/T1016-System_Network_Configuration_Discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] has the ability to gather network configuration information.[^6]  |
| [[kb/mitre/attack/techniques/T1027-Obfuscated_Files_or_Information\|T1027]] | Obfuscated Files or Information | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] obfuscates configuration and other static files using native Go libraries such as `garble` and `gobfuscate` to inhibit configuration analysis and static detection.[^5]  |
| [[kb/mitre/attack/techniques/T1027.004-Compile_After_Delivery\|T1027.004]] | Compile After Delivery | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] includes functionality to retrieve source code and compile locally prior to execution in victim environments.[^9]  |
| [[kb/mitre/attack/techniques/T1027.013-Encrypted_Encoded_File\|T1027.013]] | Encrypted／Encoded File | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] can encrypt strings at compile time.[^1] [^3]  |
| [[kb/mitre/attack/techniques/T1041-Exfiltration_Over_C2_Channel\|T1041]] | Exfiltration Over C2 Channel | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] can exfiltrate files from the victim using the `download` command.[^8]  |
| [[kb/mitre/attack/techniques/T1049-System_Network_Connections_Discovery\|T1049]] | System Network Connections Discovery | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] can collect network connection information.[^14]  |
| [[kb/mitre/attack/techniques/T1055-Process_Injection\|T1055]] | Process Injection | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] includes multiple methods to perform process injection to migrate the framework into other, potentially privileged processes on the victim machine.[^5] [^9] [^1] [^3]  |
| [[kb/mitre/attack/techniques/T1059.001-PowerShell\|T1059.001]] | PowerShell | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] has built-in functionality to launch a Powershell command prompt.[^9]  |
| [[kb/mitre/attack/techniques/T1071-Application_Layer_Protocol\|T1071]] | Application Layer Protocol | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] can utilize the Wireguard VPN protocol for command and control.[^9]  |
| [[kb/mitre/attack/techniques/T1071.001-Web_Protocols\|T1071.001]] | Web Protocols |  [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] has the ability to support C2 communications over HTTP and HTTPS.[^10] [^1] [^3] [^9] [^5]  |
| [[kb/mitre/attack/techniques/T1071.004-DNS\|T1071.004]] | DNS | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] can support C2 communications over DNS.[^10] [^1] [^13] [^9] [^5]  |
| [[kb/mitre/attack/techniques/T1083-File_and_Directory_Discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] can enumerate files on a target system.[^7]  |
| [[kb/mitre/attack/techniques/T1090.001-Internal_Proxy\|T1090.001]] | Internal Proxy | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] has a built-in SOCKS5 proxying capability allowing for [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] clients to proxy network traffic through other clients within a victim network.[^9]  |
| [[kb/mitre/attack/techniques/T1105-Ingress_Tool_Transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] can download additional content and files from the [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] server to the client residing on the victim machine using the `upload` command.[^4] [^9]  |
| [[kb/mitre/attack/techniques/T1113-Screen_Capture\|T1113]] | Screen Capture | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] can take screenshots of the victim’s active display.[^11]  |
| [[kb/mitre/attack/techniques/T1132.001-Standard_Encoding\|T1132.001]] | Standard Encoding | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] can use standard encoding techniques like gzip and hex to ASCII to encode the C2 communication payload.[^2]  |
| [[kb/mitre/attack/techniques/T1134-Access_Token_Manipulation\|T1134]] | Access Token Manipulation | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] has the ability to manipulate user tokens on targeted Windows systems.[^1] [^3]  |
| [[kb/mitre/attack/techniques/T1548.002-Bypass_User_Account_Control\|T1548.002]] | Bypass User Account Control | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] can leverage multiple techniques to bypass User Account Control (UAC) on Windows systems.[^9]  |
| [[kb/mitre/attack/techniques/T1558.001-Golden_Ticket\|T1558.001]] | Golden Ticket | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] incorporates the [[kb/mitre/attack/software/S1071-Rubeus\|Rubeus]] framework to allow for Kerberos ticket manipulation, specifically for forging Kerberos Golden Tickets.[^9]  |
| [[kb/mitre/attack/techniques/T1573.001-Symmetric_Cryptography\|T1573.001]] | Symmetric Cryptography | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] can use AES-GCM-256 to encrypt a session key for C2 message exchange.[^12]  |
| [[kb/mitre/attack/techniques/T1573.002-Asymmetric_Cryptography\|T1573.002]] | Asymmetric Cryptography | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] can use mutual TLS and RSA  cryptography to exchange a session key.[^10] [^1] [^12] [^9] [^5]  |





> [!info]- References
> [^1]: [Bishop Fox Sliver Framework August 2019](https://labs.bishopfox.com/tech-blog/sliver)

> [^2]: [GitHub Sliver HTTP](https://github.com/BishopFox/sliver/wiki/HTTP(S)-C2)

> [^3]: [GitHub Sliver C2](https://github.com/BishopFox/sliver/)

> [^4]: [GitHub Sliver Upload](https://github.com/BishopFox/sliver/blob/ea329226636ab8e470086a17f13aa8d330baad22/client/command/filesystem/upload.go)

> [^5]: [Microsoft Sliver 2022](https://www.microsoft.com/en-us/security/blog/2022/08/24/looking-for-the-sliver-lining-hunting-for-emerging-command-and-control-frameworks/)

> [^6]: [GitHub Sliver Ifconfig](https://github.com/BishopFox/sliver/blob/ea329226636ab8e470086a17f13aa8d330baad22/client/command/network/ifconfig.go)

> [^7]: [GitHub Sliver File System August 2021](https://github.com/BishopFox/sliver/tree/master/client/command/filesystem)

> [^8]: [GitHub Sliver Download](https://github.com/BishopFox/sliver/blob/7489c69962b52b09ed377d73d142266564845297/client/command/filesystem/download.go)

> [^9]: [Cybereason Sliver Undated](https://www.cybereason.com/blog/sliver-c2-leveraged-by-many-threat-actors)

> [^10]: [Cybersecurity Advisory SVR TTP May 2021](https://www.ncsc.gov.uk/files/Advisory-further-TTPs-associated-with-SVR-cyber-actors.pdf)

> [^11]: [GitHub Sliver Screen](https://github.com/BishopFox/sliver/blob/master/implant/sliver/screen/screenshot_windows.go)

> [^12]: [GitHub Sliver Encryption](https://github.com/BishopFox/sliver/wiki/Transport-Encryption)

> [^13]: [GitHub Sliver C2 DNS](https://github.com/BishopFox/sliver/wiki/DNS-C2)

> [^14]: [GitHub Sliver Netstat](https://github.com/BishopFox/sliver/tree/58a56a077f0813bb312f9fa4df7453b510c3a73b/implant/sliver/netstat)


