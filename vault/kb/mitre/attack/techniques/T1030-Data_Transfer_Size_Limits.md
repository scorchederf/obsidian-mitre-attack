---
aliases: 
    - T1030
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/exfiltration
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1030-Data_Transfer_Size_Limits
tactic: 
     - Exfiltration
platforms:
     - Linux - macOS - Windows - ESXi
permissions required:
     - none
---

## Description

An adversary may exfiltrate data in fixed size chunks instead of whole files or limit packet sizes below certain thresholds. This approach may be used to avoid triggering network data transfer threshold alerts.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0699-Mythic\|S0699]] | Mythic | [[kb/mitre/attack/software/S0699-Mythic\|Mythic]] supports custom chunk sizes used to upload/download files.[^1] 	 |
| [[kb/mitre/attack/software/S1040-Rclone\|S1040]] | Rclone | The [[kb/mitre/attack/software/S1040-Rclone\|Rclone]] "chunker" overlay supports splitting large files in smaller chunks during upload to circumvent size limits.[^4] [^2]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-Network_Intrusion_Prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary command and control infrastructure and malware can be used to mitigate activity at the network level. |






> [!info]- References
> [^1]: [Mythc Documentation](https://docs.mythic-c2.net/)

> [^2]: [DFIR Conti Bazar Nov 2021](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)

> [^3]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)

> [^4]: [Rclone](https://rclone.org)


