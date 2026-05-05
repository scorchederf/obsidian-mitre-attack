---
aliases: 
    - S0050
    
mitre-attack: https://attack.mitre.org/software/S0050
---

## S0050

[CosmicDuke](https://attack.mitre.org/software/S0050) is malware that was used by [APT29](https://attack.mitre.org/groups/G0016) from 2010 to 2015. [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Service\|T1543.003]] | Windows Service | [CosmicDuke](https://attack.mitre.org/software/S0050) uses Windows services typically named "javamtsup" for persistence.[^2]  |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | [CosmicDuke](https://attack.mitre.org/software/S0050) collects LSA secrets.[^3]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [CosmicDuke](https://attack.mitre.org/software/S0050) exfiltrates collected files over FTP or WebDAV. Exfiltration servers can be separately configured from C2 servers.[^2]  |
| [[Data from Network Shared Drive\|T1039]] | Data from Network Shared Drive | [CosmicDuke](https://attack.mitre.org/software/S0050) steals user files from network shared drives with file extensions and keywords that match a predefined list.[^2]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [CosmicDuke](https://attack.mitre.org/software/S0050) collects user credentials, including passwords, for various programs including popular instant messaging applications and email clients as well as WLAN keys.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [CosmicDuke](https://attack.mitre.org/software/S0050) searches attached and mounted drives for file extensions and keywords that match a predefined list.[^2]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [CosmicDuke](https://attack.mitre.org/software/S0050) collects user credentials, including passwords, for various programs including Web browsers.[^3]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [CosmicDuke](https://attack.mitre.org/software/S0050) attempts to exploit privilege escalation vulnerabilities CVE-2010-0232 or CVE-2010-4398.[^3]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [CosmicDuke](https://attack.mitre.org/software/S0050) copies and exfiltrates the clipboard contents every 30 seconds.[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [CosmicDuke](https://attack.mitre.org/software/S0050) uses a keylogger.[^3]  |
| [[Screen Capture\|T1113]] | Screen Capture | [CosmicDuke](https://attack.mitre.org/software/S0050) takes periodic screenshots and exfiltrates them.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [CosmicDuke](https://attack.mitre.org/software/S0050) can use HTTP or HTTPS for command and control to hard-coded C2 servers.[^3] [^2]  |
| [[Local Email Collection\|T1114.001]] | Local Email Collection | [CosmicDuke](https://attack.mitre.org/software/S0050) searches for Microsoft Outlook data files with extensions .pst and .ost for collection and exfiltration.[^2]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [CosmicDuke](https://attack.mitre.org/software/S0050) collects Windows account hashes.[^3]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [CosmicDuke](https://attack.mitre.org/software/S0050) exfiltrates collected files automatically over FTP to remote servers.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [CosmicDuke](https://attack.mitre.org/software/S0050) steals user files from local hard drives with file extensions that match a predefined list.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [CosmicDuke](https://attack.mitre.org/software/S0050) uses scheduled tasks typically named "Watchmon Service" for persistence.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [CosmicDuke](https://attack.mitre.org/software/S0050) contains a custom version of the RC4 algorithm that includes a programming error.[^2]  |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | [CosmicDuke](https://attack.mitre.org/software/S0050) steals user files from removable media with file extensions and keywords that match a predefined list.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [Secureworks IRON HEMLOCK Profile](http://www.secureworks.com/research/threat-profiles/iron-hemlock)


[^2]: [F-Secure Cosmicduke](https://blog.f-secure.com/wp-content/uploads/2019/10/CosmicDuke.pdf)


[^3]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)


