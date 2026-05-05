---
aliases: 
    - Carbanak
    - Anunak
mitre-attack: https://attack.mitre.org/groups/G0008
---

## G0008

[Carbanak](https://attack.mitre.org/groups/G0008) is a cybercriminal group that has used [Carbanak](https://attack.mitre.org/software/S0030) malware to target financial institutions since at least 2013. [Carbanak](https://attack.mitre.org/groups/G0008) may be linked to groups tracked separately as [Cobalt Group](https://attack.mitre.org/groups/G0080) and [FIN7](https://attack.mitre.org/groups/G0046) that have also used [Carbanak](https://attack.mitre.org/software/S0030) malware.[^9] [^6] [^2] [^7] [^5] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Carbanak](https://attack.mitre.org/groups/G0008) has copied legitimate service names to use for malicious services.[^9]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Carbanak](https://attack.mitre.org/groups/G0008) installs VNC server software that executes through rundll32.[^9]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Carbanak](https://attack.mitre.org/groups/G0008) actors used legitimate credentials of banking employees to perform operations that sent them millions of dollars.[^9]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [Carbanak](https://attack.mitre.org/groups/G0008) has used a VBScript named "ggldr" that uses Google Apps Script, Sheets, and Forms services for C2.[^3]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Carbanak](https://attack.mitre.org/groups/G0008) malware installs itself as a service to provide persistence and SYSTEM privileges.[^9]  |
| [[Remote Access Tools\|T1219]] | Remote Access Tools | [Carbanak](https://attack.mitre.org/groups/G0008) used legitimate programs such as AmmyyAdmin and Team Viewer for remote interactive C2 to target systems.[^10]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Carbanak](https://attack.mitre.org/groups/G0008) has named malware "svchost.exe," which is the name of the Windows shared service host program.[^9]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [Carbanak](https://attack.mitre.org/groups/G0008) may use [netsh](https://attack.mitre.org/software/S0108) to add local firewall rule exceptions.[^10]  |
| [[Tool\|T1588.002]] | Tool | [Carbanak](https://attack.mitre.org/groups/G0008) has obtained and used open-source tools such as [PsExec](https://attack.mitre.org/software/S0029) and [Mimikatz](https://attack.mitre.org/software/S0002).[^9]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[netsh\|S0108]] | netsh | [^10]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^9]  |
| [[PsExec\|S0029]] | PsExec | [^9]  |
| [[Carbanak\|S0030]] | Carbanak | [^9]  |



## References

[^1]: Carbanak


[^2]: [Europol Cobalt Mar 2018](https://www.europol.europa.eu/newsroom/news/mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain)


[^3]: [Forcepoint Carbanak Google C2](https://blogs.forcepoint.com/security-labs/carbanak-group-uses-google-malware-command-and-control)


[^4]: [Fox-It Anunak Feb 2015](https://www.fox-it.com/en/news/blog/anunak-aka-carbanak-update/)


[^5]: [Secureworks GOLD KINGSWOOD Threat Profile](https://www.secureworks.com/research/threat-profiles/gold-kingswood?filter=item-financial-gain)


[^6]: [FireEye FIN7 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html)


[^7]: [Secureworks GOLD NIAGARA Threat Profile](https://www.secureworks.com/research/threat-profiles/gold-niagara)


[^8]: Anunak


[^9]: [Kaspersky Carbanak](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064518/Carbanak_APT_eng.pdf)


[^10]: [Group-IB Anunak](http://www.group-ib.com/files/Anunak_APT_against_financial_institutions.pdf)


