---
aliases: 
    - T1560
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/collection
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1560-Archive_Collected_Data
tactic: 
     - Collection
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

An adversary may compress and/or encrypt data that is collected prior to exfiltration. Compressing the data can help to obfuscate the collected data and minimize the amount of data sent over the network.[^3]  Encryption can be used to hide information that is being exfiltrated from detection or make exfiltration less conspicuous upon inspection by a defender.<br><br>Both compression and encryption are done prior to exfiltration, and can be performed using a utility, 3rd party library, or custom method.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can ZIP directories on the target system.[^5]  |
| [[kb/mitre/attack/software/S0445-ShimRatReporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] used LZ compression to compress initial reconnaissance reports before sending to the C2.[^6] 	 |
| [[kb/mitre/attack/software/S0521-BloodHound\|S0521]] | BloodHound | [[kb/mitre/attack/software/S0521-BloodHound\|BloodHound]] can compress data collected by its SharpHound ingestor into a ZIP file to be written to disk.[^2] [^1]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | System scans can be performed to identify unauthorized archival utilities. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1560.001-Archive_via_Utility\|T1560.001]] | Archive via Utility |
| [[kb/mitre/attack/techniques/T1560.002-Archive_via_Library\|T1560.002]] | Archive via Library |
| [[kb/mitre/attack/techniques/T1560.003-Archive_via_Custom_Method\|T1560.003]] | Archive via Custom Method |




> [!info]- References
> [^1]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)

> [^2]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)

> [^3]: [DOJ GRU Indictment Jul 2018](https://cdn.cnn.com/cnn/2018/images/07/13/gru.indictment.pdf)

> [^4]: [Wikipedia File Header Signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)

> [^5]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)

> [^6]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)


