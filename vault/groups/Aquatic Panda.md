---
aliases: 
    - Aquatic Panda
mitre-attack: https://attack.mitre.org/groups/G0143
---

## G0143

[Aquatic Panda](https://attack.mitre.org/groups/G0143) is a suspected China-based threat group with a dual mission of intelligence collection and industrial espionage. Active since at least May 2020, [Aquatic Panda](https://attack.mitre.org/groups/G0143) has primarily targeted entities in the telecommunications, technology, and government sectors.[^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has encoded PowerShell commands in Base64.[^2]  |
| [[Account Discovery\|T1087]] | Account Discovery | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used the `last` command in Linux environments to identify recently logged-in users on victim machines.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has deleted malicious executables from compromised machines.[^2] [^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used malicious shell scripts in Linux environments following access via SSH to install Linux versions of Winnti malware.[^1]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used remote shares to enable lateral movement in victim environments.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Aquatic Panda](https://attack.mitre.org/groups/G0143) created new, malicious services using names such as `Windows User Service` to attempt to blend in with legitimate items on victim systems.[^1]  |
| [[Dynamic Linker Hijacking\|T1574.006]] | Dynamic Linker Hijacking | [Aquatic Panda](https://attack.mitre.org/groups/G0143) modified the `ld.so` preload file in Linux environments to enable persistence for Winnti malware.[^1]  |
| [[Clear Command History\|T1070.003]] | Clear Command History | [Aquatic Panda](https://attack.mitre.org/groups/G0143) cleared command history in Linux environments to remove traces of activity after operations.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Aquatic Panda](https://attack.mitre.org/groups/G0143) created new Windows services for persistence that masqueraded as legitimate Windows services via name change.[^1]  |
| [[Pass the Hash\|T1550.002]] | Pass the Hash | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used a registry edit to enable a Windows feature called `RestrictedAdmin` in victim environments. This change allowed [Aquatic Panda](https://attack.mitre.org/groups/G0143) to leverage "pass the hash" mechanisms as the alteration allows for RDP connections with a valid account name and hash only, without possessing a cleartext password value.[^1]  |
| [[DLL\|T1574.001]] | DLL | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has used DLL search-order hijacking to load `exe`, `dll`, and `dat` files into memory.[^2]  [Aquatic Panda](https://attack.mitre.org/groups/G0143) loaded a malicious DLL into the legitimate Windows Security Health Service executable (`SecurityHealthService.exe`) to execute malicious code on victim systems.[^1]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Aquatic Panda](https://attack.mitre.org/groups/G0143) leveraged stolen credentials to move laterally via RDP in victim environments.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Aquatic Panda](https://attack.mitre.org/groups/G0143) captured local Windows security event log data from victim machines using the `wevtutil` utility to extract contents to an `evtx` output file.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has downloaded additional malware onto compromised hosts.[^2]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has attempted to discover services for third party EDR products.[^2]  |
| [[Log Enumeration\|T1654]] | Log Enumeration | [Aquatic Panda](https://attack.mitre.org/groups/G0143) enumerated logs related to authentication in Linux environments prior to deleting selective entries for defense evasion purposes.[^1]  |
| [[SSH\|T1021.004]] | SSH | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used SSH with captured user credentials to move laterally in victim environments.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Aquatic Panda](https://attack.mitre.org/groups/G0143) modified the victim registry to enable the `RestrictedAdmin` mode feature, allowing for pass the hash behaviors to function via RDP.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Aquatic Panda](https://attack.mitre.org/groups/G0143) renamed or moved malicious binaries to legitimate locations to evade defenses and blend into victim environments.[^1]  |
| [[Malware\|T1588.001]] | Malware | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has acquired and used [njRAT](https://attack.mitre.org/software/S0385) in its operations.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has attempted to discover third party endpoint detection and response (EDR) tools on compromised systems.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has attempted and failed to run Bash commands on a Windows host by passing them to `cmd /C`.[^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has attempted to stop endpoint detection and response (EDR) tools on compromised systems.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Aquatic Panda](https://attack.mitre.org/groups/G0143) gathers information on recently logged-in users on victim devices.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used WMI for lateral movement in victim environments.[^1]  |
| [[Tool\|T1588.002]] | Tool | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has acquired and used [Cobalt Strike](https://attack.mitre.org/software/S0154) in its operations.[^2]  |
| [[Vulnerability Scanning\|T1595.002]] | Vulnerability Scanning | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has used publicly accessible DNS logging services to identify servers vulnerable to Log4j (CVE 2021-44228).[^2]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has attempted to harvest credentials through LSASS memory dumping.[^2]  |
| [[Remote Services\|T1021]] | Remote Services | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used remote scheduled tasks to install malicious software on victim systems during lateral movement actions.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has used native OS commands to understand privilege levels and system details.[^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used rundll32.exe to proxy execution of a malicious DLL file identified as a keylogging binary.[^1]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [Aquatic Panda](https://attack.mitre.org/groups/G0143) clears Windows Event Logs following activity to evade defenses.[^1]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used multiple mechanisms to capture valid user accounts for victim domains to enable lateral movement and access to additional hosts in victim environments.[^1]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has used several publicly available tools, including WinRAR and 7zip, to compress collected files and memory dumps prior to exfiltration.[^2] [^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has downloaded additional scripts and executed Base64 encoded commands in PowerShell.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Wevtutil\|S0645]] | Wevtutil | [Aquatic Panda](https://attack.mitre.org/groups/G0143) uses [Wevtutil](https://attack.mitre.org/software/S0645) to extract Windows security event log data from victim machines.[^1]  |
| [[Winnti for Linux\|S0430]] | Winnti for Linux | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used [Winnti for Linux](https://attack.mitre.org/software/S0430) for access to victim Linux hosts during intrusions[^1] . |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^2]  |
| [[Winnti for Windows\|S0141]] | Winnti for Windows | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used [Winnti for Windows](https://attack.mitre.org/software/S0141) for persistent access to Windows victims.[^1]  |
| [[njRAT\|S0385]] | njRAT | [^2]  |
| [[ShadowPad\|S0596]] | ShadowPad | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used [ShadowPad](https://attack.mitre.org/software/S0596) as a remote access tool to victim environments.[^1]  |



## References

[^1]: [Crowdstrike HuntReport 2022](https://go.crowdstrike.com/rs/281-OBQ-266/images/2022OverWatchThreatHuntingReport.pdf)


[^2]: [CrowdStrike AQUATIC PANDA December 2021](https://www.crowdstrike.com/blog/overwatch-exposes-aquatic-panda-in-possession-of-log-4-shell-exploit-tools/)


