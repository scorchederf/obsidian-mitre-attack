---
aliases: 
    - S0366
    
mitre-attack: https://attack.mitre.org/software/S0366
---

## S0366

[WannaCry](https://attack.mitre.org/software/S0366) is ransomware that was first seen in a global attack during May 2017, which affected more than 150 countries. It contains worm-like features to spread itself across a computer network using the SMBv1 exploit EternalBlue.[^2] [^5] [^10] [^9] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [WannaCry](https://attack.mitre.org/software/S0366) uses an exploit in SMBv1 to spread itself to other remote systems on a network.[^2] [^9] [^5]  |
| [[Service Stop\|T1489]] | Service Stop | [WannaCry](https://attack.mitre.org/software/S0366) attempts to kill processes associated with Exchange, Microsoft SQL Server, and MySQL to make it possible to encrypt their data stores.[^9] [^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [WannaCry](https://attack.mitre.org/software/S0366) searches for variety of user files by file extension before encrypting them using RSA and AES, including Office, PDF, image, audio, video, source code, archive/compression format, and key and certificate files.[^2] [^9]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [WannaCry](https://attack.mitre.org/software/S0366) contains a thread that will attempt to scan for new attached drives every few seconds. If one is identified, it will encrypt the files on the attached device.[^9]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [WannaCry](https://attack.mitre.org/software/S0366) encrypts user files and demands that a ransom be paid in Bitcoin to decrypt those files.[^2] [^9] [^3]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [WannaCry](https://attack.mitre.org/software/S0366) utilizes `wmic` to delete shadow copies.[^2] [^9] [^3]  |
| [[RDP Hijacking\|T1563.002]] | RDP Hijacking | [WannaCry](https://attack.mitre.org/software/S0366) enumerates current remote desktop sessions and tries to execute the malware on each session.[^2]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [WannaCry](https://attack.mitre.org/software/S0366) uses `vssadmin`, `wbadmin`, `bcdedit`, and `wmic` to delete and disable operating system recovery features.[^2] [^9] [^3]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [WannaCry](https://attack.mitre.org/software/S0366) scans its local network segment for remote systems to try to exploit and copy itself to.[^3]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [WannaCry](https://attack.mitre.org/software/S0366) uses `[attrib](https://attack.mitre.org/software/S1176) +h` to make some of its files hidden.[^2] [^4]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [WannaCry](https://attack.mitre.org/software/S0366) will attempt to determine the local network segment it is a part of.[^3]  |
| [[Windows Permissions\|T1222.001]] | Windows Permissions | [WannaCry](https://attack.mitre.org/software/S0366) uses `attrib +h` and `icacls . /grant Everyone:F /T /C /Q` to make some of its files hidden and grant all users full access controls.[^2]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [WannaCry](https://attack.mitre.org/software/S0366) uses [Tor](https://attack.mitre.org/software/S0183) for command and control traffic.[^3]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [WannaCry](https://attack.mitre.org/software/S0366) uses [Tor](https://attack.mitre.org/software/S0183) for command and control traffic and routes a custom cryptographic protocol over the [Tor](https://attack.mitre.org/software/S0183) circuit.[^3]  |
| [[Windows Service\|T1543.003]] | Windows Service | [WannaCry](https://attack.mitre.org/software/S0366) creates the service "mssecsvc2.0" with the display name "Microsoft Security Center (2.0) Service."[^2] [^9]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [WannaCry](https://attack.mitre.org/software/S0366) attempts to copy itself to remote computers after gaining access via an SMB exploit.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: WCry


[^2]: [LogRhythm WannaCry](https://web.archive.org/web/20230522041200/https://logrhythm.com/blog/a-technical-analysis-of-wannacry-ransomware/)


[^3]: [SecureWorks WannaCry Analysis](https://www.secureworks.com/research/wcry-ransomware-analysis)


[^4]: [Checkpoint WannaCry 2017](https://blog.checkpoint.com/research/crying-futile-sandblast-forensic-analysis-wannacry/)


[^5]: [US-CERT WannaCry 2017](https://www.us-cert.gov/ncas/alerts/TA17-132A)


[^6]: [FireEye APT38 Oct 2018](https://services.google.com/fh/files/misc/apt38-un-usual-suspects.pdf)


[^7]: WanaCrypt


[^8]: WanaCry


[^9]: [FireEye WannaCry 2017](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)


[^10]: [Washington Post WannaCry 2017](https://www.washingtonpost.com/business/economy/more-than-150-countries-affected-by-massive-cyberattack-europol-says/2017/05/14/5091465e-3899-11e7-9e48-c4f199710b69_story.html?utm_term=.7fa16b41cad4)


[^11]: WanaCrypt0r


