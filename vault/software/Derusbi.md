---
aliases: 
    - S0021
    
mitre-attack: https://attack.mitre.org/software/S0021
---

## S0021

[Derusbi](https://attack.mitre.org/software/S0021) is malware used by multiple Chinese APT groups.[^5] [^11]  Both Windows and Linux variants have been observed.[^7] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Keylogging\|T1056.001]] | Keylogging | [Derusbi](https://attack.mitre.org/software/S0021) is capable of logging keystrokes.[^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Derusbi](https://attack.mitre.org/software/S0021) is capable of creating a remote Bash shell and executing commands.[^7] [^1]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Derusbi](https://attack.mitre.org/software/S0021) variants have been seen that use Registry persistence to proxy execution through regsvr32.exe.[^9]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Derusbi](https://attack.mitre.org/software/S0021) gathers the name of the local host, version of GNU Compiler Collection (GCC), and the system information about the CPU, machine, and operating system.[^7]  |
| [[Timestomp\|T1070.006]] | Timestomp | The [Derusbi](https://attack.mitre.org/software/S0021) malware supports timestomping.[^5] [^7]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Derusbi](https://attack.mitre.org/software/S0021) injects itself into the secure shell (SSH) process.[^10]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Derusbi](https://attack.mitre.org/software/S0021) is capable of deleting files. It has been observed loading a Linux Kernel Module (LKM) and then deleting it from the hard disk as well as overwriting the data with null bytes.[^7] [^1]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [Derusbi](https://attack.mitre.org/software/S0021) has used unencrypted HTTP on port 443 for C2.[^7]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Derusbi](https://attack.mitre.org/software/S0021) obfuscates C2 traffic with variable 4-byte XOR keys.[^7]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | A Linux version of [Derusbi](https://attack.mitre.org/software/S0021) checks if the victim user ID is anything other than zero (normally used for root), and the malware will not execute if it does not have root privileges. [Derusbi](https://attack.mitre.org/software/S0021) also gathers the username of the victim.[^7]  |
| [[Audio Capture\|T1123]] | Audio Capture | [Derusbi](https://attack.mitre.org/software/S0021) is capable of performing audio captures.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Derusbi](https://attack.mitre.org/software/S0021) is capable of obtaining directory, file, and drive listings.[^7] [^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Derusbi](https://attack.mitre.org/software/S0021) uses a backup communication method with an HTTP beacon.[^7]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Derusbi](https://attack.mitre.org/software/S0021) binds to a raw socket on a random source port between 31800 and 31900 for C2.[^7]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Derusbi](https://attack.mitre.org/software/S0021) is capable of performing screen captures.[^1]  |
| [[Video Capture\|T1125]] | Video Capture | [Derusbi](https://attack.mitre.org/software/S0021) is capable of capturing video.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Derusbi](https://attack.mitre.org/software/S0021) collects current and parent process IDs.[^7] [^1]  |
| [[Query Registry\|T1012]] | Query Registry | [Derusbi](https://attack.mitre.org/software/S0021) is capable of enumerating Registry keys and values.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Leviathan\|G0065]] | Leviathan |
| [[Deep Panda\|G0009]] | Deep Panda |
| [[Axiom\|G0001]] | Axiom |
| [[APT41\|G0096]] | APT41 |



## References

[^1]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)


[^2]: PHOTO


[^3]: Derusbi


[^4]: [CISA AA21-200A APT40 July 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-200a)


[^5]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)


[^6]: [Cisco Group 72](http://blogs.cisco.com/security/talos/threat-spotlight-group-72)


[^7]: [Fidelis Turbo](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)


[^8]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^9]: [ThreatGeek Derusbi Converge](https://www.fidelissecurity.com/threatgeek/threat-intelligence/turbo-twist-two-64-bit-derusbi-strains-converge)


[^10]: [Airbus Derusbi 2015](https://web.archive.org/web/20180607084223/http://blog.airbuscybersecurity.com/post/2015/11/Newcomers-in-the-Derusbi-family)


[^11]: [ThreatConnect Anthem](https://www.threatconnect.com/the-anthem-hack-all-roads-lead-to-china/)


