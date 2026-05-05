---
aliases: 
    - T1127
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/execution
    - attack/tactic/stealth
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1127-Trusted_Developer_Utilities_Proxy_Execution
tactic: 
     - Stealth - Execution
platforms:
     - Windows
permissions required:
     - none
---

## Description

Adversaries may take advantage of trusted developer utilities to proxy execution of malicious payloads. There are many utilities used for software development related tasks that can be used to execute code in various forms to assist in development, debugging, and reverse engineering.[^2] [^4] [^6] [^3]  These utilities may often be signed with legitimate certificates that allow them to execute on a system and proxy execution of malicious code through a trusted process that effectively bypasses application control solutions.<br><br>Smart App Control is a feature of Windows that blocks applications it considers potentially malicious from running by verifying unsigned applications against a known safe list from a Microsoft cloud service before executing them.[^5]  However, adversaries may leverage "reputation hijacking" to abuse an operating system’s trust of safe, signed applications that support the execution of arbitrary code. By leveraging [[kb/mitre/attack/techniques/T1127-Trusted_Developer_Utilities_Proxy_Execution\|Trusted Developer Utilities Proxy Execution]] to run their malicious code, adversaries may bypass Smart App Control protections.[^1] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1021-Restrict_Web-Based_Content\|M1021]] | Restrict Web-Based Content | Consider disabling software installation or execution from the internet via developer utilities. |
| [[kb/mitre/attack/mitigations/M1038-Execution_Prevention\|M1038]] | Execution Prevention | Certain developer utilities should be blocked or restricted if not required. |
| [[kb/mitre/attack/mitigations/M1042-Disable_or_Remove_Feature_or_Program\|M1042]] | Disable or Remove Feature or Program | Specific developer utilities may not be necessary within a given environment and should be removed if not used. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1127.001-MSBuild\|T1127.001]] | MSBuild |
| [[kb/mitre/attack/techniques/T1127.002-ClickOnce\|T1127.002]] | ClickOnce |
| [[kb/mitre/attack/techniques/T1127.003-JamPlus\|T1127.003]] | JamPlus |




> [!info]- References
> [^1]: [Elastic Security Labs](https://www.elastic.co/security-labs/dismantling-smart-app-control)

> [^2]: [engima0x3 DNX Bypass](https://enigma0x3.net/2016/11/17/bypassing-application-whitelisting-by-using-dnx-exe/)

> [^3]: [LOLBAS Tracker](https://lolbas-project.github.io/lolbas/OtherMSBinaries/Tracker/)

> [^4]: [engima0x3 RCSI Bypass](https://enigma0x3.net/2016/11/21/bypassing-application-whitelisting-by-using-rcsi-exe/)

> [^5]: [Microsoft Smart App Control](https://support.microsoft.com/en-us/windows/smart-app-control-frequently-asked-questions-285ea03d-fa88-4d56-882e-6698afdb7003)

> [^6]: [Exploit Monday WinDbg](https://web.archive.org/web/20160816135945/http://www.exploit-monday.com/2016/08/windbg-cdb-shellcode-runner.html)


