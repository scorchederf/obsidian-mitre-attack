---
aliases: 
    - S1226
    
mitre-attack: https://attack.mitre.org/software/S1226
---

## S1226

[BOOKWORM](https://attack.mitre.org/software/S1226) is a modular trojan known to be leveraged by [Mustang Panda](https://attack.mitre.org/groups/G0129) and was first observed utilized in 2015.  [BOOKWORM](https://attack.mitre.org/software/S1226) was later updated in late 2021 and the fall of 2022 to launch shellcode represented as UUID parameters. [^2] [^3] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [BOOKWORM](https://attack.mitre.org/software/S1226) has obtained the username from an infected host. [^3]  |
| [[Code Signing\|T1553.002]] | Code Signing | [BOOKWORM](https://attack.mitre.org/software/S1226) has used valid legitimate digital signatures and certificates to evade detection. [^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [BOOKWORM](https://attack.mitre.org/software/S1226) has communicated with its C2 via HTTP POST requests. [^3] [^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [BOOKWORM](https://attack.mitre.org/software/S1226) has modified Registry key values as part of its created service `DeviceSync`. [^3]  |
| [[Windows Service\|T1543.003]] | Windows Service | [BOOKWORM](https://attack.mitre.org/software/S1226) has created a service named `Microsoft Windows DeviceSync Service` at `HKLM\SYSTEM\CurrentControlSet\Services\DeviceSync\` to trigger execution when the system starts and to maintain persistence. [^3]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [BOOKWORM](https://attack.mitre.org/software/S1226) has created a hidden window when conducting key logging and clipboard theft through its KBLogger.dll module.[^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [BOOKWORM](https://attack.mitre.org/software/S1226) has decoded its Base64 encoded payload prior to execution.[^1]   [BOOKWORM](https://attack.mitre.org/software/S1226) has also encrypted files with RC4 and has decrypted its payload prior to execution.[^3]  |
| [[DLL\|T1574.001]] | DLL | [BOOKWORM](https://attack.mitre.org/software/S1226) has used DLL side-loading to execute the malicious payload. [^2] [^1]   [BOOKWORM](https://attack.mitre.org/software/S1226) has also side-loaded DLL components into a legitimate process, including Microsoft Malware Protection `MsMpEng.exe` and Kaspersky Anti-Virus `ushata.exe`.[^3]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [BOOKWORM](https://attack.mitre.org/software/S1226) has created services that attempt to resemble legitimate services to include a service named `Microsoft Windows DeviceSync Service`.[^3]  |
| [[Keylogging\|T1056.001]] | Keylogging | [BOOKWORM](https://attack.mitre.org/software/S1226) has used its KBLogger.dll module to capture keystrokes and stored them in a folder. [^3]  |
| [[Native API\|T1106]] | Native API | [BOOKWORM](https://attack.mitre.org/software/S1226) has used various Windows API calls during execution and defense evasion.[^2]  [^1]  [BOOKWORM](https://attack.mitre.org/software/S1226) has created a buffer on the heap using `HeapCreate` and `HeapAlloc` which allows for copying of shell code and then execution on the heap is initiated through callback function of legitimate API functions such as `EnumChildWindows` or `EnumSystemLanguageGroupsA`. [^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [BOOKWORM](https://attack.mitre.org/software/S1226) has used encryption and compression algorithms to obfuscate the traffic between the system and C2 server, methods observed included RC4, AES, XOR with 0x5a, and LZO. [^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [BOOKWORM](https://attack.mitre.org/software/S1226) has utilized Base64 encoding to obfuscate its payload.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [BOOKWORM](https://attack.mitre.org/software/S1226) has been delivered using self-extracting RAR archives.[^3]  |
| [[Timestomp\|T1070.006]] | Timestomp | [BOOKWORM](https://attack.mitre.org/software/S1226) has modified file timestamps from the export address table (EAT) to make it difficult to discern when the module was created. [^1]  |
| [[Protocol or Service Impersonation\|T1001.003]] | Protocol or Service Impersonation | [BOOKWORM](https://attack.mitre.org/software/S1226) has modified HTTP POST requests to resemble legitimate communications.[^1]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [BOOKWORM](https://attack.mitre.org/software/S1226) has used its KBLogger.dll module to steal data saved to the clipboard. [^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Mustang Panda\|G0129]] | Mustang Panda |



## References

[^1]: [Palo Alto Networks, Unit 42](https://unit42.paloaltonetworks.com/stately-taurus-uses-bookworm-malware/)


[^2]: [Broadcom](https://www.broadcom.com/support/security-center/protection-bulletin/bookworm-malware-linked-to-fireant-aka-stately-tarurus-activity-observed-in-southeast-asia)


[^3]: [Unit42 Bookworm Nov2015](https://unit42.paloaltonetworks.com/bookworm-trojan-a-model-of-modular-architecture/)


