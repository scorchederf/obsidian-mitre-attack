---
aliases: 
    - S0641
    
mitre-attack: https://attack.mitre.org/software/S0641
---

## S0641

[Kobalos](https://attack.mitre.org/software/S0641) is a multi-platform backdoor that can be used against Linux, FreeBSD, and Solaris. [Kobalos](https://attack.mitre.org/software/S0641) has been deployed against high profile targets, including high-performance computers, academic servers, an endpoint security vendor, and a large internet service provider; it has been found in Europe, North America, and Asia. [Kobalos](https://attack.mitre.org/software/S0641) was first identified in late 2019.[^2] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Kobalos](https://attack.mitre.org/software/S0641) can spawn a new pseudo-terminal and execute arbitrary commands at the command prompt.[^2]   |
| [[Compromise Host Software Binary\|T1554]] | Compromise Host Software Binary | [Kobalos](https://attack.mitre.org/software/S0641) replaced the SSH client with a trojanized SSH client to steal credentials on compromised systems.[^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Kobalos](https://attack.mitre.org/software/S0641) can record the IP address of the target machine.[^3]  |
| [[Clear Command History\|T1070.003]] | Clear Command History | [Kobalos](https://attack.mitre.org/software/S0641) can remove all command history on compromised hosts.[^2] 	 |
| [[Data Staged\|T1074]] | Data Staged | [Kobalos](https://attack.mitre.org/software/S0641) can write captured SSH connection credentials to a file under the `/var/run` directory with a `.pid` extension for exfiltration.[^3]   |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Kobalos](https://attack.mitre.org/software/S0641) decrypts strings right after the initial communication, but before the authentication process.[^3]   |
| [[Traffic Signaling\|T1205]] | Traffic Signaling | [Kobalos](https://attack.mitre.org/software/S0641) is triggered by an incoming TCP connection to a legitimate service from a specific source port.[^2] [^3]   |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Kobalos](https://attack.mitre.org/software/S0641)'s post-authentication communication channel uses a 32-byte-long password with RC4 for inbound and outbound traffic.[^2] [^3]   |
| [[Exfiltration Over Alternative Protocol\|T1048]] | Exfiltration Over Alternative Protocol | [Kobalos](https://attack.mitre.org/software/S0641) can exfiltrate credentials over the network via UDP.[^3]  |
| [[Timestomp\|T1070.006]] | Timestomp | [Kobalos](https://attack.mitre.org/software/S0641) can modify timestamps of replaced files, such as `ssh` with the added credential stealer or `sshd` used to deploy [Kobalos](https://attack.mitre.org/software/S0641).[^3]   |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Kobalos](https://attack.mitre.org/software/S0641) encrypts all strings using RC4 and bundles all functionality into a single function call.[^2]   |
| [[Input Capture\|T1056]] | Input Capture | [Kobalos](https://attack.mitre.org/software/S0641) has used a compromised SSH client to capture the hostname, port, username and password used to establish an SSH connection from the compromised host.[^2] [^3]   |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Kobalos](https://attack.mitre.org/software/S0641)'s authentication and key exchange is performed using RSA-512.[^2] [^3]   |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Kobalos](https://attack.mitre.org/software/S0641) can record the hostname and kernel version of the target machine.[^3]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [Kobalos](https://attack.mitre.org/software/S0641) can chain together multiple compromised machines as proxies to reach their final targets.[^2] [^3]  |




## References

[^1]: Kobalos


[^2]: [ESET Kobalos Feb 2021](https://www.welivesecurity.com/2021/02/02/kobalos-complex-linux-threat-high-performance-computing-infrastructure/)


[^3]: [ESET Kobalos Jan 2021](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)


