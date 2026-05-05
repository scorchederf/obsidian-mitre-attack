---
aliases: 
    - S0176
    
mitre-attack: https://attack.mitre.org/software/S0176
---

## S0176

[Wingbird](https://attack.mitre.org/software/S0176) is a backdoor that appears to be a version of commercial software [FinFisher](https://attack.mitre.org/software/S0182). It is reportedly used to attack individual computers instead of networks. It was used by [NEODYMIUM](https://attack.mitre.org/groups/G0055) in a May 2016 campaign. [^2]  [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[LSASS Driver\|T1547.008]] | LSASS Driver | [Wingbird](https://attack.mitre.org/software/S0176) drops a malicious file (sspisrv.dll) alongside a copy of lsass.exe, which is used to register a service that loads sspisrv.dll as a driver. The payload of the malicious driver (located in its entry-point function) is executed when loaded by lsass.exe before the spoofed service becomes unstable and crashes.[^2] [^1]  |
| [[DLL\|T1574.001]] | DLL | [Wingbird](https://attack.mitre.org/software/S0176) side loads a malicious file, sspisrv.dll, in part of a spoofed lssas.exe service.[^2] [^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Wingbird](https://attack.mitre.org/software/S0176) deletes its payload along with the payload's parent process after it finishes copying files.[^2]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Wingbird](https://attack.mitre.org/software/S0176) uses services.exe to register a new autostart service named "Audit Service" using a copy of the local lsass.exe file.[^2] [^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Wingbird](https://attack.mitre.org/software/S0176) uses services.exe to register a new autostart service named "Audit Service" using a copy of the local lsass.exe file.[^2] [^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Wingbird](https://attack.mitre.org/software/S0176) checks for the presence of Bitdefender security software.[^2]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [Wingbird](https://attack.mitre.org/software/S0176) exploits CVE-2016-4117 to allow an executable to gain escalated privileges.[^2]  |
| [[Process Injection\|T1055]] | Process Injection | [Wingbird](https://attack.mitre.org/software/S0176) performs multiple process injections to hijack system processes and execute malicious code.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Wingbird](https://attack.mitre.org/software/S0176) checks the victim OS version after executing to determine where to drop files based on whether the victim is 32-bit or 64-bit.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[NEODYMIUM\|G0055]] | NEODYMIUM |



## References

[^1]: [Microsoft Wingbird Nov 2017](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Backdoor:Win32/Wingbird.A!dha)


[^2]: [Microsoft SIR Vol 21](http://download.microsoft.com/download/E/B/0/EB0F50CC-989C-4B66-B7F6-68CD3DC90DE3/Microsoft_Security_Intelligence_Report_Volume_21_English.pdf)


[^3]: [Microsoft NEODYMIUM Dec 2016](https://blogs.technet.microsoft.com/mmpc/2016/12/14/twin-zero-day-attacks-promethium-and-neodymium-target-individuals-in-europe/)


[^4]: Wingbird


