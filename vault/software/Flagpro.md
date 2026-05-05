---
aliases: 
    - S0696
    
mitre-attack: https://attack.mitre.org/software/S0696
---

## S0696

[Flagpro](https://attack.mitre.org/software/S0696) is a Windows-based, first-stage downloader that has been used by [BlackTech](https://attack.mitre.org/groups/G0098) since at least October 2020. It has primarily been used against defense, media, and communications companies in Japan.[^1]  

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Flagpro](https://attack.mitre.org/software/S0696) has encoded bidirectional data communications between a target system and C2 server using Base64.[^1]   |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [Flagpro](https://attack.mitre.org/software/S0696) can check the name of the window displayed on the system.[^1]   |
| [[Scheduled Transfer\|T1029]] | Scheduled Transfer | [Flagpro](https://attack.mitre.org/software/S0696) has the ability to wait for a specified time interval between communicating with and executing commands from C2.[^1]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [Flagpro](https://attack.mitre.org/software/S0696) can check whether the target system is using Japanese, Taiwanese, or English through detection of specific Windows Security and Internet Explorer dialog.[^1]   |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Flagpro](https://attack.mitre.org/software/S0696) can execute malicious VBA macros embedded in .xlsm files.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Flagpro](https://attack.mitre.org/software/S0696) can use `cmd.exe` to execute commands received from C2.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Flagpro](https://attack.mitre.org/software/S0696) has been delivered within ZIP or RAR password-protected archived files.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Flagpro](https://attack.mitre.org/software/S0696) can collect data from a compromised host, including Windows authentication information.[^1]  |
| [[Masquerading\|T1036]] | Masquerading | [Flagpro](https://attack.mitre.org/software/S0696) can download malicious files with a .tmp extension and append them with .exe prior to execution.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Flagpro](https://attack.mitre.org/software/S0696) has relied on users clicking a malicious attachment delivered through spearphishing.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Flagpro](https://attack.mitre.org/software/S0696) can download additional malware from the C2 server.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Flagpro](https://attack.mitre.org/software/S0696) has dropped an executable file to the startup directory.[^1]   |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Flagpro](https://attack.mitre.org/software/S0696) can communicate with its C2 using HTTP.[^1]   |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Flagpro](https://attack.mitre.org/software/S0696) has been used to execute `net view` on a targeted system.[^1]   |
| [[Local Groups\|T1069.001]] | Local Groups | [Flagpro](https://attack.mitre.org/software/S0696) has been used to execute the `net localgroup administrators` command on a targeted system.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Flagpro](https://attack.mitre.org/software/S0696) has exfiltrated data to the C2 server.[^1]   |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Flagpro](https://attack.mitre.org/software/S0696) has been used to run the `whoami` command on the system.[^1]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Flagpro](https://attack.mitre.org/software/S0696) has been used to execute `net view` to discover mapped network shares.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Flagpro](https://attack.mitre.org/software/S0696) has been used to execute the `ipconfig /all` command on a victim system.[^1]  |
| [[Native API\|T1106]] | Native API | [Flagpro](https://attack.mitre.org/software/S0696) can use Native API to enable obfuscation including `GetLastError` and `GetTickCount`.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Flagpro](https://attack.mitre.org/software/S0696) has been distributed via spearphishing as an email attachment.[^1]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [Flagpro](https://attack.mitre.org/software/S0696) can close specific Windows Security and Internet Explorer dialog boxes to mask external connections.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Flagpro](https://attack.mitre.org/software/S0696) has been used to execute `netstat -ano` on a compromised host.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Flagpro](https://attack.mitre.org/software/S0696) has been used to run the `tasklist` command on a compromised system.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[BlackTech\|G0098]] | BlackTech |



## References

[^1]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)


