---
aliases: 
    - S0242
    
mitre-attack: https://attack.mitre.org/software/S0242
---

## S0242

[SynAck](https://attack.mitre.org/software/S0242) is variant of Trojan ransomware targeting mainly English-speaking users since at least fall 2017. [^1]  [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [SynAck](https://attack.mitre.org/software/S0242) checks its directory location in an attempt to avoid launching in a sandbox.[^1] [^3]  |
| [[Modify Registry\|T1112]] | Modify Registry | [SynAck](https://attack.mitre.org/software/S0242) can manipulate Registry keys.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [SynAck](https://attack.mitre.org/software/S0242) payloads are obfuscated prior to compilation to inhibit analysis and/or reverse engineering.[^1] [^3]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [SynAck](https://attack.mitre.org/software/S0242) gathers user names from infected hosts.[^1]  |
| [[System Checks\|T1497.001]] | System Checks | [SynAck](https://attack.mitre.org/software/S0242) checks its directory location in an attempt to avoid launching in a sandbox.[^1] [^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SynAck](https://attack.mitre.org/software/S0242) gathers computer names, OS version info, and also checks installed keyboard layouts to estimate if it has been launched from a certain list of countries.[^1]  |
| [[Process Doppelgänging\|T1055.013]] | Process Doppelgänging | [SynAck](https://attack.mitre.org/software/S0242) abuses NTFS transactions to launch and conceal malicious processes.[^1] [^3]  |
| [[Native API\|T1106]] | Native API | [SynAck](https://attack.mitre.org/software/S0242) parses the export tables of system DLLs to locate and call various Windows API functions.[^1] [^3]  |
| [[Query Registry\|T1012]] | Query Registry | [SynAck](https://attack.mitre.org/software/S0242) enumerates Registry keys associated with event logs.[^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [SynAck](https://attack.mitre.org/software/S0242) encrypts the victims machine followed by asking the victim to pay a ransom. [^1]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [SynAck](https://attack.mitre.org/software/S0242) enumerates all running services.[^1] [^3]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [SynAck](https://attack.mitre.org/software/S0242) clears event logs.[^1]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [SynAck](https://attack.mitre.org/software/S0242) lists all the keyboard layouts installed on the victim’s system using `GetKeyboardLayoutList` API and checks against a hardcoded language code list. If a match if found, SynAck sleeps for 300 seconds and then exits without encrypting files.[^1]   |
| [[Process Discovery\|T1057]] | Process Discovery | [SynAck](https://attack.mitre.org/software/S0242) enumerates all running processes.[^1] [^3]  |




## References

[^1]: [SecureList SynAck Doppelgänging May 2018](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)


[^2]: SynAck


[^3]: [Kaspersky Lab SynAck May 2018](https://usa.kaspersky.com/about/press-releases/2018_synack-doppelganging)


