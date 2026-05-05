---
aliases: 
    - S0261
    
mitre-attack: https://attack.mitre.org/software/S0261
---

## S0261

[Catchamas](https://attack.mitre.org/software/S0261) is a Windows Trojan that steals information from compromised systems. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Modify Registry\|T1112]] | Modify Registry | [Catchamas](https://attack.mitre.org/software/S0261) creates three Registry keys to establish persistence by adding a [Windows Service](https://attack.mitre.org/techniques/T1543/003).[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Catchamas](https://attack.mitre.org/software/S0261) collects keystrokes from the victim’s machine.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Catchamas](https://attack.mitre.org/software/S0261) adds a new service named NetAdapter to establish persistence.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Catchamas](https://attack.mitre.org/software/S0261) gathers the Mac address, IP address, and the network adapter information from the victim’s machine.[^1]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [Catchamas](https://attack.mitre.org/software/S0261) steals data stored in the clipboard.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Catchamas](https://attack.mitre.org/software/S0261) stores the gathered data from the machine in .db files and .bmp files under four separate locations.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Catchamas](https://attack.mitre.org/software/S0261) adds a new service named NetAdapter in an apparent attempt to masquerade as a legitimate service.[^1]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [Catchamas](https://attack.mitre.org/software/S0261) obtains application windows titles and then determines which windows to perform [Screen Capture](https://attack.mitre.org/techniques/T1113) on.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Catchamas](https://attack.mitre.org/software/S0261) captures screenshots based on specific keywords in the window’s title.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Thrip\|G0076]] | Thrip |



## References

[^1]: [Symantec Catchamas April 2018](https://web.archive.org/web/20190508165711/https://www-west.symantec.com/content/symantec/english/en/security-center/writeup.html/2018-040209-1742-99)


[^2]: Catchamas


[^3]: [Symantec Thrip June 2018](https://www.symantec.com/blogs/threat-intelligence/thrip-hits-satellite-telecoms-defense-targets)


