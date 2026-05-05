---
aliases: 
    - S1179
    
mitre-attack: https://attack.mitre.org/software/S1179
---

## S1179

[Exbyte](https://attack.mitre.org/software/S1179) is an exfiltration tool written in Go that is uniquely associated with [BlackByte](https://attack.mitre.org/groups/G1043) operations. Observed since 2022, [Exbyte](https://attack.mitre.org/software/S1179) transfers collected files to online file sharing and hosting services.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Native API\|T1106]] | Native API | [Exbyte](https://attack.mitre.org/software/S1179) calls `ShellExecuteW` with the `IpOperation` parameter `RunAs` to launch `explorer.exe` with elevated privileges.[^2]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [Exbyte](https://attack.mitre.org/software/S1179) checks for the presence of a configuration file before completing execution.[^2]  |
| [[Local Groups\|T1069.001]] | Local Groups | [Exbyte](https://attack.mitre.org/software/S1179) checks whether the process is running with privileged local access during execution.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Exbyte](https://attack.mitre.org/software/S1179) decodes and decrypts data stored in the configuration file with a key provided on the command line during execution.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Exbyte](https://attack.mitre.org/software/S1179) enumerates all document files on an infected machine, then creates a summary of these items including filename and directory location prior to exfiltration to cloud hosting services.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Exbyte](https://attack.mitre.org/software/S1179) checks for the presence of various security software products during execution.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Exbyte](https://attack.mitre.org/software/S1179) will self-delete if a hard-coded configuration file is not found.[^2]  |
| [[System Checks\|T1497.001]] | System Checks | [Exbyte](https://attack.mitre.org/software/S1179) performs various checks to determine if it is running in a sandboxed environment to prevent analysis.[^1]  |
| [[Exfiltration Over Web Service\|T1567]] | Exfiltration Over Web Service | [Exbyte](https://attack.mitre.org/software/S1179) exfiltrates collected data to online file hosting sites such as `Mega.co.nz`.[^1] [^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[BlackByte\|G1043]] | BlackByte |



## References

[^1]: [Symantec BlackByte 2022](https://www.security.com/threat-intelligence/blackbyte-exbyte-ransomware)


[^2]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)


