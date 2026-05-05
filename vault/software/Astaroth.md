---
aliases: 
    - S0373
    
mitre-attack: https://attack.mitre.org/software/S0373
---

## S0373

[Astaroth](https://attack.mitre.org/software/S0373) is a Trojan and information stealer known to affect companies in Europe, Brazil, and throughout Latin America. It has been known publicly since at least late 2017. [^3] [^1] [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | [Astaroth](https://attack.mitre.org/software/S0373) can store C2 information on cloud hosting services such as AWS and CloudFlare and websites like YouTube and Facebook.[^4]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Astaroth](https://attack.mitre.org/software/S0373) collects the timestamp from the infected machine. [^1]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [Astaroth](https://attack.mitre.org/software/S0373) loads its module with the XSL script parameter `vShow` set to zero, which opens the application with a hidden window. [^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Astaroth](https://attack.mitre.org/software/S0373) has used an XOR-based algorithm to encrypt payloads twice with different keys.[^4]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [Astaroth](https://attack.mitre.org/software/S0373) collects information from the clipboard by using the OpenClipboard() and GetClipboardData() libraries. [^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Astaroth](https://attack.mitre.org/software/S0373) collects the machine name and keyboard language from the system. [^1] [^3]  |
| [[System Checks\|T1497.001]] | System Checks | [Astaroth](https://attack.mitre.org/software/S0373) can check for Windows product ID's used by sandboxes and usernames and disk serial numbers associated with analyst environments.[^4]  |
| [[Shared Modules\|T1129]] | Shared Modules | [Astaroth](https://attack.mitre.org/software/S0373) uses the LoadLibraryExW() function to load additional modules. [^3]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Astaroth](https://attack.mitre.org/software/S0373) has used malicious VBS e-mail attachments for execution.[^4]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Astaroth](https://attack.mitre.org/software/S0373) searches for different processes on the system.[^3]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Astaroth](https://attack.mitre.org/software/S0373) has used malicious files including VBS, LNK, and HTML for execution.[^4]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Astaroth](https://attack.mitre.org/software/S0373) uses a fromCharCode() deobfuscation method to avoid explicitly writing execution commands and to hide its code. [^3] [^4]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Astaroth](https://attack.mitre.org/software/S0373) encodes data using Base64 before sending it to the C2 server. [^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Astaroth](https://attack.mitre.org/software/S0373) uses a software packer called Pe123\RPolyCryptor.[^3]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Astaroth](https://attack.mitre.org/software/S0373) can be loaded through regsvr32.exe.[^3]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Astaroth](https://attack.mitre.org/software/S0373) checks for the presence of Avast antivirus in the `C:\Program\Files\` folder. [^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Astaroth](https://attack.mitre.org/software/S0373) has been delivered via malicious e-mail attachments.[^4]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Astaroth](https://attack.mitre.org/software/S0373) logs keystrokes from the victim's machine. [^1]  |
| [[DLL\|T1574.001]] | DLL | [Astaroth](https://attack.mitre.org/software/S0373) can launch itself via DLL Search Order Hijacking.[^4]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Astaroth](https://attack.mitre.org/software/S0373) uses JavaScript to perform its core functionalities. [^1] [^4]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Astaroth](https://attack.mitre.org/software/S0373) exfiltrates collected information from its r1.log file to the external C2 server. [^3]  |
| [[XSL Script Processing\|T1220]] | XSL Script Processing | [Astaroth](https://attack.mitre.org/software/S0373) executes embedded JScript or VBScript in an XSL stylesheet located on a remote domain. [^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Astaroth](https://attack.mitre.org/software/S0373) collects the external IP address from the system. [^1]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Astaroth](https://attack.mitre.org/software/S0373) can create a new process in a suspended state from a targeted legitimate process in order to unmap its memory and replace it with malicious code.[^3] [^4]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [Astaroth](https://attack.mitre.org/software/S0373)'s initial payload is a malicious .LNK file. [^1] [^3]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Astaroth](https://attack.mitre.org/software/S0373) uses WMIC to execute payloads. [^1]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [Astaroth](https://attack.mitre.org/software/S0373) uses an external software known as NetPass to recover passwords. [^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Astaroth](https://attack.mitre.org/software/S0373) uses [certutil](https://attack.mitre.org/software/S0160) and [BITSAdmin](https://attack.mitre.org/software/S0190) to download additional malware. [^1] [^3] [^4]  |
| [[Unsecured Credentials\|T1552]] | Unsecured Credentials | [Astaroth](https://attack.mitre.org/software/S0373) uses an external software known as NetPass to recover passwords. [^3]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Astaroth](https://attack.mitre.org/software/S0373) has obfuscated and randomized parts of the JScript code it is initiating.[^3]  |
| [[NTFS File Attributes\|T1564.004]] | NTFS File Attributes | [Astaroth](https://attack.mitre.org/software/S0373) can abuse alternate data streams (ADS) to store content for malicious payloads.[^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Astaroth](https://attack.mitre.org/software/S0373) creates a startup item for persistence. [^1]  |
| [[Compiled HTML File\|T1218.001]] | Compiled HTML File | [Astaroth](https://attack.mitre.org/software/S0373) uses ActiveX objects for file execution and manipulation. [^1]  |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [Astaroth](https://attack.mitre.org/software/S0373) has used a DGA in C2 communications.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Astaroth](https://attack.mitre.org/software/S0373) spawns a CMD process to execute commands. [^3]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Astaroth](https://attack.mitre.org/software/S0373) collects data in a plaintext file named r1.log before exfiltration. [^1]  |




## References

[^1]: [Cofense Astaroth Sept 2018](https://web.archive.org/web/20200302071436/https://cofense.com/seeing-resurgence-demonic-astaroth-wmic-trojan/)


[^2]: Guildma


[^3]: [Cybereason Astaroth Feb 2019](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)


[^4]: [Securelist Brazilian Banking Malware July 2020](https://securelist.com/the-tetrade-brazilian-banking-malware/97779/)


