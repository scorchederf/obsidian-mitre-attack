---
aliases: 
    - S0182
    
mitre-attack: https://attack.mitre.org/software/S0182
---

## S0182

[FinFisher](https://attack.mitre.org/software/S0182) is a government-grade commercial surveillance spyware reportedly sold exclusively to government agencies for use in targeted and lawful criminal investigations. It is heavily obfuscated and uses multiple anti-analysis techniques. It has other variants including [Wingbird](https://attack.mitre.org/software/S0176). [^1]  [^4]  [^9]  [^2]  [^7] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Token Impersonation／Theft\|T1134.001]] | Token Impersonation／Theft | [FinFisher](https://attack.mitre.org/software/S0182) uses token manipulation with NtFilterToken as part of UAC bypass.[^1] [^7]  |
| [[Screen Capture\|T1113]] | Screen Capture | [FinFisher](https://attack.mitre.org/software/S0182) takes a screenshot of the screen and displays it on top of all other windows for few seconds in an apparent attempt to hide some messages showed by the system during the setup process.[^1] [^7]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [FinFisher](https://attack.mitre.org/software/S0182) establishes persistence by creating the Registry key `HKCU\Software\Microsoft\Windows\Run`.[^1] [^7]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [FinFisher](https://attack.mitre.org/software/S0182) clears the system event logs using ` OpenEventLog/ClearEventLog APIs `.[^1] [^7]  |
| [[System Checks\|T1497.001]] | System Checks | [FinFisher](https://attack.mitre.org/software/S0182) obtains the hardware device list and checks if the MD5 of the vendor ID is equal to a predefined list in order to check for sandbox/virtualized environments.[^7]  |
| [[DLL\|T1574.001]] | DLL | [FinFisher](https://attack.mitre.org/software/S0182) uses DLL side-loading to load malicious programs.[^1] [^7]  A [FinFisher](https://attack.mitre.org/software/S0182) variant also uses DLL search order hijacking.[^1] [^2]   |
| [[Credential API Hooking\|T1056.004]] | Credential API Hooking | [FinFisher](https://attack.mitre.org/software/S0182) hooks processes by modifying IAT pointers to CreateWindowEx.[^1] [^6]  |
| [[Software Packing\|T1027.002]] | Software Packing | A [FinFisher](https://attack.mitre.org/software/S0182) variant uses a custom packer.[^1] [^2]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [FinFisher](https://attack.mitre.org/software/S0182) injects itself into various processes depending on whether it is low integrity or high integrity.[^1] [^7]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [FinFisher](https://attack.mitre.org/software/S0182) performs UAC bypass.[^1] [^7]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [FinFisher](https://attack.mitre.org/software/S0182) enumerates directories and scans for certain files.[^1] [^7]  |
| [[Bootkit\|T1542.003]] | Bootkit | Some [FinFisher](https://attack.mitre.org/software/S0182) variants incorporate an MBR rootkit.[^1] [^7]  |
| [[Query Registry\|T1012]] | Query Registry | [FinFisher](https://attack.mitre.org/software/S0182) queries Registry values as part of its anti-sandbox checks.[^1] [^7]  |
| [[Windows Service\|T1543.003]] | Windows Service | [FinFisher](https://attack.mitre.org/software/S0182) creates a new Windows service with the malicious executable for persistence.[^1] [^7]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [FinFisher](https://attack.mitre.org/software/S0182) contains junk code in its functions in an effort to confuse disassembly programs.[^1] [^7]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [FinFisher](https://attack.mitre.org/software/S0182) renames one of its .dll files to uxtheme.dll in an apparent attempt to masquerade as a legitimate file.[^1] [^7]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [FinFisher](https://attack.mitre.org/software/S0182) extracts and decrypts stage 3 malware, which is stored in encrypted resources.[^1] [^7]  |
| [[Process Discovery\|T1057]] | Process Discovery | [FinFisher](https://attack.mitre.org/software/S0182) checks its parent process for indications that it is running in a sandbox setup.[^1] [^7]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [FinFisher](https://attack.mitre.org/software/S0182) probes the system to check for antimalware processes.[^1] [^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [FinFisher](https://attack.mitre.org/software/S0182) checks if the victim OS is 32 or 64-bit.[^1] [^7]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [FinFisher](https://attack.mitre.org/software/S0182) is heavily obfuscated in many ways, including through the use of spaghetti code in its functions in an effort to confuse disassembly programs. It also uses a custom XOR algorithm to obfuscate code.[^1] [^7]  |
| [[KernelCallbackTable\|T1574.013]] | KernelCallbackTable | [FinFisher](https://attack.mitre.org/software/S0182) has used the `KernelCallbackTable` to hijack the execution flow of a process by replacing the `__fnDWORD` function with the address of a created [Asynchronous Procedure Call](https://attack.mitre.org/techniques/T1055/004) stub routine.[^8]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Dark Caracal\|G0070]] | Dark Caracal |



## References

[^1]: [FinFisher Citation](https://web.archive.org/web/20171222050934/http://www.finfisher.com/FinFisher/index.html)


[^2]: [Securelist BlackOasis Oct 2017](https://securelist.com/blackoasis-apt-and-new-targeted-attacks-leveraging-zero-day-exploit/82732/)


[^3]: [Lookout Dark Caracal Jan 2018](https://info.lookout.com/rs/051-ESQ-475/images/Lookout_Dark-Caracal_srr_20180118_us_v.1.0.pdf)


[^4]: [Microsoft SIR Vol 21](http://download.microsoft.com/download/E/B/0/EB0F50CC-989C-4B66-B7F6-68CD3DC90DE3/Microsoft_Security_Intelligence_Report_Volume_21_English.pdf)


[^5]: FinFisher


[^6]: [Elastic Process Injection July 2017](https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process)


[^7]: [Microsoft FinFisher March 2018](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)


[^8]: [FinFisher exposed ](https://www.microsoft.com/security/blog/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)


[^9]: [FireEye FinSpy Sept 2017](https://www.fireeye.com/blog/threat-research/2017/09/zero-day-used-to-distribute-finspy.html)


[^10]: FinSpy


