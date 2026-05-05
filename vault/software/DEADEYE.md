---
aliases: 
    - S1052
    
mitre-attack: https://attack.mitre.org/software/S1052
---

## S1052

[DEADEYE](https://attack.mitre.org/software/S1052) is a malware launcher that has been used by [APT41](https://attack.mitre.org/groups/G0096) since at least May 2021. [DEADEYE](https://attack.mitre.org/software/S1052) has variants that can either embed a payload inside a compiled binary (DEADEYE.EMBED) or append it to the end of a file (DEADEYE.APPEND).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [DEADEYE](https://attack.mitre.org/software/S1052) has encrypted its payload.[^1]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [DEADEYE](https://attack.mitre.org/software/S1052) can ensure it executes only on intended systems by identifying the victim's volume serial number, hostname, and/or DNS domain.[^1]  |
| [[Msiexec\|T1218.007]] | Msiexec | [DEADEYE](https://attack.mitre.org/software/S1052) can use `msiexec.exe` for execution of malicious DLL.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [DEADEYE](https://attack.mitre.org/software/S1052) can enumerate a victim computer's volume serial number and host name.[^1]  |
| [[Embedded Payloads\|T1027.009]] | Embedded Payloads | <br>The DEADEYE.EMBED variant of [DEADEYE](https://attack.mitre.org/software/S1052) has the ability to embed payloads inside of a compiled binary.[^1]  |
| [[Native API\|T1106]] | Native API | [DEADEYE](https://attack.mitre.org/software/S1052) can execute the `GetComputerNameA` and `GetComputerNameExA` WinAPI functions.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [DEADEYE](https://attack.mitre.org/software/S1052) can use `rundll32.exe` for execution of living off the land binaries (lolbin) such as `SHELL32.DLL`.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [DEADEYE](https://attack.mitre.org/software/S1052) can run `cmd /c copy /y /b C:\Users\public\syslog_6-*.dat C:\Users\public\syslog.dll` to combine separated sections of code into a single DLL prior to execution.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [DEADEYE](https://attack.mitre.org/software/S1052) has the ability to combine multiple sections of a binary which were broken up to evade detection into a single .dll prior to execution.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [DEADEYE](https://attack.mitre.org/software/S1052) can discover the DNS domain name of a targeted system.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [DEADEYE](https://attack.mitre.org/software/S1052) has used `schtasks /change` to modify scheduled tasks including `\Microsoft\Windows\PLA\Server Manager Performance Monitor`, `\Microsoft\Windows\Ras\ManagerMobility, \Microsoft\Windows\WDI\SrvSetupResults`, and `\Microsoft\Windows\WDI\USOShared`.[^1]  |
| [[NTFS File Attributes\|T1564.004]] | NTFS File Attributes | The DEADEYE.EMBED variant of [DEADEYE](https://attack.mitre.org/software/S1052) can embed its payload in an alternate data stream of a local file.[^1]  |




## References

[^1]: [Mandiant APT41](https://www.mandiant.com/resources/apt41-us-state-governments)


[^2]: DEADEYE.APPEND


[^3]: DEADEYE.EMBED


