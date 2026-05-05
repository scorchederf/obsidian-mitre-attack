---
aliases: 
    - S9037
    
mitre-attack: https://attack.mitre.org/software/S9037
---

## S9037

[RustyWater](https://attack.mitre.org/software/S9037) is a Rust-based implant used by [MuddyWater](https://attack.mitre.org/groups/G0069). Historically, [MuddyWater](https://attack.mitre.org/groups/G0069) has used PowerShell-based tools and [RustyWater](https://attack.mitre.org/software/S9037) reflects a shift in tooling, demonstrating better techniques for defense evasion and reverse engineering.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Impersonation\|T1684.001]] | Impersonation | [RustyWater](https://attack.mitre.org/software/S9037) has impersonated TMCell (Altyn Asyr CJSC), the primary mobile operator in Turkmenistan, sending phishing emails with the email domain `info@tmcell`.[^1]    |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [RustyWater](https://attack.mitre.org/software/S9037) has gathered the victim machine’s username.[^1]     |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [RustyWater](https://attack.mitre.org/software/S9037) has encrypted all strings in the code using position independent XOR encryption.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [RustyWater](https://attack.mitre.org/software/S9037) has gathered the victim machine’s computer name.[^1]      |
| [[Web Protocols\|T1071.001]] | Web Protocols | [RustyWater](https://attack.mitre.org/software/S9037) has used the Rust request library for HTTP C2 communication.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [RustyWater](https://attack.mitre.org/software/S9037) has encoded collected data with Base64.[^1]     |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [RustyWater](https://attack.mitre.org/software/S9037) has sent spearphishing emails with the attachment Cybersecurity.doc, which served as the primary payload for the next stage.[^1]  |
| [[Native API\|T1106]] | Native API | [RustyWater](https://attack.mitre.org/software/S9037) has used `CreateObject` to instantiate a WScript.Shell Component Object Model (COM) object.[^1]   Additionally, [RustyWater](https://attack.mitre.org/software/S9037) has used `VirtualAllocEx` and `WriteProcessMemory` to inject shellcode into explorer.exe.[^1]        |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [RustyWater](https://attack.mitre.org/software/S9037) has encrypted encoded data with XOR before sending it to the C2 server.[^1]     |
| [[Portable Executable Injection\|T1055.002]] | Portable Executable Injection | [RustyWater](https://attack.mitre.org/software/S9037) has injected its shellcode into explorer.exe by allocating memory via `VirtualAllocEx`, then by writing the payload via `WriteProcessMemory`.[^1]         |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [RustyWater](https://attack.mitre.org/software/S9037) has established persistence by adding `C:\ProgramData\CertificationKit.ini` to a Windows startup Registry key or to a Run or RunOnce Registry key.[^1]  |
| [[Delay Execution\|T1678]] | Delay Execution | [RustyWater](https://attack.mitre.org/software/S9037) has generated random sleep intervals between C2 communication.[^1]  |
| [[Domain Account\|T1087.002]] | Domain Account | [RustyWater](https://attack.mitre.org/software/S9037) has gathered the domain membership of the victim machine’s user.[^1]     |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [RustyWater](https://attack.mitre.org/software/S9037) has an obfuscated function (i.e. love_me__()) that dynamically reconstructs the string WScript.Shell using hard-coded ASCII values and the Chr() function.[^1]       |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [RustyWater](https://attack.mitre.org/software/S9037) has registered a Vectored Exception Handler (VEH) to catch debugging efforts.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [RustyWater](https://attack.mitre.org/software/S9037) has attempted to detect more than 25 antivirus and EDR tools.[^1]      |
| [[Component Object Model\|T1559.001]] | Component Object Model | [RustyWater](https://attack.mitre.org/software/S9037) has used a WScript.Shell COM object to execute the CertificationKit.ini file.[^1]     |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [RustyWater](https://attack.mitre.org/software/S9037) has used the WriteHexToFile function to transform an embedded hex string to the payload CertificationKit.ini.[^1]     |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [RustyWater](https://attack.mitre.org/software/S9037) has used reddit.exe as its file name and a Cloudflare logo.[^1]      |
| [[Malicious File\|T1204.002]] | Malicious File | [RustyWater](https://attack.mitre.org/software/S9037) has used a Word document with a malicious Visual Basic for Applications (VBA) macro; when enabled, the CertificationKit.ini payload is constructed and executed.[^1]  |




## References

[^1]: [CloudSEK_RustyWater_Jan2026](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)


[^2]: Archer RAT / RUSTRIC


