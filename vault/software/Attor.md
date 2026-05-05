---
aliases: 
    - S0438
    
mitre-attack: https://attack.mitre.org/software/S0438
---

## S0438

[Attor](https://attack.mitre.org/software/S0438) is a Windows-based espionage platform that has been seen in use since 2013. [Attor](https://attack.mitre.org/software/S0438) has a loadable plugin architecture to customize functionality for specific targets.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Attor](https://attack.mitre.org/software/S0438) has a plugin that enumerates files with specific extensions on all hard disk drives and stores file information in encrypted log files.[^1]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [Attor](https://attack.mitre.org/software/S0438) encrypts collected data with a custom implementation of Blowfish and RSA ciphers.[^1]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [Attor](https://attack.mitre.org/software/S0438) can obtain application window titles and then determines which windows to perform Screen Capture on.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Attor](https://attack.mitre.org/software/S0438) has encrypted data symmetrically using a randomly generated Blowfish (OFB) key which is encrypted with a public RSA key.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Attor](https://attack.mitre.org/software/S0438)'s dispatcher disguises itself as a legitimate task (i.e., the task name and description appear legitimate).[^1]  |
| [[System Checks\|T1497.001]] | System Checks | [Attor](https://attack.mitre.org/software/S0438) can detect whether it is executed in some virtualized or emulated environment by searching for specific artifacts, such as communication with I/O ports and using VM-specific instructions.[^1]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [Attor](https://attack.mitre.org/software/S0438) has used [Tor](https://attack.mitre.org/software/S0183) for C2 communication.[^1]  |
| [[Logon Script (Windows)\|T1037.001]] | Logon Script (Windows) | [Attor](https://attack.mitre.org/software/S0438)'s dispatcher can establish persistence via adding a Registry key with a logon script `HKEY_CURRENT_USER\Environment "UserInitMprLogonScript" `.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Attor](https://attack.mitre.org/software/S0438)'s installer plugin can schedule rundll32.exe to load the dispatcher.[^1]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [Attor](https://attack.mitre.org/software/S0438) has a plugin that collects data stored in the Windows clipboard by using the OpenClipboard and GetClipboardData APIs.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Attor](https://attack.mitre.org/software/S0438)'s Blowfish key is encrypted with a public RSA key.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Attor](https://attack.mitre.org/software/S0438) can download additional plugins, updates and other files. [^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Attor](https://attack.mitre.org/software/S0438) has staged collected data in a central upload directory prior to exfiltration.[^1]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [Attor](https://attack.mitre.org/software/S0438) has a plugin that collects information about inserted storage devices, modems, and phone devices.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Attor](https://attack.mitre.org/software/S0438)'s dispatcher can modify the Run registry key.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Attor](https://attack.mitre.org/software/S0438)'s has a plugin that captures screenshots of the target applications.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Attor](https://attack.mitre.org/software/S0438) has exfiltrated data over the C2 channel.[^1]  |
| [[Shared Modules\|T1129]] | Shared Modules | [Attor](https://attack.mitre.org/software/S0438)'s dispatcher can execute additional plugins by loading the respective DLLs.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Attor](https://attack.mitre.org/software/S0438)'s dispatcher can establish persistence by registering a new service.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | Strings in [Attor](https://attack.mitre.org/software/S0438)'s components are encrypted with a XOR cipher, using a hardcoded key and the configuration data, log files and plugins are encrypted using a hybrid encryption scheme of Blowfish-OFB combined with RSA.[^1]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [Attor](https://attack.mitre.org/software/S0438) has used FTP protocol for C2 communication.[^1]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Attor](https://attack.mitre.org/software/S0438) has automatically collected data about the compromised system.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Attor](https://attack.mitre.org/software/S0438)'s installer plugin can schedule a new task that loads the dispatcher on boot/logon.[^1]  |
| [[Timestomp\|T1070.006]] | Timestomp | [Attor](https://attack.mitre.org/software/S0438) has manipulated the time of last access to files and registry keys after they have been created or modified.[^1]  |
| [[Process Injection\|T1055]] | Process Injection | [Attor](https://attack.mitre.org/software/S0438)'s dispatcher can inject itself into running processes to gain higher privileges and to evade detection.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | One of [Attor](https://attack.mitre.org/software/S0438)'s plugins can collect user credentials via capturing keystrokes and can capture keystrokes pressed within the window of the injected process.[^1]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Attor](https://attack.mitre.org/software/S0438)'s dispatcher can be executed as a service.[^1]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [Attor](https://attack.mitre.org/software/S0438) can set attributes of log files and directories to HIDDEN, SYSTEM, ARCHIVE, or a combination of those.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Attor](https://attack.mitre.org/software/S0438)’s plugin deletes the collected files and log files after exfiltration.[^1]  |
| [[Audio Capture\|T1123]] | Audio Capture | [Attor](https://attack.mitre.org/software/S0438)'s has a plugin that is capable of recording audio using available input sound devices.[^1]  |
| [[Native API\|T1106]] | Native API | [Attor](https://attack.mitre.org/software/S0438)'s dispatcher has used CreateProcessW API for execution.[^1]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [Attor](https://attack.mitre.org/software/S0438) has a file uploader plugin that automatically exfiltrates the collected data and log files to the C2 server.[^1]  |
| [[Asynchronous Procedure Call\|T1055.004]] | Asynchronous Procedure Call | [Attor](https://attack.mitre.org/software/S0438) performs the injection by attaching its code into the APC queue using NtQueueApcThread API.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Attor](https://attack.mitre.org/software/S0438) monitors the free disk space on the system.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [Attor](https://attack.mitre.org/software/S0438) has opened the registry and performed query searches.[^1]  |




## References

[^1]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)


[^2]: Attor


