---
aliases: 
    - S0147
    
mitre-attack: https://attack.mitre.org/software/S0147
---

## S0147

[Pteranodon](https://attack.mitre.org/software/S0147) is a custom backdoor used by [Gamaredon Group](https://attack.mitre.org/groups/G0047). [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Screen Capture\|T1113]] | Screen Capture | [Pteranodon](https://attack.mitre.org/software/S0147) can capture screenshots at a configurable interval.[^2] [^5]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Pteranodon](https://attack.mitre.org/software/S0147) can use `cmd.exe` for execution on victim systems.[^2] [^4]  |
| [[Native API\|T1106]] | Native API | [Pteranodon](https://attack.mitre.org/software/S0147) has used various API calls.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Pteranodon](https://attack.mitre.org/software/S0147) can download and execute additional files.[^2] [^4] [^5]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Pteranodon](https://attack.mitre.org/software/S0147) copies itself to the Startup folder to establish persistence.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Pteranodon](https://attack.mitre.org/software/S0147) can use HTTP for C2.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Pteranodon](https://attack.mitre.org/software/S0147) identifies files matching certain file extension and copies them to subdirectories it created.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Pteranodon](https://attack.mitre.org/software/S0147) can decrypt encrypted data strings prior to using them.[^3]  |
| [[Dynamic API Resolution\|T1027.007]] | Dynamic API Resolution | [Pteranodon](https://attack.mitre.org/software/S0147) can use a dynamic Windows hashing algorithm to map API components.[^3]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Pteranodon](https://attack.mitre.org/software/S0147) can use a malicious VBS file for execution.[^4]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Pteranodon](https://attack.mitre.org/software/S0147) executes functions using rundll32.exe.[^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Pteranodon](https://attack.mitre.org/software/S0147) exfiltrates screenshot files to its C2 server.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Pteranodon](https://attack.mitre.org/software/S0147) can delete files that may interfere with it executing. It also can delete temporary files and itself after the initial script executes.[^2]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Pteranodon](https://attack.mitre.org/software/S0147) creates various subdirectories under `%Temp%\reports\%` and copies files to those subdirectories. It also creates a folder at `C:\Users\<Username>\AppData\Roaming\Microsoft\store` to store screenshot JPEG files.[^2]  |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [Pteranodon](https://attack.mitre.org/software/S0147) has the ability to use anti-detection functions to identify sandbox environments.[^5]  |
| [[Mshta\|T1218.005]] | Mshta | [Pteranodon](https://attack.mitre.org/software/S0147) can use mshta.exe to execute an HTA file hosted on a remote server.[^4]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Pteranodon](https://attack.mitre.org/software/S0147) schedules tasks to invoke its components in order to establish persistence.[^2] [^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Gamaredon Group\|G0047]] | Gamaredon Group |



## References

[^1]: Pterodo


[^2]: [Palo Alto Gamaredon Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/)


[^3]: [Microsoft Actinium February 2022](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)


[^4]: [Symantec Shuckworm January 2022](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/shuckworm-gamaredon-espionage-ukraine)


[^5]: [Unit 42 Gamaredon February 2022](https://unit42.paloaltonetworks.com/gamaredon-primitive-bear-ukraine-update-2021/)


[^6]: [Secureworks IRON TILDEN Profile](https://www.secureworks.com/research/threat-profiles/iron-tilden)


