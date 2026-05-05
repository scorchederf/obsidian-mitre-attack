---
aliases: 
    - S0671
    
mitre-attack: https://attack.mitre.org/software/S0671
---

## S0671

[Tomiris](https://attack.mitre.org/software/S0671) is a backdoor written in Go that continuously queries its C2 server for executables to download and execute on a victim system. It was first reported in September 2021 during an investigation of a successful DNS hijacking campaign against a Commonwealth of Independent States (CIS) member. Security researchers assess there are similarities between [Tomiris](https://attack.mitre.org/software/S0671) and [GoldMax](https://attack.mitre.org/software/S0588).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Dynamic Resolution\|T1568]] | Dynamic Resolution | [Tomiris](https://attack.mitre.org/software/S0671) has connected to a signalization server that provides a URL and port, and then [Tomiris](https://attack.mitre.org/software/S0671) sends a GET request to that URL to establish C2.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Tomiris](https://attack.mitre.org/software/S0671) can use HTTP to establish C2 communications.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Tomiris](https://attack.mitre.org/software/S0671) has used `SCHTASKS /CREATE /SC DAILY /TN StartDVL /TR "[path to self]" /ST 10:00` to establish persistence.[^1]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [Tomiris](https://attack.mitre.org/software/S0671) has the ability to sleep for at least nine minutes to evade sandbox-based analysis systems.[^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Tomiris](https://attack.mitre.org/software/S0671) has been packed with UPX.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Tomiris](https://attack.mitre.org/software/S0671) has the ability to collect recent files matching a hardcoded list of extensions prior to exfiltration.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Tomiris](https://attack.mitre.org/software/S0671) can download files and execute them on a victim's system.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel |  [Tomiris](https://attack.mitre.org/software/S0671) can upload files matching a hardcoded set of extensions, such as .doc, .docx, .pdf, and .rar, to its C2 server.[^1]  |




## References

[^1]: [Kaspersky Tomiris Sep 2021](https://securelist.com/darkhalo-after-solarwinds-the-tomiris-connection/104311/)


