---
aliases: 
    - S0396
    
mitre-attack: https://attack.mitre.org/software/S0396
---

## S0396

[EvilBunny](https://attack.mitre.org/software/S0396) is a C++ malware sample observed since 2011 that was designed to be a execution platform for Lua scripts.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Native API\|T1106]] | Native API | [EvilBunny](https://attack.mitre.org/software/S0396) has used various API calls as part of its checks to see if the malware is running in a sandbox.[^2] 	 |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [EvilBunny](https://attack.mitre.org/software/S0396) has downloaded additional Lua scripts from the C2.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [EvilBunny](https://attack.mitre.org/software/S0396) has created Registry keys for persistence in `[HKLM|HKCU]\…\CurrentVersion\Run`.[^2] 	 |
| [[Lua\|T1059.011]] | Lua | [EvilBunny](https://attack.mitre.org/software/S0396) has used Lua scripts to execute payloads.[^3]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [EvilBunny](https://attack.mitre.org/software/S0396) has used the API calls NtQuerySystemTime, GetSystemTimeAsFileTime, and GetTickCount to gather time metrics as part of its checks to see if the malware is running in a sandbox.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [EvilBunny](https://attack.mitre.org/software/S0396) has executed C2 commands directly via HTTP.[^2]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [EvilBunny](https://attack.mitre.org/software/S0396) has used WMI to gather information about the system.[^2]  |
| [[System Checks\|T1497.001]] | System Checks | [EvilBunny](https://attack.mitre.org/software/S0396)'s dropper has checked the number of processes and the length and strings of its own file name to identify if the malware is in a sandbox environment.[^2] 	 |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [EvilBunny](https://attack.mitre.org/software/S0396) has exploited CVE-2011-4369, a vulnerability in the PRC component in Adobe Reader.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [EvilBunny](https://attack.mitre.org/software/S0396) has an integrated scripting engine to download and execute Lua scripts.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [EvilBunny](https://attack.mitre.org/software/S0396) has executed commands via scheduled tasks.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [EvilBunny](https://attack.mitre.org/software/S0396) has deleted the initial dropper after running through the environment checks.[^2]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [EvilBunny](https://attack.mitre.org/software/S0396) has used time measurements from 3 different APIs before and after performing sleep operations to check and abort if the malware is running in a sandbox.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [EvilBunny](https://attack.mitre.org/software/S0396) has used EnumProcesses() to identify how many process are running in the environment.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [EvilBunny](https://attack.mitre.org/software/S0396) has been observed querying installed antivirus software.[^2]  |




## References

[^1]: EvilBunny


[^2]: [Cyphort EvilBunny Dec 2014](https://web.archive.org/web/20150311013500/http://www.cyphort.com/evilbunny-malware-instrumented-lua/)


[^3]: [Cyphort EvilBunny](https://web.archive.org/web/20150311013500/http:/www.cyphort.com/evilbunny-malware-instrumented-lua/)


