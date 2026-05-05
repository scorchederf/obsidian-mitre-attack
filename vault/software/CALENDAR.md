---
aliases: 
    - S0025
    
mitre-attack: https://attack.mitre.org/software/S0025
---

## S0025

[CALENDAR](https://attack.mitre.org/software/S0025) is malware used by [APT1](https://attack.mitre.org/groups/G0006) that mimics legitimate Gmail Calendar traffic. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [CALENDAR](https://attack.mitre.org/software/S0025) has a command to run cmd.exe to execute commands.[^1]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | The [CALENDAR](https://attack.mitre.org/software/S0025) malware communicates through the use of events in Google Calendar.[^2] [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT1\|G0006]] | APT1 |



## References

[^1]: [Mandiant APT1 Appendix](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)


[^2]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)


