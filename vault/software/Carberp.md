---
aliases: 
    - S0484
    
mitre-attack: https://attack.mitre.org/software/S0484
---

## S0484

[Carberp](https://attack.mitre.org/software/S0484) is a credential and information stealing malware that has been active since at least 2009. [Carberp](https://attack.mitre.org/software/S0484)'s source code was leaked online in 2013, and subsequently used as the foundation for the [Carbanak](https://attack.mitre.org/software/S0030) backdoor.[^4] [^1] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Bootkit\|T1542.003]] | Bootkit | [Carberp](https://attack.mitre.org/software/S0484) has installed a bootkit on the system to maintain persistence.[^6]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [Carberp](https://attack.mitre.org/software/S0484)'s passw.plug plugin can gather account information from multiple instant messaging, email, and social media services, as well as FTP, VNC, and VPN clients.[^5]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Carberp](https://attack.mitre.org/software/S0484) has masqueraded as Windows system file names, as well as "chkntfs.exe" and "syscron.exe".[^5] [^2]  |
| [[Rootkit\|T1014]] | Rootkit | [Carberp](https://attack.mitre.org/software/S0484) has used user mode rootkit techniques to remain hidden on the system.[^5]  |
| [[Credential API Hooking\|T1056.004]] | Credential API Hooking | [Carberp](https://attack.mitre.org/software/S0484) has hooked several Windows API functions to steal credentials.[^5]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Carberp](https://attack.mitre.org/software/S0484) has maintained persistence by placing itself inside the current user's startup folder.[^5]  |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [Carberp](https://attack.mitre.org/software/S0484) has removed various hooks before installing the trojan or bootkit to evade sandbox analysis or other analysis software.[^6]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Carberp](https://attack.mitre.org/software/S0484) has exfiltrated data via HTTP to already established C2 servers.[^5] [^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Carberp](https://attack.mitre.org/software/S0484) can download and execute new plugins from the C2 server. [^5] [^2]  |
| [[VNC\|T1021.005]] | VNC | [Carberp](https://attack.mitre.org/software/S0484) can start a remote VNC session by downloading a new plugin.[^5]  |
| [[Browser Session Hijacking\|T1185]] | Browser Session Hijacking | [Carberp](https://attack.mitre.org/software/S0484) has captured credentials when a user performs login through a SSL session.[^5] [^2]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [Carberp](https://attack.mitre.org/software/S0484) has exploited multiple Windows vulnerabilities (CVE-2010-2743, CVE-2010-3338, CVE-2010-4398, CVE-2008-1084) and a .NET Runtime Optimization vulnerability for privilege escalation.[^6] [^5]  |
| [[Asynchronous Procedure Call\|T1055.004]] | Asynchronous Procedure Call | [Carberp](https://attack.mitre.org/software/S0484) has queued an APC routine to explorer.exe by calling ZwQueueApcThread.[^5]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Carberp](https://attack.mitre.org/software/S0484) has queried the infected system's registry searching for specific registry keys associated with antivirus products.[^5]  |
| [[Query Registry\|T1012]] | Query Registry | [Carberp](https://attack.mitre.org/software/S0484) has searched the Image File Execution Options registry key for "Debugger" within every subkey.[^5]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [Carberp](https://attack.mitre.org/software/S0484) has created a hidden file in the Startup folder of the current user.[^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Carberp](https://attack.mitre.org/software/S0484) has attempted to disable security software by creating a suspended process for the security software and injecting code to delete antivirus core files when the process is resumed.[^5]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Carberp](https://attack.mitre.org/software/S0484) has connected to C2 servers via HTTP.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Carberp](https://attack.mitre.org/software/S0484) has used XOR-based encryption to mask C2 server locations within the trojan.[^5]  |
| [[Native API\|T1106]] | Native API | [Carberp](https://attack.mitre.org/software/S0484) has used the NtQueryDirectoryFile and ZwQueryDirectoryFile functions to hide files and directories.[^2]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Carberp](https://attack.mitre.org/software/S0484)'s bootkit can inject a malicious DLL into the address space of running processes.[^6]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Carberp](https://attack.mitre.org/software/S0484) has collected the operating system version from the infected system.[^5]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Carberp](https://attack.mitre.org/software/S0484) can capture display screenshots with the screens_dll.dll plugin.[^5]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Carberp](https://attack.mitre.org/software/S0484) has collected a list of running processes.[^2]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Carberp](https://attack.mitre.org/software/S0484)'s passw.plug plugin can gather passwords saved in Opera, Internet Explorer, Safari, Firefox, and Chrome.[^5]  |




## References

[^1]: [KasperskyCarbanak](https://securelist.com/the-great-bank-robbery-the-carbanak-apt/68732/)


[^2]: [Trusteer Carberp October 2010](https://web.archive.org/web/20111004014029/http://www.trusteer.com/sites/default/files/Carberp_Analysis.pdf)


[^3]: [RSA Carbanak November 2017](https://www.rsa.com/content/dam/en/white-paper/the-carbanak-fin7-syndicate.pdf)


[^4]: [Trend Micro Carberp February 2014](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/carberp)


[^5]: [Prevx Carberp March 2011](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)


[^6]: [ESET Carberp March 2012](https://www.eset.com/fileadmin/eset/US/resources/docs/white-papers/white-papers-win-32-carberp.pdf)


