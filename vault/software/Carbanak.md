---
aliases: 
    - S0030
    
mitre-attack: https://attack.mitre.org/software/S0030
---

## S0030

[Carbanak](https://attack.mitre.org/software/S0030) is a full-featured, remote backdoor used by a group of the same name ([Carbanak](https://attack.mitre.org/groups/G0008)). It is intended for espionage, data exfiltration, and providing remote access to infected machines. [^12]  [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | [Carbanak](https://attack.mitre.org/software/S0030) obtains Windows logon password details.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Carbanak](https://attack.mitre.org/software/S0030) performs desktop video recording and captures screenshots of the desktop and sends it to the C2 server.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | The [Carbanak](https://attack.mitre.org/software/S0030) malware communicates to its command server using HTTP with an encrypted payload.[^12]  |
| [[Query Registry\|T1012]] | Query Registry | [Carbanak](https://attack.mitre.org/software/S0030) checks the Registry key `HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings` for proxy configurations information.[^2]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Carbanak](https://attack.mitre.org/software/S0030) enables concurrent Remote Desktop Protocol (RDP) sessions.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Carbanak](https://attack.mitre.org/software/S0030) has a command to create a reverse shell.[^2]  |
| [[Portable Executable Injection\|T1055.002]] | Portable Executable Injection | [Carbanak](https://attack.mitre.org/software/S0030) downloads an executable and injects it directly into a new process.[^2]  |
| [[Local Email Collection\|T1114.001]] | Local Email Collection | [Carbanak](https://attack.mitre.org/software/S0030) searches recursively for Outlook personal storage tables (PST) files within user directories and sends them back to the C2 server.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Carbanak](https://attack.mitre.org/software/S0030) lists running processes.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Carbanak](https://attack.mitre.org/software/S0030) encrypts strings to make analysis more difficult.[^2]  |
| [[Remote Access Tools\|T1219]] | Remote Access Tools | [Carbanak](https://attack.mitre.org/software/S0030) has a plugin for VNC and Ammyy Admin Tool.[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Carbanak](https://attack.mitre.org/software/S0030) logs key strokes for configured processes and sends them back to the C2 server.[^12] [^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Carbanak](https://attack.mitre.org/software/S0030) stores a configuration files in the startup directory to automatically execute commands in order to persist across reboots.[^2]  |
| [[Local Account\|T1136.001]] | Local Account | [Carbanak](https://attack.mitre.org/software/S0030) can create a Windows account.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Carbanak](https://attack.mitre.org/software/S0030) encrypts the message body of HTTP traffic with RC2 (in CBC mode). [Carbanak](https://attack.mitre.org/software/S0030) also uses XOR with random keys for its communications.[^12] [^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Carbanak](https://attack.mitre.org/software/S0030) has a command to delete files.[^2]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Carbanak](https://attack.mitre.org/software/S0030) encodes the message body of HTTP traffic with Base64.[^12] [^2]  |
| [[Data Transfer Size Limits\|T1030]] | Data Transfer Size Limits | [Carbanak](https://attack.mitre.org/software/S0030) exfiltrates data in compressed chunks if a message is larger than 4096 bytes .[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN7\|G0046]] | FIN7 |
| [[Carbanak\|G0008]] | Carbanak |



## References

[^1]: Carbanak


[^2]: [FireEye CARBANAK June 2017](https://www.fireeye.com/blog/threat-research/2017/06/behind-the-carbanak-backdoor.html)


[^3]: [BlackBerry_FIN7_April2024](https://blogs.blackberry.com/en/2024/04/fin7-targets-the-united-states-automotive-industry)


[^4]: [DOJ FIN7 Aug 2018](https://www.justice.gov/opa/press-release/file/1084361/download)


[^5]: [Mandiant FIN7 Apr 2022](https://www.mandiant.com/resources/evolution-of-fin7)


[^6]: [FBI Flash FIN7 USB](https://therecord.media/fbi-fin7-hackers-target-us-companies-with-badusb-devices-to-install-ransomware/)


[^7]: [CrowdStrike Carbon Spider August 2021](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)


[^8]: [Fox-It Anunak Feb 2015](https://www.fox-it.com/en/news/blog/anunak-aka-carbanak-update/)


[^9]: [FireEye FIN7 Aug 2018](https://www.fireeye.com/blog/threat-research/2018/08/fin7-pursuing-an-enigmatic-and-evasive-global-criminal-operation.html)


[^10]: [FireEye FIN7 March 2017](https://web.archive.org/web/20180808125108/https:/www.fireeye.com/blog/threat-research/2017/03/fin7_spear_phishing.html)


[^11]: Anunak


[^12]: [Kaspersky Carbanak](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064518/Carbanak_APT_eng.pdf)


[^13]: [IBM Ransomware Trends September 2020](https://securityintelligence.com/posts/ransomware-2020-attack-trends-new-techniques-affecting-organizations-worldwide/)


