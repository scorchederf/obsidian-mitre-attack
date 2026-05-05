---
aliases: 
    - S0193
    
mitre-attack: https://attack.mitre.org/software/S0193
---

## S0193

[Forfiles](https://attack.mitre.org/software/S0193) is a Windows utility commonly used in batch jobs to execute commands on one or more selected files or directories (ex: list all directories in a drive, read the first line of all files created yesterday, etc.). Forfiles can be executed from either the command line, Run window, or batch files/scripts. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Indirect Command Execution\|T1202]] | Indirect Command Execution | [Forfiles](https://attack.mitre.org/software/S0193) can be used to subvert controls and possibly conceal command execution by not directly invoking [cmd](https://attack.mitre.org/software/S0106).[^3] [^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Forfiles](https://attack.mitre.org/software/S0193) can be used to act on (ex: copy, move, etc.) files/directories in a system during (ex: copy files into a staging area before).[^4]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Forfiles](https://attack.mitre.org/software/S0193) can be used to locate certain types of files/directories in a system.(ex: locate all files with a specific extension, name, and/or age)[^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT28\|G0007]] | APT28 |



## References

[^1]: [Evi1cg Forfiles Nov 2017](https://x.com/Evi1cg/status/935027922397573120)


[^2]: [Microsoft Forfiles Aug 2016](https://docs.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/cc753551(v=ws.11))


[^3]: [VectorSec ForFiles Aug 2017](https://x.com/vector_sec/status/896049052642533376)


[^4]: [Überwachung APT28 Forfiles June 2015](https://netzpolitik.org/2015/digital-attack-on-german-parliament-investigative-report-on-the-hack-of-the-left-party-infrastructure-in-bundestag/)


