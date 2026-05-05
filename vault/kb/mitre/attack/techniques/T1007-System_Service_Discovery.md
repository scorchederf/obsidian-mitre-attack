---
aliases: 
    - T1007
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1007-System_Service_Discovery
tactic: 
     - Discovery
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may try to gather information about registered local system services. Adversaries may obtain information about services using tools as well as OS utility commands such as `sc query`, `tasklist /svc`, `systemctl --type=service`, and `net start`. Adversaries may also gather information about schedule tasks via commands such as `schtasks` on Windows or `crontab -l` on Linux and macOS.[^3] [^4] [^6] [^2] <br><br>Adversaries may use the information from [[kb/mitre/attack/techniques/T1007-System_Service_Discovery\|System Service Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0039-Net\|S0039]] | Net | The `net start` command can be used in [[kb/mitre/attack/software/S0039-Net\|Net]] to find information about Windows services.[^7]  |
| [[kb/mitre/attack/software/S0057-Tasklist\|S0057]] | Tasklist | [[kb/mitre/attack/software/S0057-Tasklist\|Tasklist]] can be used to discover services running on a system.[^1]  |
| [[kb/mitre/attack/software/S0378-PoshC2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] can enumerate service and service permission information.[^8]  |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can search for modifiable services that could be used for privilege escalation.[^5]  |








> [!info]- References
> [^1]: [Microsoft Tasklist](https://technet.microsoft.com/en-us/library/bb491010.aspx)

> [^2]: [Aquasec Kinsing 2020](https://www.aquasec.com/blog/threat-alert-kinsing-malware-container-vulnerability/)

> [^3]: [Elastic Security Labs GOSAR 2024](https://www.elastic.co/security-labs/under-the-sadbridge-with-gosar)

> [^4]: [SentinelLabs macOS Malware 2021](https://www.sentinelone.com/labs/20-common-tools-techniques-used-by-macos-threat-actors-malware/)

> [^5]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^6]: [Splunk Linux Gormir 2024](https://www.splunk.com/en_us/blog/security/breaking-down-linux-gomir-understanding-this-backdoors-ttps.html)

> [^7]: [Savill 1999](https://web.archive.org/web/20150511162820/http://windowsitpro.com/windows/netexe-reference)

> [^8]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)


