---
aliases: 
    - S0022
    
mitre-attack: https://attack.mitre.org/software/S0022
---

## S0022

[Uroburos](https://attack.mitre.org/software/S0022) is a sophisticated cyber espionage tool written in C that has been used by units within Russia's Federal Security Service (FSB) associated with the [Turla](https://attack.mitre.org/groups/G0010) toolset to collect intelligence on sensitive targets worldwide. [Uroburos](https://attack.mitre.org/software/S0022) has several variants and has undergone nearly constant upgrade since its initial development in 2003 to keep it viable after public disclosures. [Uroburos](https://attack.mitre.org/software/S0022) is typically deployed to external-facing nodes on a targeted network and has the ability to leverage additional tools and TTPs to further exploit an internal network. [Uroburos](https://attack.mitre.org/software/S0022) has interoperable implants for Windows, Linux, and macOS, employs a high level of stealth in communications and architecture, and can easily incorporate new or replacement components.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Uroburos](https://attack.mitre.org/software/S0022) has used a combination of a Diffie-Hellman key exchange mixed with a pre-shared key (PSK) to encrypt its top layer of C2 communications.[^1]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [Uroburos](https://attack.mitre.org/software/S0022) has the ability to load new modules directly into memory using its `Load Modules Mem` command.[^1]  |
| [[Native API\|T1106]] | Native API | [Uroburos](https://attack.mitre.org/software/S0022) can use native Windows APIs including `GetHostByName`.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Uroburos](https://attack.mitre.org/software/S0022) can use its `Get` command to exfiltrate specified files from the compromised system.[^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Uroburos](https://attack.mitre.org/software/S0022) uses a custom packer.[^4] [^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Uroburos](https://attack.mitre.org/software/S0022) can communicate through custom methodologies for UDP,  ICMP, and TCP that use distinct sessions to ride over the legitimate protocols.[^1]  |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [Uroburos](https://attack.mitre.org/software/S0022) can use custom communications protocols that ride over SMTP.[^1]  |
| [[Junk Data\|T1001.001]] | Junk Data | [Uroburos](https://attack.mitre.org/software/S0022) can add extra characters in encoded strings to help mimic DNS legitimate requests.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Uroburos](https://attack.mitre.org/software/S0022) can encrypt the data beneath its http2 or tcp encryption at the session layer with CAST-128, using a different key for incoming and outgoing data.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Uroburos](https://attack.mitre.org/software/S0022) can use a custom HTTP-based protocol for large data communications that can blend with normal network traffic by riding on top of standard HTTP.[^1]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [Uroburos](https://attack.mitre.org/software/S0022) can use implants on multiple compromised machines to proxy communications through its worldwide P2P network.[^1] <br> |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Uroburos](https://attack.mitre.org/software/S0022) has the ability to use the command line for execution on the targeted system.[^1]  |
| [[Hidden File System\|T1564.005]] | Hidden File System | [Uroburos](https://attack.mitre.org/software/S0022) can use concealed storage mechanisms including an NTFS or FAT-16 filesystem encrypted with CAST-128 in CBC mode.[^1]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [Uroburos](https://attack.mitre.org/software/S0022) can store configuration information for the kernel driver and kernel driver loader components in an encrypted blob typically found at `HKLM:\SOFTWARE\Classes\.wav\OpenWithProgIds.`[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Uroburos](https://attack.mitre.org/software/S0022) can store configuration information in the Registry including the initialization vector and AES key needed to find and decrypt other [Uroburos](https://attack.mitre.org/software/S0022) components.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Uroburos](https://attack.mitre.org/software/S0022) has registered a service named `WerFaultSvc`, likely to spoof the legitimate Windows error reporting service.[^1]  |
| [[Non-Standard Encoding\|T1132.002]] | Non-Standard Encoding | [Uroburos](https://attack.mitre.org/software/S0022) can use a custom base62 and a de-facto base32 encoding that uses digits 0-9 and lowercase letters a-z in C2 communications.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [Uroburos](https://attack.mitre.org/software/S0022) can query the Registry, typically `HKLM:\SOFTWARE\Classes\.wav\OpenWithProgIds`, to find the key and path to decrypt and load its kernel driver and kernel driver loader.[^1]  |
| [[Inter-Process Communication\|T1559]] | Inter-Process Communication | [Uroburos](https://attack.mitre.org/software/S0022) has the ability to move data between its kernel and user mode components, generally using named pipes.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Uroburos](https://attack.mitre.org/software/S0022) has the ability to gather basic system information and run the POSIX API `gethostbyname`.[^1]  |
| [[Multi-Stage Channels\|T1104]] | Multi-Stage Channels | Individual [Uroburos](https://attack.mitre.org/software/S0022) implants can use multiple communication channels based on one of four available modes of operation.[^1]  |
| [[Protocol or Service Impersonation\|T1001.003]] | Protocol or Service Impersonation | [Uroburos](https://attack.mitre.org/software/S0022) can use custom communication methodologies that ride over common  protocols including TCP, UDP, HTTP, SMTP, and DNS in order to blend with normal network traffic. [^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Uroburos](https://attack.mitre.org/software/S0022) can use up to 10 channels to communicate between implants.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Uroburos](https://attack.mitre.org/software/S0022) has registered a service, typically named `WerFaultSvc`, to decrypt and find a kernel driver and kernel driver loader to maintain persistence.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Uroburos](https://attack.mitre.org/software/S0022) can use a `Put` command to write files to an infected machine.[^1]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Uroburos](https://attack.mitre.org/software/S0022) has the ability to communicate over custom communications methodologies that ride over common network protocols including raw TCP and UDP sockets, HTTP, SMTP, and DNS.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Uroburos](https://attack.mitre.org/software/S0022) can decrypt command parameters sent through C2 and use unpacking code to extract its packed executable.[^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Uroburos](https://attack.mitre.org/software/S0022) can use DLL injection to load embedded files and modules.[^1]  |
| [[Traffic Signaling\|T1205]] | Traffic Signaling | [Uroburos](https://attack.mitre.org/software/S0022) can intercept the first client to server packet in the 3-way TCP handshake to determine if the packet contains the correct unique value for a specific [Uroburos](https://attack.mitre.org/software/S0022) implant. If the value does not match, the packet and the rest of the TCP session are passed to the legitimate listening application.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Uroburos](https://attack.mitre.org/software/S0022) can use its `Process List` command to enumerate processes on compromised hosts.[^1]  |
| [[Rootkit\|T1014]] | Rootkit | [Uroburos](https://attack.mitre.org/software/S0022) can use its kernel module to prevent its host components from being listed by the targeted system's OS and to mediate requests between user mode and concealed components.[^2] [^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Uroburos](https://attack.mitre.org/software/S0022) can use AES and CAST-128 encryption to obfuscate resources.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Uroburos](https://attack.mitre.org/software/S0022) can run a `Clear Agents Track` command on an infected machine to delete [Uroburos](https://attack.mitre.org/software/S0022)-related logs.[^1]  |
| [[DNS\|T1071.004]] | DNS | [Uroburos](https://attack.mitre.org/software/S0022) has encoded outbound C2 communications in DNS requests consisting of character strings made to resemble standard domain names. The actual information transmitted by [Uroburos](https://attack.mitre.org/software/S0022) is contained in the part of the character string prior to the first ‘.’ character.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Uroburos](https://attack.mitre.org/software/S0022) can search for specific files on a compromised system.[^1]  |
| [[Embedded Payloads\|T1027.009]] | Embedded Payloads | The [Uroburos](https://attack.mitre.org/software/S0022) Queue file contains embedded executable files along with key material, communication channels, and modes of operation.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Turla\|G0010]] | Turla |



## References

[^1]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)


[^2]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)


[^3]: Snake


[^4]: [Symantec Waterbug](https://www.threatminer.org/report.php?q=waterbug-attack-group.pdf&y=2015#gsc.tab=0&gsc.q=waterbug-attack-group.pdf&gsc.page=1)


