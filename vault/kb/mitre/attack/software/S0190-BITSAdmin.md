---
aliases: 
    - S0190
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0190-BITSAdmin
---

## Description

[[kb/mitre/attack/software/S0190-BITSAdmin\|BITSAdmin]] is a command line tool used to create and manage [[kb/mitre/attack/techniques/T1197-BITS_Jobs\|BITS Jobs]]. [^3] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1048.003-Exfiltration_Over_Unencrypted_Non-C2_Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [[kb/mitre/attack/software/S0190-BITSAdmin\|BITSAdmin]] can be used to create [[kb/mitre/attack/techniques/T1197-BITS_Jobs\|BITS Jobs]] to upload files from a compromised host.[^3]  |
| [[kb/mitre/attack/techniques/T1105-Ingress_Tool_Transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0190-BITSAdmin\|BITSAdmin]] can be used to create [[kb/mitre/attack/techniques/T1197-BITS_Jobs\|BITS Jobs]] to upload and/or download files.[^3]  |
| [[kb/mitre/attack/techniques/T1197-BITS_Jobs\|T1197]] | BITS Jobs | [[kb/mitre/attack/software/S0190-BITSAdmin\|BITSAdmin]] can be used to create [[kb/mitre/attack/techniques/T1197-BITS_Jobs\|BITS Jobs]] to launch a malicious process.[^2]  |
| [[kb/mitre/attack/techniques/T1570-Lateral_Tool_Transfer\|T1570]] | Lateral Tool Transfer | [[kb/mitre/attack/software/S0190-BITSAdmin\|BITSAdmin]] can be used to create [[kb/mitre/attack/techniques/T1197-BITS_Jobs\|BITS Jobs]] to upload and/or download files from SMB file servers.[^1]  |





> [!info]- References
> [^1]: [Microsoft About BITS](https://docs.microsoft.com/en-us/windows/win32/bits/about-bits)

> [^2]: [TrendMicro Tropic Trooper Mar 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/tropic-trooper-new-strategy/)

> [^3]: [Microsoft BITSAdmin](https://msdn.microsoft.com/library/aa362813.aspx)


