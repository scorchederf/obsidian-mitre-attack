---
aliases: 
    - S0171
    
mitre-attack: https://attack.mitre.org/software/S0171
---

## S0171

[Felismus](https://attack.mitre.org/software/S0171) is a modular backdoor that has been used by [Sowbug](https://attack.mitre.org/groups/G0054). [^2]  [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Felismus](https://attack.mitre.org/software/S0171) has masqueraded as legitimate Adobe Content Management System files.[^3]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Felismus](https://attack.mitre.org/software/S0171) collects the current username and sends it to the C2 server.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Felismus](https://attack.mitre.org/software/S0171) uses HTTP for C2.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Felismus](https://attack.mitre.org/software/S0171) checks for processes associated with anti-virus vendors.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Felismus](https://attack.mitre.org/software/S0171) collects the system information, including hostname and OS version, and sends it to the C2 server.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | Some [Felismus](https://attack.mitre.org/software/S0171) samples use a custom method for C2 traffic that utilizes Base64.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Felismus](https://attack.mitre.org/software/S0171) collects the victim LAN IP address and sends it to the C2 server.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Felismus](https://attack.mitre.org/software/S0171) can download files from remote servers.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | Some [Felismus](https://attack.mitre.org/software/S0171) samples use a custom encryption method for C2 traffic that utilizes AES and multiple keys.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Felismus](https://attack.mitre.org/software/S0171) uses command line for execution.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Sowbug\|G0054]] | Sowbug |



## References

[^1]: [Forcepoint Felismus Mar 2017](https://blogs.forcepoint.com/security-labs/playing-cat-mouse-introducing-felismus-malware)


[^2]: [Symantec Sowbug Nov 2017](https://www.symantec.com/connect/blogs/sowbug-cyber-espionage-group-targets-south-american-and-southeast-asian-governments)


[^3]: [ATT Felismus](https://levelblue.com/blogs/security-essentials/the-felismus-rat-powerful-threat-mysterious-purpose)


[^4]: Felismus


