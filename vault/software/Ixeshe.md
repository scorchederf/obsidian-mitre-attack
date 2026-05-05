---
aliases: 
    - S0015
    
mitre-attack: https://attack.mitre.org/software/S0015
---

## S0015

[Ixeshe](https://attack.mitre.org/software/S0015) is a malware family that has been used since at least 2009 against targets in East Asia. [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [Ixeshe](https://attack.mitre.org/software/S0015) can list running processes.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Ixeshe](https://attack.mitre.org/software/S0015) uses HTTP for command and control.[^3] [^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Ixeshe](https://attack.mitre.org/software/S0015) has a command to delete a file from the machine.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Ixeshe](https://attack.mitre.org/software/S0015) can achieve persistence by adding itself to the `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` Registry key.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Ixeshe](https://attack.mitre.org/software/S0015) collects the computer name of the victim's system during the initial infection.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Ixeshe](https://attack.mitre.org/software/S0015) enumerates the IP address, network proxy settings, and domain name from a victim's system.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Ixeshe](https://attack.mitre.org/software/S0015) can download and execute additional files.[^1]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [Ixeshe](https://attack.mitre.org/software/S0015) sets its own executable file's attributes to hidden.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Ixeshe](https://attack.mitre.org/software/S0015) uses custom Base64 encoding schemes to obfuscate command and control traffic in the message body of HTTP requests.[^3] [^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Ixeshe](https://attack.mitre.org/software/S0015) can list file and directory information.[^1]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Ixeshe](https://attack.mitre.org/software/S0015) can list running services.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Ixeshe](https://attack.mitre.org/software/S0015) can collect data from a local system.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Ixeshe](https://attack.mitre.org/software/S0015) collects the username from the victim’s machine.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Ixeshe](https://attack.mitre.org/software/S0015) has used registry values and file names associated with Adobe software, such as AcroRd32.exe.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Ixeshe](https://attack.mitre.org/software/S0015) is capable of executing commands via [cmd](https://attack.mitre.org/software/S0106).[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT12\|G0005]] | APT12 |



## References

[^1]: [Trend Micro IXESHE 2012](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)


[^2]: [Moran 2014](https://www.fireeye.com/blog/threat-research/2014/09/darwins-favorite-apt-group-2.html)


[^3]: [Moran 2013](https://web.archive.org/web/20191224162418/https://www.fireeye.com/blog/threat-research/2013/08/survival-of-the-fittest-new-york-times-attackers-evolve-quickly.html)


