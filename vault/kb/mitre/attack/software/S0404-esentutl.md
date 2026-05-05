---
aliases: 
    - S0404
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0404-esentutl
---

## Description

[[kb/mitre/attack/software/S0404-esentutl\|esentutl]] is a command-line tool that provides database utilities for the Windows Extensible Storage Engine.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.003-NTDS\|T1003.003]] | NTDS | [[kb/mitre/attack/software/S0404-esentutl\|esentutl]] can copy `ntds.dit` using the Volume Shadow Copy service.[^4] [^3]  |
| [[kb/mitre/attack/techniques/T1005-Data_from_Local_System\|T1005]] | Data from Local System | [[kb/mitre/attack/software/S0404-esentutl\|esentutl]] can be used to collect data from local file systems.[^2]  |
| [[kb/mitre/attack/techniques/T1006-Direct_Volume_Access\|T1006]] | Direct Volume Access | [[kb/mitre/attack/software/S0404-esentutl\|esentutl]] can use the Volume Shadow Copy service to copy locked files such as `ntds.dit`.[^4] [^3]  |
| [[kb/mitre/attack/techniques/T1105-Ingress_Tool_Transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0404-esentutl\|esentutl]] can be used to copy files from a given URL.[^4]  |
| [[kb/mitre/attack/techniques/T1564.004-NTFS_File_Attributes\|T1564.004]] | NTFS File Attributes | [[kb/mitre/attack/software/S0404-esentutl\|esentutl]] can be used to read and write alternate data streams.[^4]  |
| [[kb/mitre/attack/techniques/T1570-Lateral_Tool_Transfer\|T1570]] | Lateral Tool Transfer | [[kb/mitre/attack/software/S0404-esentutl\|esentutl]] can be used to copy files to/from a remote share.[^4]  |





> [!info]- References
> [^1]: [Microsoft Esentutl](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh875546(v=ws.11))

> [^2]: [Red Canary 2021 Threat Detection Report March 2021](https://resource.redcanary.com/rs/003-YRU-314/images/2021-Threat-Detection-Report.pdf?mkt_tok=MDAzLVlSVS0zMTQAAAF_PIlmhNTaG2McG4X_foM-cIr20UfyB12MIQ10W0HbtMRwxGOJaD0Xj6CRTNg_S-8KniRxtf9xzhz_ACvm_TpbJAIgWCV8yIsFgbhb8cuaZA)

> [^3]: [Cary Esentutl](https://dfironthemountain.wordpress.com/2018/12/06/locked-file-access-using-esentutl-exe/)

> [^4]: [LOLBAS Esentutl](https://lolbas-project.github.io/lolbas/Binaries/Esentutl/)


