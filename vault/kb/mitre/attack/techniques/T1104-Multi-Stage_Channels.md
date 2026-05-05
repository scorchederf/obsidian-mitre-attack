---
aliases: 
    - T1104
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1104-Multi-Stage_Channels
tactic: 
     - Command and Control
platforms:
     - Linux - macOS - Windows - ESXi
permissions required:
     - none
---

## Description

Adversaries may create multiple stages for command and control that are employed under different conditions or for certain functions. Use of multiple stages may obfuscate the command and control channel to make detection more difficult.<br><br>Remote access tools will call back to the first-stage command and control server for instructions. The first stage may have automated capabilities to collect basic host information, update tools, and upload additional files. A second remote access tool (RAT) could be uploaded at that point to redirect the host to the second-stage command and control server. The second stage will likely be more fully featured and allow the adversary to interact with the system through a reverse shell and additional RAT features.<br><br>The different stages will likely be hosted separately with no overlapping infrastructure. The loader may also have backup first-stage callbacks or [[kb/mitre/attack/techniques/T1008-Fallback_Channels\|Fallback Channels]] in case the original first-stage communication path is discovered and blocked.




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-Network_Intrusion_Prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. |





