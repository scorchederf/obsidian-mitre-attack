---
aliases: 
    - Blue Mockingbird
mitre-attack: https://attack.mitre.org/groups/G0108
---

## G0108

[Blue Mockingbird](https://attack.mitre.org/groups/G0108) is a cluster of observed activity involving Monero cryptocurrency-mining payloads in dynamic-link library (DLL) form on Windows systems. The earliest observed Blue Mockingbird tools were created in December 2019.[^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[PowerShell\|T1059.001]] | PowerShell | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has used PowerShell reverse TCP shells to issue interactive commands over a network connection.[^1]  |
| [[COR_PROFILER\|T1574.012]] | COR_PROFILER | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has used wmic.exe and Windows Registry modifications to set the COR_PROFILER environment variable to execute a malicious DLL whenever a process loads the .NET CLR.[^1]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has used mofcomp.exe to establish WMI Event Subscription persistence mechanisms configured from a *.mof file.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has collected hardware details for the victim's system, including CPU and memory information.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has made their XMRIG payloads persistent as a Windows Service.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has used Windows Scheduled Tasks to establish persistence on local and remote hosts.[^1]  |
| [[Proxy\|T1090]] | Proxy | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has used [FRP](https://attack.mitre.org/software/S1144), ssf, and Venom to establish SOCKS proxy connections.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has used wmic.exe to set environment variables.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has used batch script files to automate execution and deployment of payloads.[^1]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has used Mimikatz to retrieve credentials from LSASS memory.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has executed custom-compiled XMRIG miner DLLs using rundll32.exe.[^1]  |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has used JuicyPotato to abuse the `SeImpersonate` token privilege to escalate from web application pool accounts to NT Authority\SYSTEM.[^1]  |
| [[Compute Hijacking\|T1496.001]] | Compute Hijacking | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has used XMRIG to mine cryptocurrency on victim systems.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has obfuscated the wallet address in the payload binary.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has used Windows Registry modifications to specify a DLL payload.[^1] 	 |
| [[Service Execution\|T1569.002]] | Service Execution | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has executed custom-compiled XMRIG miner DLLs by configuring them to execute via the "wercplsupport" service.[^1] 	 |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has gained initial access by exploiting CVE-2019-18935, a vulnerability within Telerik UI for ASP.NET AJAX.[^1]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has used Remote Desktop to log on to servers interactively and manually copy files to remote hosts.[^1]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has executed custom-compiled XMRIG miner DLLs using regsvr32.exe.[^1] 	 |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has used Windows Explorer to manually copy malicious files to remote hosts over SMB.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has masqueraded their XMRIG payload name by naming it wercplsupporte.dll after the legitimate wercplsupport.dll file.[^1]  |
| [[Tool\|T1588.002]] | Tool | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has obtained and used tools such as [Mimikatz](https://attack.mitre.org/software/S0002).[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[FRP\|S1144]] | FRP | [^1]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^1]  |



## References

[^1]: [RedCanary Mockingbird May 2020](https://redcanary.com/blog/blue-mockingbird-cryptominer/)


