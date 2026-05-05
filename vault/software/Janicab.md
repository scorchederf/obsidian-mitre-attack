---
aliases: 
    - S0163
    
mitre-attack: https://attack.mitre.org/software/S0163
---

## S0163

[Janicab](https://attack.mitre.org/software/S0163) is an OS X trojan that relied on a valid developer ID and oblivious users to install it. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Cron\|T1053.003]] | Cron | [Janicab](https://attack.mitre.org/software/S0163) used a cron job for persistence on Mac devices.[^1]  |
| [[Audio Capture\|T1123]] | Audio Capture | [Janicab](https://attack.mitre.org/software/S0163) captured audio and sent it out to a C2 server.[^2] [^1]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Janicab](https://attack.mitre.org/software/S0163) used a valid AppleDeveloperID to sign the code to get past security restrictions.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Janicab](https://attack.mitre.org/software/S0163) captured screenshots and sent them out to a C2 server.[^2] [^1]  |




## References

[^1]: [Janicab](https://web.archive.org/web/20230331162455/https://www.thesafemac.com/new-signed-malware-called-janicab/)


[^2]: [f-secure janicab](https://www.f-secure.com/weblog/archives/00002576.html)


