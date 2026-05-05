---
aliases: 
    - S9018
    
mitre-attack: https://attack.mitre.org/software/S9018
---

## S9018

[HeartCrypt](https://attack.mitre.org/software/S9018) is a packer-as-a-service (PaaS) used to protect malware that has been available since at least 2024. [HeartCrypt](https://attack.mitre.org/software/S9018) has been used to pack a variety of malware including [Lumma Stealer](https://attack.mitre.org/software/S1213), [Remcos](https://attack.mitre.org/software/S0332), and Rhadamanthys. In the [HeartCrypt](https://attack.mitre.org/software/S9018) PaaS model, customers submit malware via private messaging services and it is then packed and returned by the operator as a new binary.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Asynchronous Procedure Call\|T1055.004]] | Asynchronous Procedure Call | [HeartCrypt](https://attack.mitre.org/software/S9018) has the ability to use `NtQueueApcThread` as an alternate method for process injection.[^2] <br> |
| [[Masquerade File Type\|T1036.008]] | Masquerade File Type | [HeartCrypt](https://attack.mitre.org/software/S9018) can append a BMP header to encoded malicious payloads to masquerade them as BMP files.[^2]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | For .NET payloads, [HeartCrypt](https://attack.mitre.org/software/S9018) can use process hollowing to inject into processes spawned by csc.exe or AppLaunch.exe.[^2]  |
| [[System Checks\|T1497.001]] | System Checks | [HeartCrypt](https://attack.mitre.org/software/S9018) will attempt to load non-existent DLLs in attempt to detect sandbox creation of a dummy DLL to prevent the program from crashing.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [HeartCrypt](https://attack.mitre.org/software/S9018) can decrypt payloads prior to execution.[^2] [^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [HeartCrypt](https://attack.mitre.org/software/S9018) can pack malicious Windows x86 and .NET payloads in order to evade detection.[^2] [^1] <br> |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [HeartCrypt](https://attack.mitre.org/software/S9018) strings are encrypted via a single-byte XOR operation rotating over a hard-coded key, possibly provided by the PaaS customers. [^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [HeartCrypt](https://attack.mitre.org/software/S9018) can set the `CurrentVersion\Run` key to establish persistence.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [HeartCrypt](https://attack.mitre.org/software/S9018) can use the `reg add` command via `cmd.exe` for Registry modification.[^2]  |
| [[Native API\|T1106]] | Native API | [HeartCrypt](https://attack.mitre.org/software/S9018) can use Windows API functions to modify the Registry and `FindResourceW`, `LoadResource`, and `LockResource` to acquire a pointer to corresponding code resources.[^2]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [HeartCrypt](https://attack.mitre.org/software/S9018) can add several hundred thousand kilobytes of null padding to payloads before saving onto the file system.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT-C-36\|G0099]] | APT-C-36 |



## References

[^1]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)


[^2]: [Palo Alto HeartCrypt DEC 2024](https://unit42.paloaltonetworks.com/packer-as-a-service-heartcrypt-malware/)


