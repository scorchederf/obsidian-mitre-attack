---
aliases: 
    - S0271
    
mitre-attack: https://attack.mitre.org/software/S0271
---

## S0271

[KEYMARBLE](https://attack.mitre.org/software/S0271) is a Trojan that has reportedly been used by the North Korean government. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [KEYMARBLE](https://attack.mitre.org/software/S0271) gathers the MAC address of the victim’s machine.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [KEYMARBLE](https://attack.mitre.org/software/S0271) can obtain a list of running processes on the system.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [KEYMARBLE](https://attack.mitre.org/software/S0271) can execute shell commands using cmd.exe.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [KEYMARBLE](https://attack.mitre.org/software/S0271) has a command to search for files on the victim’s machine.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [KEYMARBLE](https://attack.mitre.org/software/S0271) can upload files to the victim’s machine and can download additional payloads.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [KEYMARBLE](https://attack.mitre.org/software/S0271) has the capability to collect the computer name, language settings, the OS version, CPU information, and time elapsed since system start.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [KEYMARBLE](https://attack.mitre.org/software/S0271) has the capability to collect information on disk devices.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [KEYMARBLE](https://attack.mitre.org/software/S0271) can capture screenshots of the victim’s machine.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [KEYMARBLE](https://attack.mitre.org/software/S0271) has a command to create Registry entries for storing data under `HKEY_CURRENT_USER\SOFTWARE\Microsoft\WABE\DataPath`.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [KEYMARBLE](https://attack.mitre.org/software/S0271) uses a customized XOR algorithm to encrypt C2 communications.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [KEYMARBLE](https://attack.mitre.org/software/S0271) has the capability to delete files off the victim’s machine.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: [US-CERT KEYMARBLE Aug 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)


[^2]: KEYMARBLE


