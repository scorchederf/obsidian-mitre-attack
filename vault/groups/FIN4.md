---
aliases: 
    - FIN4
mitre-attack: https://attack.mitre.org/groups/G0085
---

## G0085

[FIN4](https://attack.mitre.org/groups/G0085) is a financially-motivated threat group that has targeted confidential information related to the public financial market, particularly regarding healthcare and pharmaceutical companies, since at least 2013.[^3] [^2]  [FIN4](https://attack.mitre.org/groups/G0085) is unique in that they do not infect victims with typical persistent malware, but rather they focus on capturing credentials authorized to access email and other non-public correspondence.[^3] [^4] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Valid Accounts\|T1078]] | Valid Accounts | [FIN4](https://attack.mitre.org/groups/G0085) has used legitimate credentials to hijack email communications.[^3] [^4]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [FIN4](https://attack.mitre.org/groups/G0085) has used VBA macros to display a dialog box and collect victim credentials.[^3] [^4]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [FIN4](https://attack.mitre.org/groups/G0085) has used [Tor](https://attack.mitre.org/software/S0183) to log in to victims' email accounts.[^3]  |
| [[Malicious File\|T1204.002]] | Malicious File | [FIN4](https://attack.mitre.org/groups/G0085) has lured victims to launch malicious attachments delivered via spearphishing emails (often sent from compromised accounts).[^3] [^4]  |
| [[Email Hiding Rules\|T1564.008]] | Email Hiding Rules | [FIN4](https://attack.mitre.org/groups/G0085) has created rules in victims' Microsoft Outlook accounts to automatically delete emails containing words such as “hacked," "phish," and “malware" in a likely attempt to prevent organizations from communicating about their activities.[^3]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [FIN4](https://attack.mitre.org/groups/G0085) has lured victims to click malicious links delivered via spearphishing emails (often sent from compromised accounts).[^3] [^4]  |
| [[Keylogging\|T1056.001]] | Keylogging | [FIN4](https://attack.mitre.org/groups/G0085) has captured credentials via fake Outlook Web App (OWA) login pages and has also used a .NET based keylogger.[^3] [^4]  |
| [[GUI Input Capture\|T1056.002]] | GUI Input Capture | [FIN4](https://attack.mitre.org/groups/G0085) has presented victims with spoofed Windows Authentication prompts to collect their credentials.[^3] [^4]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [FIN4](https://attack.mitre.org/groups/G0085) has used spearphishing emails (often sent from compromised accounts) containing malicious links.[^3] [^4]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [FIN4](https://attack.mitre.org/groups/G0085) has used spearphishing emails containing attachments (which are often stolen, legitimate documents sent from compromised accounts) with embedded malicious macros.[^3] [^4]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [FIN4](https://attack.mitre.org/groups/G0085) has used HTTP POST requests to transmit data.[^3] [^4]  |
| [[Remote Email Collection\|T1114.002]] | Remote Email Collection | [FIN4](https://attack.mitre.org/groups/G0085) has accessed and hijacked online email communications using stolen credentials.[^3] [^4]  |




## References

[^1]: FIN4


[^2]: [FireEye FIN4 Stealing Insider NOV 2014](https://web.archive.org/web/20190508171649/https://www.fireeye.com/blog/threat-research/2014/11/fin4_stealing_insid.html)


[^3]: [FireEye Hacking FIN4 Dec 2014](https://www.mandiant.com/sites/default/files/2021-09/rpt-fin4.pdf)


[^4]: [FireEye Hacking FIN4 Video Dec 2014](https://www2.fireeye.com/WBNR-14Q4NAMFIN4.html)


