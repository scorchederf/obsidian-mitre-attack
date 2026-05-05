---
aliases: 
    - S0178
    
mitre-attack: https://attack.mitre.org/software/S0178
---

## S0178

[Truvasys](https://attack.mitre.org/software/S0178) is first-stage malware that has been used by [PROMETHIUM](https://attack.mitre.org/groups/G0056). It is a collection of modules written in the Delphi programming language. [^3]  [^2]  [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Truvasys](https://attack.mitre.org/software/S0178) adds a Registry Run key to establish persistence.[^3]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | To establish persistence, [Truvasys](https://attack.mitre.org/software/S0178) adds a Registry Run key with a value "TaskMgr" in an attempt to masquerade as the legitimate Windows Task Manager.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[PROMETHIUM\|G0056]] | PROMETHIUM |



## References

[^1]: [Microsoft SIR Vol 21](http://download.microsoft.com/download/E/B/0/EB0F50CC-989C-4B66-B7F6-68CD3DC90DE3/Microsoft_Security_Intelligence_Report_Volume_21_English.pdf)


[^2]: [Microsoft NEODYMIUM Dec 2016](https://blogs.technet.microsoft.com/mmpc/2016/12/14/twin-zero-day-attacks-promethium-and-neodymium-target-individuals-in-europe/)


[^3]: [Microsoft Win Defender Truvasys Sep 2017](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Backdoor:Win32/Truvasys.A!dha)


[^4]: Truvasys


