---
aliases: 
    - T1534
tags: 
    - attack/domain/enterprise_attack
    - attack/tactic/lateral_movement
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1534-Internal_Spearphishing
tactic: 
     - Lateral Movement
platforms:
     - Linux - macOS - Office Suite - SaaS - Windows
permissions required:
     - none
---

## Description

After they already have access to accounts or systems within the environment, adversaries may use internal spearphishing to gain access to additional information or compromise other users within the same organization. Internal spearphishing is multi-staged campaign where a legitimate account is initially compromised either by controlling the user's device or by compromising the account credentials of the user. Adversaries may then attempt to take advantage of the trusted internal account to increase the likelihood of tricking more victims into falling for phish attempts, often incorporating [[kb/mitre/attack/techniques/T1684.001-Impersonation\|Impersonation]].[^1] <br><br>For example, adversaries may leverage [[kb/mitre/attack/techniques/T1566.001-Spearphishing_Attachment\|Spearphishing Attachment]] or [[kb/mitre/attack/techniques/T1566.002-Spearphishing_Link\|Spearphishing Link]] as part of internal spearphishing to deliver a payload or redirect to an external site to capture credentials through [[kb/mitre/attack/techniques/T1056-Input_Capture\|Input Capture]] on sites that mimic login interfaces.<br><br>Adversaries may also leverage internal chat apps, such as Microsoft Teams, to spread malicious content or engage users in attempts to capture sensitive information and/or credentials.[^2] 








> [!info]- References
> [^1]: [Trend Micro - Int SP](https://www.trendmicro.com/en_us/research.html)

> [^2]: [Int SP - chat apps](https://www.microsoft.com/en-us/security/blog/2023/08/02/midnight-blizzard-conducts-targeted-social-engineering-over-microsoft-teams/)


