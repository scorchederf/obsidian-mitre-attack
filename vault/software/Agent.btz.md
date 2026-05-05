---
aliases: 
    - S0092
    
mitre-attack: https://attack.mitre.org/software/S0092
---

## S0092

[Agent.btz](https://attack.mitre.org/software/S0092) is a worm that primarily spreads itself via removable devices such as USB drives. It reportedly infected U.S. military networks in 2008. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Agent.btz](https://attack.mitre.org/software/S0092) obtains the victim username and saves it to a file.[^2]  |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [Agent.btz](https://attack.mitre.org/software/S0092) drops itself onto removable media devices and creates an autorun.inf file with an instruction to run that file. When the device is inserted into another system, it opens autorun.inf and loads the malware.[^2]  |
| [[Exfiltration over USB\|T1052.001]] | Exfiltration over USB | [Agent.btz](https://attack.mitre.org/software/S0092) creates a file named thumb.dd on all USB flash drives connected to the victim. This file contains information about the infected system and activity logs.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Agent.btz](https://attack.mitre.org/software/S0092) collects the network adapter’s IP and MAC address as well as IP addresses of the network adapter’s default gateway, primary/secondary WINS, DHCP, and DNS servers, and saves them into a log file.[^2]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [Agent.btz](https://attack.mitre.org/software/S0092) saves system information into an XML file that is then XOR-encoded.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Agent.btz](https://attack.mitre.org/software/S0092) attempts to download an encrypted binary from a specified domain.[^2]  |




## References

[^1]: [Securelist Agent.btz](https://securelist.com/agent-btz-a-source-of-inspiration/58551/)


[^2]: [ThreatExpert Agent.btz](http://blog.threatexpert.com/2008/11/agentbtz-threat-that-hit-pentagon.html)


