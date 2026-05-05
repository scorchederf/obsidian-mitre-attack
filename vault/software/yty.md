---
aliases: 
    - S0248
    
mitre-attack: https://attack.mitre.org/software/S0248
---

## S0248

[yty](https://attack.mitre.org/software/S0248) is a modular, plugin-based malware framework. The components of the framework are written in a variety of programming languages. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [yty](https://attack.mitre.org/software/S0248) gathers the the serial number of the main disk volume.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [yty](https://attack.mitre.org/software/S0248) gathers information on victim’s drives and has a plugin for document listing.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [yty](https://attack.mitre.org/software/S0248) establishes persistence by creating a scheduled task with the command `SchTasks /Create /SC DAILY /TN BigData /TR “ + path_file + “/ST 09:30“`.[^2]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [yty](https://attack.mitre.org/software/S0248) communicates to the C2 server by retrieving a Google Doc.[^2]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [yty](https://attack.mitre.org/software/S0248) contains junk code in its binary, likely to confuse malware analysts.[^2]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [yty](https://attack.mitre.org/software/S0248) uses the `net view` command for discovery.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [yty](https://attack.mitre.org/software/S0248) collects files with the following extensions: .ppt, .pptx, .pdf, .doc, .docx, .xls, .xlsx, .docm, .rtf, .inp, .xlsm, .csv, .odt, .pps, .vcf and sends them back to the C2 server.[^2]  |
| [[System Checks\|T1497.001]] | System Checks | [yty](https://attack.mitre.org/software/S0248) has some basic anti-sandbox detection that tries to detect Virtual PC, Sandboxie, and VMware. [^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [yty](https://attack.mitre.org/software/S0248) gets an output of running processes using the `tasklist` command.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [yty](https://attack.mitre.org/software/S0248) collects the victim’s username.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [yty](https://attack.mitre.org/software/S0248) gathers the computer name, CPU information, Microsoft Windows version, and runs the command `systeminfo`.[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [yty](https://attack.mitre.org/software/S0248) uses a keylogger plugin to gather keystrokes.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [yty](https://attack.mitre.org/software/S0248) collects screenshots of the victim machine.[^2]  |
| [[Software Packing\|T1027.002]] | Software Packing | [yty](https://attack.mitre.org/software/S0248) packs a plugin with UPX.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [yty](https://attack.mitre.org/software/S0248) runs `ipconfig /all` and collects the domain name.[^2]  |




## References

[^1]: yty


[^2]: [ASERT Donot March 2018](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)


