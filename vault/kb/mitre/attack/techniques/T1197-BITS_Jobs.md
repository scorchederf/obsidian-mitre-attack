---
aliases: 
    - T1197
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/execution
    - attack/tactic/persistence
    - attack/tactic/stealth
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1197-BITS_Jobs
tactic: 
     - Stealth - Persistence - Execution
platforms:
     - Windows
permissions required:
     - none
---

## Description

Adversaries may abuse BITS jobs to persistently execute code and perform various background tasks. Windows Background Intelligent Transfer Service (BITS) is a low-bandwidth, asynchronous file transfer mechanism exposed through [[kb/mitre/attack/techniques/T1559.001-Component_Object_Model\|Component Object Model]] (COM).[^8] [^4]  BITS is commonly used by updaters, messengers, and other applications preferred to operate in the background (using available idle bandwidth) without interrupting other networked applications. File transfer tasks are implemented as BITS jobs, which contain a queue of one or more file operations.<br><br>The interface to create and manage BITS jobs is accessible through [[kb/mitre/attack/techniques/T1059.001-PowerShell\|PowerShell]] and the [[kb/mitre/attack/software/S0190-BITSAdmin\|BITSAdmin]] tool.[^4] [^3] <br><br>Adversaries may abuse BITS to download (e.g. [[kb/mitre/attack/techniques/T1105-Ingress_Tool_Transfer\|Ingress Tool Transfer]]), execute, and even clean up after running malicious code (e.g. [[kb/mitre/attack/techniques/T1070-Indicator_Removal\|Indicator Removal]]). BITS tasks are self-contained in the BITS job database, without new files or registry modifications, and often permitted by host firewalls.[^5] [^2] [^1]  BITS enabled execution may also enable persistence by creating long-standing jobs (the default maximum lifetime is 90 days and extendable) or invoking an arbitrary program when a job completes or errors (including after system reboots).[^6] [^5] <br><br>BITS upload functionalities can also be used to perform [[kb/mitre/attack/techniques/T1048-Exfiltration_Over_Alternative_Protocol\|Exfiltration Over Alternative Protocol]].[^5] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0190-BITSAdmin\|S0190]] | BITSAdmin | [[kb/mitre/attack/software/S0190-BITSAdmin\|BITSAdmin]] can be used to create [[kb/mitre/attack/techniques/T1197-BITS_Jobs\|BITS Jobs]] to launch a malicious process.[^7]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | <br>Consider limiting access to the BITS interface to specific users or groups.[^1]  |
| [[kb/mitre/attack/mitigations/M1028-Operating_System_Configuration\|M1028]] | Operating System Configuration | <br>Consider reducing the default BITS job lifetime in Group Policy or by editing the `JobInactivityTimeout` and `MaxDownloadTime` Registry values in ` HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\BITS`.[^4]  |
| [[kb/mitre/attack/mitigations/M1037-Filter_Network_Traffic\|M1037]] | Filter Network Traffic | Modify network and/or host firewall rules, as well as other network controls, to only allow legitimate BITS traffic. |






> [!info]- References
> [^1]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)

> [^2]: [Mondok Windows PiggyBack BITS May 2007](https://arstechnica.com/information-technology/2007/05/malware-piggybacks-on-windows-background-intelligent-transfer-service/)

> [^3]: [Microsoft BITSAdmin](https://msdn.microsoft.com/library/aa362813.aspx)

> [^4]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)

> [^5]: [CTU BITS Malware June 2016](https://www.secureworks.com/blog/malware-lingers-with-bits)

> [^6]: [PaloAlto UBoatRAT Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-uboatrat-navigates-east-asia/)

> [^7]: [TrendMicro Tropic Trooper Mar 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/tropic-trooper-new-strategy/)

> [^8]: [Microsoft COM](https://msdn.microsoft.com/library/windows/desktop/ms680573.aspx)


