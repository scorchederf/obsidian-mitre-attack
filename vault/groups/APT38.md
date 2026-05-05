---
aliases: 
    - APT38
    - NICKEL GLADSTONE
    - BeagleBoyz
    - Bluenoroff
    - Stardust Chollima
    - Sapphire Sleet
    - COPERNICIUM
mitre-attack: https://attack.mitre.org/groups/G0082
---

## G0082

[APT38](https://attack.mitre.org/groups/G0082) is a North Korean state-sponsored threat group that specializes in financial cyber operations; it has been attributed to the Reconnaissance General Bureau.[^8]  Active since at least 2014, [APT38](https://attack.mitre.org/groups/G0082) has targeted banks, financial institutions, casinos, cryptocurrency exchanges, SWIFT system endpoints, and ATMs in at least 38 countries worldwide. Significant operations include the 2016 Bank of Bangladesh heist, during which [APT38](https://attack.mitre.org/groups/G0082) stole $81 million, as well as attacks against Bancomext [^15]  and Banco de Chile [^15] ; some of their attacks have been destructive.[^8] [^15] [^4] [^5] <br><br>North Korean group definitions are known to have significant overlap, and some security researchers report all North Korean state-sponsored cyber activity under the name [Lazarus Group](https://attack.mitre.org/groups/G0032) instead of tracking clusters or subgroups.

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [APT38](https://attack.mitre.org/groups/G0082) has used Hermes ransomware to encrypt files with AES256.[^15]  |
| [[Process Injection\|T1055]] | Process Injection | [APT38](https://attack.mitre.org/groups/G0082) has injected malicious payloads into the `explorer.exe` process.[^17]   |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [APT38](https://attack.mitre.org/groups/G0082) has identified primary users, currently logged in users, sets of users that commonly use a system, or inactive users.[^8]  |
| [[Modify Registry\|T1112]] | Modify Registry | [APT38](https://attack.mitre.org/groups/G0082) uses a tool called CLEANTOAD that has the capability to modify Registry keys.[^15]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [APT38](https://attack.mitre.org/groups/G0082) installed a port monitoring tool, MAPMAKER, to print the active TCP connections on the local system.[^15]  |
| [[File Deletion\|T1070.004]] | File Deletion | [APT38](https://attack.mitre.org/groups/G0082) has used a utility called CLOSESHAVE that can securely delete a file from the system. They have also removed malware, tools, or other non-native files used during the intrusion to reduce their footprint or as part of the post-intrusion cleanup process.[^15] [^8]  |
| [[Space after Filename\|T1036.006]] | Space after Filename | [APT38](https://attack.mitre.org/groups/G0082) has put several spaces before a file extension to avoid detection and suspicion.[^17]   |
| [[Keylogging\|T1056.001]] | Keylogging | [APT38](https://attack.mitre.org/groups/G0082) used a Trojan called KEYLIME to capture keystrokes from the victim’s machine.[^15]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [APT38](https://attack.mitre.org/groups/G0082) has identified security software, configurations, defensive tools, and sensors installed on a compromised system.[^8] [^17]  |
| [[Windows Service\|T1543.003]] | Windows Service | [APT38](https://attack.mitre.org/groups/G0082) has installed a new Windows service to establish persistence.[^8]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [APT38](https://attack.mitre.org/groups/G0082) has used the legitimate application `ieinstal.exe` to bypass UAC.[^17]   |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [APT38](https://attack.mitre.org/groups/G0082) has conducted watering holes schemes to gain initial access to victims.[^15] [^8]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [APT38](https://attack.mitre.org/groups/G0082) have enumerated files and directories, or searched in specific locations within a compromised host.[^8]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [APT38](https://attack.mitre.org/groups/G0082) has used a command-line tunneler, NACHOCHEESE, to give them shell access to a victim’s machine.[^15]  Additionally, [APT38](https://attack.mitre.org/groups/G0082) has used batch scripts.[^17]   |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [APT38](https://attack.mitre.org/groups/G0082) has used the RC4 algorithm to decrypt configuration data. [^17]   |
| [[Visual Basic\|T1059.005]] | Visual Basic | [APT38](https://attack.mitre.org/groups/G0082) has used VBScript to execute commands and other operational tasks.[^8] [^17]  |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [APT38](https://attack.mitre.org/groups/G0082) has used a custom MBR wiper named BOOTWRECK, which will initiate a system reboot after wiping the victim's MBR.[^15]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [APT38](https://attack.mitre.org/groups/G0082) has used links to execute a malicious Visual Basic script.[^17]   |
| [[Web Protocols\|T1071.001]] | Web Protocols | [APT38](https://attack.mitre.org/groups/G0082) used a backdoor, QUICKRIDE, to communicate to the C2 server over HTTP and HTTPS.[^15]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [APT38](https://attack.mitre.org/groups/G0082) used a backdoor, NESTEGG, that has the capability to download and upload files to and from a victim’s machine.[^15]  Additionally, [APT38](https://attack.mitre.org/groups/G0082) has downloaded other payloads onto a victim’s machine.[^17]   |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [APT38](https://attack.mitre.org/groups/G0082) has unhooked DLLs to disable endpoint detection and response (EDR) or anti-virus (AV) tools.[^17]   |
| [[Software Packing\|T1027.002]] | Software Packing | [APT38](https://attack.mitre.org/groups/G0082) has used several code packing methods such as Themida, Enigma, VMProtect, and Obsidium, to pack their implants.[^15]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [APT38](https://attack.mitre.org/groups/G0082) has collected browser bookmark information to learn more about compromised hosts, obtain personal information about users, and acquire details about internal network resources.[^8]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [APT38](https://attack.mitre.org/groups/G0082) clears Window Event logs and Sysmon logs from the system.[^15]  |
| [[Mshta\|T1218.005]] | Mshta | [APT38](https://attack.mitre.org/groups/G0082) has used a renamed version of `mshta.exe` to execute malicious HTML files.[^17]   |
| [[Timestomp\|T1070.006]] | Timestomp | [APT38](https://attack.mitre.org/groups/G0082) has modified data timestamps to mimic files that are in the same folder on a compromised host.[^8]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [APT38](https://attack.mitre.org/groups/G0082) have created firewall exemptions on specific ports, including ports 443, 6443, 8443, and 9443.[^8]  |
| [[Data Destruction\|T1485]] | Data Destruction | [APT38](https://attack.mitre.org/groups/G0082) has used a custom secure delete function to make deleted files unrecoverable.[^15]  |
| [[Brute Force\|T1110]] | Brute Force | [APT38](https://attack.mitre.org/groups/G0082) has used brute force techniques to attempt account access when passwords are unknown or when password hashes are unavailable.[^8]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [APT38](https://attack.mitre.org/groups/G0082) has enumerated network shares on a compromised host.[^8]  |
| [[Mark-of-the-Web Bypass\|T1553.005]] | Mark-of-the-Web Bypass | [APT38](https://attack.mitre.org/groups/G0082) has used ISO and VHD files to deploy malware and to bypass Mark-of-the-Web (MOTW) security measures.[^17]   |
| [[System Information Discovery\|T1082]] | System Information Discovery | [APT38](https://attack.mitre.org/groups/G0082) has attempted to get detailed information about a compromised host, including the operating system, version, patches, hotfixes, and service packs.[^8]  |
| [[Transmitted Data Manipulation\|T1565.002]] | Transmitted Data Manipulation | [APT38](https://attack.mitre.org/groups/G0082) has used DYEPACK to manipulate SWIFT messages en route to a printer.[^15]  |
| [[Network Device Firewall\|T1686.002]] | Network Device Firewall | [APT38](https://attack.mitre.org/groups/G0082) have created firewall exemptions on specific ports, including ports 443, 6443, 8443, and 9443. [^8]   |
| [[Disk Structure Wipe\|T1561.002]] | Disk Structure Wipe | [APT38](https://attack.mitre.org/groups/G0082) has used a custom MBR wiper named BOOTWRECK to render systems inoperable.[^15]  |
| [[Rename Legitimate Utilities\|T1036.003]] | Rename Legitimate Utilities | [APT38](https://attack.mitre.org/groups/G0082) has renamed system utilities, such as `rundll32.exe` and `mshta.exe`, to avoid detection.[^17]   |
| [[Prevent Command History Logging\|T1690]] | Prevent Command History Logging | [APT38](https://attack.mitre.org/groups/G0082) has prepended a space to all of their terminal commands to operate without leaving traces in the HISTCONTROL environment.[^8]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [APT38](https://attack.mitre.org/groups/G0082) has used Task Scheduler to run programs at system startup or on a scheduled basis for persistence.[^8]  Additionally, [APT38](https://attack.mitre.org/groups/G0082) has used living-off-the-land scripts to execute a malicious script via a scheduled task.[^17]   |
| [[Tool\|T1588.002]] | Tool | [APT38](https://attack.mitre.org/groups/G0082) has obtained and used open-source tools such as [Mimikatz](https://attack.mitre.org/software/S0002).[^12]  |
| [[Web Shell\|T1505.003]] | Web Shell | [APT38](https://attack.mitre.org/groups/G0082) has used web shells for persistence or to ensure redundant access.[^8]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [APT38](https://attack.mitre.org/groups/G0082) used a Trojan called KEYLIME to collect data from the clipboard.[^15]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [APT38](https://attack.mitre.org/groups/G0082) has used rundll32.exe to execute binaries, scripts, and Control Panel Item files and to execute code via proxy to avoid triggering security tools.[^8] [^17]  |
| [[Runtime Data Manipulation\|T1565.003]] | Runtime Data Manipulation | [APT38](https://attack.mitre.org/groups/G0082) has used DYEPACK.FOX to manipulate PDF data as it is accessed to remove traces of fraudulent SWIFT transactions from the data displayed to the end user.[^15]  |
| [[Domains\|T1583.001]] | Domains | [APT38](https://attack.mitre.org/groups/G0082) has created fake domains to imitate legitimate venture capital or bank domains.[^17]   |
| [[Native API\|T1106]] | Native API | [APT38](https://attack.mitre.org/groups/G0082) has used the Windows API to execute code within a victim's system.[^8]   |
| [[Compiled HTML File\|T1218.001]] | Compiled HTML File | [APT38](https://attack.mitre.org/groups/G0082) has used CHM files to move concealed payloads.[^3]  |
| [[Malicious File\|T1204.002]] | Malicious File | [APT38](https://attack.mitre.org/groups/G0082)  has attempted to lure victims into enabling malicious macros within email attachments.[^8]  Additionally, [APT38](https://attack.mitre.org/groups/G0082) has used malicious Word documents and shortcut files.[^17]   |
| [[Stored Data Manipulation\|T1565.001]] | Stored Data Manipulation | [APT38](https://attack.mitre.org/groups/G0082) has used DYEPACK to create, delete, and alter records in databases used for SWIFT transactions.[^15]  |
| [[Data from Local System\|T1005]] | Data from Local System | [APT38](https://attack.mitre.org/groups/G0082) has collected data from a compromised host.[^8]  |
| [[PowerShell\|T1059.001]] | PowerShell | [APT38](https://attack.mitre.org/groups/G0082) has used PowerShell to execute commands and other operational tasks.[^8]  |
| [[Cron\|T1053.003]] | Cron | [APT38](https://attack.mitre.org/groups/G0082) has used cron to create pre-scheduled and periodic background jobs on a Linux system.[^8]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [APT38](https://attack.mitre.org/groups/G0082) has conducted spearphishing campaigns using malicious email attachments.[^8]  |
| [[Msiexec\|T1218.007]] | Msiexec | [APT38](https://attack.mitre.org/groups/G0082) has used `msiexec.exe` to execute malicious files.[^17]   |
| [[Service Execution\|T1569.002]] | Service Execution | [APT38](https://attack.mitre.org/groups/G0082) has created new services or modified existing ones to run executables, commands, or scripts.[^8]  |
| [[Mutual Exclusion\|T1480.002]] | Mutual Exclusion | [APT38](https://attack.mitre.org/groups/G0082) has created a mutex to avoid duplicate execution.[^17]   |
| [[Process Discovery\|T1057]] | Process Discovery | [APT38](https://attack.mitre.org/groups/G0082) leveraged Sysmon to understand the processes, services in the organization.[^15]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^15]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^15]  |
| [[HOPLIGHT\|S0376]] | HOPLIGHT | [^8]  |
| [[DarkComet\|S0334]] | DarkComet | [^15]  |
| [[KillDisk\|S0607]] | KillDisk | [^12]  |
| [[ECCENTRICBANDWAGON\|S0593]] | ECCENTRICBANDWAGON | [^8]  |



## References

[^1]: Bluenoroff


[^2]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^3]: [Kaspersky Lazarus Under The Hood APR 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180244/Lazarus_Under_The_Hood_PDF_final.pdf)


[^4]: [DOJ North Korea Indictment Feb 2021](https://www.justice.gov/opa/pr/three-north-korean-military-hackers-indicted-wide-ranging-scheme-commit-cyberattacks-and)


[^5]: [Kaspersky Lazarus Under The Hood Blog 2017](https://securelist.com/lazarus-under-the-hood/77908/)


[^6]: Stardust Chollima


[^7]: NICKEL GLADSTONE


[^8]: [CISA AA20-239A BeagleBoyz August 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-239a)


[^9]: APT38


[^10]: [SecureWorks NICKEL GLADSTONE profile Sept 2021](https://www.secureworks.com/research/threat-profiles/nickel-gladstone)


[^11]: [CrowdStrike Stardust Chollima Profile April 2018](https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-april-stardust-chollima/)


[^12]: [ESET Lazarus KillDisk April 2018](https://www.welivesecurity.com/2018/04/03/lazarus-killdisk-central-american-casino/)


[^13]: COPERNICIUM


[^14]: [CrowdStrike GTR 2021 June 2021](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2021GTR.pdf)


[^15]: [FireEye APT38 Oct 2018](https://services.google.com/fh/files/misc/apt38-un-usual-suspects.pdf)


[^16]: Sapphire Sleet


[^17]: [1 - appv](https://securelist.com/bluenoroff-methods-bypass-motw/108383/)


[^18]: BeagleBoyz


