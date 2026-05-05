---
aliases: 
    - S0589
    
mitre-attack: https://attack.mitre.org/software/S0589
---

## S0589

[Sibot](https://attack.mitre.org/software/S0589) is dual-purpose malware written in VBScript designed to achieve persistence on a compromised system as well as download and execute additional payloads. Microsoft discovered three [Sibot](https://attack.mitre.org/software/S0589) variants in early 2021 during its investigation of [APT29](https://attack.mitre.org/groups/G0016) and the [SolarWinds Compromise](https://attack.mitre.org/campaigns/C0024).[^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Query Registry\|T1012]] | Query Registry | [Sibot](https://attack.mitre.org/software/S0589) has queried the registry for proxy server information.[^3]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Sibot](https://attack.mitre.org/software/S0589) has been executed via a scheduled task.[^3]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Sibot](https://attack.mitre.org/software/S0589) has downloaded a DLL to the `C:\windows\system32\drivers\` folder and renamed it with a `.sys` extension.[^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Sibot](https://attack.mitre.org/software/S0589) checked if the compromised system is configured to use proxies.[^3]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Sibot](https://attack.mitre.org/software/S0589) has obfuscated scripts used in execution.[^3]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Sibot](https://attack.mitre.org/software/S0589) has used WMI to discover network connections and configurations. [Sibot](https://attack.mitre.org/software/S0589) has also used the Win32_Process class to execute a malicious DLL.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Sibot](https://attack.mitre.org/software/S0589) can download and execute a payload onto a compromised system.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Sibot](https://attack.mitre.org/software/S0589) will delete itself if a certain server response is received.[^3]  |
| [[Web Service\|T1102]] | Web Service | [Sibot](https://attack.mitre.org/software/S0589) has used a legitimate compromised website to download DLLs to the victim's machine.[^3]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Sibot](https://attack.mitre.org/software/S0589) executes commands using VBScript.[^3] 	 |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Sibot](https://attack.mitre.org/software/S0589) can decrypt data received from a C2 and save to a file.[^3]  |
| [[Mshta\|T1218.005]] | Mshta | [Sibot](https://attack.mitre.org/software/S0589) has been executed via MSHTA application.[^3]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Sibot](https://attack.mitre.org/software/S0589) has executed downloaded DLLs with `rundll32.exe`.[^3]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Sibot](https://attack.mitre.org/software/S0589) has retrieved a GUID associated with a present LAN connection on a compromised machine.[^3]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [Sibot](https://attack.mitre.org/software/S0589) will delete an associated registry key if a certain server response is received.[^3]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [Sibot](https://attack.mitre.org/software/S0589) has installed a second-stage script in the `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\sibot` registry key.[^3]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Sibot](https://attack.mitre.org/software/S0589) has modified the Registry to install a second-stage script in the `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\sibot`.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Sibot](https://attack.mitre.org/software/S0589) communicated with its C2 server via HTTP GET requests.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [Cybersecurity Advisory SVR TTP May 2021](https://www.ncsc.gov.uk/files/Advisory-further-TTPs-associated-with-SVR-cyber-actors.pdf)


[^2]: [Secureworks IRON RITUAL Profile](https://www.sophos.com/en-us/threat-profiles/iron-ritual)


[^3]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)


[^4]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)


