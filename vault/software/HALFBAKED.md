---
aliases: 
    - S0151
    
mitre-attack: https://attack.mitre.org/software/S0151
---

## S0151

[HALFBAKED](https://attack.mitre.org/software/S0151) is a malware family consisting of multiple components intended to establish persistence in victim networks. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [HALFBAKED](https://attack.mitre.org/software/S0151) can obtain information about running processes on the victim.[^2]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [HALFBAKED](https://attack.mitre.org/software/S0151) can use WMI queries to gather system information.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [HALFBAKED](https://attack.mitre.org/software/S0151) can obtain screenshots from the victim.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [HALFBAKED](https://attack.mitre.org/software/S0151) can execute PowerShell scripts.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [HALFBAKED](https://attack.mitre.org/software/S0151) can delete a specified file.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [HALFBAKED](https://attack.mitre.org/software/S0151) can obtain information about the OS, processor, and BIOS.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN7\|G0046]] | FIN7 |



## References

[^1]: [FireEye FIN7 Aug 2018](https://www.fireeye.com/blog/threat-research/2018/08/fin7-pursuing-an-enigmatic-and-evasive-global-criminal-operation.html)


[^2]: [FireEye FIN7 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html)


