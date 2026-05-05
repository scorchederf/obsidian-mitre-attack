---
aliases: 
    - S1043
    
mitre-attack: https://attack.mitre.org/software/S1043
---

## S1043

[ccf32](https://attack.mitre.org/software/S1043) is data collection malware that has been used since at least February 2019, most notably during the [FunnyDream](https://attack.mitre.org/campaigns/C0007) campaign; there is also a similar x64 version.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data from Local System\|T1005]] | Data from Local System | [ccf32](https://attack.mitre.org/software/S1043) can collect files from a compromised host.[^1]  |
| [[Automated Collection\|T1119]] | Automated Collection | [ccf32](https://attack.mitre.org/software/S1043) can be used to automatically collect files from a compromised host.[^1]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [ccf32](https://attack.mitre.org/software/S1043) can upload collected data and files to an FTP server.[^1]  |
| [[Remote Data Staging\|T1074.002]] | Remote Data Staging | [ccf32](https://attack.mitre.org/software/S1043) has copied files to a remote machine infected with [Chinoxy](https://attack.mitre.org/software/S1041) or another backdoor.[^1]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [ccf32](https://attack.mitre.org/software/S1043) has used `xcopy \\<target_host>\c$\users\public\path.7z c:\users\public\bin\<target_host>.7z /H /Y` to archive collected files.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [ccf32](https://attack.mitre.org/software/S1043) has used `cmd.exe` for archiving data and deleting files.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [ccf32](https://attack.mitre.org/software/S1043) can determine the local time on targeted machines.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [ccf32](https://attack.mitre.org/software/S1043) can delete files and folders from compromised machines.[^1]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [ccf32](https://attack.mitre.org/software/S1043) has created a hidden directory on targeted systems, naming it after the current local time (year, month, and day).[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [ccf32](https://attack.mitre.org/software/S1043) can temporarily store files in a hidden directory on the local host.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [ccf32](https://attack.mitre.org/software/S1043) can run on a daily basis using a scheduled task.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [ccf32](https://attack.mitre.org/software/S1043) can parse collected files to identify specific file extensions.[^1]  |




## References

[^1]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)


