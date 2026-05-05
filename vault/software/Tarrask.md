---
aliases: 
    - S1011
    
mitre-attack: https://attack.mitre.org/software/S1011
---

## S1011

[Tarrask](https://attack.mitre.org/software/S1011) is malware that has been used by [HAFNIUM](https://attack.mitre.org/groups/G0125) since at least August 2021. [Tarrask](https://attack.mitre.org/software/S1011) was designed to evade digital defenses and maintain persistence by generating concealed scheduled tasks.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Tarrask](https://attack.mitre.org/software/S1011) has masqueraded as executable files such as `winupdate.exe`, `date.exe`, or `win.exe`.[^1]     |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Tarrask](https://attack.mitre.org/software/S1011) may abuse the Windows schtasks command-line tool to create "hidden" scheduled tasks.[^1]  |
| [[Token Impersonation／Theft\|T1134.001]] | Token Impersonation／Theft | [Tarrask](https://attack.mitre.org/software/S1011) leverages token theft to obtain `lsass.exe` security permissions.[^1]   |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Tarrask](https://attack.mitre.org/software/S1011) creates a scheduled task called “WinUpdate” to re-establish any dropped  C2 connections.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Tarrask](https://attack.mitre.org/software/S1011) is able to create “hidden” scheduled tasks for persistence.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Tarrask](https://attack.mitre.org/software/S1011) is able to delete the Security Descriptor (`SD`) registry subkey in order to “hide” scheduled tasks.[^1]  |
| [[Hide Artifacts\|T1564]] | Hide Artifacts | [Tarrask](https://attack.mitre.org/software/S1011) is able to create “hidden” scheduled tasks by deleting the Security Descriptor (`SD`) registry value.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[HAFNIUM\|G0125]] | HAFNIUM |



## References

[^1]: [Tarrask scheduled task](https://www.microsoft.com/security/blog/2022/04/12/tarrask-malware-uses-scheduled-tasks-for-defense-evasion/)


