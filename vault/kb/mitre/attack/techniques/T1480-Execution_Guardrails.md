---
aliases: 
    - T1480
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/stealth
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1480-Execution_Guardrails
tactic: 
     - Stealth
platforms:
     - ESXi - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may use execution guardrails to constrain execution or actions based on adversary supplied and environment specific conditions that are expected to be present on the target. Guardrails ensure that a payload only executes against an intended target and reduces collateral damage from an adversary’s campaign.[^1]  Values an adversary can provide about a target system or environment to use as guardrails may include specific network share names, attached physical devices, files, joined Active Directory (AD) domains, and local/external IP addresses.[^2] <br><br>Guardrails can be used to prevent exposure of capabilities in environments that are not intended to be compromised or operated within. This use of guardrails is distinct from typical [[kb/mitre/attack/techniques/T1497-Virtualization_Sandbox_Evasion\|Virtualization/Sandbox Evasion]]. While use of [[kb/mitre/attack/techniques/T1497-Virtualization_Sandbox_Evasion\|Virtualization/Sandbox Evasion]] may involve checking for known sandbox values and continuing with execution only if there is no match, the use of guardrails will involve checking for an expected target-specific value and only continuing with execution if there is such a match.<br><br>Adversaries may identify and block certain user-agents to evade defenses and narrow the scope of their attack to victims and platforms on which it will be most effective. A user-agent self-identifies data such as a user's software application, operating system, vendor, and version. Adversaries may check user-agents for operating system identification and then only serve malware for the exploitable software while ignoring all other operating systems.[^3] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S9003-evilginx2\|S9003]] | evilginx2 | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can reject requests to phishing URLs if the User-Agent of the visitor doesn't match the allowlist REGEX filter for a specific lure.[^4]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1055-Do_Not_Mitigate\|M1055]] | Do Not Mitigate | [[kb/mitre/attack/techniques/T1480-Execution_Guardrails\|Execution Guardrails]] likely should not be mitigated with preventative controls because it may protect unintended targets from being compromised. If targeted, efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identifying subsequent malicious behavior if compromised. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1480.001-Environmental_Keying\|T1480.001]] | Environmental Keying |
| [[kb/mitre/attack/techniques/T1480.002-Mutual_Exclusion\|T1480.002]] | Mutual Exclusion |




> [!info]- References
> [^1]: [FireEye Kevin Mandia Guardrails](https://www.cyberscoop.com/kevin-mandia-fireeye-u-s-malware-nice/)

> [^2]: [FireEye Outlook Dec 2019](https://www.fireeye.com/blog/threat-research/2019/12/breaking-the-rules-tough-outlook-for-home-page-attacks.html)

> [^3]: [Trellix-Qakbot](https://www.trellix.com/blogs/research/qakbot-evolves-to-onenote-malware-distribution/)

> [^4]: [Breakdev Evilginx 2.4 SEP 2020](https://breakdev.org/evilginx-2-4-gone-phishing/)


