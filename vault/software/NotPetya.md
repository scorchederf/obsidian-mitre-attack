---
aliases: 
    - S0368
    
mitre-attack: https://attack.mitre.org/software/S0368
---

## S0368

[NotPetya](https://attack.mitre.org/software/S0368) is malware that was used by [Sandworm Team](https://attack.mitre.org/groups/G0034) in a worldwide attack starting on June 27, 2017. While [NotPetya](https://attack.mitre.org/software/S0368) appears as a form of ransomware, its main purpose was to destroy data and disk structures on compromised systems; the attackers never intended to make the encrypted data recoverable. As such, [NotPetya](https://attack.mitre.org/software/S0368) may be more appropriately thought of as a form of wiper malware. [NotPetya](https://attack.mitre.org/software/S0368) contains worm-like features to spread itself across a computer network using the SMBv1 exploits EternalBlue and EternalRomance.[^10] [^1] [^6] [^9] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Service Execution\|T1569.002]] | Service Execution | [NotPetya](https://attack.mitre.org/software/S0368) can use [PsExec](https://attack.mitre.org/software/S0029) to help propagate itself across a network.[^10] [^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [NotPetya](https://attack.mitre.org/software/S0368) creates a task to reboot the system one hour after infection.[^10]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [NotPetya](https://attack.mitre.org/software/S0368) can use [PsExec](https://attack.mitre.org/software/S0029), which interacts with the `ADMIN$` network share to execute commands on remote systems.[^10] [^1] [^8]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [NotPetya](https://attack.mitre.org/software/S0368) uses `wevtutil` to clear the Windows event logs.[^10] [^9]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [NotPetya](https://attack.mitre.org/software/S0368) determines if specific antivirus programs are running on an infected host machine.[^9]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [NotPetya](https://attack.mitre.org/software/S0368) can use `wmic` to help propagate itself across a network.[^10] [^1]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [NotPetya](https://attack.mitre.org/software/S0368) can use two exploits in SMBv1, EternalBlue and EternalRomance, to spread itself to other remote systems on the network.[^10] [^1] [^9]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [NotPetya](https://attack.mitre.org/software/S0368) searches for files ending with dozens of different file extensions prior to encryption.[^9]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [NotPetya](https://attack.mitre.org/software/S0368) contains a modified version of [Mimikatz](https://attack.mitre.org/software/S0002) to help gather credentials that are later used for lateral movement.[^10] [^1] [^4]  |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [NotPetya](https://attack.mitre.org/software/S0368) will reboot the system one hour after infection.[^10] [^9]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [NotPetya](https://attack.mitre.org/software/S0368) encrypts user files and disk structures like the MBR with 2048-bit RSA.[^10] [^1] [^9]  |
| [[Masquerading\|T1036]] | Masquerading | [NotPetya](https://attack.mitre.org/software/S0368) drops [PsExec](https://attack.mitre.org/software/S0029) with the filename dllhost.dat.[^10]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [NotPetya](https://attack.mitre.org/software/S0368) uses `rundll32.exe` to install itself on remote systems when accessed via [PsExec](https://attack.mitre.org/software/S0029) or `wmic`.[^10]  |
| [[Local Accounts\|T1078.003]] | Local Accounts | [NotPetya](https://attack.mitre.org/software/S0368) can use valid credentials with [PsExec](https://attack.mitre.org/software/S0029) or `wmic` to spread itself to remote systems.[^10] [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Sandworm Team\|G0034]] | Sandworm Team |



## References

[^1]: [US-CERT NotPetya 2017](https://www.us-cert.gov/ncas/alerts/TA17-181A)


[^2]: [NCSC Sandworm Feb 2020](https://www.ncsc.gov.uk/news/ncsc-supports-sandworm-advisory)


[^3]: [Secureworks IRON VIKING ](https://www.secureworks.com/research/threat-profiles/iron-viking)


[^4]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)


[^5]: Diskcoder.C


[^6]: [ESET Telebots June 2017](https://www.welivesecurity.com/2017/06/30/telebots-back-supply-chain-attacks-against-ukraine/)


[^7]: Petrwrap


[^8]: [PsExec Russinovich](http://windowsitpro.com/systems-management/psexec)


[^9]: [US District Court Indictment GRU Unit 74455 October 2020](https://www.justice.gov/opa/press-release/file/1328521/download)


[^10]: [Talos Nyetya June 2017](https://blog.talosintelligence.com/2017/06/worldwide-ransomware-variant.html)


[^11]: GoldenEye


[^12]: [mandiant_apt44_unearthing_sandworm](https://services.google.com/fh/files/misc/apt44-unearthing-sandworm.pdf)


[^13]: ExPetr


[^14]: [Trend Micro Cyclops Blink March 2022](https://www.trendmicro.com/en_us/research/22/c/cyclops-blink-sets-sights-on-asus-routers--.html)


[^15]: Nyetya


[^16]: [UK NCSC Olympic Attacks October 2020](https://www.gov.uk/government/news/uk-exposes-series-of-russian-cyber-attacks-against-olympic-and-paralympic-games)


