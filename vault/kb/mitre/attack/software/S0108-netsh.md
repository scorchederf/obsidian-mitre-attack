---
aliases: 
    - S0108
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0108-netsh
---

## Description

[[kb/mitre/attack/software/S0108-netsh\|netsh]] is a scripting utility used to interact with networking components on local or remote systems. [^4] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1090-Proxy\|T1090]] | Proxy | [[kb/mitre/attack/software/S0108-netsh\|netsh]] can be used to set up a proxy tunnel to allow remote host access to an infected host.[^1]  |
| [[kb/mitre/attack/techniques/T1518.001-Security_Software_Discovery\|T1518.001]] | Security Software Discovery | [[kb/mitre/attack/software/S0108-netsh\|netsh]] can be used to discover system firewall settings.[^4] [^3]  |
| [[kb/mitre/attack/techniques/T1546.007-Netsh_Helper_DLL\|T1546.007]] | Netsh Helper DLL | [[kb/mitre/attack/software/S0108-netsh\|netsh]] can be used as a persistence proxy technique to execute a helper DLL when netsh.exe is executed.[^2]  |
| [[kb/mitre/attack/techniques/T1686-Disable_or_Modify_System_Firewall\|T1686]] | Disable or Modify System Firewall | [[kb/mitre/attack/software/S0108-netsh\|netsh]] can be used to disable local firewall settings.[^4] [^3]  |





> [!info]- References
> [^1]: [Securelist fileless attacks Feb 2017](https://securelist.com/fileless-attacks-against-enterprise-networks/77403/)

> [^2]: [Demaske Netsh Persistence](https://htmlpreview.github.io/?https://github.com/MatthewDemaske/blogbackup/blob/master/netshell.html)

> [^3]: [TechNet Netsh Firewall](https://technet.microsoft.com/en-us/library/cc771046(v=ws.10).aspx)

> [^4]: [TechNet Netsh](https://technet.microsoft.com/library/bb490939.aspx)


