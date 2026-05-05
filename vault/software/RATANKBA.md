---
aliases: 
    - S0241
    
mitre-attack: https://attack.mitre.org/software/S0241
---

## S0241

[RATANKBA](https://attack.mitre.org/software/S0241) is a remote controller tool used by [Lazarus Group](https://attack.mitre.org/groups/G0032). [RATANKBA](https://attack.mitre.org/software/S0241) has been used in attacks targeting financial institutions in Poland, Mexico, Uruguay, the United Kingdom, and Chile. It was also seen used against organizations related to telecommunications, management consulting, information technology, insurance, aviation, and education. [RATANKBA](https://attack.mitre.org/software/S0241) has a graphical user interface to allow the attacker to issue jobs to perform on the infected machines. [^1]  [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [RATANKBA](https://attack.mitre.org/software/S0241) runs the `whoami` and `query user` commands.[^2]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [RATANKBA](https://attack.mitre.org/software/S0241) uses `netstat -ano` to search for specific IP address ranges.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [RATANKBA](https://attack.mitre.org/software/S0241) uses cmd.exe to execute commands.[^1] [^2]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [RATANKBA](https://attack.mitre.org/software/S0241) uses `tasklist /svc` to display running tasks.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [RATANKBA](https://attack.mitre.org/software/S0241) uses HTTP/HTTPS for command and control communication.[^1] [^2]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [RATANKBA](https://attack.mitre.org/software/S0241) performs a reflective DLL injection using a given pid.[^1] [^2]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [RATANKBA](https://attack.mitre.org/software/S0241) uses WMI to perform process monitoring.[^1] [^2]  |
| [[Local Account\|T1087.001]] | Local Account | [RATANKBA](https://attack.mitre.org/software/S0241) uses the `net user` command.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [RATANKBA](https://attack.mitre.org/software/S0241) lists the system’s processes.[^1] [^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [RATANKBA](https://attack.mitre.org/software/S0241) gathers the victim’s IP address via the `ipconfig -all` command.[^1] [^2]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [RATANKBA](https://attack.mitre.org/software/S0241) runs the `net view /domain` and `net view` commands.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [RATANKBA](https://attack.mitre.org/software/S0241) uses the command `reg query “HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\InternetSettings”`.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [RATANKBA](https://attack.mitre.org/software/S0241) uploads and downloads information.[^1] [^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | There is a variant of [RATANKBA](https://attack.mitre.org/software/S0241) that uses a PowerShell script instead of the traditional PE form.[^1] [^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [RATANKBA](https://attack.mitre.org/software/S0241) gathers information about the OS architecture, OS name, and OS version/Service pack.[^1] [^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: [Lazarus RATANKBA](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-campaign-targeting-cryptocurrencies-reveals-remote-controller-tool-evolved-ratankba/)


[^2]: [RATANKBA](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)


