---
aliases: 
    - S0605
    
mitre-attack: https://attack.mitre.org/software/S0605
---

## S0605

[EKANS](https://attack.mitre.org/software/S0605) is ransomware variant written in Golang that first appeared in mid-December 2019 and has been used against multiple sectors, including energy, healthcare, and automotive manufacturing, which in some cases resulted in significant operational disruptions. [EKANS](https://attack.mitre.org/software/S0605) has used a hard-coded kill-list of processes, including some associated with common ICS software platforms (e.g., GE Proficy, Honeywell HMIWeb, etc), similar to those defined in [MegaCortex](https://attack.mitre.org/software/S0576).[^4] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [EKANS](https://attack.mitre.org/software/S0605) looks for processes from a hard-coded list.[^4] [^1] [^6]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [EKANS](https://attack.mitre.org/software/S0605) uses standard encryption library functions to encrypt files.[^4] [^3]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [EKANS](https://attack.mitre.org/software/S0605) removes backups of Volume Shadow Copies to disable any restoration capabilities.[^4] [^3]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [EKANS](https://attack.mitre.org/software/S0605) can use Windows Mangement Instrumentation (WMI) calls to execute operations.[^4]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [EKANS](https://attack.mitre.org/software/S0605) can determine the domain of a compromised host.[^6]  |
| [[Service Stop\|T1489]] | Service Stop | [EKANS](https://attack.mitre.org/software/S0605) stops database, data backup solution, antivirus, and ICS-related processes.[^4] [^1] [^3]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [EKANS](https://attack.mitre.org/software/S0605) uses encoded strings in its process kill list.[^1]   |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [EKANS](https://attack.mitre.org/software/S0605) has been disguised as `update.exe` to appear as a valid executable.[^4]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [EKANS](https://attack.mitre.org/software/S0605) stops processes related to security and management software.[^4] [^1]  |




## References

[^1]: [FireEye Ransomware Feb 2020](https://www.fireeye.com/blog/threat-research/2020/02/ransomware-against-machine-learning-to-disrupt-industrial-production.html)


[^2]: SNAKEHOSE


[^3]: [Palo Alto Unit 42 EKANS](https://unit42.paloaltonetworks.com/threat-assessment-ekans-ransomware/)


[^4]: [Dragos EKANS](https://www.dragos.com/blog/industry-news/ekans-ransomware-and-ics-operations/)


[^5]: EKANS


[^6]: [IBM Ransomware Trends September 2020](https://securityintelligence.com/posts/ransomware-2020-attack-trends-new-techniques-affecting-organizations-worldwide/)


