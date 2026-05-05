---
aliases: 
    - S1200
    
mitre-attack: https://attack.mitre.org/software/S1200
---

## S1200

[StealBit](https://attack.mitre.org/software/S1200) is a data exfiltration tool that is developed and maintained by the operators of the the LockBit Ransomware-as-a-Service (RaaS) and offered to affiliates to exfiltrate data from compromised systems for double extortion purposes.[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [StealBit](https://attack.mitre.org/software/S1200) can detect it is being run in the context of a debugger.[^2]  |
| [[Inter-Process Communication\|T1559]] | Inter-Process Communication | [StealBit](https://attack.mitre.org/software/S1200) can use interprocess communication (IPC) to enable the designation of multiple files for exfiltration in a scalable manner.[^2] <br> |
| [[File Deletion\|T1070.004]] | File Deletion | [StealBit](https://attack.mitre.org/software/S1200) can self-delete its executable file from the compromised system.[^2] [^1]  |
| [[Data Transfer Size Limits\|T1030]] | Data Transfer Size Limits | [StealBit](https://attack.mitre.org/software/S1200) can be configured to exfiltrate files at a specified rate to evade network detection mechanisms.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [StealBit](https://attack.mitre.org/software/S1200) stores obfuscated DLL file names in its executable.[^2]  |
| [[Native API\|T1106]] | Native API | [StealBit](https://attack.mitre.org/software/S1200) can use native APIs including `LoadLibraryExA` for execution and `NtSetInformationProcess` for defense evasion purposes.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [StealBit](https://attack.mitre.org/software/S1200) can enumerate the computer name and domain membership of the compromised system.[^2]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [StealBit](https://attack.mitre.org/software/S1200) will execute an empty infinite loop if it detects it is being run in the context of a debugger.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [StealBit](https://attack.mitre.org/software/S1200) can upload data and files to the LockBit victim-shaming site.[^1] [^2]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [StealBit](https://attack.mitre.org/software/S1200) can determine system location based on the default language setting and will not execute on systems located in former Soviet countries.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [StealBit](https://attack.mitre.org/software/S1200) can use the Windows Socket networking library to communicate with attacker-controlled endpoints.[^2] <br> |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [StealBit](https://attack.mitre.org/software/S1200) can configure processes to not display certain Windows error messages by through use of the `NtSetInformationProcess`.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [StealBit](https://attack.mitre.org/software/S1200) can use HTTP to exfiltrate files to actor-controlled infrastructure.[^1] [^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [StealBit](https://attack.mitre.org/software/S1200) can deobfuscate loaded modules prior to execution.[^1] [^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [StealBit](https://attack.mitre.org/software/S1200) can be configured to exfiltrate specific file types.[^1] [^2]  |




## References

[^1]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)


[^2]: [Cybereason StealBit Exfiltration Tool](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)


