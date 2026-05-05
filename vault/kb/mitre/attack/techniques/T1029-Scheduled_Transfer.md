---
aliases: 
    - T1029
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/exfiltration
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1029-Scheduled_Transfer
tactic: 
     - Exfiltration
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may schedule data exfiltration to be performed only at certain times of day or at certain intervals. This could be done to blend traffic patterns with normal activity or availability.<br><br>When scheduled exfiltration is used, other exfiltration techniques likely apply as well to transfer the information out of the network, such as [[kb/mitre/attack/techniques/T1041-Exfiltration_Over_C2_Channel\|Exfiltration Over C2 Channel]] or [[kb/mitre/attack/techniques/T1048-Exfiltration_Over_Alternative_Protocol\|Exfiltration Over Alternative Protocol]].




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-Network_Intrusion_Prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary command and control infrastructure and malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool command and control signatures over time or construct protocols in such a way to avoid detection by common defensive tools. [^1]  |






> [!info]- References
> [^1]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


