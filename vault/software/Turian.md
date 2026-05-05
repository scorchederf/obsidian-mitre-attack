---
aliases: 
    - S0647
    
mitre-attack: https://attack.mitre.org/software/S0647
---

## S0647

[Turian](https://attack.mitre.org/software/S0647) is a backdoor that has been used by [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) to target Ministries of Foreign Affairs, telecommunication companies, and charities in Africa, Europe, the Middle East, and Asia. First reported in 2021, [Turian](https://attack.mitre.org/software/S0647) is likely related to Quarian, an older backdoor that was last observed being used in 2013 against diplomatic targets in Syria and the United States.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Turian](https://attack.mitre.org/software/S0647) has the ability to use `/bin/sh` to execute commands.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Turian](https://attack.mitre.org/software/S0647) can search for specific files and list directories.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Turian](https://attack.mitre.org/software/S0647) can use VMProtect for obfuscation.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Turian](https://attack.mitre.org/software/S0647) has the ability to take screenshots.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Turian](https://attack.mitre.org/software/S0647) can retrieve usernames.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Turian](https://attack.mitre.org/software/S0647) can establish persistence by adding Registry Run keys.[^1]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Turian](https://attack.mitre.org/software/S0647) can use WinRAR to create a password-protected archive for files of interest.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Turian](https://attack.mitre.org/software/S0647) has the ability to use a XOR decryption key to extract C2 server domains and IP addresses.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Turian](https://attack.mitre.org/software/S0647) can retrieve the internal IP address of a compromised host.[^1]  |
| [[Python\|T1059.006]] | Python | [Turian](https://attack.mitre.org/software/S0647) has the ability to use Python to spawn a Unix shell.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Turian](https://attack.mitre.org/software/S0647) can store copied files in a specific directory prior to exfiltration.[^1]  |
| [[Junk Data\|T1001.001]] | Junk Data | [Turian](https://attack.mitre.org/software/S0647) can insert pseudo-random characters into its network encryption setup.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Turian](https://attack.mitre.org/software/S0647) has the ability to use HTTP for its C2.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Turian](https://attack.mitre.org/software/S0647) can download additional files and tools from its C2.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Turian](https://attack.mitre.org/software/S0647) can create a remote shell and execute commands using [cmd](https://attack.mitre.org/software/S0106).[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Turian](https://attack.mitre.org/software/S0647) can retrieve system information including OS version, memory usage, local hostname, and system adapter information.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Turian](https://attack.mitre.org/software/S0647) can disguise as a legitimate service to blend into normal operations.[^1]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [Turian](https://attack.mitre.org/software/S0647) can scan for removable media to collect data.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[BackdoorDiplomacy\|G0135]] | BackdoorDiplomacy |



## References

[^1]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)


