---
aliases: 
    - Nomadic Octopus
    - DustSquad
mitre-attack: https://attack.mitre.org/groups/G0133
---

## G0133

<br>[Nomadic Octopus](https://attack.mitre.org/groups/G0133) is a Russian-speaking cyber espionage threat group that has primarily targeted Central Asia, including local governments, diplomatic missions, and individuals, since at least 2014. [Nomadic Octopus](https://attack.mitre.org/groups/G0133) has been observed conducting campaigns involving Android and Windows malware, mainly using the Delphi programming language, and building custom variants.[^6] [^2] [^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Nomadic Octopus](https://attack.mitre.org/groups/G0133) used `cmd.exe /c` within a malicious macro.[^1]  |
| [[Masquerading\|T1036]] | Masquerading | [Nomadic Octopus](https://attack.mitre.org/groups/G0133) attempted to make [Octopus](https://attack.mitre.org/software/S0340) appear as a  Telegram Messenger with a Russian interface.[^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Nomadic Octopus](https://attack.mitre.org/groups/G0133) has targeted victims with spearphishing emails containing malicious attachments.[^6] [^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Nomadic Octopus](https://attack.mitre.org/groups/G0133) as attempted to lure victims into clicking on malicious attachments within spearphishing emails.[^2] [^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Nomadic Octopus](https://attack.mitre.org/groups/G0133) has used malicious macros to download additional files to the victim's machine.[^1]   |
| [[Hidden Window\|T1564.003]] | Hidden Window | [Nomadic Octopus](https://attack.mitre.org/groups/G0133) executed PowerShell in a hidden window.[^1]   |
| [[PowerShell\|T1059.001]] | PowerShell | [Nomadic Octopus](https://attack.mitre.org/groups/G0133) has used PowerShell for execution.[^1]   |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Octopus\|S0340]] | Octopus | [^6] [^2] [^1]   |



## References

[^1]: [ESET Nomadic Octopus 2018](https://www.virusbulletin.com/uploads/pdf/conference_slides/2018/Cherepanov-VB2018-Octopus.pdf)


[^2]: [Securelist Octopus Oct 2018](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)


[^3]: [SecurityWeek Nomadic Octopus Oct 2018](https://www.securityweek.com/russia-linked-hackers-target-diplomatic-entities-central-asia)


[^4]: DustSquad


[^5]: Nomadic Octopus


[^6]: [Security Affairs DustSquad Oct 2018](https://securityaffairs.co/wordpress/77165/apt/russia-linked-apt-dustsquad.html)


