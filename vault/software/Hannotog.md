---
aliases: 
    - S1211
    
mitre-attack: https://attack.mitre.org/software/S1211
---

## S1211

[Hannotog](https://attack.mitre.org/software/S1211) is a type of backdoor malware uniquely assoicated with [Lotus Blossom](https://attack.mitre.org/groups/G0030) operations since at least 2022.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [Hannotog](https://attack.mitre.org/software/S1211) uses non-standard listening ports, such as UDP 5900, for command and control purposes.[^1]  |
| [[Service Stop\|T1489]] | Service Stop | [Hannotog](https://attack.mitre.org/software/S1211) can stop Windows services.[^1]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [Hannotog](https://attack.mitre.org/software/S1211) can upload encyrpted data for exfiltration.[^1]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [Hannotog](https://attack.mitre.org/software/S1211) can modify local firewall settings via `netsh` commands to open a listening UDP port.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Hannotog](https://attack.mitre.org/software/S1211) creates a new service for persistence.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Hannotog](https://attack.mitre.org/software/S1211) can execute various `cmd.exe /c %s` commands.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Hannotog](https://attack.mitre.org/software/S1211) can download additional files to the victim machine.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lotus Blossom\|G0030]] | Lotus Blossom |



## References

[^1]: [Symantec Bilbug 2022](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)


