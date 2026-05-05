---
aliases: 
    - S0502
    
mitre-attack: https://attack.mitre.org/software/S0502
---

## S0502

[Drovorub](https://attack.mitre.org/software/S0502) is a Linux malware toolset comprised of an agent, client, server, and kernel modules, that has been used by [APT28](https://attack.mitre.org/groups/G0007).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Drovorub](https://attack.mitre.org/software/S0502) can use the WebSocket protocol and has initiated communication with C2 servers with an HTTP Upgrade request.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Drovorub](https://attack.mitre.org/software/S0502) can transfer files from the victim machine.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Drovorub](https://attack.mitre.org/software/S0502) has used XOR encrypted payloads in WebSocket client to server messages.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Drovorub](https://attack.mitre.org/software/S0502) can delete specific files from a compromised host.[^1]  |
| [[Kernel Modules and Extensions\|T1547.006]] | Kernel Modules and Extensions | [Drovorub](https://attack.mitre.org/software/S0502) can use kernel modules to establish persistence.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Drovorub](https://attack.mitre.org/software/S0502) can use TCP to communicate between its agent and client modules.[^1]  |
| [[Rootkit\|T1014]] | Rootkit | [Drovorub](https://attack.mitre.org/software/S0502) has used a kernel module rootkit to hide processes, files, executables, and network artifacts from user space view.[^1]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [Drovorub](https://attack.mitre.org/software/S0502) can use a port forwarding rule on its agent module to relay network traffic through the client module to a remote host on the same network.[^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Drovorub](https://attack.mitre.org/software/S0502) can execute arbitrary commands as root on a compromised system.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Drovorub](https://attack.mitre.org/software/S0502) has de-obsfuscated XOR encrypted payloads in WebSocket messages.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Drovorub](https://attack.mitre.org/software/S0502) can exfiltrate files over C2 infrastructure.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Drovorub](https://attack.mitre.org/software/S0502) can download files to a compromised host.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT28\|G0007]] | APT28 |



## References

[^1]: [NSA/FBI Drovorub August 2020](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF)


