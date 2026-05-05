---
aliases: 
    - T1689
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/defense_impairment
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1689-Downgrade_Attack
tactic: 
     - Defense Impairment
platforms:
     - macOS - Windows - Linux
permissions required:
     - none
---

## Description

Adversaries may downgrade or use a version of system features that may be outdated, vulnerable, and/or does not support updated security controls. Downgrade attacks typically take advantage of a system’s backward compatibility to force it into less secure modes of operation.<br><br>Adversaries may downgrade and use various less-secure versions of features of a system, such as [[kb/mitre/attack/techniques/T1059-Command_and_Scripting_Interpreter\|Command and Scripting Interpreter]] or even network protocols that can be abused to enable [[kb/mitre/attack/techniques/T1557-Adversary-in-the-Middle\|Adversary-in-the-Middle]] or [[kb/mitre/attack/techniques/T1040-Network_Sniffing\|Network Sniffing]].[^1]  For example, [[kb/mitre/attack/techniques/T1059.001-PowerShell\|PowerShell]] versions 5+ includes Script Block Logging (SBL), which can record executed script content. However, adversaries may attempt to execute a previous version of PowerShell that does not support SBL with the intent to impair defenses while running malicious scripts that may have otherwise been detected.[^6] [^3] [^2] <br><br>Adversaries may similarly target network traffic to downgrade from an encrypted HTTPS connection to an unsecured HTTP connection that exposes network data in clear text.[^4] [^5]  On Windows systems, adversaries may downgrade the boot manager to a vulnerable version that bypasses Secure Boot, granting the ability to disable various operating system security mechanisms.[^9] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can downgrade NTLM to capture NTLM hashes.[^8]   |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1042-Disable_or_Remove_Feature_or_Program\|M1042]] | Disable or Remove Feature or Program | Consider removing previous versions of tools that are unnecessary to the environment when possible. |
| [[kb/mitre/attack/mitigations/M1054-Software_Configuration\|M1054]] | Software Configuration | Consider implementing policies on internal web servers, such HTTP Strict Transport Security, that enforce the use of HTTPS/network traffic encryption to prevent insecure connections.[^7]  |






> [!info]- References
> [^1]: [Praetorian TLS Downgrade Attack 2014](https://www.praetorian.com/blog/man-in-the-middle-tls-ssl-protocol-downgrade-attack/)

> [^2]: [att_def_ps_logging](https://nsfocusglobal.com/attack-and-defense-around-powershell-event-logging/)

> [^3]: [Google Cloud downgrade attack](https://cloud.google.com/blog/topics/threat-intelligence/bring-your-own-land-novel-red-teaming-technique/)

> [^4]: [Targeted SSL Stripping Attacks Are Real](https://blog.checkpoint.com/research/targeted-ssl-stripping-attacks-are-real/amp/)

> [^5]: [CrowdStrike Downgrade attack 2](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/downgrade-attack/)

> [^6]: [CrowdStrike downgrade attack](https://www.crowdstrike.com/en-us/blog/how-falcon-complete-stopped-a-big-game-hunting-ransomware-attack/)

> [^7]: [Chromium HSTS](https://www.chromium.org/hsts/)

> [^8]: [Github_SILENTTRINITY](https://github.com/byt3bl33d3r/SILENTTRINITY)

> [^9]: [SafeBreach](https://www.safebreach.com/blog/downgrade-attacks-using-windows-updates/)


