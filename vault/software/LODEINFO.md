---
aliases: 
    - S9020
    
mitre-attack: https://attack.mitre.org/software/S9020
---

## S9020

[LODEINFO](https://attack.mitre.org/software/S9020) is a fileless backdoor malware first identified in 2020 that has been used by actors including [MirrorFace](https://attack.mitre.org/groups/G1054), primarily against media, diplomatic, governmental, and public sector organizations in Japan.[^4] [^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File Deletion\|T1070.004]] | File Deletion | [LODEINFO](https://attack.mitre.org/software/S9020) can delete files to remove traces of activity from victim systems.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [LODEINFO](https://attack.mitre.org/software/S9020) can kill a process using specific process ID.[^3] [^1]  |
| [[Junk Data\|T1001.001]] | Junk Data | [LODEINFO](https://attack.mitre.org/software/S9020) can append C2 communication with randomly generated junk data.[^3] [^2]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | <br>[LODEINFO](https://attack.mitre.org/software/S9020) can incorporate a ransom command to encrypt specified files and folders.[^3] [^2] [^1]  |
| [[DLL\|T1574.001]] | DLL | [LODEINFO](https://attack.mitre.org/software/S9020) can use legitimate EXE files to sideload malicious DLLs.[^4]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [LODEINFO](https://attack.mitre.org/software/S9020) has collected stolen web cookies locally in the `%TEMP%` folder.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [LODEINFO](https://attack.mitre.org/software/S9020) can encrypt C2 communication with a hardcoded (NV4HDOeOVyL) Vigenere cipher key.[^3]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [LODEINFO](https://attack.mitre.org/software/S9020) can run `net view` and `net view /domain` for network discovery.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [LODEINFO](https://attack.mitre.org/software/S9020) has the ability to download additional files from the C2.[^3] [^2] [^1]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [LODEINFO](https://attack.mitre.org/software/S9020) can halt execution if the “en_US” locale is identified on a victim's machine.[^3]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [LODEINFO](https://attack.mitre.org/software/S9020) can execute commands with WMI.[^3] [^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [LODEINFO](https://attack.mitre.org/software/S9020) can exfiltrate collected credentials and browser cookies to the C2 server.[^2]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [LODEINFO](https://attack.mitre.org/software/S9020) can looks for the “en_US” locale on the victim’s machine.[^3]  |
| [[Compression\|T1027.015]] | Compression | [LODEINFO](https://attack.mitre.org/software/S9020) components have been compressed with zip for delivery.[^4]  |
| [[Keylogging\|T1056.001]] | Keylogging | [LODEINFO](https://attack.mitre.org/software/S9020) can capture keystrokes on targeted systems.[^2] [^1] [^5]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [LODEINFO](https://attack.mitre.org/software/S9020) has inserted junk code to obstruct code analysis.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | The [LODEINFO](https://attack.mitre.org/software/S9020) loader module contains XOR-encrypted shellcode.[^4] [^3] [^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [LODEINFO](https://attack.mitre.org/software/S9020) has the ability to take screenshots.[^3] [^2] [^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [LODEINFO](https://attack.mitre.org/software/S9020) has been distributed to targeted victims via malicious email attachments.[^4] [^2] [^1]  |
| [[Dynamic API Resolution\|T1027.007]] | Dynamic API Resolution | [LODEINFO](https://attack.mitre.org/software/S9020) can use a hashing algorithm to dynamically resolve API function addresses.[^3]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [LODEINFO](https://attack.mitre.org/software/S9020) can capture system time to send to the C2.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [LODEINFO](https://attack.mitre.org/software/S9020) can disover machine information including OS architecture, the ANSI code page (ACP) identifier, and hostname.[^3] [^1]  |
| [[Process Injection\|T1055]] | Process Injection | [LODEINFO](https://attack.mitre.org/software/S9020) can inject shellcode into the memory of compromised hosts.[^3] [^2] [^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [LODEINFO](https://attack.mitre.org/software/S9020) has been executed via victims opening malicious email attachments.[^4] [^2] [^1]  |
| [[Native API\|T1106]] | Native API | [LODEINFO](https://attack.mitre.org/software/S9020) can use Windows APIs such as `VirtualAllocEx()`, `WriteProcessMemory()`, `CreateRemoteThread()`, `NtAllocateVirtualMemory()`, `NtWriteVirtualMemory()`, and `RtlCreateUserThread()` to enable memory injection of shellcode.[^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [LODEINFO](https://attack.mitre.org/software/S9020) can enumerate the MAC address of the compromised host.[^4]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [LODEINFO](https://attack.mitre.org/software/S9020) can use VBA to drop malicious components on targeted hosts.[^4]  |
| [[Data from Local System\|T1005]] | Data from Local System | [LODEINFO](https://attack.mitre.org/software/S9020) can upload files from infected hosts to the C2.[^3] [^2] [^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [LODEINFO](https://attack.mitre.org/software/S9020) has used Registry run keys to set persistence.[^2] [^5]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | <br>[LODEINFO](https://attack.mitre.org/software/S9020) has the ability to designate specific files and folders to encryption.[^2] [^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [LODEINFO](https://attack.mitre.org/software/S9020) can identify the associated username on targeted machines.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [LODEINFO](https://attack.mitre.org/software/S9020) has used control flow flattening to obfuscate code.[^1]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [LODEINFO](https://attack.mitre.org/software/S9020) can list the contents of `%LocalAppData%\Google\Chrome\User Data\` and `%LocalAppData%\Microsoft\Edge\User Data\` to obtain cookies.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MirrorFace\|G1054]] | MirrorFace |



## References

[^1]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)


[^2]: [ESET MirrorFace DEC 2022](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)


[^3]: [Kaspersky LODEINFO Part II OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)


[^4]: [Kaspersky LODEINFO OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-i/107742/)


[^5]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)


