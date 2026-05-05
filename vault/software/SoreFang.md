---
aliases: 
    - S0516
    
mitre-attack: https://attack.mitre.org/software/S0516
---

## S0516

[SoreFang](https://attack.mitre.org/software/S0516) is first stage downloader used by [APT29](https://attack.mitre.org/groups/G0016) for exfiltration and to load other malware.[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SoreFang](https://attack.mitre.org/software/S0516) can download additional payloads from C2.[^1] [^2]  |
| [[Domain Account\|T1087.002]] | Domain Account | [SoreFang](https://attack.mitre.org/software/S0516) can enumerate domain accounts via `net.exe user /domain`.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [SoreFang](https://attack.mitre.org/software/S0516) can enumerate processes on a victim machine through use of [Tasklist](https://attack.mitre.org/software/S0057).[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [SoreFang](https://attack.mitre.org/software/S0516) has the ability to list directories.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [SoreFang](https://attack.mitre.org/software/S0516) can use HTTP in C2 communications.[^1] [^2]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [SoreFang](https://attack.mitre.org/software/S0516) can gain access by exploiting a Sangfor SSL VPN vulnerability that allows for the placement and delivery of malicious update binaries.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [SoreFang](https://attack.mitre.org/software/S0516) can gain persistence through use of scheduled tasks.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SoreFang](https://attack.mitre.org/software/S0516) can collect the hostname, operating system configuration, and product ID on victim machines by executing [Systeminfo](https://attack.mitre.org/software/S0096).[^1]  |
| [[Local Account\|T1087.001]] | Local Account | [SoreFang](https://attack.mitre.org/software/S0516) can collect usernames from the local system via `net.exe user`.[^1]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [SoreFang](https://attack.mitre.org/software/S0516) can enumerate domain groups by executing `net.exe group /domain`.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [SoreFang](https://attack.mitre.org/software/S0516) can collect the TCP/IP, DNS, DHCP, and network adapter configuration on a compromised host via `ipconfig.exe /all`.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [SoreFang](https://attack.mitre.org/software/S0516) can collect disk space information on victim machines by executing [Systeminfo](https://attack.mitre.org/software/S0096).[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [SoreFang](https://attack.mitre.org/software/S0516) has the ability to encode and RC6 encrypt data sent to C2.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [SoreFang](https://attack.mitre.org/software/S0516) can decode and decrypt exfiltrated data sent to C2.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [CISA SoreFang July 2016](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)


[^2]: [NCSC APT29 July 2020](https://www.ncsc.gov.uk/files/Advisory-APT29-targets-COVID-19-vaccine-development-V1-1.pdf)


