---
aliases: 
    - S0139
    
mitre-attack: https://attack.mitre.org/software/S0139
---

## S0139

[PowerDuke](https://attack.mitre.org/software/S0139) is a backdoor that was used by [APT29](https://attack.mitre.org/groups/G0016) in 2016. It has primarily been delivered through Microsoft Word or Excel attachments containing malicious macros. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [PowerDuke](https://attack.mitre.org/software/S0139) has a command to get the victim's domain and NetBIOS name.[^1]  |
| [[Steganography\|T1027.003]] | Steganography | [PowerDuke](https://attack.mitre.org/software/S0139) uses steganography to hide backdoors in PNG files, which are also encrypted using the Tiny Encryption Algorithm (TEA).[^1]   |
| [[Rundll32\|T1218.011]] | Rundll32 | [PowerDuke](https://attack.mitre.org/software/S0139) uses rundll32.exe to load.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [PowerDuke](https://attack.mitre.org/software/S0139) has commands to get information about the victim's name, build, version, serial number, and memory usage.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [PowerDuke](https://attack.mitre.org/software/S0139) has commands to get the current directory name as well as the size of a file. It also has commands to obtain information about logical drives, drive type, and free space.[^1]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [PowerDuke](https://attack.mitre.org/software/S0139) has a command to get text of the current foreground window.[^1]  |
| [[Data Destruction\|T1485]] | Data Destruction | [PowerDuke](https://attack.mitre.org/software/S0139) has a command to write random data across a file and delete it.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [PowerDuke](https://attack.mitre.org/software/S0139) has commands to get the current user's name and SID.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [PowerDuke](https://attack.mitre.org/software/S0139) has a command to list the victim's processes.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [PowerDuke](https://attack.mitre.org/software/S0139) has commands to get the time the machine was built, the time, and the time zone.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [PowerDuke](https://attack.mitre.org/software/S0139) has a command to write random data across a file and delete it.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [PowerDuke](https://attack.mitre.org/software/S0139) has a command to download a file.[^1]  |
| [[NTFS File Attributes\|T1564.004]] | NTFS File Attributes | [PowerDuke](https://attack.mitre.org/software/S0139) hides many of its backdoor payloads in an alternate data stream (ADS).[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [PowerDuke](https://attack.mitre.org/software/S0139) runs `cmd.exe /c` and sends the output to its C2.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [PowerDuke](https://attack.mitre.org/software/S0139) achieves persistence by using various Registry Run keys.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)


[^2]: PowerDuke


