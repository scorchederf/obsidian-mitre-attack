---
aliases: 
    - S1191
    
mitre-attack: https://attack.mitre.org/software/S1191
---

## S1191

[Megazord](https://attack.mitre.org/software/S1191) is a Rust-based variant of [Akira](https://attack.mitre.org/software/S1129) ransomware that has been in use since at least August 2023 to target Windows environments. [Megazord](https://attack.mitre.org/software/S1191) has been attributed to the [Akira](https://attack.mitre.org/groups/G1024) group based on overlapping infrastructure though is possibly not exclusive to the group.[^3] [^2] [^1] <br><br>

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | <br>[Megazord](https://attack.mitre.org/software/S1191) can execute multiple commands post infection via `cmd.exe`.[^1]  |
| [[Service Stop\|T1489]] | Service Stop | [Megazord](https://attack.mitre.org/software/S1191) has the ability to terminate a list of services and processes.[^1]  |
| [[Log Enumeration\|T1654]] | Log Enumeration | [Megazord](https://attack.mitre.org/software/S1191) has the ability to print the trace, debug, error, info, and warning logs.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Megazord](https://attack.mitre.org/software/S1191) can terminate a list of specified services and processes.[^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Megazord](https://attack.mitre.org/software/S1191) can encrypt files on targeted Windows hosts leaving them with a  ".powerranges" file extension.[^3] [^2] [^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Megazord](https://attack.mitre.org/software/S1191) can ignore specified directories for encryption.[^1] <br> |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Akira\|G1024]] | Akira |



## References

[^1]: [Palo Alto Howling Scorpius DEC 2024](https://unit42.paloaltonetworks.com/threat-assessment-howling-scorpius-akira-ransomware/)


[^2]: [Cisco Akira Ransomware OCT 2024](https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/)


[^3]: [CISA Akira Ransomware APR 2024](https://www.cisa.gov/sites/default/files/2024-04/aa24-109a-stopransomware-akira-ransomware_2.pdf)


