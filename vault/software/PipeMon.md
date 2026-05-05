---
aliases: 
    - S0501
    
mitre-attack: https://attack.mitre.org/software/S0501
---

## S0501

[PipeMon](https://attack.mitre.org/software/S0501) is a multi-stage modular backdoor used by [Winnti Group](https://attack.mitre.org/groups/G0044).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Create Process with Token\|T1134.002]] | Create Process with Token | [PipeMon](https://attack.mitre.org/software/S0501) can attempt to gain administrative privileges using token impersonation.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [PipeMon](https://attack.mitre.org/software/S0501) can collect and send OS version and computer name as a part of its C2 beacon.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [PipeMon](https://attack.mitre.org/software/S0501) has modified the Registry to store its encrypted payload.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [PipeMon](https://attack.mitre.org/software/S0501) modules are stored encrypted on disk.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [PipeMon](https://attack.mitre.org/software/S0501) can install additional modules via C2 commands.[^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [PipeMon](https://attack.mitre.org/software/S0501) can inject its modules into various processes using reflective DLL loading.[^1]  |
| [[Print Processors\|T1547.012]] | Print Processors | The [PipeMon](https://attack.mitre.org/software/S0501) installer has modified the Registry key `HKLM\SYSTEM\CurrentControlSet\Control\Print\Environments\Windows x64\Print Processors` to install [PipeMon](https://attack.mitre.org/software/S0501) as a Print Processor.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | The [PipeMon](https://attack.mitre.org/software/S0501) communication module can use a custom protocol based on TLS over TCP.[^1]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [PipeMon](https://attack.mitre.org/software/S0501) installer can use UAC bypass techniques to install the payload.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [PipeMon](https://attack.mitre.org/software/S0501) can iterate over the running processes to find a suitable injection target.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [PipeMon](https://attack.mitre.org/software/S0501) can send time zone information from a compromised host to C2.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [PipeMon](https://attack.mitre.org/software/S0501) communications are RC4 encrypted.[^1]  |
| [[Parent PID Spoofing\|T1134.004]] | Parent PID Spoofing | [PipeMon](https://attack.mitre.org/software/S0501) can use parent PID spoofing to elevate privileges.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [PipeMon](https://attack.mitre.org/software/S0501) can decrypt password-protected executables.[^1]  |
| [[Native API\|T1106]] | Native API | [PipeMon](https://attack.mitre.org/software/S0501)'s first stage has been executed by a call to `CreateProcess` with the decryption password in an argument. [PipeMon](https://attack.mitre.org/software/S0501) has used a call to `LoadLibrary` to load its installer.[^1]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [PipeMon](https://attack.mitre.org/software/S0501) has stored its encrypted payload in the Registry under `HKLM\SOFTWARE\Microsoft\Print\Components\`.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [PipeMon](https://attack.mitre.org/software/S0501) can establish persistence by registering a malicious DLL as an alternative Print Processor which is loaded when the print spooler service starts.[^1]  |
| [[Code Signing\|T1553.002]] | Code Signing | [PipeMon](https://attack.mitre.org/software/S0501), its installer, and tools are signed with stolen code-signing certificates.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [PipeMon](https://attack.mitre.org/software/S0501) can switch to an alternate C2 domain when a particular date has been reached.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [PipeMon](https://attack.mitre.org/software/S0501) modules are stored on disk with seemingly benign names including use of a file extension associated with a popular word processor.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [PipeMon](https://attack.mitre.org/software/S0501) can collect and send the local IP address, RDP information, and the network adapter physical address as a part of its C2 beacon.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [PipeMon](https://attack.mitre.org/software/S0501) can check for the presence of ESET and Kaspersky security software.[^1]  |
| [[Shared Modules\|T1129]] | Shared Modules | [PipeMon](https://attack.mitre.org/software/S0501) has used call to `LoadLibrary` to load its installer. [PipeMon](https://attack.mitre.org/software/S0501) loads its modules using reflective loading or custom shellcode.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Winnti Group\|G0044]] | Winnti Group |



## References

[^1]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)


