---
aliases: 
    - S1207
    
mitre-attack: https://attack.mitre.org/software/S1207
---

## S1207

[XLoader](https://attack.mitre.org/software/S1207) is an infostealer malware in use since at least 2016. Previously known and sometimes still referred to as Formbook, [XLoader](https://attack.mitre.org/software/S1207) is a Malware as a Service (MaaS) known for stealing data from web browsers, email clients and File Transfer Protocol (FTP) applications.[^1] [^7] [^3] [^5] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Screen Capture\|T1113]] | Screen Capture | [XLoader](https://attack.mitre.org/software/S1207) can capture screenshots on compromised hosts.[^2] [^6]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [XLoader](https://attack.mitre.org/software/S1207) can collect credentials stored in email clients.[^2] [^6]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [XLoader](https://attack.mitre.org/software/S1207) uses process hollowing by injecting itself into the `explorer.exe` process and other files ithin the Windows `SysWOW64` directory.[^1] [^2] [^7]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [XLoader](https://attack.mitre.org/software/S1207) loads a copy of NTDLL to evade hooks from security monitoring tools on this library.[^1]  [XLoader](https://attack.mitre.org/software/S1207) can add the path of its executable to the Microsoft Defender exclusion list.[^6]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [XLoader](https://attack.mitre.org/software/S1207) can capture web session cookies and session information from victim browsers.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [XLoader](https://attack.mitre.org/software/S1207) features encrypted functions using the RC4 algorithm and bytecode operations.[^1] [^7]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [XLoader](https://attack.mitre.org/software/S1207) can create scheduled tasks for persistence.[^6]  |
| [[AutoHotKey & AutoIT\|T1059.010]] | AutoHotKey & AutoIT | [XLoader](https://attack.mitre.org/software/S1207) can use an AutoIT script to decrypt a payload file, load it into victim memory, then execute it on the victim machine.[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [XLoader](https://attack.mitre.org/software/S1207) can capture keystrokes from the victim machine.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [XLoader](https://attack.mitre.org/software/S1207) can delete malicious executables from compromised machines.[^5]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [XLoader](https://attack.mitre.org/software/S1207) has exploited Office vulnerabilities during local execution such as CVE-2017-11882 and CVE-2018-0798.[^6]  |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [XLoader](https://attack.mitre.org/software/S1207) can utilize decoy command and control domains within the malware configuration to circumvent sandbox analysis.[^7] [^3]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [XLoader](https://attack.mitre.org/software/S1207) can collect data stored in the victim's clipboard.[^2] [^6]  |
| [[Native API\|T1106]] | Native API | [XLoader](https://attack.mitre.org/software/S1207) uses the native Windows API for functionality, including defense evasion.[^1]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [XLoader](https://attack.mitre.org/software/S1207) can gather credentials from several web browsers.[^1] [^2] [^6]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [XLoader](https://attack.mitre.org/software/S1207) has been delivered as a phishing attachment, including PDFs with embedded links, Word and Excel files, and various archive files (ZIP, RAR, ACE, and ISOs) containing EXE payloads.[^2] [^5]  |
| [[Browser Session Hijacking\|T1185]] | Browser Session Hijacking | [XLoader](https://attack.mitre.org/software/S1207) can conduct form grabbing, steal cookies, and extract data from HTTP sessions.[^2]  |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [XLoader](https://attack.mitre.org/software/S1207) can initiate a system reboot or shutdown.[^2]  |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [XLoader](https://attack.mitre.org/software/S1207) uses anti-debugging mechanisms such as calling `NtQueryInformationProcess` with `InfoClass=7`, referencing `ProcessDebugPort`, to determine if it is being analyzed.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [XLoader](https://attack.mitre.org/software/S1207) uses XOR and RC4 algorithms to decrypt payloads and functions.[^1]  [XLoader](https://attack.mitre.org/software/S1207) can be distributed as a self-extracting RAR archive that launches an AutoIT loader.[^2]  |
| [[System Checks\|T1497.001]] | System Checks | [XLoader](https://attack.mitre.org/software/S1207) performs timing checks using the Read-Time Stamp Counter (RDTSC) instruction on the victim CPU.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [XLoader](https://attack.mitre.org/software/S1207) uses HTTP and HTTPS for command and control communication.[^2]  |
| [[Asynchronous Procedure Call\|T1055.004]] | Asynchronous Procedure Call | [XLoader](https://attack.mitre.org/software/S1207) injects code into the APC queue using `NtQueueApcThread` API.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [XLoader](https://attack.mitre.org/software/S1207) can identify the username from a victim machine.[^5]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [XLoader](https://attack.mitre.org/software/S1207) can collect system information and supported language information from the victim machine.[^5]  |
| [[Domains\|T1583.001]] | Domains | [XLoader](https://attack.mitre.org/software/S1207) can utilize hardcoded command and control domain configurations created by the XLoader authors. These are designed to mimic domain registrars and hosting service providers such as Hostinger and Namecheap.[^3]  |
| [[Software Packing\|T1027.002]] | Software Packing | [XLoader](https://attack.mitre.org/software/S1207) uses various packers, including CyaX, to obfuscate malicious executables.[^6]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [XLoader](https://attack.mitre.org/software/S1207) establishes persistence by copying its executable in a subdirectory of `%APPDATA%` or `%PROGRAMFILES%`, and then modifies Windows Registry Run keys or policies keys to execute the executable on system start.[^1] [^2]  |




## References

[^1]: [Zscaler XLoader 2025](https://www.zscaler.com/blogs/security-research/technical-analysis-xloader-versions-6-and-7-part-1)


[^2]: [Google XLoader 2017](https://cloud.google.com/blog/topics/threat-intelligence/formbook-malware-distribution-campaigns/)


[^3]: [CheckPoint XLoader 2022](https://research.checkpoint.com/2022/xloader-botnet-find-me-if-you-can/)


[^4]: Formbook


[^5]: [Acronis XLoader 2021](https://www.acronis.com/en-us/cyber-protection-center/posts/trojan-as-a-service-from-formbook-to-xloader/)


[^6]: [Netskope XLoader 2022](https://www.netskope.com/blog/new-formbook-campaign-delivered-through-phishing-emails)


[^7]: [ANY.RUN XLoader 2023](https://any.run/cybersecurity-blog/xloader-formbook-encryption-analysis-and-malware-decryption/)


