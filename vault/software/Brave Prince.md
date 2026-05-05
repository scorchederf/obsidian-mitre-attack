---
aliases: 
    - S0252
    
mitre-attack: https://attack.mitre.org/software/S0252
---

## S0252

[Brave Prince](https://attack.mitre.org/software/S0252) is a Korean-language implant that was first observed in the wild in December 2017. It contains similar code and behavior to [Gold Dragon](https://attack.mitre.org/software/S0249), and was seen along with [Gold Dragon](https://attack.mitre.org/software/S0249) and [RunningRAT](https://attack.mitre.org/software/S0253) in operations surrounding the 2018 Pyeongchang Winter Olympics. [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Brave Prince](https://attack.mitre.org/software/S0252) collects hard drive content and system configuration information.[^3]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | Some [Brave Prince](https://attack.mitre.org/software/S0252) variants have used South  Korea's Daum email service to exfiltrate information, and later variants have posted the data to a web server via an HTTP post command.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Brave Prince](https://attack.mitre.org/software/S0252) lists the running processes.[^3]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Brave Prince](https://attack.mitre.org/software/S0252) terminates antimalware processes.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Brave Prince](https://attack.mitre.org/software/S0252) gathers file and directory information from the victim’s machine.[^3]  |
| [[Query Registry\|T1012]] | Query Registry | [Brave Prince](https://attack.mitre.org/software/S0252) gathers information about the Registry.[^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Brave Prince](https://attack.mitre.org/software/S0252) gathers network configuration information as well as the ARP cache.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Kimsuky\|G0094]] | Kimsuky |



## References

[^1]: [Talos Kimsuky Nov 2021](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)


[^2]: Brave Prince


[^3]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)


[^4]: [Mandiant APT43 March 2024](https://services.google.com/fh/files/misc/apt43-report-en.pdf)


