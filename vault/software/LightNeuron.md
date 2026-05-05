---
aliases: 
    - S0395
    
mitre-attack: https://attack.mitre.org/software/S0395
---

## S0395

[LightNeuron](https://attack.mitre.org/software/S0395) is a sophisticated backdoor that has targeted Microsoft Exchange servers since at least 2014. [LightNeuron](https://attack.mitre.org/software/S0395) has been used by [Turla](https://attack.mitre.org/groups/G0010) to target diplomatic and foreign affairs-related organizations. The presence of certain strings in the malware suggests a Linux variant of [LightNeuron](https://attack.mitre.org/software/S0395) exists.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File Deletion\|T1070.004]] | File Deletion | [LightNeuron](https://attack.mitre.org/software/S0395) has a function to delete files.[^1]  |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [LightNeuron](https://attack.mitre.org/software/S0395) uses SMTP for C2.[^1]  |
| [[Scheduled Transfer\|T1029]] | Scheduled Transfer | [LightNeuron](https://attack.mitre.org/software/S0395) can be configured to exfiltrate data during nighttime or working hours.[^1]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [LightNeuron](https://attack.mitre.org/software/S0395) can be configured to automatically exfiltrate files under a specified directory.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [LightNeuron](https://attack.mitre.org/software/S0395) exfiltrates data over its email C2 channel.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [LightNeuron](https://attack.mitre.org/software/S0395) encrypts its configuration files with AES-256.[^1]  |
| [[Steganography\|T1001.002]] | Steganography | [LightNeuron](https://attack.mitre.org/software/S0395) is controlled via commands that are embedded into PDFs and JPGs using steganographic methods.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [LightNeuron](https://attack.mitre.org/software/S0395) has used AES and XOR to decrypt configuration files and commands.[^1]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [LightNeuron](https://attack.mitre.org/software/S0395) contains a function to encrypt and store emails that it collects.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [LightNeuron](https://attack.mitre.org/software/S0395) has used filenames associated with Exchange and Outlook for binary and configuration files, such as `winmail.dat`.[^1]  |
| [[Remote Email Collection\|T1114.002]] | Remote Email Collection | [LightNeuron](https://attack.mitre.org/software/S0395) collects Exchange emails matching rules specified in its configuration.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [LightNeuron](https://attack.mitre.org/software/S0395) gathers the victim computer name using the Win32 API call `GetComputerName`.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [LightNeuron](https://attack.mitre.org/software/S0395) has the ability to download and execute additional files.[^1]  |
| [[Automated Collection\|T1119]] | Automated Collection | [LightNeuron](https://attack.mitre.org/software/S0395) can be configured to automatically collect files under a specified directory.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [LightNeuron](https://attack.mitre.org/software/S0395) uses AES to encrypt C2 traffic.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [LightNeuron](https://attack.mitre.org/software/S0395) can store email data in files and directories specified in its configuration, such as `C:\Windows\ServiceProfiles\NetworkService\appdata\Local\Temp\`.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [LightNeuron](https://attack.mitre.org/software/S0395) is capable of executing commands via cmd.exe.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [LightNeuron](https://attack.mitre.org/software/S0395) can collect files from a local system.[^1]  |
| [[Transmitted Data Manipulation\|T1565.002]] | Transmitted Data Manipulation | [LightNeuron](https://attack.mitre.org/software/S0395) is capable of modifying email content, headers, and attachments during transit.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [LightNeuron](https://attack.mitre.org/software/S0395) gathers information about network adapters using the Win32 API call `GetAdaptersInfo`.[^1]  |
| [[Native API\|T1106]] | Native API | [LightNeuron](https://attack.mitre.org/software/S0395) is capable of starting a process using CreateProcess.[^1]  |
| [[Transport Agent\|T1505.002]] | Transport Agent | [LightNeuron](https://attack.mitre.org/software/S0395) has used a malicious Microsoft Exchange transport agent for persistence.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Turla\|G0010]] | Turla |



## References

[^1]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)


[^2]: [Secureworks IRON HUNTER Profile](http://www.secureworks.com/research/threat-profiles/iron-hunter)


