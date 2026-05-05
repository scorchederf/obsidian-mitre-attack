---
aliases: 
    - S0024
    
mitre-attack: https://attack.mitre.org/software/S0024
---

## S0024

[Dyre](https://attack.mitre.org/software/S0024) is a banking Trojan that has been used for financial gain. <br> [^4] [^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Dyre](https://attack.mitre.org/software/S0024) has the ability to identify network settings on a compromised host.[^5]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Dyre](https://attack.mitre.org/software/S0024) has the ability to identify the users on a compromised host.[^5]  |
| [[System Checks\|T1497.001]] | System Checks | [Dyre](https://attack.mitre.org/software/S0024) can detect sandbox analysis environments by inspecting the process list and Registry.[^4] [^5]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Dyre](https://attack.mitre.org/software/S0024) has the ability to create files in a TEMP folder to act as a database to store information.[^5]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Dyre](https://attack.mitre.org/software/S0024) has a command to download and executes additional files.[^4]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Dyre](https://attack.mitre.org/software/S0024) injects into other processes to load modules.[^4]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Dyre](https://attack.mitre.org/software/S0024) has the ability to achieve persistence by adding a new task in the task scheduler to run every minute.[^5]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Dyre](https://attack.mitre.org/software/S0024) decrypts resources needed for targeting the victim.[^4] [^5]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Dyre](https://attack.mitre.org/software/S0024) uses HTTPS for C2 communications.[^4] [^5] 	  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Dyre](https://attack.mitre.org/software/S0024) has the ability to identify the computer name, OS version, and hardware configuration on a compromised host.[^5]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Dyre](https://attack.mitre.org/software/S0024) has been delivered with encrypted resources and must be unpacked for execution.[^5]  |
| [[Process Injection\|T1055]] | Process Injection | [Dyre](https://attack.mitre.org/software/S0024) has the ability to directly inject its code into the web browser process.[^5]  |
| [[Software Discovery\|T1518]] | Software Discovery | [Dyre](https://attack.mitre.org/software/S0024) has the ability to identify installed programs on a compromised host.[^5]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Dyre](https://attack.mitre.org/software/S0024) registers itself as a service by adding several Registry keys.[^4]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Dyre](https://attack.mitre.org/software/S0024) has the ability to send information staged on a compromised host externally to C2.[^5]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Dyre](https://attack.mitre.org/software/S0024) has the ability to identify running services on a compromised host.[^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Wizard Spider\|G0102]] | Wizard Spider |



## References

[^1]: [Sophos Dyreza April 2015](https://nakedsecurity.sophos.com/2015/04/20/notes-from-sophoslabs-dyreza-the-malware-that-discriminates-against-old-computers/)


[^2]: [Malwarebytes TrickBot Sep 2019](https://blog.malwarebytes.com/trojans/2019/09/trickbot-adds-new-trick-to-its-arsenal-tampering-with-trusted-texts/)


[^3]: [CrowdStrike Wizard Spider March 2019](https://www.crowdstrike.com/blog/wizard-spider-lunar-spider-shared-proxy-module/)


[^4]: [Symantec Dyre June 2015](http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/dyre-emerging-threat.pdf)


[^5]: [Malwarebytes Dyreza November 2015](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)


[^6]: Dyre


[^7]: [Forbes Dyre May 2017](https://www.forbes.com/sites/thomasbrewster/2017/05/04/dyre-hackers-stealing-millions-from-american-coporates/#601c77842a0a)


[^8]: Dyreza


[^9]: Dyzap


