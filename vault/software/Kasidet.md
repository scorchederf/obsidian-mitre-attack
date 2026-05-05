---
aliases: 
    - S0088
    
mitre-attack: https://attack.mitre.org/software/S0088
---

## S0088

[Kasidet](https://attack.mitre.org/software/S0088) is a backdoor that has been dropped by using malicious VBA macros. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Kasidet](https://attack.mitre.org/software/S0088) can execute commands using cmd.exe.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Kasidet](https://attack.mitre.org/software/S0088) has the ability to obtain a victim's system name and operating system version.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Kasidet](https://attack.mitre.org/software/S0088) has the ability to search for a given process name in processes currently running in the system.[^1]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [Kasidet](https://attack.mitre.org/software/S0088) has the ability to change firewall settings to allow a plug-in to be downloaded.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Kasidet](https://attack.mitre.org/software/S0088) creates a Registry Run key to establish persistence.[^1] [^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Kasidet](https://attack.mitre.org/software/S0088) has the ability to identify any anti-virus installed on the infected system.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Kasidet](https://attack.mitre.org/software/S0088) has the ability to initiate keylogging and screen captures.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Kasidet](https://attack.mitre.org/software/S0088) has the ability to download and execute additional files.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Kasidet](https://attack.mitre.org/software/S0088) has the ability to search for a given filename on a victim.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Kasidet](https://attack.mitre.org/software/S0088) has the ability to initiate keylogging.[^1]  |




## References

[^1]: [Zscaler Kasidet](http://research.zscaler.com/2016/01/malicious-office-files-dropping-kasidet.html)


[^2]: [Microsoft Kasidet](http://www.microsoft.com/security/portal/threat/encyclopedia/entry.aspx?Name=Win32%2FKasidet)


