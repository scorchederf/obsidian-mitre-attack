---
aliases: 
    - S0237
    
mitre-attack: https://attack.mitre.org/software/S0237
---

## S0237

[GravityRAT](https://attack.mitre.org/software/S0237) is a remote access tool (RAT) and has been in ongoing development since 2016. The actor behind the tool remains unknown, but two usernames have been recovered that link to the author, which are "TheMartian" and "The Invincible." According to the National Computer Emergency Response Team (CERT) of India, the malware has been identified in attacks against organization and entities in India. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Indicator Removal from Tools\|T1027.005]] | Indicator Removal from Tools | The author of [GravityRAT](https://attack.mitre.org/software/S0237) submitted samples to VirusTotal for testing, showing that the author modified the code to try to hide the DDE object in a different part of the document.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [GravityRAT](https://attack.mitre.org/software/S0237) collects the MAC address, computer name, and CPU information.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [GravityRAT](https://attack.mitre.org/software/S0237) collects the victim IP address, MAC address, as well as the victim account domain name.[^2]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [GravityRAT](https://attack.mitre.org/software/S0237) uses the `netstat` command to find open ports on the victim’s machine.[^2]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [GravityRAT](https://attack.mitre.org/software/S0237) can obtain the date and time of a system.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [GravityRAT](https://attack.mitre.org/software/S0237) supports file encryption (AES with the key "lolomycin2017").[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [GravityRAT](https://attack.mitre.org/software/S0237) uses HTTP for C2.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [GravityRAT](https://attack.mitre.org/software/S0237) lists the running processes on the system.[^2]  |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | [GravityRAT](https://attack.mitre.org/software/S0237) steals files based on an extension list if a USB drive is connected to the system.[^2]  |
| [[System Checks\|T1497.001]] | System Checks | [GravityRAT](https://attack.mitre.org/software/S0237) uses WMI to check the BIOS and manufacturer information for strings like "VMWare", "Virtual", and "XEN" and another WMI request to get the current temperature of the hardware to determine if it's a virtual machine environment. [^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [GravityRAT](https://attack.mitre.org/software/S0237) creates a scheduled task to ensure it is re-executed everyday.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [GravityRAT](https://attack.mitre.org/software/S0237) collects the volumes mapped on the system, and also steals files with the following extensions: .docx, .doc, .pptx, .ppt, .xlsx, .xls, .rtf, and .pdf.[^2]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [GravityRAT](https://attack.mitre.org/software/S0237) has a feature to list the available services on the system.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [GravityRAT](https://attack.mitre.org/software/S0237) steals files with the following extensions: .docx, .doc, .pptx, .ppt, .xlsx, .xls, .rtf, and .pdf.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [GravityRAT](https://attack.mitre.org/software/S0237) executes commands remotely on the infected host.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [GravityRAT](https://attack.mitre.org/software/S0237) collects the victim username along with other account information (account type, description, full name, SID and status).[^2]  |
| [[Dynamic Data Exchange\|T1559.002]] | Dynamic Data Exchange | [GravityRAT](https://attack.mitre.org/software/S0237) has been delivered via Word documents using DDE for execution.[^2]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [GravityRAT](https://attack.mitre.org/software/S0237) has used HTTP over a non-standard port, such as TCP port 46769.[^2]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [GravityRAT](https://attack.mitre.org/software/S0237) collects various information via WMI requests, including CPU information in the Win32_Processor entry (Processor ID, Name, Manufacturer and the clock speed).[^2]  |




## References

[^1]: GravityRAT


[^2]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)


