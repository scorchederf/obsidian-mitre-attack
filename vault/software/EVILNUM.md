---
aliases: 
    - S0568
    
mitre-attack: https://attack.mitre.org/software/S0568
---

## S0568

[EVILNUM](https://attack.mitre.org/software/S0568) is fully capable backdoor that was first identified in 2018. [EVILNUM](https://attack.mitre.org/software/S0568) is used by the APT group [Evilnum](https://attack.mitre.org/groups/G0120) which has the same name.[^3] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[One-Way Communication\|T1102.003]] | One-Way Communication | [EVILNUM](https://attack.mitre.org/software/S0568) has used a one-way communication method via GitLab and Digital Point to perform C2.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [EVILNUM](https://attack.mitre.org/software/S0568) can achieve persistence through the Registry Run key.[^3] [^2]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [EVILNUM](https://attack.mitre.org/software/S0568) has a function called "DeleteLeftovers" to remove certain artifacts of the attack.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [EVILNUM](https://attack.mitre.org/software/S0568) can obtain the computer name from the victim's system.[^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [EVILNUM](https://attack.mitre.org/software/S0568) can upload files over the C2 channel from the infected host.[^2]   |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [EVILNUM](https://attack.mitre.org/software/S0568) can harvest cookies and upload them to the C2 server.[^2]  |
| [[Timestomp\|T1070.006]] | Timestomp | [EVILNUM](https://attack.mitre.org/software/S0568) has changed the creation date of files.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [EVILNUM](https://attack.mitre.org/software/S0568) can make modifications to the Regsitry for persistence.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [EVILNUM](https://attack.mitre.org/software/S0568) can download and upload files to the victim's computer.[^3] [^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [EVILNUM](https://attack.mitre.org/software/S0568) can obtain the username from the victim's machine.[^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [EVILNUM](https://attack.mitre.org/software/S0568) can execute commands and scripts through rundll32.[^2]   |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [EVILNUM](https://attack.mitre.org/software/S0568) can search for anti-virus products on the system.[^2]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [EVILNUM](https://attack.mitre.org/software/S0568) can run a remote scriptlet that drops a file and executes it via regsvr32.exe.[^3]   |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [EVILNUM](https://attack.mitre.org/software/S0568) has used the Windows Management Instrumentation (WMI) tool to enumerate infected machines.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Evilnum\|G0120]] | Evilnum |



## References

[^1]: EVILNUM


[^2]: [Prevailion EvilNum May 2020](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)


[^3]: [ESET EvilNum July 2020](https://www.welivesecurity.com/2020/07/09/more-evil-deep-look-evilnum-toolset/)


