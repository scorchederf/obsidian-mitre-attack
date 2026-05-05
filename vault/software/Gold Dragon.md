---
aliases: 
    - S0249
    
mitre-attack: https://attack.mitre.org/software/S0249
---

## S0249

[Gold Dragon](https://attack.mitre.org/software/S0249) is a Korean-language, data gathering implant that was first observed in the wild in South Korea in July 2017. [Gold Dragon](https://attack.mitre.org/software/S0249) was used along with [Brave Prince](https://attack.mitre.org/software/S0252) and [RunningRAT](https://attack.mitre.org/software/S0253) in operations targeting organizations associated with the 2018 Pyeongchang Winter Olympics. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Gold Dragon](https://attack.mitre.org/software/S0249) terminates anti-malware processes if they’re found running on the system.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Gold Dragon](https://attack.mitre.org/software/S0249) deletes one of its files, 2.hwp, from the endpoint after establishing persistence.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Gold Dragon](https://attack.mitre.org/software/S0249) collects the endpoint victim's username and uses it as a basis for downloading additional components from the C2 server.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Gold Dragon](https://attack.mitre.org/software/S0249) can download additional components from the C2 server.[^2]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Gold Dragon](https://attack.mitre.org/software/S0249) stores information gathered from the endpoint in a file named 1.hwp.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Gold Dragon](https://attack.mitre.org/software/S0249) establishes persistence in the Startup folder.[^2]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Gold Dragon](https://attack.mitre.org/software/S0249) encrypts data using Base64 before being sent to the command and control server.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Gold Dragon](https://attack.mitre.org/software/S0249) checks the running processes on the victim’s machine.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Gold Dragon](https://attack.mitre.org/software/S0249) lists the directories for Desktop, program files, and the user’s recently accessed files.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Gold Dragon](https://attack.mitre.org/software/S0249) uses cmd.exe to execute commands for discovery.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Gold Dragon](https://attack.mitre.org/software/S0249) collects endpoint information using the `systeminfo` command.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Gold Dragon](https://attack.mitre.org/software/S0249) uses HTTP for communication to the control servers.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Gold Dragon](https://attack.mitre.org/software/S0249) checks for anti-malware products and processes.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [Gold Dragon](https://attack.mitre.org/software/S0249) enumerates registry keys with the command `regkeyenum` and obtains information for the Registry key `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Kimsuky\|G0094]] | Kimsuky |



## References

[^1]: [Talos Kimsuky Nov 2021](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)


[^2]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)


[^3]: Gold Dragon


[^4]: [Mandiant APT43 March 2024](https://services.google.com/fh/files/misc/apt43-report-en.pdf)


