---
aliases: 
    - S0086
    
mitre-attack: https://attack.mitre.org/software/S0086
---

## S0086

[ZLib](https://attack.mitre.org/software/S0086) is a full-featured backdoor that was used as a second-stage implant during [Operation Dust Storm](https://attack.mitre.org/campaigns/C0016) since at least 2014. [ZLib](https://attack.mitre.org/software/S0086) is malware and should not be confused with the legitimate compression library from which its name is derived.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [ZLib](https://attack.mitre.org/software/S0086) has the ability to download files.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [ZLib](https://attack.mitre.org/software/S0086) has the ability to enumerate system information.[^1]  |
| [[Archive via Library\|T1560.002]] | Archive via Library | The [ZLib](https://attack.mitre.org/software/S0086) backdoor compresses communications using the standard Zlib compression library.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [ZLib](https://attack.mitre.org/software/S0086) creates Registry keys to allow itself to run as various services.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [ZLib](https://attack.mitre.org/software/S0086) has the ability to enumerate files and drives.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [ZLib](https://attack.mitre.org/software/S0086) has the ability to obtain screenshots of the compromised system.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [ZLib](https://attack.mitre.org/software/S0086) has the ability to execute shell commands.[^1]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [ZLib](https://attack.mitre.org/software/S0086) has the ability to discover and manipulate Windows services.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [ZLib](https://attack.mitre.org/software/S0086) has sent data and files from a compromised host to its C2 servers.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [ZLib](https://attack.mitre.org/software/S0086) communicates over HTTP for C2.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [ZLib](https://attack.mitre.org/software/S0086) mimics the resource version information of legitimate Realtek Semiconductor, Nvidia, or Synaptics modules.[^1]  |




## References

[^1]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)


