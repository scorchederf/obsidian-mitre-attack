---
aliases: 
    - S1085
    
mitre-attack: https://attack.mitre.org/software/S1085
---

## S1085

[Sardonic](https://attack.mitre.org/software/S1085) is a backdoor written in C and C++ that is known to be used by [FIN8](https://attack.mitre.org/groups/G0061), as early as August 2021 to target a financial institution in the United States. [Sardonic](https://attack.mitre.org/software/S1085) has a plugin system that can load specially made DLLs and execute their functions.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Sardonic](https://attack.mitre.org/software/S1085) can use WMI to execute PowerShell commands on a compromised machine.[^1]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Sardonic](https://attack.mitre.org/software/S1085) PowerShell scripts can be encrypted with RC4 and compressed using Gzip.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to collect the computer name, and CPU manufacturer name from a compromised machine. [Sardonic](https://attack.mitre.org/software/S1085) also has the ability to execute the `ver` and `systeminfo` commands.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to execute the `ipconfig` command.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to use an RC4 key to encrypt communications to and from actor-controlled C2 servers.[^1]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [Sardonic](https://attack.mitre.org/software/S1085) can use a WMI event filter to invoke a command-line event consumer to gain persistence.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to upload additional malicious files to a compromised machine.[^1]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to execute the `net view` command.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Sardonic](https://attack.mitre.org/software/S1085) can first decrypt with the RC4 algorithm using a hardcoded decryption key before decompressing.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to collect data from a compromised machine to deliver to the attacker.[^2]   |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to run `cmd.exe` or other interactive processes on a compromised computer.[^2]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to collect the C:\ drive serial number from a compromised machine.[^1]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to connect with actor-controlled C2 servers using a custom binary protocol over port 443.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to execute the `tasklist` command.[^1]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to execute the `net start` command.[^1]  |
| [[Native API\|T1106]] | Native API | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to call Win32 API functions to determine if `powershell.exe` is running.[^1]   |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Sardonic](https://attack.mitre.org/software/S1085) can encode client ID data in 32 uppercase hex characters and transfer to the actor-controlled C2 server.[^1]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to delete created WMI objects to evade detections.[^1]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [Sardonic](https://attack.mitre.org/software/S1085) has a plugin system that can load specially made DLLs into memory and execute their functions.[^1] [^2]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to send a random 64-byte RC4 key to communicate with actor-controlled C2 servers by using an RSA public key.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Sardonic](https://attack.mitre.org/software/S1085) can use certain ConfuserEx features for obfuscation and can be encoded in a base64 string.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to execute PowerShell commands on a compromised machine.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to execute the `netstat` command.[^1]  |
| [[Asynchronous Procedure Call\|T1055.004]] | Asynchronous Procedure Call | [Sardonic](https://attack.mitre.org/software/S1085) can use the `QueueUserAPC` API to execute shellcode on a compromised machine.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Sardonic](https://attack.mitre.org/software/S1085) can communicate with actor-controlled C2 servers by using a custom little-endian binary protocol.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN8\|G0061]] | FIN8 |



## References

[^1]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)


[^2]: [Symantec FIN8 Jul 2023](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/syssphinx-fin8-backdoor)


