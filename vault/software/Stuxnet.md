---
aliases: 
    - S0603
    
mitre-attack: https://attack.mitre.org/software/S0603
---

## S0603

[Stuxnet](https://attack.mitre.org/software/S0603) was the first publicly reported malware to specifically target industrial control systems devices. [Stuxnet](https://attack.mitre.org/software/S0603) is a large and complex malware that utilized multiple behaviors, including numerous zero-day vulnerabilities, a sophisticated Windows rootkit, and network infection routines.[^2] [^4] [^1] [^3]  [Stuxnet](https://attack.mitre.org/software/S0603) was discovered in 2010, with some components being used as early as November 2008.[^2]  

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Stuxnet](https://attack.mitre.org/software/S0603) collects the IP address of a compromised system.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Stuxnet](https://attack.mitre.org/software/S0603) collects system information including computer and domain names, OS version, and S7P paths.[^2]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Stuxnet](https://attack.mitre.org/software/S0603) transforms encrypted binary data into an ASCII string in order to use it as a URL parameter value.[^2]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [Stuxnet](https://attack.mitre.org/software/S0603) encrypts exfiltrated data via C2 with static 31-byte long XOR keys.[^2]  |
| [[Timestomp\|T1070.006]] | Timestomp | [Stuxnet](https://attack.mitre.org/software/S0603) extracts and writes driver files that match the times of other legitimate files.[^2]  |
| [[Shared Modules\|T1129]] | Shared Modules | [Stuxnet](https://attack.mitre.org/software/S0603) calls LoadLibrary then executes exports from a DLL.[^2]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Stuxnet](https://attack.mitre.org/software/S0603) used WMI with an `explorer.exe` token to execute on a remote share.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Stuxnet](https://attack.mitre.org/software/S0603) can create registry keys to load driver files.[^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Stuxnet](https://attack.mitre.org/software/S0603) uses a driver registered as a boot start service as the main load-point.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Stuxnet](https://attack.mitre.org/software/S0603) decrypts resources that are loaded into memory and executed.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Stuxnet](https://attack.mitre.org/software/S0603) uses an RPC server that contains a routine for file deletion and also removes itself from the system through a DLL export by deleting specific files.[^2]  |
| [[Token Impersonation／Theft\|T1134.001]] | Token Impersonation／Theft | [Stuxnet](https://attack.mitre.org/software/S0603) attempts to impersonate an anonymous token to enumerate bindings in the service control manager.[^2]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [Stuxnet](https://attack.mitre.org/software/S0603) propagates using the MS10-061 Print Spooler and MS08-067 Windows Server Service vulnerabilities.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Stuxnet](https://attack.mitre.org/software/S0603) uses encrypted configuration blocks and writes encrypted files to disk.[^2]  |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [Stuxnet](https://attack.mitre.org/software/S0603) can propagate via removable media using an autorun.inf file or the CVE-2010-2568 LNK vulnerability.[^2]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [Stuxnet](https://attack.mitre.org/software/S0603) checks for specific operating systems on 32-bit machines, Registry keys, and dates for vulnerabilities, and will exit execution if the values are not met.[^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Stuxnet](https://attack.mitre.org/software/S0603) sends compromised victim information via HTTP.[^2]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [Stuxnet](https://attack.mitre.org/software/S0603) can delete OLE Automation and SQL stored procedures used to store malicious payloads.[^2]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Stuxnet](https://attack.mitre.org/software/S0603) injects an entire DLL into an existing, newly created, or preselected trusted process.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Stuxnet](https://attack.mitre.org/software/S0603) encodes the payload of system information sent to the command and control servers using a one byte 0xFF XOR key. [Stuxnet](https://attack.mitre.org/software/S0603) also uses a 31-byte long static byte string to XOR data sent to command and control servers. The servers use a different static key to encrypt replies to the implant.[^2]  |
| [[Rootkit\|T1014]] | Rootkit | [Stuxnet](https://attack.mitre.org/software/S0603) uses a Windows rootkit to mask its binaries and other relevant files.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Stuxnet](https://attack.mitre.org/software/S0603) uses HTTP to communicate with a command and control server. [^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Stuxnet](https://attack.mitre.org/software/S0603) uses a driver to scan for specific filesystem driver objects.[^2]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Stuxnet](https://attack.mitre.org/software/S0603) has the ability to generate new C2 domains.[^2]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Stuxnet](https://attack.mitre.org/software/S0603) enumerates user accounts of the domain.[^2]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [Stuxnet](https://attack.mitre.org/software/S0603) enumerates removable drives for infection.[^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Stuxnet](https://attack.mitre.org/software/S0603) reduces the integrity level of objects to allow write actions.[^2]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [Stuxnet](https://attack.mitre.org/software/S0603) used MS10-073 and an undisclosed Task Scheduler vulnerability to escalate privileges on local Windows machines.[^2]  |
| [[Default Accounts\|T1078.001]] | Default Accounts | [Stuxnet](https://attack.mitre.org/software/S0603) infected WinCC machines via a hardcoded database server password.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Stuxnet](https://attack.mitre.org/software/S0603) enumerates the currently running processes related to a variety of security products.[^2]  |
| [[Local Account\|T1087.001]] | Local Account | [Stuxnet](https://attack.mitre.org/software/S0603) enumerates user accounts of the local host.[^2]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Stuxnet](https://attack.mitre.org/software/S0603) propagates to available network shares.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [Stuxnet](https://attack.mitre.org/software/S0603) searches the Registry for indicators of security programs.[^2]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Stuxnet](https://attack.mitre.org/software/S0603) collects the time and date of a system when it is infected.[^2]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Stuxnet](https://attack.mitre.org/software/S0603) used a digitally signed driver with a compromised Realtek certificate.[^2]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Stuxnet](https://attack.mitre.org/software/S0603) enumerates the directories of a network resource.[^2]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [Stuxnet](https://attack.mitre.org/software/S0603) attempts to access network resources with a domain account’s credentials.[^2]  |
| [[Native API\|T1106]] | Native API | [Stuxnet](https://attack.mitre.org/software/S0603) uses the SetSecurityDescriptorDacl API to reduce object integrity levels.[^2]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Stuxnet](https://attack.mitre.org/software/S0603) uses an RPC server that contains a file dropping routine and support for payload version updates for P2P communications within a victim network.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Stuxnet](https://attack.mitre.org/software/S0603) schedules a network job to execute two minutes after host infection.[^2]  |
| [[Remote Services\|T1021]] | Remote Services | [Stuxnet](https://attack.mitre.org/software/S0603) can propagate via peer-to-peer communication and updates using RPC.[^2]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [Stuxnet](https://attack.mitre.org/software/S0603) installs an RPC server for P2P communications.[^2]  |
| [[Taint Shared Content\|T1080]] | Taint Shared Content | [Stuxnet](https://attack.mitre.org/software/S0603) infects remote servers via network shares and by infecting WinCC database views with malicious code.[^2]  |
| [[SQL Stored Procedures\|T1505.001]] | SQL Stored Procedures | [Stuxnet](https://attack.mitre.org/software/S0603) used xp_cmdshell to store and execute SQL code.[^2]  |




## References

[^1]: [ESET Stuxnet Under the Microscope](https://web-assets.esetstatic.com/wls/2012/11/Stuxnet_Under_the_Microscope.pdf)


[^2]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)


[^3]: [Langer Stuxnet](https://www.langner.com/wp-content/uploads/2017/03/to-kill-a-centrifuge.pdf)


[^4]: [CISA ICS Advisory ICSA-10-272-01](https://us-cert.cisa.gov/ics/advisories/ICSA-10-272-01)


[^5]: W32.Stuxnet


