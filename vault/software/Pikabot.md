---
aliases: 
    - S1145
    
mitre-attack: https://attack.mitre.org/software/S1145
---

## S1145

[Pikabot](https://attack.mitre.org/software/S1145) is a backdoor used for initial access and follow-on tool deployment active since early 2023. [Pikabot](https://attack.mitre.org/software/S1145) is notable for extensive use of multiple encoding, encryption, and defense evasion mechanisms to evade defenses and avoid analysis. [Pikabot](https://attack.mitre.org/software/S1145) has some overlaps with [QakBot](https://attack.mitre.org/software/S0650), but insufficient evidence exists to definitively link these two malware families. [Pikabot](https://attack.mitre.org/software/S1145) is frequently used to deploy follow on tools such as [Cobalt Strike](https://attack.mitre.org/software/S0154) or ransomware variants.[^2] [^4] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Pikabot](https://attack.mitre.org/software/S1145) gathers victim network information through commands such as `ipconfig` and `ipconfig /all`.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Pikabot](https://attack.mitre.org/software/S1145) can execute Windows shell commands via `cmd.exe`.[^2]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [Pikabot](https://attack.mitre.org/software/S1145) will gather information concerning the Windows Domain the victim machine is a member of during execution.[^4]  |
| [[Thread Execution Hijacking\|T1055.003]] | Thread Execution Hijacking | [Pikabot](https://attack.mitre.org/software/S1145) can create a suspended instance of a legitimate process (e.g., ctfmon.exe), allocate memory within the suspended process corresponding to [Pikabot](https://attack.mitre.org/software/S1145)'s core module, then redirect execution flow via `SetContextThread` API so that when the thread resumes the [Pikabot](https://attack.mitre.org/software/S1145) core module is executed.[^4]  |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [Pikabot](https://attack.mitre.org/software/S1145) features several methods to evade debugging by analysts, including checks for active debuggers, the use of breakpoints during execution, and checking various system information items such as system memory and the number of processors.[^2] [^4] [^1]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [Pikabot](https://attack.mitre.org/software/S1145) uses non-standard ports, such as 2967, 2223, and others, for HTTPS command and control communication.[^4]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | Earlier [Pikabot](https://attack.mitre.org/software/S1145) variants use a custom encryption procedure leveraging multiple mechanisms including AES with multiple rounds of Base64 encoding for its command and control communication.[^2]  Later [Pikabot](https://attack.mitre.org/software/S1145) variants eliminate the use of AES and instead use RC4 encryption for transmitted information.[^4]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | During the initial [Pikabot](https://attack.mitre.org/software/S1145) command and control check-in, [Pikabot](https://attack.mitre.org/software/S1145) will transmit collected system information encrypted using RC4.[^4]  |
| [[Local Account\|T1087.001]] | Local Account | [Pikabot](https://attack.mitre.org/software/S1145) will retrieve the name of the user associated with the thread under which the malware is executing.[^4]  |
| [[Native API\|T1106]] | Native API | [Pikabot](https://attack.mitre.org/software/S1145) uses native Windows APIs to determine if the process is being debugged and analyzed, such as `CheckRemoteDebuggerPresent`, `NtQueryInformationProcess`, `ProcessDebugPort`, and `ProcessDebugFlags`.[^2]  Other [Pikabot](https://attack.mitre.org/software/S1145) variants populate a global list of Windows API addresses from the `NTDLL` and `KERNEL32` libraries, and references these items instead of calling the API items to obfuscate execution.[^4]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Pikabot](https://attack.mitre.org/software/S1145) performs a variety of system checks and gathers system information, including commands such as `whoami`.[^2] [^4]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | Some versions of [Pikabot](https://attack.mitre.org/software/S1145) build the final PE payload in memory to avoid writing contents to disk on the executing machine.[^4]  |
| [[Steganography\|T1027.003]] | Steganography | [Pikabot](https://attack.mitre.org/software/S1145) loads a set of PNG images stored in the malware's resources section (RCDATA), each with an encrypted section containing portions of the core [Pikabot](https://attack.mitre.org/software/S1145) core module. These sections are loaded and decrypted using a bitwise XOR operation with a hardcoded 32 bit key.[^2]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [Pikabot](https://attack.mitre.org/software/S1145) reflectively loads stored, previously encrypted components of the PE file into memory of the currently executing process to avoid writing content to disk on the executing machine.[^4]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Pikabot](https://attack.mitre.org/software/S1145) uses base64 encoding in conjunction with symmetric encryption mechanisms to obfuscate command and control communications.[^2] [^4]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Pikabot](https://attack.mitre.org/software/S1145) decrypts command and control URIs using ADVobfuscator, and decrypts IP addresses and port numbers with a custom algorithm.[^2]  Other versions of [Pikabot](https://attack.mitre.org/software/S1145) decode chunks of stored stage 2 payload content in the initial payload `.text` section before consolidating them for further execution.[^4]  Overall [LunarMail](https://attack.mitre.org/software/S1142) is associated with multiple encoding and encryption mechanisms to obfuscate the malware's presence and avoid analysis or detection.[^1]  |
| [[Embedded Payloads\|T1027.009]] | Embedded Payloads | [Pikabot](https://attack.mitre.org/software/S1145) further decrypts information embedded via steganography using AES-CBC with the same 32 bit key as initial XOR operations combined with the first 16 bytes of the encrypted data as an initialization vector.[^2]  Other [Pikabot](https://attack.mitre.org/software/S1145) variants include encrypted, chunked sections of the stage 2 payload in the initial loader `.text` section before decrypting and assembling these during execution.[^4]  |
| [[Portable Executable Injection\|T1055.002]] | Portable Executable Injection | [Pikabot](https://attack.mitre.org/software/S1145), following payload decryption, creates a process hard-coded into the dropped (e.g., WerFault.exe) and injects the decrypted core modules into it.[^2]  |
| [[Environmental Keying\|T1480.001]] | Environmental Keying | [Pikabot](https://attack.mitre.org/software/S1145) stops execution if the infected system language matches one of several languages, with various versions referencing: Georgian, Kazakh, Uzbek, Tajik, Russian, Ukrainian, Belarussian, and Slovenian.[^2] [^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Pikabot](https://attack.mitre.org/software/S1145) maintains persistence following system checks through the Run key in the registry.[^2]  |
| [[System Checks\|T1497.001]] | System Checks | [Pikabot](https://attack.mitre.org/software/S1145) performs a variety of system checks to determine if it is running in an analysis environment or sandbox, such as checking the number of processors (must be greater than two), and the amount of RAM (must be greater than 2GB).[^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA577\|G1037]] | TA577 |



## References

[^1]: [Logpoint Pikabot 2024](https://www.logpoint.com/wp-content/uploads/2024/02/logpoint-etpr-pikabot.pdf)


[^2]: [Zscaler Pikabot 2023](https://www.zscaler.com/blogs/security-research/technical-analysis-pikabot)


[^3]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)


[^4]: [Elastic Pikabot 2024](https://www.elastic.co/security-labs/pikabot-i-choose-you)


