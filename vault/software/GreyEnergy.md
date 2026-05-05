---
aliases: 
    - S0342
    
mitre-attack: https://attack.mitre.org/software/S0342
---

## S0342

[GreyEnergy](https://attack.mitre.org/software/S0342) is a backdoor written in C and compiled in Visual Studio. [GreyEnergy](https://attack.mitre.org/software/S0342) shares similarities with the [BlackEnergy](https://attack.mitre.org/software/S0089) malware and is thought to be the successor of it.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [GreyEnergy](https://attack.mitre.org/software/S0342) has used [Tor](https://attack.mitre.org/software/S0183) relays for Command and Control servers.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [GreyEnergy](https://attack.mitre.org/software/S0342) uses PsExec locally in order to execute rundll32.exe at the highest privileges (NTAUTHORITY\SYSTEM).[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [GreyEnergy](https://attack.mitre.org/software/S0342) can securely delete a file by hooking into the DeleteFileA and DeleteFileW functions in the Windows API.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [GreyEnergy](https://attack.mitre.org/software/S0342) chooses a service, drops a DLL file, and writes it to that serviceDLL Registry key.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [GreyEnergy](https://attack.mitre.org/software/S0342) uses HTTP and HTTPS for C2 communications.[^1]  |
| [[Code Signing\|T1553.002]] | Code Signing | [GreyEnergy](https://attack.mitre.org/software/S0342) digitally signs the malware with a code-signing certificate.[^1]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [GreyEnergy](https://attack.mitre.org/software/S0342) enumerates all Windows services.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [GreyEnergy](https://attack.mitre.org/software/S0342) encrypts communications using RSA-2048.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [GreyEnergy](https://attack.mitre.org/software/S0342) uses cmd.exe to execute itself in-memory.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [GreyEnergy](https://attack.mitre.org/software/S0342) can download additional modules and payloads.[^1]  |
| [[Portable Executable Injection\|T1055.002]] | Portable Executable Injection | [GreyEnergy](https://attack.mitre.org/software/S0342) has a module to inject a PE binary into a remote process.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [GreyEnergy](https://attack.mitre.org/software/S0342) encrypts communications using AES256.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [GreyEnergy](https://attack.mitre.org/software/S0342) modifies conditions in the Registry and adds keys.[^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [GreyEnergy](https://attack.mitre.org/software/S0342) is packed for obfuscation.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [GreyEnergy](https://attack.mitre.org/software/S0342) has a module to harvest pressed keystrokes.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [GreyEnergy](https://attack.mitre.org/software/S0342) encrypts its configuration files with AES-256 and also encrypts its strings.[^1]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [GreyEnergy](https://attack.mitre.org/software/S0342) has a module for [Mimikatz](https://attack.mitre.org/software/S0002) to collect Windows credentials from the victim’s machine.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Sandworm Team\|G0034]] | Sandworm Team |



## References

[^1]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)


[^2]: GreyEnergy


[^3]: [Secureworks IRON VIKING ](https://www.secureworks.com/research/threat-profiles/iron-viking)


