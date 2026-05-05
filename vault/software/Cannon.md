---
aliases: 
    - S0351
    
mitre-attack: https://attack.mitre.org/software/S0351
---

## S0351

[Cannon](https://attack.mitre.org/software/S0351) is a Trojan with variants written in C# and Delphi. It was first observed in April 2018. [^1] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [Cannon](https://attack.mitre.org/software/S0351) can obtain a list of processes running on the system.[^1] [^3]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Cannon](https://attack.mitre.org/software/S0351) can gather drive information from the victim's machine.[^1] [^3]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Cannon](https://attack.mitre.org/software/S0351) can take a screenshot of the desktop.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Cannon](https://attack.mitre.org/software/S0351) can gather the username from the system.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Cannon](https://attack.mitre.org/software/S0351) exfiltrates collected data over email via SMTP/S and POP3/S C2 channels.[^1]  |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [Cannon](https://attack.mitre.org/software/S0351) uses SMTP/S and POP3/S for C2 communications by sending and receiving emails.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Cannon](https://attack.mitre.org/software/S0351) can collect the current time zone information from the victim’s machine.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Cannon](https://attack.mitre.org/software/S0351) can obtain victim drive information as well as a list of folders in C:\Program Files.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Cannon](https://attack.mitre.org/software/S0351) can download a payload for execution.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Cannon](https://attack.mitre.org/software/S0351) can gather system information from the victim’s machine such as the OS version, and machine name.[^1] [^3]  |
| [[Winlogon Helper DLL\|T1547.004]] | Winlogon Helper DLL | [Cannon](https://attack.mitre.org/software/S0351) adds the Registry key `HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon` to establish persistence.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT28\|G0007]] | APT28 |



## References

[^1]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)


[^2]: Cannon


[^3]: [Unit42 Sofacy Dec 2018](https://unit42.paloaltonetworks.com/dear-joohn-sofacy-groups-global-campaign/)


