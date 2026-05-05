---
aliases: 
    - APT5
    - Mulberry Typhoon
    - MANGANESE
    - BRONZE FLEETWOOD
    - Keyhole Panda
    - UNC2630
mitre-attack: https://attack.mitre.org/groups/G1023
---

## G1023

[APT5](https://attack.mitre.org/groups/G1023) is a China-based espionage actor that has been active since at least 2007 primarily targeting the telecommunications, aerospace, and defense industries throughout the U.S., Europe, and Asia. [APT5](https://attack.mitre.org/groups/G1023) has displayed advanced tradecraft and significant interest in compromising networking devices and their underlying software including through the use of zero-day exploits.[^10] [^4] [^9] [^7] [^11] [^1]   

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[PowerShell\|T1059.001]] | PowerShell | [APT5](https://attack.mitre.org/groups/G1023) has used PowerShell to accomplish tasks within targeted environments.[^7]  |
| [[Local Account\|T1136.001]] | Local Account | [APT5](https://attack.mitre.org/groups/G1023) has created Local Administrator accounts to maintain access to systems with short-cycle credential rotation.[^7]  |
| [[Timestomp\|T1070.006]] | Timestomp | [APT5](https://attack.mitre.org/groups/G1023) has modified file timestamps.[^7]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [APT5](https://attack.mitre.org/groups/G1023) has moved laterally throughout victim environments using RDP.[^7]  |
| [[Log Enumeration\|T1654]] | Log Enumeration | [APT5](https://attack.mitre.org/groups/G1023) has used the BLOODMINE utility to parse and extract information from Pulse Secure Connect logs.[^7]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [APT5](https://attack.mitre.org/groups/G1023) has used the CLEANPULSE utility to insert command line strings into a targeted process to prevent certain log events from occurring.[^7]  |
| [[Botnet\|T1583.005]] | Botnet | [APT5](https://attack.mitre.org/groups/G1023) has acquired a network of compromised systems – specifically an ORB (operational relay box) network – for follow on activities.[^3]    |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [APT5](https://attack.mitre.org/groups/G1023) has staged data on compromised systems prior to exfiltration often in `C:\Users\Public`.[^7]  |
| [[Compromise Host Software Binary\|T1554]] | Compromise Host Software Binary | [APT5](https://attack.mitre.org/groups/G1023) has modified legitimate binaries and scripts for Pulse Secure VPNs including the legitimate DSUpgrade.pm file to install the ATRIUM webshell for persistence.[^9] [^7]  |
| [[Keylogging\|T1056.001]] | Keylogging | [APT5](https://attack.mitre.org/groups/G1023) has used malware with keylogging capabilities to monitor the communications of targeted entities.[^11] [^1]  |
| [[Cloud Accounts\|T1078.004]] | Cloud Accounts | [APT5](https://attack.mitre.org/groups/G1023) has accessed Microsoft M365 cloud environments using stolen credentials. [^7]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [APT5](https://attack.mitre.org/groups/G1023) has used the JAR/ZIP file format for exfiltrated files.[^7]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [APT5](https://attack.mitre.org/groups/G1023) has used the Task Manager process to target LSASS process memory in order to obtain NTLM password hashes. [APT5](https://attack.mitre.org/groups/G1023) has also dumped clear text passwords and hashes from memory using [Mimikatz](https://attack.mitre.org/software/S0002) hosted through an RDP mapped drive.[^7]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [APT5](https://attack.mitre.org/groups/G1023) has copied and exfiltrated the SAM Registry hive from targeted systems.[^7]  |
| [[File Deletion\|T1070.004]] | File Deletion | [APT5](https://attack.mitre.org/groups/G1023) has deleted scripts and web shells to evade detection.[^9] [^7]  |
| [[Additional Local or Domain Groups\|T1098.007]] | Additional Local or Domain Groups | [APT5](https://attack.mitre.org/groups/G1023) has created their own accounts with Local Administrator privileges to maintain access to systems with short-cycle credential rotation.[^7]  |
| [[Process Discovery\|T1057]] | Process Discovery | [APT5](https://attack.mitre.org/groups/G1023) has used Windows-based utilities to carry out tasks including tasklist.exe. [^7]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [APT5](https://attack.mitre.org/groups/G1023) has used the THINBLOOD utility to clear SSL VPN log files located at `/home/runtime/logs`.[^9] [^7]  |
| [[Cron\|T1053.003]] | Cron | [APT5](https://attack.mitre.org/groups/G1023) has made modifications to the crontab file including in `/var/cron/tabs/`.[^10]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [APT5](https://attack.mitre.org/groups/G1023) has used cmd.exe for execution on compromised systems.[^7]  |
| [[SSH\|T1021.004]] | SSH | [APT5](https://attack.mitre.org/groups/G1023) has used SSH for lateral movement in compromised environments including for enabling access to ESXi host servers.[^7]  |
| [[Process Injection\|T1055]] | Process Injection | [APT5](https://attack.mitre.org/groups/G1023) has used the CLEANPULSE utility to insert command line strings into a targeted process to alter its functionality.[^7]  |
| [[Web Shell\|T1505.003]] | Web Shell | [APT5](https://attack.mitre.org/groups/G1023) has installed multiple web shells on compromised servers including on Pulse Secure VPN appliances.[^9] [^7]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [APT5](https://attack.mitre.org/groups/G1023) has used the BLOODMINE utility to collect data on web requests from Pulse Secure Connect logs.[^7]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [APT5](https://attack.mitre.org/groups/G1023) has used legitimate account credentials to move laterally through compromised environments.[^9]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [APT5](https://attack.mitre.org/groups/G1023) has named exfiltration archives to mimic Windows Updates at times using filenames with a `KB<digits>.zip` pattern.[^7]  |
| [[Clear Command History\|T1070.003]] | Clear Command History | [APT5](https://attack.mitre.org/groups/G1023) has cleared the command history on targeted ESXi servers.[^7]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [APT5](https://attack.mitre.org/groups/G1023) has used the BLOODMINE utility to discover files with .css, .jpg, .png, .gif, .ico, .js, and .jsp extensions in Pulse Secure Connect logs.[^7]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [APT5](https://attack.mitre.org/groups/G1023) has exploited vulnerabilities in externally facing software and devices including Pulse Secure VPNs and Citrix Application Delivery Controllers.[^9] [^7] [^10]  [^4]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^7]  |
| [[Tasklist\|S0057]] | Tasklist | [^7]  |
| [[PcShare\|S1050]] | PcShare | [^12]  |
| [[netstat\|S0104]] | netstat | [^7]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^7]  |
| [[PACEMAKER\|S1109]] | PACEMAKER | [^9]  |
| [[RAPIDPULSE\|S1113]] | RAPIDPULSE | [^7]  |
| [[gh0st RAT\|S0032]] | gh0st RAT | [^12]  |
| [[Skeleton Key\|S0007]] | Skeleton Key | [^12]  |
| [[PULSECHECK\|S1108]] | PULSECHECK | [^9]  |
| [[PoisonIvy\|S0012]] | PoisonIvy | [^1]  |
| [[SLIGHTPULSE\|S1110]] | SLIGHTPULSE | [^9] [^7]  |
| [[SLOWPULSE\|S1104]] | SLOWPULSE | [^9]  |



## References

[^1]: [Mandiant Advanced Persistent Threats](https://www.mandiant.com/resources/insights/apt-groups)


[^2]: UNC2630


[^3]: [ORB Mandiant](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-espionage-orb-networks)


[^4]: [Microsoft East Asia Threats September 2023](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RW1aFyW)


[^5]: Mulberry Typhoon


[^6]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^7]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)


[^8]: Keyhole Panda


[^9]: [Mandiant Pulse Secure Zero-Day April 2021](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)


[^10]: [NSA APT5 Citrix Threat Hunting December 2022](https://media.defense.gov/2022/Dec/13/2003131586/-1/-1/0/CSA-APT5-CITRIXADC-V1.PDF)


[^11]: [FireEye Southeast Asia Threat Landscape March 2015](https://web.archive.org/web/20220122121143/https://www.fireeye.com/content/dam/fireeye-www/current-threats/pdfs/rpt-southeast-asia-threat-landscape.pdf)


[^12]: [Secureworks BRONZE FLEETWOOD Profile](https://www.secureworks.com/research/threat-profiles/bronze-fleetwood)


[^13]: BRONZE FLEETWOOD


[^14]: MANGANESE


