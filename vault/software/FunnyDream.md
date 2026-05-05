---
aliases: 
    - S1044
    
mitre-attack: https://attack.mitre.org/software/S1044
---

## S1044

[FunnyDream](https://attack.mitre.org/software/S1044) is a backdoor with multiple components that was used during the [FunnyDream](https://attack.mitre.org/campaigns/C0007) campaign since at least 2019, primarily for execution and exfiltration.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Service\|T1543.003]] | Windows Service | [FunnyDream](https://attack.mitre.org/software/S1044) has established persistence by running `sc.exe` and by setting the `WSearch` service to run automatically.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [FunnyDream](https://attack.mitre.org/software/S1044) can use a Registry Run Key and the Startup folder to establish persistence.[^2]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [FunnyDream](https://attack.mitre.org/software/S1044) can use WMI to open a Windows command shell on a remote machine.[^2]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | The [FunnyDream](https://attack.mitre.org/software/S1044) FilepakMonitor component can detect removable drive insertion.[^2]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [FunnyDream](https://attack.mitre.org/software/S1044) can stage collected information including screen captures and logged keystrokes locally.[^2]  |
| [[Component Object Model\|T1559.001]] | Component Object Model | [FunnyDream](https://attack.mitre.org/software/S1044) can use com objects identified with `CLSID_ShellLink`(`IShellLink` and `IPersistFile`) and `WScript.Shell`(`RegWrite` method) to enable persistence mechanisms.[^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [FunnyDream](https://attack.mitre.org/software/S1044) can use `rundll32` for execution of its components.[^2]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | The [FunnyDream](https://attack.mitre.org/software/S1044) FilepakMonitor component can inject into the Bka.exe process using the `VirtualAllocEx`, `WriteProcessMemory` and `CreateRemoteThread` APIs to load the DLL component.[^2]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [FunnyDream](https://attack.mitre.org/software/S1044) can connect to HTTP proxies via TCP to create a tunnel to C2.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [FunnyDream](https://attack.mitre.org/software/S1044) has the ability to discover processes, including `Bka.exe` and `BkavUtil.exe`.[^2]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [FunnyDream](https://attack.mitre.org/software/S1044) has used a service named `WSearch` for execution.[^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [FunnyDream](https://attack.mitre.org/software/S1044) can execute commands, including gathering user information, and send the results to C2.[^2]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [FunnyDream](https://attack.mitre.org/software/S1044) can collect information about hosts on the victim network.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | The [FunnyDream](https://attack.mitre.org/software/S1044) Keyrecord component can capture keystrokes.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [FunnyDream](https://attack.mitre.org/software/S1044) can parse the `ProxyServer` string in the Registry to discover http proxies.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [FunnyDream](https://attack.mitre.org/software/S1044) has the ability to gather user information from the targeted system using `whoami/upn&whoami/fqdn&whoami/logonid&whoami/all`.[^2]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [FunnyDream](https://attack.mitre.org/software/S1044) can check system time to help determine when changes were made to specified files.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [FunnyDream](https://attack.mitre.org/software/S1044) can check `Software\Microsoft\Windows\CurrentVersion\Internet Settings` to extract the `ProxyServer` string.[^2]  |
| [[Automated Collection\|T1119]] | Automated Collection | [FunnyDream](https://attack.mitre.org/software/S1044) can monitor files for changes and automatically collect them.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | The [FunnyDream](https://attack.mitre.org/software/S1044) ScreenCap component can take screenshots on a compromised host.[^2]  |
| [[Proxy\|T1090]] | Proxy | [FunnyDream](https://attack.mitre.org/software/S1044) can identify and use configured proxies in a compromised network for C2 communication.[^2]  |
| [[Archive via Library\|T1560.002]] | Archive via Library | [FunnyDream](https://attack.mitre.org/software/S1044) has compressed collected files with zLib.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [FunnyDream](https://attack.mitre.org/software/S1044) can download additional files onto a compromised host.[^2]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [FunnyDream](https://attack.mitre.org/software/S1044) has the ability to clean traces of malware deployment.[^2]  |
| [[Native API\|T1106]] | Native API | [FunnyDream](https://attack.mitre.org/software/S1044) can use Native API for defense evasion, discovery, and collection.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [FunnyDream](https://attack.mitre.org/software/S1044) can upload files from victims' machines.[^2] [^1]  |
| [[Data Obfuscation\|T1001]] | Data Obfuscation | [FunnyDream](https://attack.mitre.org/software/S1044) can send compressed and obfuscated packets to C2.[^2]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [FunnyDream](https://attack.mitre.org/software/S1044) has compressed collected files with zLib and encrypted them using an XOR operation with the string key from the command line or `qwerasdf` if the command line argument doesn’t contain the key. File names are obfuscated using XOR with the same key as the compressed file content.[^2]  |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | The [FunnyDream](https://attack.mitre.org/software/S1044) FilePakMonitor component has the ability to collect files from removable devices.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [FunnyDream](https://attack.mitre.org/software/S1044) can identify the processes for Bkav antivirus.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [FunnyDream](https://attack.mitre.org/software/S1044) can use `cmd.exe` for execution on remote hosts.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [FunnyDream](https://attack.mitre.org/software/S1044) can Base64 encode its C2 address stored in a template binary with the `xyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw_-` or<br>`xyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw_=` character sets.[^2]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [FunnyDream](https://attack.mitre.org/software/S1044) can enumerate all logical drives on a targeted machine.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [FunnyDream](https://attack.mitre.org/software/S1044) can delete files including its dropper component.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [FunnyDream](https://attack.mitre.org/software/S1044) can identify files with .doc, .docx, .ppt, .pptx, .xls, .xlsx, and .pdf extensions and specific timestamps for collection.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [FunnyDream](https://attack.mitre.org/software/S1044) can communicate with C2 over TCP and UDP.[^2]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [FunnyDream](https://attack.mitre.org/software/S1044) has the ability to discover application windows via execution of `EnumWindows`.[^2]  |




## References

[^1]: [Kaspersky APT Trends Q1 2020](https://securelist.com/apt-trends-report-q1-2020/96826/)


[^2]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)


