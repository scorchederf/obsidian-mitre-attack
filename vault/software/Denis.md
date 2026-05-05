---
aliases: 
    - S0354
    
mitre-attack: https://attack.mitre.org/software/S0354
---

## S0354

[Denis](https://attack.mitre.org/software/S0354) is a Windows backdoor and Trojan used by [APT32](https://attack.mitre.org/groups/G0050). [Denis](https://attack.mitre.org/software/S0354) shares several similarities to the [SOUNDBITE](https://attack.mitre.org/software/S0157) backdoor and has been used in conjunction with the [Goopy](https://attack.mitre.org/software/S0477) backdoor.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[DNS\|T1071.004]] | DNS | [Denis](https://attack.mitre.org/software/S0354) has used DNS tunneling for C2 communications.[^2] [^1] [^4]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Denis](https://attack.mitre.org/software/S0354) has a command to delete files from the victim’s machine.[^2] [^4]  |
| [[System Checks\|T1497.001]] | System Checks | [Denis](https://attack.mitre.org/software/S0354) ran multiple system checks, looking for processor and register characteristics, to evade emulation and analysis.[^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Denis](https://attack.mitre.org/software/S0354) deploys additional backdoors and hacking tools to the system.[^4]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Denis](https://attack.mitre.org/software/S0354) performed process hollowing through the API calls CreateRemoteThread, ResumeThread, and Wow64SetThreadContext.[^4]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Denis](https://attack.mitre.org/software/S0354) collects OS information and the computer name from the victim’s machine.[^1] [^4]  |
| [[Query Registry\|T1012]] | Query Registry | [Denis](https://attack.mitre.org/software/S0354) queries the Registry for keys and values.[^4]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Denis](https://attack.mitre.org/software/S0354) will decrypt important strings used for C&C communication.[^4]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Denis](https://attack.mitre.org/software/S0354) has encoded its PowerShell commands in Base64.[^4]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Denis](https://attack.mitre.org/software/S0354) uses `ipconfig` to gather the IP address from the system.[^4]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Denis](https://attack.mitre.org/software/S0354) encodes the data sent to the server in Base64.[^4]  |
| [[Archive via Library\|T1560.002]] | Archive via Library | [Denis](https://attack.mitre.org/software/S0354) compressed collected data using zlib.[^1]  |
| [[Hijack Execution Flow\|T1574]] | Hijack Execution Flow | [Denis](https://attack.mitre.org/software/S0354) replaces the nonexistent Windows DLL "msfte.dll" with its own malicious version, which is loaded by the SearchIndexer.exe and SearchProtocolHost.exe.[^4]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Denis](https://attack.mitre.org/software/S0354) has several commands to search directories for files.[^2] [^4]  |
| [[Native API\|T1106]] | Native API | [Denis](https://attack.mitre.org/software/S0354) used the `IsDebuggerPresent`, `OutputDebugString`, and `SetLastError` APIs to avoid debugging. [Denis](https://attack.mitre.org/software/S0354) used `GetProcAddress` and `LoadLibrary` to dynamically resolve APIs. [Denis](https://attack.mitre.org/software/S0354) also used the `Wow64SetThreadContext` API as part of a process hollowing process.[^4] 	 |
| [[PowerShell\|T1059.001]] | PowerShell | [Denis](https://attack.mitre.org/software/S0354) has a version written in PowerShell.[^4] 	 |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Denis](https://attack.mitre.org/software/S0354) enumerates and collects the username from the victim’s machine.[^1] [^4]  |
| [[DLL\|T1574.001]] | DLL | [Denis](https://attack.mitre.org/software/S0354) exploits a security vulnerability to load a fake DLL and execute its code.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Denis](https://attack.mitre.org/software/S0354) obfuscates its code and encrypts the API names.[^4]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Denis](https://attack.mitre.org/software/S0354) can launch a remote shell to execute arbitrary commands on the victim’s machine.[^2] [^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT32\|G0050]] | APT32 |



## References

[^1]: [Securelist Denis April 2017](https://securelist.com/use-of-dns-tunneling-for-cc-communications/78203/)


[^2]: [Cybereason Oceanlotus May 2017](https://www.cybereason.com/blog/operation-cobalt-kitty-apt)


[^3]: Denis


[^4]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


