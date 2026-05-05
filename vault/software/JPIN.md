---
aliases: 
    - S0201
    
mitre-attack: https://attack.mitre.org/software/S0201
---

## S0201

[JPIN](https://attack.mitre.org/software/S0201) is a custom-built backdoor family used by [PLATINUM](https://attack.mitre.org/groups/G0068). Evidence suggests developers of [JPIN](https://attack.mitre.org/software/S0201) and [Dipsind](https://attack.mitre.org/software/S0200) code bases were related in some way. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [JPIN](https://attack.mitre.org/software/S0201) can lower security settings by changing Registry keys.[^2]  |
| [[Windows Permissions\|T1222.001]] | Windows Permissions | [JPIN](https://attack.mitre.org/software/S0201) can use the command-line utility cacls.exe to change file permissions.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [JPIN](https://attack.mitre.org/software/S0201) can use the command-line utility cacls.exe to change file permissions.[^2]  |
| [[Local Groups\|T1069.001]] | Local Groups | [JPIN](https://attack.mitre.org/software/S0201) can obtain the permissions of the victim user.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [JPIN](https://attack.mitre.org/software/S0201) can obtain network information, including DNS, IP, and proxies.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [JPIN](https://attack.mitre.org/software/S0201) can list running processes.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [JPIN](https://attack.mitre.org/software/S0201)'s installer/uninstaller component deletes itself if it encounters a version of Windows earlier than Windows XP or identifies security-related processes running.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [JPIN](https://attack.mitre.org/software/S0201) can enumerate Registry keys.[^2]  |
| [[BITS Jobs\|T1197]] | BITS Jobs | A [JPIN](https://attack.mitre.org/software/S0201) variant downloads the backdoor payload via the BITS service.[^2]  |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [JPIN](https://attack.mitre.org/software/S0201) can send email over SMTP.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [JPIN](https://attack.mitre.org/software/S0201) can enumerate drives and their types. It can also change file permissions using cacls.exe.[^2]  |
| [[Process Injection\|T1055]] | Process Injection | [JPIN](https://attack.mitre.org/software/S0201) can inject content into lsass.exe to load a module.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [JPIN](https://attack.mitre.org/software/S0201) can download files and upgrade itself.[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [JPIN](https://attack.mitre.org/software/S0201) contains a custom keylogger.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [JPIN](https://attack.mitre.org/software/S0201) can obtain the victim user name.[^2]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [JPIN](https://attack.mitre.org/software/S0201) can communicate over FTP.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [JPIN](https://attack.mitre.org/software/S0201) checks for the presence of certain security-related processes and deletes its installer/uninstaller component if it identifies any of them.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [JPIN](https://attack.mitre.org/software/S0201) can obtain system information such as OS version and disk space.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | A [JPIN](https://attack.mitre.org/software/S0201) uses a encrypted and compressed payload that is disguised as a bitmap within the resource section of the installer.[^2]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [JPIN](https://attack.mitre.org/software/S0201) can list running services.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[PLATINUM\|G0068]] | PLATINUM |



## References

[^1]: JPIN


[^2]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)


