---
aliases: 
    - VOID MANTICORE
    - COBALT MYSTIQUE
    - Handala Hack
    - Homeland Justice
    - Karma
    - Karmabelow80
    - BANISHED KITTEN
    - Red Sandstorm
mitre-attack: https://attack.mitre.org/groups/G1055
---

## G1055

[VOID MANTICORE](https://attack.mitre.org/groups/G1055) is a threat group assessed to operate on behalf of Iran’s Ministry of Intelligence and Security (MOIS).[^1]  Active since at least mid-2022, VOID MANTICORE has targeted government entities, critical infrastructure, and private sector organizations across Albania, Israel, and the United States.[^1] [^7]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) conducts destructive cyber operations, combining wiper attacks with hack-and-leak campaigns. The group has operated under multiple public-facing personas, including (LinkByld: C0038) in operations against Albania, Karma and Karma Below in campaigns targeting Israeli organizations, and Handala Hack, its current primary persona, which has claimed activity against Israeli and U.S. entities, including a March 2026 attack against Stryker Corporation.[^1] [^9]   [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has been observed collaborating with Scarred Manticore, which has been linked to initial access operations preceding VOID MANTICORE’s activity.[^11]  

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Screen Capture\|T1113]] | Screen Capture | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has captured screen content during an active Zoom session.[^8]  |
| [[Password Guessing\|T1110.001]] | Password Guessing | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has conducted password guessing to gain initial access.[^11]  |
| [[Automated Collection\|T1119]] | Automated Collection | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) conducted large-scale data exfiltration in the Stryker operation, consistent with automated or scripted collection against enterprise systems.[^11]  |
| [[Disk Content Wipe\|T1561.001]] | Disk Content Wipe | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized a disk wiping utility to facilitate destructive actions on victim servers.[^9]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also utilized legitimate remote disk wiping commands.[^5]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized legitimate disk encryption utilities to increase likelihood of encrypting system drives and reduce system recovery efforts.[^1] [^9]  |
| [[Phishing\|T1566]] | Phishing | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has emailed victims threatening messages.[^9]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has used phishing as an initial access vector.[^11]  |
| [[Gather Victim Identity Information\|T1589]] | Gather Victim Identity Information | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has gathered details on their intended victims to aid in social engineering efforts for leveraging tailored themes of attacks.[^8]  |
| [[Financial Theft\|T1657]] | Financial Theft | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has conducted data exfiltration and posted stolen information on data leak sites for the purposes of financial and political extortion.[^5] [^9]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also sold stolen data to prospective buyers for cryptocurrency.[^9]  |
| [[Web Service\|T1102]] | Web Service | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized Telegram API for C2.[^9] [^8]  |
| [[PowerShell\|T1059.001]] | PowerShell | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized PowerShell to execute malware in victim environments.[^9] [^8]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized WMIC to log into the victim host and create a process `process call create “cmd.exe /c  copy \\?\\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\system32\config\system c:\users\public”`.[^1]  |
| [[Group Policy Modification\|T1484.001]] | Group Policy Modification | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) had utilized Group Policy logon scripts to distribute the malicious payloads to victim devices through the execution of a batch file.[^1]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized PowerShell scripts that run without notifying the user of its execution to include `-nop -w hidden- ep bypass -enc`.[^8]  |
| [[Domains\|T1583.001]] | Domains | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has registered domains for messaging purposes.[^5]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has created typosquatted domains and sub-domains in attempts to avoid detection or draw suspicion.[^9] [^8]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also purchased domains leveraging cryptocurrency platforms to include LiteCoin and Ramzinex.[^9]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has registered and rotated domains to support public-facing dissemination infrastructure, replacing disrupted domains with new registrations.[^11]  |
| [[Audio Capture\|T1123]] | Audio Capture | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has gathered audio during a Zoom session.[^8]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has exploited public facing vulnerabilities within victim environments to include SharePoint CVE-2019-0604.[^9]  |
| [[Remote Email Collection\|T1114.002]] | Remote Email Collection | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has gathered victim email-content from victim servers.[^9]  |
| [[Data Staged\|T1074]] | Data Staged | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has staged compressed files in specified locations prior to exfiltration over C2.[^8]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has used previously compromised Domain Administrator credentials to maintain persistent access.[^1]  |
| [[Compression\|T1027.015]] | Compression | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has compressed their payloads by leveraging zip files.[^8]  |
| [[Impersonation\|T1684.001]] | Impersonation | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has impersonated individuals familiar to the victim and technical support associated with social messaging services.[^8]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has masqueraded malicious payloads to resemble legitimate applications.[^9] [^8]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has leveraged malicious payloads that use nomenclature associated with common applications that include Pictory, KeePass, WhatsApp, and Telegram.[^8]  |
| [[Selective Exclusion\|T1679]] | Selective Exclusion | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has avoided interacting with specific directories in order to reduce the likelihood of detection.[^8]  |
| [[Domain Account\|T1087.002]] | Domain Account | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized ADRecon to enumerate the active directory environment.[^1]  |
| [[Malware\|T1588.001]] | Malware | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has developed or obtained trojanized applications used for persistent surveillance of targeted individuals.[^11]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has deleted virtual machines directly from the virtualization platform.[^1]  |
| [[Software Deployment Tools\|T1072]] | Software Deployment Tools | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has leveraged legitimate built-in features of cloud-based management platforms to include mobile device management (MDM) and Remote Monitoring and Management (RMM) solutions.[^5] [^7]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also initiated built-in remote wipe instructions using a privileged account within Microsoft Intune.[^5] [^7]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has dumped LSASS credentials using `comsvcs.dll` via `rundll32.exe`.[^1]  |
| [[Cloud Administration Command\|T1651]] | Cloud Administration Command | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has abused built-in remote wipe or factory reset commands to wipe devices managed within an organization’s Cloud management solution impacting laptops, servers, and mobile devices.[^7]  |
| [[Virtual Private Server\|T1583.003]] | Virtual Private Server | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized VPS solutions for C2.[^1]  |
| [[Web Services\|T1583.006]] | Web Services | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has obtained access to commercial VPN services to launch malicious activity.[^1] [^5]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also leveraged Starlink internet services.[^1]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has used operator-controlled Telegram bots and channels as C2 infrastructure.[^11]  |
| [[Windows Host Firewall\|T1686.003]] | Windows Host Firewall | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has disabled Windows Defender protections to allow for follow-on activities within the compromised host.[^1]  |
| [[Credentials in Registry\|T1552.002]] | Credentials in Registry | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) had exported credentials from registry hives to include those stored in HKLM.[^1]  |
| [[Sharepoint\|T1213.002]] | Sharepoint | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has accessed victim’s public facing SharePoint servers and exfiltrated data.[^9]  |
| [[Remote Desktop Software\|T1219.002]] | Remote Desktop Software | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has installed NetBird on victim devices to create a mesh network that facilitated control of several victim devices at once.[^1]  |
| [[Vulnerability Scanning\|T1595.002]] | Vulnerability Scanning | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has scanned victim environments for susceptibility to vulnerability exploitation.[^9]  |
| [[Disk Structure Wipe\|T1561.002]] | Disk Structure Wipe | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has deployed custom wipers that overwrite system files and the host devices master boot records (MBR) to corrupt or destroy files.[^1]  |
| [[Server\|T1583.004]] | Server | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has leveraged backend servers within Iran.[^9]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has deployed additional payloads from dedicated C2 servers.[^1] [^9] [^8]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also downloaded legitimate tools and software from publicly available services.[^1]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) had utilized VeraCrypt a legitimate disk encrypting utility that was downloaded directly from the website.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has gathered system information and disseminated it back to C2.[^8]  |
| [[Cloud Accounts\|T1078.004]] | Cloud Accounts | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has leveraged privileged cloud accounts to access cloud-based management consoles to include Microsoft Intune.[^7]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also compromised existing accounts within the Microsoft Entra ID environment.[^6]  |
| [[External Remote Services\|T1133]] | External Remote Services | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has leveraged public facing VPN infrastructure to gain initial access to victim environments.[^1]  |
| [[Tool\|T1588.002]] | Tool | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has obtained and utilized commercial VPN services, open-source software and publicly available offensive security tools to facilitate malicious activities.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has created Windows Registry entries to autorun stage two malware payloads to maintain persistence.[^8]  |
| [[Malicious File\|T1204.002]] | Malicious File | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has delivered malicious payloads that initiate through user execution to include interaction with a masqueraded file.[^9] [^8]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has used trojanized application lures to induce targets into executing malware enabling persistent surveillance.[^11]  |
| [[Data from Local System\|T1005]] | Data from Local System | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has collected cached data and files from within the victim environment.[^5] [^9] [^8]  |
| [[Account Manipulation\|T1098]] | Account Manipulation | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has leveraged access to administrative control systems to achieve disruptive effects, consistent with administrative account abuse or privilege escalation within existing access.[^11] [^14]  |
| [[Video Capture\|T1125]] | Video Capture | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has collected video from compromised victim devices.[^8]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has used tunneling tools to facilitate destructive attacks on compromised devices.[^1]  |
| [[Malware\|T1587.001]] | Malware | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized custom-malware and wipers to include BiBi Wiper.[^9]  |
| [[Email Accounts\|T1585.002]] | Email Accounts | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has created email accounts to send threatening messages to victims to include ‘Handala_Team[@]outlook[.]com’.[^9]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized HTTPS for communication to C2 domains.[^8]  |
| [[Trusted Relationship\|T1199]] | Trusted Relationship | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has targeted IT and service providers in an effort to obtain credentials, relying largely on compromised VPN accounts for initial access.[^1]  |
| [[Credential Stuffing\|T1110.004]] | Credential Stuffing | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized credential stuffing attacks to obtain initial access to victim environments.[^11]  |
| [[Social Media Accounts\|T1585.001]] | Social Media Accounts | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has created Telegram Accounts.[^8]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also leveraged online personas such as Handala Hack, Karma, and Homeland Justice on social media to include Telegram.[^1] [^5] [^9]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has established and maintained social media accounts on Twitter/X and Telegram to amplify operational claims and stolen data disclosures.[^11]  |
| [[Data Destruction\|T1485]] | Data Destruction | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has conducted data wiping attacks on compromised systems.[^1] [^5] [^9] [^7]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also manually deleted files from compromised hosts, to include selecting all files and then deleting them.[^1] [^9]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has leveraged valid accounts to log into VPN infrastructure.[^1]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has used compromised valid credentials to gain access to management infrastructure and enterprise control systems.[^11]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also validated and tested authentication using compromised credentials prior to malicious actions.[^1]  |
| [[Brute Force\|T1110]] | Brute Force | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has conducted brute-force attempts against organizational VPN infrastructure.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has masqueraded as commonly used programs and services on Windows hosts.[^8]  |
| [[Python\|T1059.006]] | Python | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized Python scripts to execute its malicious payloads.[^8]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has stored collected data in a password protected compressed file prior to exfiltration.[^8]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) malware has exfiltrated collected data via Telegram bot C2 channels using encrypted communications.[^11]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has used RDP to move laterally within the victim environment.[^1]  |




## References

[^1]: [Check Point VOID MANTICORE Handala Hack March 2026](https://research.checkpoint.com/2026/handala-hack-unveiling-groups-modus-operandi/)


[^2]: Homeland Justice


[^3]: Karma


[^4]: Karmabelow80


[^5]: [SPECOPS Outpost24 Handala Hack Stryker March 2026](https://specopssoft.com/blog/stryker-cyber-attack-what-we-know-remote-wipe/)


[^6]: [SEC 8-K Stryker Corporation Filing Handala Hack March 2026](https://www.sec.gov/ix?doc=/Archives/edgar/data/0000310764/000119312526118634/d94012d8k.htm)


[^7]: [Palo Alto VOID MANTICORE Iran Cyber Threats March 2026](https://unit42.paloaltonetworks.com/evolution-of-iran-cyber-threats/)


[^8]: [FBI IC3 Flash VOID MANTICORE Handala Hack March 2026](https://www.ic3.gov/CSA/2026/260320.pdf)


[^9]: [DOJ FBI Handala Hack March 2026](https://www.justice.gov/opa/media/1431956/dl?inline)


[^10]: COBALT MYSTIQUE


[^11]: [Domain Tools Handala Hack Karma Homeland Justice MOIS April 2026](https://dti.domaintools.com/research/handala-mois-linked-cyber-influence-ecosystem-threat-intelligence-assessment)


[^12]: Red Sandstorm


[^13]: [Sophos VOID MANTICORE COBALT MYSTIQUE other Names April 2026](https://www.sophos.com/en-us/threat-profiles/cobalt-mystique)


[^14]: [SEC 8K Palo Alto Statement Stryker Corp Handala March 2026](https://www.sec.gov/Archives/edgar/data/310764/000119312526118634/d94012dex991.htm)


[^15]: BANISHED KITTEN


[^16]: Handala Hack


