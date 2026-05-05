---
aliases: 
    - S0623
    
mitre-attack: https://attack.mitre.org/software/S0623
---

## S0623

[Siloscape](https://attack.mitre.org/software/S0623) is malware that targets Kubernetes clusters through Windows containers. [Siloscape](https://attack.mitre.org/software/S0623) was first observed in March 2021.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Software Discovery\|T1518]] | Software Discovery | [Siloscape](https://attack.mitre.org/software/S0623) searches for the kubectl binary.[^1]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Siloscape](https://attack.mitre.org/software/S0623) is executed after the attacker gains initial access to a Windows container using a known vulnerability.[^1]   |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [Siloscape](https://attack.mitre.org/software/S0623) uses [Tor](https://attack.mitre.org/software/S0183) to communicate with C2.[^1]  |
| [[Escape to Host\|T1611]] | Escape to Host | [Siloscape](https://attack.mitre.org/software/S0623) maps the host’s C drive to the container by creating a global symbolic link to the host through the calling of `NtSetInformationSymbolicLink`.[^1]  |
| [[Application Layer Protocol\|T1071]] | Application Layer Protocol | [Siloscape](https://attack.mitre.org/software/S0623) connects to an IRC server for C2.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Siloscape](https://attack.mitre.org/software/S0623) has decrypted the password of the C2 server with a simple byte by byte XOR. [Siloscape](https://attack.mitre.org/software/S0623) also writes both an archive of [Tor](https://attack.mitre.org/software/S0183) and the `unzip` binary to disk from data embedded within the payload using Visual Studio’s Resource Manager.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Siloscape](https://attack.mitre.org/software/S0623) can run cmd through an IRC channel.[^1]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [Siloscape](https://attack.mitre.org/software/S0623) has leveraged a vulnerability in Windows containers to perform an [Escape to Host](https://attack.mitre.org/techniques/T1611).[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery |  [Siloscape](https://attack.mitre.org/software/S0623) searches for the Kubernetes config file and other related files using a regular expression.[^1]   |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Siloscape](https://attack.mitre.org/software/S0623) itself is obfuscated and uses obfuscated API calls.[^1]  |
| [[Container Administration Command\|T1609]] | Container Administration Command | [Siloscape](https://attack.mitre.org/software/S0623) can send kubectl commands to victim clusters through an IRC channel and can run kubectl locally to spread once within a victim cluster.[^1]  |
| [[Permission Groups Discovery\|T1069]] | Permission Groups Discovery | [Siloscape](https://attack.mitre.org/software/S0623) checks for Kubernetes node permissions.[^1]  |
| [[Token Impersonation／Theft\|T1134.001]] | Token Impersonation／Theft | [Siloscape](https://attack.mitre.org/software/S0623) impersonates the main thread of `CExecSvc.exe` by calling `NtImpersonateThread`.[^1]  |
| [[Native API\|T1106]] | Native API | [Siloscape](https://attack.mitre.org/software/S0623) makes various native API calls.[^1]  |




## References

[^1]: [Unit 42 Siloscape Jun 2021](https://unit42.paloaltonetworks.com/siloscape/)


