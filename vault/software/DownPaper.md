---
aliases: 
    - S0186
    
mitre-attack: https://attack.mitre.org/software/S0186
---

## S0186

[DownPaper](https://attack.mitre.org/software/S0186) is a backdoor Trojan; its main functionality is to download and run second stage malware. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [DownPaper](https://attack.mitre.org/software/S0186) collects the victim host name and serial number, and then sends the information to the C2 server.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [DownPaper](https://attack.mitre.org/software/S0186) searches and reads the value of the Windows Update Registry Run key.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [DownPaper](https://attack.mitre.org/software/S0186) collects the victim username and sends it to the C2 server.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [DownPaper](https://attack.mitre.org/software/S0186) uses PowerShell to add a Registry Run key in order to establish persistence.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [DownPaper](https://attack.mitre.org/software/S0186) communicates to its C2 server over HTTP.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [DownPaper](https://attack.mitre.org/software/S0186) uses PowerShell for execution.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [DownPaper](https://attack.mitre.org/software/S0186) uses the command line.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Magic Hound\|G0059]] | Magic Hound |



## References

[^1]: [ClearSky Charming Kitten Dec 2017](http://www.clearskysec.com/wp-content/uploads/2017/12/Charming_Kitten_2017.pdf)


[^2]: DownPaper


