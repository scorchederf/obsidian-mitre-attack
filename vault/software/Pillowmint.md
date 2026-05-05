---
aliases: 
    - S0517
    
mitre-attack: https://attack.mitre.org/software/S0517
---

## S0517

[Pillowmint](https://attack.mitre.org/software/S0517) is a point-of-sale malware used by [FIN7](https://attack.mitre.org/groups/G0046) designed to capture credit card information.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Application Shimming\|T1546.011]] | Application Shimming | [Pillowmint](https://attack.mitre.org/software/S0517) has used a malicious shim database to maintain persistence.[^2]  |
| [[Asynchronous Procedure Call\|T1055.004]] | Asynchronous Procedure Call | [Pillowmint](https://attack.mitre.org/software/S0517) has used the NtQueueApcThread syscall to inject code into svchost.exe.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Pillowmint](https://attack.mitre.org/software/S0517) has modified the Registry key `HKLM\SOFTWARE\Microsoft\DRM` to store a malicious payload.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [Pillowmint](https://attack.mitre.org/software/S0517) has used shellcode which reads code stored in the registry keys `\REGISTRY\SOFTWARE\Microsoft\DRM` using the native Windows API as well as read `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters\Interfaces` as part of its C2.[^2] 	 |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Pillowmint](https://attack.mitre.org/software/S0517) has obfuscated the AES key used for encryption.[^2] 	 |
| [[Compression\|T1027.015]] | Compression | [Pillowmint](https://attack.mitre.org/software/S0517) has been compressed and stored within a registry key.[^2] 	 |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [Pillowmint](https://attack.mitre.org/software/S0517) has stored a compressed payload in the Registry key `HKLM\SOFTWARE\Microsoft\DRM`.[^2]  |
| [[Clear Persistence\|T1070.009]] | Clear Persistence | [Pillowmint](https://attack.mitre.org/software/S0517) can uninstall the malicious service from an infected machine.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Pillowmint](https://attack.mitre.org/software/S0517) can iterate through running processes every six seconds collecting a list of processes to capture from later.[^2] 	 |
| [[Native API\|T1106]] | Native API | [Pillowmint](https://attack.mitre.org/software/S0517) has used multiple native Windows APIs to execute and conduct process injections.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Pillowmint](https://attack.mitre.org/software/S0517) has used a PowerShell script to install a shim database.[^2] 	 |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Pillowmint](https://attack.mitre.org/software/S0517) has been decompressed by included shellcode prior to being launched.[^2] 	 |
| [[Data from Local System\|T1005]] | Data from Local System | [Pillowmint](https://attack.mitre.org/software/S0517) has collected credit card data using native API functions.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Pillowmint](https://attack.mitre.org/software/S0517) has deleted the filepath `%APPDATA%\Intel\devmonsrv.exe`.[^2]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Pillowmint](https://attack.mitre.org/software/S0517) has encrypted stolen credit card information with AES and further encoded it with Base64.[^2] 	 |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN7\|G0046]] | FIN7 |



## References

[^1]: [CrowdStrike Carbon Spider August 2021](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)


[^2]: [Trustwave Pillowmint June 2020](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)


