---
aliases: 
    - T1497
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/tactic/discovery
    - attack/tactic/stealth
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1497-Virtualization_Sandbox_Evasion
tactic: 
     - Stealth - Discovery
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may employ various means to detect and avoid virtualization and analysis environments. This may include changing behaviors based on the results of checks for the presence of artifacts indicative of a virtual machine environment (VME) or sandbox. If the adversary detects a VME, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for VME artifacts before dropping secondary or additional payloads. Adversaries may use the information learned from [[kb/mitre/attack/techniques/T1497-Virtualization_Sandbox_Evasion\|Virtualization/Sandbox Evasion]] during automated discovery to shape follow-on behaviors.[^1] <br><br>Adversaries may use several methods to accomplish [[kb/mitre/attack/techniques/T1497-Virtualization_Sandbox_Evasion\|Virtualization/Sandbox Evasion]] such as checking for security monitoring tools (e.g., Sysinternals, Wireshark, etc.) or other system artifacts associated with analysis or virtualization. Adversaries may also check for legitimate user activity to help determine if it is in an analysis environment. Additional methods include use of sleep timers or loops within malware code to avoid operating within a temporary sandbox.[^2] <br><br>






## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1497.001-System_Checks\|T1497.001]] | System Checks |
| [[kb/mitre/attack/techniques/T1497.002-User_Activity_Based_Checks\|T1497.002]] | User Activity Based Checks |
| [[kb/mitre/attack/techniques/T1497.003-Time_Based_Checks\|T1497.003]] | Time Based Checks |




> [!info]- References
> [^1]: [Deloitte Environment Awareness](https://drive.google.com/file/d/1t0jn3xr4ff2fR30oQAUn_RsWSnMpOAQc/edit)

> [^2]: [Unit 42 Pirpi July 2015](https://unit42.paloaltonetworks.com/ups-observations-on-cve-2015-3113-prior-zero-days-and-the-pirpi-payload/)


