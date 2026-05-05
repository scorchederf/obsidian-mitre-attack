---
aliases: 
    - S0143
    
mitre-attack: https://attack.mitre.org/software/S0143
---

## S0143

[Flame](https://attack.mitre.org/software/S0143) is a sophisticated toolkit that has been used to collect information since at least 2010, largely targeting Middle East countries. [^6] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [Flame](https://attack.mitre.org/software/S0143) contains modules to infect USB sticks and spread laterally to other Windows systems the stick is plugged into using Autorun functionality.[^6]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [Flame](https://attack.mitre.org/software/S0143) can use MS10-061 to exploit a print spooler vulnerability in a remote system with a shared printer in order to move laterally.[^6] [^3]  |
| [[Audio Capture\|T1123]] | Audio Capture | [Flame](https://attack.mitre.org/software/S0143) can record audio using any existing hardware recording devices.[^6] [^3]  |
| [[Exfiltration Over Bluetooth\|T1011.001]] | Exfiltration Over Bluetooth | [Flame](https://attack.mitre.org/software/S0143) has a module named BeetleJuice that contains Bluetooth functionality that may be used in different ways, including transmitting encoded information from the infected system over the Bluetooth protocol, acting as a Bluetooth beacon, and identifying other Bluetooth devices in the vicinity.[^2]  |
| [[Masquerade Account Name\|T1036.010]] | Masquerade Account Name | [Flame](https://attack.mitre.org/software/S0143) can create backdoor accounts with login `HelpAssistant` on domain connected systems if appropriate rights are available.[^6] [^3]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Flame](https://attack.mitre.org/software/S0143) identifies security software such as antivirus through the Security module.[^6] [^3]  |
| [[Local Account\|T1136.001]] | Local Account | [Flame](https://attack.mitre.org/software/S0143) can create backdoor accounts with login “HelpAssistant” on domain connected systems if appropriate rights are available.[^6] [^3]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Flame](https://attack.mitre.org/software/S0143) can take regular screenshots when certain applications are open that are sent to the command and control server.[^6]  |
| [[Authentication Package\|T1547.002]] | Authentication Package | [Flame](https://attack.mitre.org/software/S0143) can use Windows Authentication Packages for persistence.[^5]  |
| [[Rundll32\|T1218.011]] | Rundll32 | Rundll32.exe is used as a way of executing [Flame](https://attack.mitre.org/software/S0143) at the command-line.[^5]  |




## References

[^1]: Flame


[^2]: [Symantec Beetlejuice](https://www.symantec.com/connect/blogs/flamer-recipe-bluetoothache)


[^3]: [Kaspersky Flame Functionality](https://securelist.com/flame-bunny-frog-munch-and-beetlejuice-2/32855/)


[^4]: sKyWIper


[^5]: [Crysys Skywiper](https://www.crysys.hu/publications/files/skywiper.pdf)


[^6]: [Kaspersky Flame](https://securelist.com/the-flame-questions-and-answers-51/34344/)


[^7]: Flamer


