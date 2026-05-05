---
aliases: 
    - S0149
    
mitre-attack: https://attack.mitre.org/software/S0149
---

## S0149

[MoonWind](https://attack.mitre.org/software/S0149) is a remote access tool (RAT) that was used in 2016 to target organizations in Thailand. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Keylogging\|T1056.001]] | Keylogging | [MoonWind](https://attack.mitre.org/software/S0149) has a keylogger.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [MoonWind](https://attack.mitre.org/software/S0149) has a command to return a list of running processes.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [MoonWind](https://attack.mitre.org/software/S0149) installs itself as a new service with automatic startup to establish persistence. The service checks every 60 seconds to determine if the malware is running; if not, it will spawn a new instance.[^1]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [MoonWind](https://attack.mitre.org/software/S0149) communicates over ports 80, 443, 53, and 8080 via raw sockets instead of the protocols usually associated with the ports.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [MoonWind](https://attack.mitre.org/software/S0149) completes network communication via raw sockets.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [MoonWind](https://attack.mitre.org/software/S0149) has a command to return a directory listing for a specified directory.[^1]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [MoonWind](https://attack.mitre.org/software/S0149) obtains the number of removable drives from the victim.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [MoonWind](https://attack.mitre.org/software/S0149) encrypts C2 traffic using RC4 with a static key.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [MoonWind](https://attack.mitre.org/software/S0149) can execute commands via an interactive command shell.[^1]  [MoonWind](https://attack.mitre.org/software/S0149) uses batch scripts for various purposes, including to restart and uninstall itself.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [MoonWind](https://attack.mitre.org/software/S0149) can obtain the victim hostname, Windows version, RAM amount, and screen resolution.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [MoonWind](https://attack.mitre.org/software/S0149) can delete itself or specified files.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [MoonWind](https://attack.mitre.org/software/S0149) obtains the victim's current time.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [MoonWind](https://attack.mitre.org/software/S0149) obtains the victim username.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [MoonWind](https://attack.mitre.org/software/S0149) saves information from its keylogging routine as a .zip file in the present working directory.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [MoonWind](https://attack.mitre.org/software/S0149) obtains the victim IP address.[^1]  |




## References

[^1]: [Palo Alto MoonWind March 2017](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)


