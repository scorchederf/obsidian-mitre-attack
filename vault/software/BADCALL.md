---
aliases: 
    - S0245
    
mitre-attack: https://attack.mitre.org/software/S0245
---

## S0245

[BADCALL](https://attack.mitre.org/software/S0245) is a Trojan malware variant used by the group [Lazarus Group](https://attack.mitre.org/groups/G0032). [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Host Firewall\|T1686.003]] | Windows Host Firewall | [BADCALL](https://attack.mitre.org/software/S0245) disables the Windows firewall before binding to a port.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [BADCALL](https://attack.mitre.org/software/S0245) encrypts C2 traffic using an XOR/ADD cipher.[^2]  |
| [[Protocol or Service Impersonation\|T1001.003]] | Protocol or Service Impersonation | [BADCALL](https://attack.mitre.org/software/S0245) uses a FakeTLS method during C2.[^1]  |
| [[Proxy\|T1090]] | Proxy | [BADCALL](https://attack.mitre.org/software/S0245) functions as a proxy server between the victim and C2 server.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [BADCALL](https://attack.mitre.org/software/S0245) modifies the firewall Registry key `SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfileGloballyOpenPorts\\List`.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [BADCALL](https://attack.mitre.org/software/S0245) collects the computer name and host name on the compromised system.[^2]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [BADCALL](https://attack.mitre.org/software/S0245) communicates on ports 443 and 8000 with a FakeTLS method.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [BADCALL](https://attack.mitre.org/software/S0245) collects the network adapter information.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: [Malware Analysis Report 10135536-G](https://web.archive.org/web/20200324152106/https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-G.PDF)


[^2]: [US-CERT BADCALL](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-G.PDF)


[^3]: BADCALL


