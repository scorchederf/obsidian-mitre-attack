---
aliases: 
    - S1141
    
mitre-attack: https://attack.mitre.org/software/S1141
---

## S1141

[LunarWeb](https://attack.mitre.org/software/S1141) is a backdoor that has been used by [Turla](https://attack.mitre.org/groups/G0010) since at least 2020 including in a compromise of a European ministry of foreign affairs (MFA) together with [LunarLoader](https://attack.mitre.org/software/S1143) and [LunarMail](https://attack.mitre.org/software/S1142). [LunarWeb](https://attack.mitre.org/software/S1141) has only been observed deployed against servers and can use [Steganography](https://attack.mitre.org/techniques/T1001/002) to obfuscate command and control.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Group Policy Discovery\|T1615]] | Group Policy Discovery | [LunarWeb](https://attack.mitre.org/software/S1141) can capture information on group policy settings[^1]  |
| [[Steganography\|T1001.002]] | Steganography | [LunarWeb](https://attack.mitre.org/software/S1141) can receive C2 commands hidden in the structure of .jpg and .gif images.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [LunarWeb](https://attack.mitre.org/software/S1141) can run shell commands using a BAT file with a name matching `%TEMP%\<⁠random_9_alnum_chars>.batfile` or through cmd.exe with the `/c` and `/U` option for Unicode output.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [LunarWeb](https://attack.mitre.org/software/S1141) can use WMI queries and shell commands such as systeminfo.exe to collect the operating system, BIOS version, and domain name of the targeted system.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [LunarWeb](https://attack.mitre.org/software/S1141) has the ability to run shell commands via PowerShell.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [LunarWeb](https://attack.mitre.org/software/S1141) can send short C2 commands, up to 512 bytes, encrypted with RSA-4096.[^1]  |
| [[Multi-Stage Channels\|T1104]] | Multi-Stage Channels | [LunarWeb](https://attack.mitre.org/software/S1141) can use one C2 URL for first contact and to upload information about the host computer and two additional C2 URLs for getting commands.[^1]  |
| [[Archive via Library\|T1560.002]] | Archive via Library | [LunarWeb](https://attack.mitre.org/software/S1141) can zlib-compress data prior to exfiltration.[^1]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [LunarWeb](https://attack.mitre.org/software/S1141) can pause for a number of hours before entering its C2 communication loop.[^1]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [LunarWeb](https://attack.mitre.org/software/S1141) can run a custom binary protocol under HTTPS for C2.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [LunarWeb](https://attack.mitre.org/software/S1141) has the ability to retrieve directory listings.[^1]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [LunarWeb](https://attack.mitre.org/software/S1141) can identify shared resources in compromised environments.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [LunarWeb](https://attack.mitre.org/software/S1141) can send AES encrypted C2 commands.[^1]  |
| [[Software Discovery\|T1518]] | Software Discovery | [LunarWeb](https://attack.mitre.org/software/S1141) can list installed software on compromised systems.[^1]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [LunarWeb](https://attack.mitre.org/software/S1141) can create a ZIP archive with specified files and directories.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [LunarWeb](https://attack.mitre.org/software/S1141) can use shell commands to discover network adapters and configuration.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [LunarWeb](https://attack.mitre.org/software/S1141) can decrypt strings related to communication configuration using RC4 with a static key.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [LunarWeb](https://attack.mitre.org/software/S1141) can self-delete from a compromised host if safety checks of C2 connectivity fail.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [LunarWeb](https://attack.mitre.org/software/S1141) can enumerate system network connections.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [LunarWeb](https://attack.mitre.org/software/S1141) can use `POST` to send victim identification to C2 and `GET` to retrieve commands.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | The [LunarWeb](https://attack.mitre.org/software/S1141) install files have been encrypted with AES-256.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [LunarWeb](https://attack.mitre.org/software/S1141) has used shell commands to list running processes.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [LunarWeb](https://attack.mitre.org/software/S1141) can use WMI queries for discovery on the victim host.[^1]  |
| [[Local Groups\|T1069.001]] | Local Groups | [LunarWeb](https://attack.mitre.org/software/S1141) can discover local group memberships.[^1]  |
| [[Proxy\|T1090]] | Proxy | [LunarWeb](https://attack.mitre.org/software/S1141) has the ability to use a HTTP proxy server for C&C communications.[^1]  |
| [[Data Transfer Size Limits\|T1030]] | Data Transfer Size Limits | [LunarWeb](https://attack.mitre.org/software/S1141) can split exfiltrated data that exceeds 1.33 MB in size into multiple random sized parts between 384 and 512 KB.[^1]  |
| [[Inter-Process Communication\|T1559]] | Inter-Process Communication | [LunarWeb](https://attack.mitre.org/software/S1141) can retrieve output from arbitrary processes and shell commands via a pipe.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [LunarWeb](https://attack.mitre.org/software/S1141) can use Base64 encoding to obfuscate C2 commands.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [LunarWeb](https://attack.mitre.org/software/S1141) can collect user information from the targeted host.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [LunarWeb](https://attack.mitre.org/software/S1141) has run shell commands to obtain a list of installed security products.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Turla\|G0010]] | Turla |



## References

[^1]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)


