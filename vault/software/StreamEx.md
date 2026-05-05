---
aliases: 
    - S0142
    
mitre-attack: https://attack.mitre.org/software/S0142
---

## S0142

[StreamEx](https://attack.mitre.org/software/S0142) is a malware family that has been used by [Deep Panda](https://attack.mitre.org/groups/G0009) since at least 2015. In 2016, it was distributed via legitimate compromised Korean websites. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [StreamEx](https://attack.mitre.org/software/S0142) has the ability to enumerate processes.[^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [StreamEx](https://attack.mitre.org/software/S0142) uses rundll32 to call an exported function.[^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | [StreamEx](https://attack.mitre.org/software/S0142) establishes persistence by installing a new service pointing to its DLL and setting the service to auto-start.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [StreamEx](https://attack.mitre.org/software/S0142) has the ability to modify the Registry.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [StreamEx](https://attack.mitre.org/software/S0142) has the ability to enumerate system information.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [StreamEx](https://attack.mitre.org/software/S0142) has the ability to enumerate drive types.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [StreamEx](https://attack.mitre.org/software/S0142) has the ability to scan for security tools such as firewalls and antivirus tools.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [StreamEx](https://attack.mitre.org/software/S0142) obfuscates some commands by using statically programmed fragments of strings when starting a DLL. It also uses a one-byte xor against 0x91 to encode configuration data.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [StreamEx](https://attack.mitre.org/software/S0142) has the ability to remotely execute commands.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Deep Panda\|G0009]] | Deep Panda |



## References

[^1]: StreamEx


[^2]: [Cylance Shell Crew Feb 2017](https://www.cylance.com/shell-crew-variants-continue-to-fly-under-big-avs-radar)


