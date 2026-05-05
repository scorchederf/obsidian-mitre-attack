---
aliases: 
    - S0032
    
mitre-attack: https://attack.mitre.org/software/S0032
---

## S0032

[gh0st RAT](https://attack.mitre.org/software/S0032) is a remote access tool (RAT). The source code is public and it has been used by multiple groups.[^19] [^16] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Shared Modules\|T1129]] | Shared Modules | [gh0st RAT](https://attack.mitre.org/software/S0032) can load DLLs into memory.[^8]  |
| [[Modify Registry\|T1112]] | Modify Registry | [gh0st RAT](https://attack.mitre.org/software/S0032) has altered the InstallTime subkey.[^8]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [gh0st RAT](https://attack.mitre.org/software/S0032) can download files to the victim’s machine.[^2] [^8]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [gh0st RAT](https://attack.mitre.org/software/S0032) is able to wipe event logs.[^19] [^8]  |
| [[Process Injection\|T1055]] | Process Injection | [gh0st RAT](https://attack.mitre.org/software/S0032) can inject malicious code into process created by the “Command_Create&Inject” function.[^8]  |
| [[Rundll32\|T1218.011]] | Rundll32 | A [gh0st RAT](https://attack.mitre.org/software/S0032) variant has used rundll32 for execution.[^16]  |
| [[Service Execution\|T1569.002]] | Service Execution | [gh0st RAT](https://attack.mitre.org/software/S0032) can execute its service if the Service key exists. If the key does not exist, [gh0st RAT](https://attack.mitre.org/software/S0032) will create and run the service.[^8]  |
| [[DLL\|T1574.001]] | DLL | A [gh0st RAT](https://attack.mitre.org/software/S0032) variant has used DLL side-loading.[^16]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [gh0st RAT](https://attack.mitre.org/software/S0032) is able to open a remote shell to execute commands.[^19] [^2]  |
| [[Query Registry\|T1012]] | Query Registry | [gh0st RAT](https://attack.mitre.org/software/S0032) has checked for the existence of a Service key to determine if it has already been installed on the system.[^8]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [gh0st RAT](https://attack.mitre.org/software/S0032) has decrypted and loaded the [gh0st RAT](https://attack.mitre.org/software/S0032) DLL into memory, once the initial dropper executable is launched.[^8]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [gh0st RAT](https://attack.mitre.org/software/S0032) uses RC4 and XOR to encrypt C2 traffic.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [gh0st RAT](https://attack.mitre.org/software/S0032) has used an encrypted protocol within TCP segments to communicate with the C2.[^8]  |
| [[Native API\|T1106]] | Native API | [gh0st RAT](https://attack.mitre.org/software/S0032) has used the `InterlockedExchange`, `SeShutdownPrivilege`, and `ExitWindowsEx` Windows API functions.[^8]  |
| [[Process Discovery\|T1057]] | Process Discovery | [gh0st RAT](https://attack.mitre.org/software/S0032) has the capability to list processes.[^19]  |
| [[Windows Service\|T1543.003]] | Windows Service | [gh0st RAT](https://attack.mitre.org/software/S0032) can create a new service to establish persistence.[^2] [^8]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [gh0st RAT](https://attack.mitre.org/software/S0032) has added a Registry Run key to establish persistence.[^2] [^8]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [gh0st RAT](https://attack.mitre.org/software/S0032) has gathered system architecture, processor, OS configuration, and installed hardware information.[^8]  |
| [[File Deletion\|T1070.004]] | File Deletion | [gh0st RAT](https://attack.mitre.org/software/S0032) has the capability to to delete files.[^19] [^8]  |
| [[Screen Capture\|T1113]] | Screen Capture | [gh0st RAT](https://attack.mitre.org/software/S0032) can capture the victim’s screen remotely.[^2]  |
| [[Fast Flux DNS\|T1568.001]] | Fast Flux DNS | [gh0st RAT](https://attack.mitre.org/software/S0032) operators have used dynamic DNS to mask the true location of their C2 behind rapidly changing IP addresses.[^8]  |
| [[Keylogging\|T1056.001]] | Keylogging | [gh0st RAT](https://attack.mitre.org/software/S0032) has a keylogger.[^5] [^8]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [gh0st RAT](https://attack.mitre.org/software/S0032) has used Zlib to compress C2 communications data before encrypting it.[^8]  |
| [[Encrypted Channel\|T1573]] | Encrypted Channel | [gh0st RAT](https://attack.mitre.org/software/S0032) has encrypted TCP communications to evade detection.[^8]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA459\|G0062]] | TA459 |
| [[APT41\|G0096]] | APT41 |
| [[PittyTiger\|G0011]] | PittyTiger |
| [[Axiom\|G0001]] | Axiom |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 |
| [[Kimsuky\|G0094]] | Kimsuky |
| [[Leviathan\|G0065]] | Leviathan |
| [[APT18\|G0026]] | APT18 |
| [[Higaisa\|G0126]] | Higaisa |
| [[Andariel\|G0138]] | Andariel |
| [[APT5\|G1023]] | APT5 |



## References

[^1]: [Secureworks BRONZEUNION Feb 2019](https://www.secureworks.com/research/a-peek-into-bronze-unions-toolbox)


[^2]: [Nccgroup Gh0st April 2018](https://research.nccgroup.com/2018/04/17/decoding-network-data-from-a-gh0st-rat-variant/)


[^3]: [Malwarebytes Higaisa 2020](https://blog.malwarebytes.com/threat-analysis/2020/06/higaisa/)


[^4]: [Cisco Group 72](http://blogs.cisco.com/security/talos/threat-spotlight-group-72)


[^5]: [Alintanahin 2014](http://blog.trendmicro.com/trendlabs-security-intelligence/kunming-attack-leads-to-gh0st-rat-variant/)


[^6]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)


[^7]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^8]: [Gh0stRAT ATT March 2019](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)


[^9]: gh0st RAT


[^10]: Mydoor


[^11]: [RSA2017 Detect and Respond Adair](https://web.archive.org/web/20210803040540/https://published-prd.lanyonevents.com/published/rsaus17/sessionsFiles/5009/HTA-F02-Detecting-and-Responding-to-Advanced-Threats-within-Exchange-Environments.pdf)


[^12]: Moudoor


[^13]: [Bizeul 2014](https://airbus-cyber-security.com/the-eye-of-the-tiger/)


[^14]: [Proofpoint TA459 April 2017](https://www.proofpoint.com/us/threat-insight/post/apt-targets-financial-analysts)


[^15]: [CISA AA21-200A APT40 July 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-200a)


[^16]: [Arbor Musical Chairs Feb 2018](https://www.arbornetworks.com/blog/asert/musical-chairs-playing-tetris/)


[^17]: [Secureworks BRONZE FLEETWOOD Profile](https://www.secureworks.com/research/threat-profiles/bronze-fleetwood)


[^18]: [Villeneuve 2014](https://www.fireeye.com/blog/threat-research/2014/07/spy-of-the-tiger.html)


[^19]: [FireEye Hacking Team](https://www.fireeye.com/blog/threat-research/2015/07/demonstrating_hustle.html)


[^20]: [Mandiant APT43 March 2024](https://services.google.com/fh/files/misc/apt43-report-en.pdf)


[^21]: [AhnLab Andariel Subgroup of Lazarus June 2018](https://web.archive.org/web/20230213154832/http://download.ahnlab.com/global/brochure/%5BAnalysis%5DAndariel_Group.pdf)


