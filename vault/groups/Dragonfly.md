---
aliases: 
    - Dragonfly
    - TEMP.Isotope
    - DYMALLOY
    - Berserk Bear
    - TG-4192
    - Crouching Yeti
    - IRON LIBERTY
    - Energetic Bear
    - Ghost Blizzard
    - BROMINE
mitre-attack: https://attack.mitre.org/groups/G0035
---

## G0035

[Dragonfly](https://attack.mitre.org/groups/G0035) is a cyber espionage group that has been attributed to Russia's Federal Security Service (FSB) Center 16.[^19] [^7]  Active since at least 2010, [Dragonfly](https://attack.mitre.org/groups/G0035) has targeted defense and aviation companies, government entities, companies related to industrial control systems, and critical infrastructure sectors worldwide through supply chain, spearphishing, and drive-by compromise attacks.[^1] [^14] [^27] [^18] [^12] [^13] [^15] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Dragonfly](https://attack.mitre.org/groups/G0035) has compressed data into .zip files prior to exfiltration.[^26]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Dragonfly](https://attack.mitre.org/groups/G0035) has performed screen captures of victims, including by using a tool, scr.exe (which matched the hash of ScreenUtil).[^26] [^27] [^12]  |
| [[Hidden Users\|T1564.002]] | Hidden Users | [Dragonfly](https://attack.mitre.org/groups/G0035) has modified the Registry to hide created user accounts.[^26]  |
| [[Web Shell\|T1505.003]] | Web Shell | [Dragonfly](https://attack.mitre.org/groups/G0035) has commonly created Web shells on victims' publicly accessible email and web servers, which they used to maintain access to a victim network and download additional malicious files.[^26]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Dragonfly](https://attack.mitre.org/groups/G0035) has used various forms of spearphishing in attempts to get users to open malicious attachments.[^12]  |
| [[Business Relationships\|T1591.002]] | Business Relationships | [Dragonfly](https://attack.mitre.org/groups/G0035) has collected open source information to identify relationships between organizations for targeting purposes.[^12]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Dragonfly](https://attack.mitre.org/groups/G0035) has compromised user credentials and used valid accounts for operations.[^26] [^12] [^13]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Dragonfly](https://attack.mitre.org/groups/G0035) has used batch scripts to enumerate network information, including information about trusts, zones, and the domain.[^26]  |
| [[Server\|T1584.004]] | Server | [Dragonfly](https://attack.mitre.org/groups/G0035) has compromised legitimate websites to host C2 and malware modules.[^12]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Dragonfly](https://attack.mitre.org/groups/G0035) has used a batch script to gather folder and file names from victim hosts.[^26] [^12] [^13]  |
| [[Local Account\|T1136.001]] | Local Account | [Dragonfly](https://attack.mitre.org/groups/G0035) has created accounts on victims, including administrator accounts, some of which appeared to be tailored to each individual staging target.[^26]  |
| [[Template Injection\|T1221]] | Template Injection | [Dragonfly](https://attack.mitre.org/groups/G0035) has injected SMB URLs into malicious Word spearphishing attachments to initiate [Forced Authentication](https://attack.mitre.org/techniques/T1187).[^26]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Dragonfly](https://attack.mitre.org/groups/G0035) has exploited CVE-2011-0611 in Adobe Flash Player to gain execution on a targeted system.[^12]  |
| [[Password Cracking\|T1110.002]] | Password Cracking | [Dragonfly](https://attack.mitre.org/groups/G0035) has dropped and executed tools used for password cracking, including Hydra and [CrackMapExec](https://attack.mitre.org/software/S0488).[^26] [^6]  |
| [[Drive-by Target\|T1608.004]] | Drive-by Target | [Dragonfly](https://attack.mitre.org/groups/G0035) has compromised websites to redirect traffic and to host exploit kits.[^12]  |
| [[Query Registry\|T1012]] | Query Registry | [Dragonfly](https://attack.mitre.org/groups/G0035) has queried the Registry to identify victim information.[^26]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Dragonfly](https://attack.mitre.org/groups/G0035) has sent emails with malicious attachments to gain initial access.[^12]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Dragonfly](https://attack.mitre.org/groups/G0035) has compromised targets via strategic web compromise (SWC) utilizing a custom exploit kit.[^14] [^26] [^12]  |
| [[Domains\|T1583.001]] | Domains | [Dragonfly](https://attack.mitre.org/groups/G0035) has registered domains for targeting intended victims.[^13]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [Dragonfly](https://attack.mitre.org/groups/G0035) has dropped and executed SecretsDump to dump password hashes.[^26]  |
| [[Spearphishing Attachment\|T1598.002]] | Spearphishing Attachment | [Dragonfly](https://attack.mitre.org/groups/G0035) has used spearphishing with Microsoft Office attachments to enable harvesting of user credentials.[^26]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Dragonfly](https://attack.mitre.org/groups/G0035) has collected data from local victim systems.[^26]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Dragonfly](https://attack.mitre.org/groups/G0035) has deleted many of its files used during operations as part of cleanup, including removing applications and deleting screenshots.[^26]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [Dragonfly](https://attack.mitre.org/groups/G0035) has used the command line for execution.[^26]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [Dragonfly](https://attack.mitre.org/groups/G0035) has cleared Windows event logs and other logs produced by tools they used, including system, security, terminal services, remote services, and audit logs. The actors also deleted specific Registry keys.[^26]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [Dragonfly](https://attack.mitre.org/groups/G0035) has disabled host-based firewalls. The group has also globally opened port 3389.[^26]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Dragonfly](https://attack.mitre.org/groups/G0035) has modified the Registry to perform multiple techniques through the use of [Reg](https://attack.mitre.org/software/S0075).[^26]  |
| [[Tool\|T1588.002]] | Tool | [Dragonfly](https://attack.mitre.org/groups/G0035) has obtained and used tools such as [Mimikatz](https://attack.mitre.org/software/S0002), [CrackMapExec](https://attack.mitre.org/software/S0488), and [PsExec](https://attack.mitre.org/software/S0029).[^14]  |
| [[Compromise Software Supply Chain\|T1195.002]] | Compromise Software Supply Chain | [Dragonfly](https://attack.mitre.org/groups/G0035) has placed trojanized installers for control system software on legitimate vendor app stores.[^14] [^12]  |
| [[Masquerade Account Name\|T1036.010]] | Masquerade Account Name | [Dragonfly](https://attack.mitre.org/groups/G0035) has created accounts disguised as legitimate backup and service accounts as well as an email administration account.[^26]  |
| [[NTDS\|T1003.003]] | NTDS | [Dragonfly](https://attack.mitre.org/groups/G0035) has dropped and executed SecretsDump to dump password hashes. They also obtained ntds.dit from domain controllers.[^26] [^24]  |
| [[Additional Local or Domain Groups\|T1098.007]] | Additional Local or Domain Groups | [Dragonfly](https://attack.mitre.org/groups/G0035) has added newly created accounts to the administrators group to maintain elevated access.[^26]  |
| [[Virtual Private Server\|T1583.003]] | Virtual Private Server | [Dragonfly](https://attack.mitre.org/groups/G0035) has acquired VPS infrastructure for use in malicious campaigns.[^12]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Dragonfly](https://attack.mitre.org/groups/G0035) has used various types of scripting to perform operations, including batch scripts.[^26]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [Dragonfly](https://attack.mitre.org/groups/G0035) has used SMB for C2.[^26]  |
| [[Spearphishing Link\|T1598.003]] | Spearphishing Link | [Dragonfly](https://attack.mitre.org/groups/G0035) has used spearphishing with PDF attachments containing malicious links that redirected to credential harvesting websites.[^26]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Dragonfly](https://attack.mitre.org/groups/G0035) has used scheduled tasks to automatically log out of created accounts every 8 hours as well as to execute malicious files.[^26]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [Dragonfly](https://attack.mitre.org/groups/G0035) has used batch scripts to enumerate administrators and users in the domain.[^26]  |
| [[Remote Email Collection\|T1114.002]] | Remote Email Collection | [Dragonfly](https://attack.mitre.org/groups/G0035) has accessed email accounts using Outlook Web Access.[^26]  |
| [[Vulnerability Scanning\|T1595.002]] | Vulnerability Scanning | [Dragonfly](https://attack.mitre.org/groups/G0035) has scanned targeted systems for vulnerable Citrix and Microsoft Exchange services.[^13]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Dragonfly](https://attack.mitre.org/groups/G0035) has added the registry value ntdll to the Registry Run key to establish persistence.[^26]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Dragonfly](https://attack.mitre.org/groups/G0035) has copied and installed tools for operations once in the victim environment.[^26]  |
| [[External Remote Services\|T1133]] | External Remote Services | [Dragonfly](https://attack.mitre.org/groups/G0035) has used VPNs and Outlook Web Access (OWA) to maintain access to victim networks.[^26] [^13]  |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | [Dragonfly](https://attack.mitre.org/groups/G0035) has dropped and executed SecretsDump to dump password hashes.[^26] [^24]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Dragonfly](https://attack.mitre.org/groups/G0035) has conducted SQL injection attacks, exploited vulnerabilities CVE-2019-19781 and CVE-2020-0688 for Citrix and MS Exchange, and CVE-2018-13379 for Fortinet VPNs.[^13]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Dragonfly](https://attack.mitre.org/groups/G0035) has identified and browsed file servers in the victim network, sometimes , viewing files pertaining to ICS or Supervisory Control and Data Acquisition (SCADA) systems.[^26]  |
| [[Brute Force\|T1110]] | Brute Force | [Dragonfly](https://attack.mitre.org/groups/G0035) has attempted to brute force credentials to gain access.[^13]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Dragonfly](https://attack.mitre.org/groups/G0035) has moved laterally via RDP.[^26]  |
| [[Forced Authentication\|T1187]] | Forced Authentication | [Dragonfly](https://attack.mitre.org/groups/G0035) has gathered hashed user credentials over SMB using spearphishing attachments with external resource links and by modifying .LNK file icon resources to collect credentials from virtualized systems.[^26] [^12]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Dragonfly](https://attack.mitre.org/groups/G0035) used the command `query user` on victim hosts.[^26]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Dragonfly](https://attack.mitre.org/groups/G0035) has created a directory named "out" in the user's %AppData% folder and copied files to it.[^26]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Dragonfly](https://attack.mitre.org/groups/G0035) has used PowerShell scripts for execution.[^26] [^27]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [Dragonfly](https://attack.mitre.org/groups/G0035) has exploited a Windows Netlogon vulnerability (CVE-2020-1472) to obtain access to Windows Active Directory servers.[^13]  |
| [[Python\|T1059.006]] | Python | [Dragonfly](https://attack.mitre.org/groups/G0035) has used various types of scripting to perform operations, including Python scripts. The group was observed installing Python 2.7 on a victim.[^26]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Dragonfly](https://attack.mitre.org/groups/G0035) has likely obtained a list of hosts in the victim environment.[^26]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Dragonfly](https://attack.mitre.org/groups/G0035) has used batch scripts to enumerate users on a victim domain controller.[^26]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^26]  |
| [[Impacket\|S0357]] | Impacket | [^26] [^24]  |
| [[netsh\|S0108]] | netsh | [^26]  |
| [[MCMD\|S0500]] | MCMD | [^5]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^14]  |
| [[CrackMapExec\|S0488]] | CrackMapExec | [^14] [^26]  |
| [[Reg\|S0075]] | Reg | [^26]  |
| [[PsExec\|S0029]] | PsExec | [^14] [^26] [^27] [^12]  |
| [[Backdoor.Oldrea\|S0093]] | Backdoor.Oldrea | [^1] [^12]  |
| [[Trojan.Karagany\|S0094]] | Trojan.Karagany | [^1] [^2] [^12]  |



## References

[^1]: [Symantec Dragonfly](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)


[^2]: [Secureworks Karagany July 2019](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)


[^3]: TEMP.Isotope


[^4]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^5]: [Secureworks MCMD July 2019](https://www.secureworks.com/research/mcmd-malware-analysis)


[^6]: [Kali Hydra](https://tools.kali.org/password-attacks/hydra)


[^7]: [UK GOV FSB Factsheet April 2022](https://www.gov.uk/government/publications/russias-fsb-malign-cyber-activity-factsheet/russias-fsb-malign-activity-factsheet)


[^8]: Crouching Yeti


[^9]: TG-4192


[^10]: Dragonfly


[^11]: [Dragos DYMALLOY ](https://www.dragos.com/threat/dymalloy/)


[^12]: [Gigamon Berserk Bear October 2021](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)


[^13]: [CISA AA20-296A Berserk Bear December 2020](https://www.cisa.gov/uscert/ncas/alerts/aa20-296a#revisions)


[^14]: [Secureworks IRON LIBERTY July 2019](https://www.secureworks.com/research/resurgent-iron-liberty-targeting-energy-sector)


[^15]: [Symantec Dragonfly 2.0 October 2017](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/dragonfly-energy-sector-cyber-attacks)


[^16]: DYMALLOY


[^17]: Berserk Bear


[^18]: [Fortune Dragonfly 2.0 Sept 2017](http://fortune.com/2017/09/06/hack-energy-grid-symantec/)


[^19]: [DOJ Russia Targeting Critical Infrastructure March 2022](https://www.justice.gov/opa/pr/four-russian-government-employees-charged-two-historical-hacking-campaigns-targeting-critical)


[^20]: Ghost Blizzard


[^21]: BROMINE


[^22]: IRON LIBERTY


[^23]: [Mandiant Ukraine Cyber Threats January 2022](https://www.mandiant.com/resources/ukraine-crisis-cyber-threats)


[^24]: [Core Security Impacket](https://www.coresecurity.com/core-labs/open-source-tools/impacket)


[^25]: Energetic Bear


[^26]: [US-CERT TA18-074A](https://www.us-cert.gov/ncas/alerts/TA18-074A)


[^27]: [Symantec Dragonfly Sept 2017](https://docs.broadcom.com/doc/dragonfly_threat_against_western_energy_suppliers)


