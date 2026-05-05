---
aliases: 
    - T1033
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1033-System_Owner_User_Discovery
tactic: 
     - Discovery
platforms:
     - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may attempt to identify the primary user, currently logged in user, set of users that commonly uses a system, or whether a user is actively using the system. They may do this, for example, by retrieving account usernames or by using [[kb/mitre/attack/techniques/T1003-OS_Credential_Dumping\|OS Credential Dumping]]. The information may be collected in a number of different ways using other Discovery techniques, because user and username details are prevalent throughout a system and include running process ownership, file/directory ownership, session information, and system logs. Adversaries may use the information from [[kb/mitre/attack/techniques/T1033-System_Owner_User_Discovery\|System Owner/User Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.<br><br>Various utilities and commands may acquire this information, including `whoami`. In macOS and Linux, the currently logged in user can be identified with `w` and `who`. On macOS the `dscl . list /Users | grep -v '_'` command can also be used to enumerate user accounts. Environment variables, such as `%USERNAME%` and `$USER`, may also be used to access this information.<br><br>On network devices, [[kb/mitre/attack/techniques/T1059.008-Network_Device_CLI\|Network Device CLI]] commands such as `show users` and `show ssh` can be used to display users currently logged into the device.[^4] [^7] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0192-Pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can enumerate local information for Linux hosts and find currently logged on users for Windows hosts.[^12]  |
| [[kb/mitre/attack/software/S0250-Koadic\|S0250]] | Koadic | [[kb/mitre/attack/software/S0250-Koadic\|Koadic]] can identify logged in users across the domain and views user sessions.[^13] [^1]  |
| [[kb/mitre/attack/software/S0262-QuasarRAT\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can enumerate the username and account type.[^11]  |
| [[kb/mitre/attack/software/S0332-Remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can enumerate the username on targeted hosts.[^8]  |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can enumerate the username on targeted hosts.[^5]  |
| [[kb/mitre/attack/software/S0521-BloodHound\|S0521]] | BloodHound | [[kb/mitre/attack/software/S0521-BloodHound\|BloodHound]] can collect information on user sessions.[^2]  |
| [[kb/mitre/attack/software/S0590-NBTscan\|S0590]] | NBTscan | [[kb/mitre/attack/software/S0590-NBTscan\|NBTscan]] can list active users on the system.[^3] [^10] 	 |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can gather a list of logged on users.[^9]   |
| [[kb/mitre/attack/software/S1087-AsyncRAT\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can check if the current user of a compromised system is an administrator. [^6]  |








> [!info]- References
> [^1]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)

> [^2]: [CrowdStrike BloodHound April 2018](https://www.crowdstrike.com/blog/hidden-administrative-accounts-bloodhound-to-the-rescue/)

> [^3]: [Debian nbtscan Nov 2019](https://manpages.debian.org/testing/nbtscan/nbtscan.1.en.html)

> [^4]: [show_ssh_users_cmd_cisco](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/security/s1/sec-s1-cr-book/sec-cr-s5.html)

> [^5]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)

> [^6]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)

> [^7]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)

> [^8]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)

> [^9]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^10]: [SecTools nbtscan June 2003](https://sectools.org/tool/nbtscan/)

> [^11]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)

> [^12]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)

> [^13]: [Github Koadic](https://github.com/offsecginger/koadic)


