---
aliases: 
    - S0404
    
mitre-attack: https://attack.mitre.org/software/S0404
---

## S0404

[esentutl](https://attack.mitre.org/software/S0404) is a command-line tool that provides database utilities for the Windows Extensible Storage Engine.[^6] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Direct Volume Access\|T1006]] | Direct Volume Access | [esentutl](https://attack.mitre.org/software/S0404) can use the Volume Shadow Copy service to copy locked files such as `ntds.dit`.[^5] [^1]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [esentutl](https://attack.mitre.org/software/S0404) can be used to copy files to/from a remote share.[^5]  |
| [[NTDS\|T1003.003]] | NTDS | [esentutl](https://attack.mitre.org/software/S0404) can copy `ntds.dit` using the Volume Shadow Copy service.[^5] [^1]  |
| [[NTFS File Attributes\|T1564.004]] | NTFS File Attributes | [esentutl](https://attack.mitre.org/software/S0404) can be used to read and write alternate data streams.[^5]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [esentutl](https://attack.mitre.org/software/S0404) can be used to copy files from a given URL.[^5]  |
| [[Data from Local System\|T1005]] | Data from Local System | [esentutl](https://attack.mitre.org/software/S0404) can be used to collect data from local file systems.[^7]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Chimera\|G0114]] | Chimera |
| [[INC Ransom\|G1032]] | INC Ransom |
| [[menuPass\|G0045]] | menuPass |



## References

[^1]: [Cary Esentutl](https://dfironthemountain.wordpress.com/2018/12/06/locked-file-access-using-esentutl-exe/)


[^2]: [SOCRadar INC Ransom January 2024](https://socradar.io/dark-web-profile-inc-ransom/)


[^3]: [SentinelOne INC Ransomware](https://www.sentinelone.com/anthology/inc-ransom/)


[^4]: [NCC Group Chimera January 2021](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)


[^5]: [LOLBAS Esentutl](https://lolbas-project.github.io/lolbas/Binaries/Esentutl/)


[^6]: [Microsoft Esentutl](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh875546(v=ws.11))


[^7]: [Red Canary 2021 Threat Detection Report March 2021](https://resource.redcanary.com/rs/003-YRU-314/images/2021-Threat-Detection-Report.pdf?mkt_tok=MDAzLVlSVS0zMTQAAAF_PIlmhNTaG2McG4X_foM-cIr20UfyB12MIQ10W0HbtMRwxGOJaD0Xj6CRTNg_S-8KniRxtf9xzhz_ACvm_TpbJAIgWCV8yIsFgbhb8cuaZA)


[^8]: [FireEye APT10 Sept 2018](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)


