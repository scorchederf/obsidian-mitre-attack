---
aliases: 
    - T1678
tags: 
    - attack/domain/enterprise_attack
    - attack/tactic/stealth
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1678-Delay_Execution
tactic: 
     - Stealth
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may employ various time-based methods to evade detection and analysis. These techniques often exploit system clocks, delays, or timing mechanisms to obscure malicious activity, blend in with benign activity, and avoid scrutiny. Adversaries can perform this behavior within virtualization/sandbox environments or natively on host systems. <br><br>Adversaries may utilize programmatic `sleep` commands or native system scheduling functionality, for example [[kb/mitre/attack/techniques/T1053-Scheduled_Task_Job\|Scheduled Task/Job]]. Benign commands or other operations may also be used to delay malware execution or ensure prior commands have had time to execute properly. Loops or otherwise needless repetitions of commands, such as `ping`, may be used to delay malware execution and potentially exceed time thresholds of automated analysis environments.[^3] [^1]  Another variation, commonly referred to as API hammering, involves making various calls to Native API functions in order to delay execution (while also potentially overloading analysis environments with junk data).[^4] [^2] 








> [!info]- References
> [^1]: [Netskope Nitol](https://www.netskope.com/blog/nitol-botnet-makes-resurgence-evasive-sandbox-analysis-technique)

> [^2]: [Joe Sec Trickbot](https://www.joesecurity.org/blog/498839998833561473)

> [^3]: [Revil Independence Day](https://news.sophos.com/en-us/2021/07/04/independence-day-revil-uses-supply-chain-exploit-to-attack-hundreds-of-businesses/)

> [^4]: [Joe Sec Nymaim](https://www.joesecurity.org/blog/3660886847485093803)


