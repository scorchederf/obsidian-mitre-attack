---
aliases: 
    - S0153
    
mitre-attack: https://attack.mitre.org/software/S0153
---

## S0153

[RedLeaves](https://attack.mitre.org/software/S0153) is a malware family used by [menuPass](https://attack.mitre.org/groups/G0045). The code overlaps with [PlugX](https://attack.mitre.org/software/S0013) and may be based upon the open source tool Trochilus. [^3]  [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [RedLeaves](https://attack.mitre.org/software/S0153) attempts to add a shortcut file in the Startup folder to achieve persistence.[^3] [^7]  |
| [[DLL\|T1574.001]] | DLL | [RedLeaves](https://attack.mitre.org/software/S0153) is launched through use of DLL search order hijacking to load a malicious dll.[^2]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [RedLeaves](https://attack.mitre.org/software/S0153) can gather browser usernames and passwords.[^7]  |
| [[Screen Capture\|T1113]] | Screen Capture | [RedLeaves](https://attack.mitre.org/software/S0153) can capture screenshots.[^2] [^7]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | A [RedLeaves](https://attack.mitre.org/software/S0153) configuration file is encrypted with a simple XOR key, 0x53.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [RedLeaves](https://attack.mitre.org/software/S0153) can delete specified files.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [RedLeaves](https://attack.mitre.org/software/S0153) can receive and execute commands with cmd.exe. It can also provide a reverse shell.[^3] [^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [RedLeaves](https://attack.mitre.org/software/S0153) can obtain information about network parameters.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [RedLeaves](https://attack.mitre.org/software/S0153) can gather extended system information including the hostname, OS version number, platform, memory information, time elapsed since system startup, and CPU information.[^3] [^7]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [RedLeaves](https://attack.mitre.org/software/S0153) has encrypted C2 traffic with RC4, previously using keys of 88888888 and babybear.[^3]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [RedLeaves](https://attack.mitre.org/software/S0153) can obtain information about the logged on user both locally and for Remote Desktop sessions.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [RedLeaves](https://attack.mitre.org/software/S0153) can communicate to its C2 over HTTP and HTTPS if directed.[^2] [^7]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [RedLeaves](https://attack.mitre.org/software/S0153) can enumerate and search for files and directories.[^3] [^2]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [RedLeaves](https://attack.mitre.org/software/S0153) can use HTTP over non-standard ports, such as 995, for C2.[^3]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [RedLeaves](https://attack.mitre.org/software/S0153) attempts to add a shortcut file in the Startup folder to achieve persistence. If this fails, it attempts to add Registry Run keys.[^3] [^7]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [RedLeaves](https://attack.mitre.org/software/S0153) can enumerate drives and Remote Desktop sessions.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [RedLeaves](https://attack.mitre.org/software/S0153) is capable of downloading a file from a specified URL.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[menuPass\|G0045]] | menuPass |



## References

[^1]: [DOJ APT10 Dec 2018](https://www.justice.gov/opa/pr/two-chinese-hackers-associated-ministry-state-security-charged-global-computer-intrusion)


[^2]: [FireEye APT10 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/apt10_menupass_grou.html)


[^3]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^4]: BUGJUICE


[^5]: [Twitter Nick Carr APT10](https://x.com/ItsReallyNick/status/850105140589633536)


[^6]: RedLeaves


[^7]: [Accenture Hogfish April 2018](http://web.archive.org/web/20220810112638/https:/www.accenture.com/t20180423T055005Z_w_/se-en/_acnmedia/PDF-76/Accenture-Hogfish-Threat-Analysis.pdf)


