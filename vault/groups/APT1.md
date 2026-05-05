---
aliases: 
    - APT1
    - Comment Crew
    - Comment Group
    - Comment Panda
mitre-attack: https://attack.mitre.org/groups/G0006
---

## G0006

[APT1](https://attack.mitre.org/groups/G0006) is a Chinese threat group that has been attributed to the 2nd Bureau of the People’s Liberation Army (PLA) General Staff Department’s (GSD) 3rd Department, commonly known by its Military Unit Cover Designator (MUCD) as Unit 61398. [^9] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [APT1](https://attack.mitre.org/groups/G0006) has been known to use credential dumping using [Mimikatz](https://attack.mitre.org/software/S0002).[^9]  |
| [[Process Discovery\|T1057]] | Process Discovery | [APT1](https://attack.mitre.org/groups/G0006) gathered a list of running processes on the system using `tasklist /v`.[^9]  |
| [[Data from Local System\|T1005]] | Data from Local System | [APT1](https://attack.mitre.org/groups/G0006) has collected files from a local victim.[^9]  |
| [[Pass the Hash\|T1550.002]] | Pass the Hash | The [APT1](https://attack.mitre.org/groups/G0006) group is known to have used pass the hash.[^9]  |
| [[Domains\|T1583.001]] | Domains | [APT1](https://attack.mitre.org/groups/G0006) has registered hundreds of domains for use in operations.[^9]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [APT1](https://attack.mitre.org/groups/G0006) has used RAR to compress files before moving them outside of the victim network.[^9]  |
| [[Automated Collection\|T1119]] | Automated Collection | [APT1](https://attack.mitre.org/groups/G0006) used a batch script to perform a series of discovery techniques and saves it to a text file.[^9]  |
| [[Remote Email Collection\|T1114.002]] | Remote Email Collection | [APT1](https://attack.mitre.org/groups/G0006) uses two utilities, GETMAIL and MAPIGET, to steal email. MAPIGET steals email still on Exchange servers that has not yet been archived.[^9]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [APT1](https://attack.mitre.org/groups/G0006) has sent spearphishing emails containing hyperlinks to malicious files.[^9]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [APT1](https://attack.mitre.org/groups/G0006) used the `ipconfig /all` command to gather network configuration information.[^9]  |
| [[Local Email Collection\|T1114.001]] | Local Email Collection | [APT1](https://attack.mitre.org/groups/G0006) uses two utilities, GETMAIL and MAPIGET, to steal email. GETMAIL extracts emails from archived Outlook .pst files.[^9]  |
| [[Malware\|T1588.001]] | Malware | [APT1](https://attack.mitre.org/groups/G0006) used publicly available malware for privilege escalation.[^9]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [APT1](https://attack.mitre.org/groups/G0006) used the `net use` command to get a listing on network connections.[^9]  |
| [[Email Accounts\|T1585.002]] | Email Accounts | [APT1](https://attack.mitre.org/groups/G0006) has created email accounts for later use in social engineering, phishing, and when registering domains.[^9]  |
| [[Domains\|T1584.001]] | Domains | [APT1](https://attack.mitre.org/groups/G0006) hijacked FQDNs associated with legitimate websites hosted by hop points.[^9]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | The file name AcroRD32.exe, a legitimate process name for Adobe's Acrobat Reader, was used by [APT1](https://attack.mitre.org/groups/G0006) as a name for malware.[^9] [^7]  |
| [[Local Account\|T1087.001]] | Local Account | [APT1](https://attack.mitre.org/groups/G0006) used the commands `net localgroup`,`net user`, and `net group` to find accounts on the system.[^9]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [APT1](https://attack.mitre.org/groups/G0006) has sent spearphishing emails containing malicious attachments.[^9]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [APT1](https://attack.mitre.org/groups/G0006) listed connected network shares.[^9]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [APT1](https://attack.mitre.org/groups/G0006) has used the Windows command shell to execute commands, and batch scripting to automate execution.[^9]  |
| [[Tool\|T1588.002]] | Tool | [APT1](https://attack.mitre.org/groups/G0006) has used various open-source tools for privilege escalation purposes.[^9]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [APT1](https://attack.mitre.org/groups/G0006) used the commands `net start` and `tasklist` to get a listing of the services on the system.[^9]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | The [APT1](https://attack.mitre.org/groups/G0006) group is known to have used RDP during operations.[^5]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^9]  |
| [[ipconfig\|S0100]] | ipconfig | [^9]  |
| [[Tasklist\|S0057]] | Tasklist | [^9]  |
| [[Lslsass\|S0121]] | Lslsass | [^9]  |
| [[xCmd\|S0123]] | xCmd | [^7]  |
| [[pwdump\|S0006]] | pwdump | [^9]  |
| [[Pass-The-Hash Toolkit\|S0122]] | Pass-The-Hash Toolkit | [^9]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^9]  |
| [[gsecdump\|S0008]] | gsecdump | [^9]  |
| [[Cachedump\|S0119]] | Cachedump | [^9]  |
| [[PsExec\|S0029]] | PsExec | [^9]  |
| [[WEBC2\|S0109]] | WEBC2 | [^9]  |
| [[CALENDAR\|S0025]] | CALENDAR | [^9]  |
| [[PoisonIvy\|S0012]] | PoisonIvy | [^9]  |
| [[Seasalt\|S0345]] | Seasalt | [^7] [^3]  |
| [[BISCUIT\|S0017]] | BISCUIT | [^9]  |
| [[GLOOXMAIL\|S0026]] | GLOOXMAIL | [^9]  |



## References

[^1]: [CrowdStrike Putter Panda](http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf)


[^2]: Comment Panda


[^3]: [McAfee Oceansalt Oct 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-oceansalt.pdf)


[^4]: Comment Crew


[^5]: [FireEye PLA](https://web.archive.org/web/20210417085454/https://www.fireeye.com/blog/threat-research/2014/05/the-pla-and-the-800am-500pm-work-day-fireeye-confirms-dojs-findings-on-apt1-intrusion-activity.html)


[^6]: Comment Group


[^7]: [Mandiant APT1 Appendix](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)


[^8]: APT1


[^9]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)


