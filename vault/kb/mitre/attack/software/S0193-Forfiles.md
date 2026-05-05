---
aliases: 
    - S0193
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0193-Forfiles
---

## Description

[[kb/mitre/attack/software/S0193-Forfiles\|Forfiles]] is a Windows utility commonly used in batch jobs to execute commands on one or more selected files or directories (ex: list all directories in a drive, read the first line of all files created yesterday, etc.). Forfiles can be executed from either the command line, Run window, or batch files/scripts. [^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1005-Data_from_Local_System\|T1005]] | Data from Local System | [[kb/mitre/attack/software/S0193-Forfiles\|Forfiles]] can be used to act on (ex: copy, move, etc.) files/directories in a system during (ex: copy files into a staging area before).[^1]  |
| [[kb/mitre/attack/techniques/T1083-File_and_Directory_Discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S0193-Forfiles\|Forfiles]] can be used to locate certain types of files/directories in a system.(ex: locate all files with a specific extension, name, and/or age)[^1]  |
| [[kb/mitre/attack/techniques/T1202-Indirect_Command_Execution\|T1202]] | Indirect Command Execution | [[kb/mitre/attack/software/S0193-Forfiles\|Forfiles]] can be used to subvert controls and possibly conceal command execution by not directly invoking [[kb/mitre/attack/software/S0106-cmd\|cmd]].[^4] [^3]  |





> [!info]- References
> [^1]: [Überwachung APT28 Forfiles June 2015](https://netzpolitik.org/2015/digital-attack-on-german-parliament-investigative-report-on-the-hack-of-the-left-party-infrastructure-in-bundestag/)

> [^2]: [Microsoft Forfiles Aug 2016](https://docs.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/cc753551(v=ws.11))

> [^3]: [Evi1cg Forfiles Nov 2017](https://x.com/Evi1cg/status/935027922397573120)

> [^4]: [VectorSec ForFiles Aug 2017](https://x.com/vector_sec/status/896049052642533376)


