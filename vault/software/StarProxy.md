---
aliases: 
    - S1227
    
mitre-attack: https://attack.mitre.org/software/S1227
---

## S1227

[StarProxy](https://attack.mitre.org/software/S1227) is custom malware used by [Mustang Panda](https://attack.mitre.org/groups/G0129) as a post-compromise tool, to enable proxying of traffic between the infected machine and other machines on the same network. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [StarProxy](https://attack.mitre.org/software/S1227) has leveraged two 256-byte XOR keys to encrypt and decrypt  network packets using a custom algorithm.[^1]  |
| [[DLL\|T1574.001]] | DLL | [StarProxy](https://attack.mitre.org/software/S1227) has been side-loaded by the legitimate, signed executable, IsoBurner.exe. [^1]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [StarProxy](https://attack.mitre.org/software/S1227) has used the command line for execution of commands.[^1]  |
| [[Protocol or Service Impersonation\|T1001.003]] | Protocol or Service Impersonation | [StarProxy](https://attack.mitre.org/software/S1227) has utilized TLS record headers in network packets to impersonate various versions of TLS protocols to blend in with legitimate network traffic.  [StarProxy](https://attack.mitre.org/software/S1227) used FakeTLS to communicate with its C2 server.[^1]  |
| [[Native API\|T1106]] | Native API | [StarProxy](https://attack.mitre.org/software/S1227) has used native windows API calls such as `GetLocalTime()` to retrieve system data.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [StarProxy](https://attack.mitre.org/software/S1227) has utilized the windows API call `GetLocalTime()` to retrieve a SystemTime structure to generate a seed value.[^1]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [StarProxy](https://attack.mitre.org/software/S1227) has proxied traffic between infected devices and their C2 servers.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [StarProxy](https://attack.mitre.org/software/S1227) has used TCP for C2 communications to target IPs or domains.  [StarProxy](https://attack.mitre.org/software/S1227) contained code to support both UDP and TCP connections.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [StarProxy](https://attack.mitre.org/software/S1227) has decrypted network packets using a custom algorithm.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Mustang Panda\|G0129]] | Mustang Panda |



## References

[^1]: [Zscaler](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)


