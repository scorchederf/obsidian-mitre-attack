---
aliases: 
    - T1112
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/defense_impairment
    - attack/tactic/persistence
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1112-Modify_Registry
tactic: 
     - Defense Impairment - Persistence
platforms:
     - Windows
permissions required:
     - none
---

## Description

Adversaries may interact with the Windows Registry as part of a variety of other techniques to aid in defense evasion, persistence, and execution.<br><br>Access to specific areas of the Registry depends on account permissions, with some keys requiring administrator-level access. The built-in Windows command-line utility [[kb/mitre/attack/software/S0075-Reg\|Reg]] may be used for local or remote Registry modification.[^19]  Other tools, such as remote access tools, may also contain functionality to interact with the Registry through the Windows API.<br><br>The Registry may be modified in order to hide configuration information or malicious payloads via [[kb/mitre/attack/techniques/T1027-Obfuscated_Files_or_Information\|Obfuscated Files or Information]].[^6] [^16] [^8] [^18]  The Registry may also be modified to impair defenses, such as by enabling macros for all Microsoft Office products, allowing privilege escalation without alerting the user, increasing the maximum number of allowed outbound requests, and/or modifying systems to store plaintext credentials in memory.[^2] [^6] <br><br>The Registry of a remote system may be modified to aid in execution of files as part of lateral movement. It requires the remote Registry service to be running on the target system.[^4]  Often [[kb/mitre/attack/techniques/T1078-Valid_Accounts\|Valid Accounts]] are required, along with access to the remote system's [[kb/mitre/attack/techniques/T1021.002-SMB_Windows_Admin_Shares\|SMB/Windows Admin Shares]] for RPC communication.<br><br>Finally, Registry modifications may also include actions to hide keys, such as prepending key names with a null character, which will cause an error and/or be ignored when read via [[kb/mitre/attack/software/S0075-Reg\|Reg]] or other utilities using the Win32 API.[^15]  Adversaries may abuse these pseudo-hidden keys to conceal payloads/commands used to maintain persistence.[^10] [^9] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0075-Reg\|S0075]] | Reg | [[kb/mitre/attack/software/S0075-Reg\|Reg]] may be used to interact with and modify the Windows Registry of a local or remote system at the command-line interface.[^19]  |
| [[kb/mitre/attack/software/S0262-QuasarRAT\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] has a command to edit the Registry on the victim’s machine.[^5] [^7]  |
| [[kb/mitre/attack/software/S0332-Remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] has full control of the Registry, including the ability to modify it.[^11] [^1]  |
| [[kb/mitre/attack/software/S0488-CrackMapExec\|S0488]] | CrackMapExec | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can create a registry key using wdigest.[^20]  |
| [[kb/mitre/attack/software/S0527-CSPY_Downloader\|S0527]] | CSPY Downloader | [[kb/mitre/attack/software/S0527-CSPY_Downloader\|CSPY Downloader]] can write to the Registry under the `%windir%` variable to execute tasks.[^17]  |
| [[kb/mitre/attack/software/S0677-AADInternals\|S0677]] | AADInternals | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can modify registry keys as part of setting a new pass-through authentication agent.[^14]  |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can modify registry keys, including to enable or disable Remote Desktop Protocol (RDP).[^12]  |
| [[kb/mitre/attack/software/S1050-PcShare\|S1050]] | PcShare | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] can delete its persistence mechanisms from the registry.[^13]  |
| [[kb/mitre/attack/software/S1131-NPPSPY\|S1131]] | NPPSPY | [[kb/mitre/attack/software/S1131-NPPSPY\|NPPSPY]] modifies the Registry to record the malicious listener for output from the Winlogon process.[^3]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1024-Restrict_Registry_Permissions\|M1024]] | Restrict Registry Permissions | Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation. |






> [!info]- References
> [^1]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)

> [^2]: [CISA LockBit 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a)

> [^3]: [Huntress NPPSPY 2022](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)

> [^4]: [Microsoft Remote](https://technet.microsoft.com/en-us/library/cc754820.aspx)

> [^5]: [GitHub QuasarRAT](https://github.com/quasar/QuasarRAT)

> [^6]: [Unit42 BabyShark Feb 2019](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)

> [^7]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)

> [^8]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)

> [^9]: [SpectorOps Hiding Reg Jul 2017](https://posts.specterops.io/hiding-registry-keys-with-psreflect-b18ec5ac8353)

> [^10]: [TrendMicro POWELIKS AUG 2014](https://blog.trendmicro.com/trendlabs-security-intelligence/poweliks-malware-hides-in-windows-registry/)

> [^11]: [Riskiq Remcos Jan 2018](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)

> [^12]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^13]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)

> [^14]: [AADInternals Documentation](https://o365blog.com/aadinternals)

> [^15]: [Microsoft Reghide NOV 2006](https://docs.microsoft.com/sysinternals/downloads/reghide)

> [^16]: [Avaddon Ransomware 2021](https://arxiv.org/pdf/2102.04796)

> [^17]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)

> [^18]: [CISA Russian Gov Critical Infra 2018](https://www.cisa.gov/news-events/alerts/2018/03/15/russian-government-cyber-activity-targeting-energy-and-other-critical-infrastructure-sectors)

> [^19]: [Microsoft Reg](https://technet.microsoft.com/en-us/library/cc732643.aspx)

> [^20]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)


