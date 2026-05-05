---
aliases: 
    - S0284
    
mitre-attack: https://attack.mitre.org/software/S0284
---

## S0284

[More_eggs](https://attack.mitre.org/software/S0284) is a JScript backdoor used by [Cobalt Group](https://attack.mitre.org/groups/G0080) and [FIN6](https://attack.mitre.org/groups/G0037). Its name was given based on the variable "More_eggs" being present in its code. There are at least two different versions of the backdoor being used, version 2.0 and version 4.4. [^6] [^9] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [More_eggs](https://attack.mitre.org/software/S0284) can download and launch additional payloads.[^6] [^9]  |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [More_eggs](https://attack.mitre.org/software/S0284) has used HTTP GET requests to check internet connectivity.[^9]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [More_eggs](https://attack.mitre.org/software/S0284) will decode malware components that are then dropped to the system.[^9]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [More_eggs](https://attack.mitre.org/software/S0284) has the capability to gather the OS version and computer name.[^6] [^9]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [More_eggs](https://attack.mitre.org/software/S0284) uses HTTPS for C2.[^6] [^9]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [More_eggs](https://attack.mitre.org/software/S0284) has used an RC4-based encryption method for its C2 communications.[^9]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [More_eggs](https://attack.mitre.org/software/S0284) has used cmd.exe for execution.[^9] [^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [More_eggs](https://attack.mitre.org/software/S0284)'s payload has been encrypted with a key that has the hostname and processor family information appended to the end.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [More_eggs](https://attack.mitre.org/software/S0284) can remove itself from a system.[^6] [^9]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [More_eggs](https://attack.mitre.org/software/S0284) has the capability to gather the IP address from the victim's machine.[^6]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [More_eggs](https://attack.mitre.org/software/S0284) has used basE91 encoding, along with encryption, for C2 communication.[^9]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [More_eggs](https://attack.mitre.org/software/S0284) can obtain information on installed anti-malware programs.[^6]  |
| [[Code Signing\|T1553.002]] | Code Signing | [More_eggs](https://attack.mitre.org/software/S0284) has used a signed binary shellcode loader and a signed Dynamic Link Library (DLL) to create a reverse shell.[^9]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [More_eggs](https://attack.mitre.org/software/S0284) has used regsvr32.exe to execute the malicious DLL.[^9]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [More_eggs](https://attack.mitre.org/software/S0284) has the capability to gather the username from the victim's machine.[^6] [^9]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Evilnum\|G0120]] | Evilnum |
| [[FIN6\|G0037]] | FIN6 |
| [[Cobalt Group\|G0080]] | Cobalt Group |



## References

[^1]: SKID


[^2]: Terra Loader


[^3]: [ESET EvilNum July 2020](https://www.welivesecurity.com/2020/07/09/more-evil-deep-look-evilnum-toolset/)


[^4]: [Visa FIN6 Feb 2019](https://usa.visa.com/dam/VCOM/global/support-legal/documents/fin6-cybercrime-group-expands-threat-To-ecommerce-merchants.pdf)


[^5]: SpicyOmelette


[^6]: [Talos Cobalt Group July 2018](https://blog.talosintelligence.com/2018/07/multiple-cobalt-personality-disorder.html)


[^7]: More_eggs


[^8]: [Crowdstrike GTR2020 Mar 2020](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)


[^9]: [Security Intelligence More Eggs Aug 2019](https://securityintelligence.com/posts/more_eggs-anyone-threat-actor-itg08-strikes-again/)


