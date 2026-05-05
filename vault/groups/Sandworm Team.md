---
aliases: 
    - Sandworm Team
    - ELECTRUM
    - Telebots
    - IRON VIKING
    - BlackEnergy (Group)
    - Quedagh
    - Voodoo Bear
    - IRIDIUM
    - Seashell Blizzard
    - FROZENBARENTS
    - APT44
mitre-attack: https://attack.mitre.org/groups/G0034
---

## G0034

[Sandworm Team](https://attack.mitre.org/groups/G0034) is a destructive threat group that has been attributed to Russia's General Staff Main Intelligence Directorate (GRU) Main Center for Special Technologies (GTsST) military unit 74455.[^16] [^17]  This group has been active since at least 2009.[^14] [^5] [^46] [^31] <br><br>In October 2020, the US indicted six GRU Unit 74455 officers associated with [Sandworm Team](https://attack.mitre.org/groups/G0034) for the following cyber operations: the 2015 and 2016 attacks against Ukrainian electrical companies and government organizations, the 2017 worldwide [NotPetya](https://attack.mitre.org/software/S0368) attack, targeting of the 2017 French presidential campaign, the 2018 [Olympic Destroyer](https://attack.mitre.org/software/S0365) attack against the Winter Olympic Games, the 2018 operation against the Organisation for the Prohibition of Chemical Weapons, and attacks against the country of Georgia in 2018 and 2019.[^16] [^17]  Some of these were conducted with the assistance of GRU Unit 26165, which is also referred to as [APT28](https://attack.mitre.org/groups/G0007).[^32] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Upload Malware\|T1608.001]] | Upload Malware | [Sandworm Team](https://attack.mitre.org/groups/G0034) staged compromised versions of legitimate software installers in forums to enable initial access to executing user.[^12]  |
| [[Vulnerabilities\|T1588.006]] | Vulnerabilities | In 2017, [Sandworm Team](https://attack.mitre.org/groups/G0034) conducted technical research related to vulnerabilities associated with websites used by the Korean Sport and Olympic Committee, a Korean power company, and a Korean airport.[^16]  |
| [[Network Sniffing\|T1040]] | Network Sniffing | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used intercepter-NG to sniff passwords in network traffic.[^19] 	 |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used ROT13 encoding, AES encryption and compression with the zlib library for their Python-based backdoor.[^19]  |
| [[Vulnerability Scanning\|T1595.002]] | Vulnerability Scanning | [Sandworm Team](https://attack.mitre.org/groups/G0034) has scanned network infrastructure for vulnerabilities as part of its operational planning.[^16]  |
| [[Social Media Accounts\|T1585.001]] | Social Media Accounts | [Sandworm Team](https://attack.mitre.org/groups/G0034) has established social media accounts to disseminate victim internal-only documents and other sensitive data.[^16]  |
| [[Social Media Accounts\|T1586.001]] | Social Media Accounts | [Sandworm Team](https://attack.mitre.org/groups/G0034) creates credential capture webpages to compromise existing, legitimate social media accounts.[^35]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Sandworm Team](https://attack.mitre.org/groups/G0034)'s BCS-server tool uses base64 encoding and HTML tags for the communication traffic between the C2 server.[^19] 	 |
| [[Databases\|T1213.006]] | Databases | [Sandworm Team](https://attack.mitre.org/groups/G0034) exfiltrates data of interest from enterprise databases using Adminer.[^44]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [Sandworm Team](https://attack.mitre.org/groups/G0034) used information stealer malware to collect browser session cookies.[^44]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used PowerShell scripts to run a credential harvesting tool in memory to evade defenses.[^16] [^36]   |
| [[Proxy\|T1090]] | Proxy | [Sandworm Team](https://attack.mitre.org/groups/G0034)'s BCS-server tool can create an internal proxy server to redirect traffic from the adversary-controlled C2 to internal servers which may not be connected to the internet, but are interconnected locally.[^19] 	 |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Sandworm Team](https://attack.mitre.org/groups/G0034) has exploited vulnerabilities in Microsoft PowerPoint via OLE objects (CVE-2014-4114) and Microsoft Word via crafted TIFF images (CVE-2013-3906).[^1] [^40] [^39]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Sandworm Team](https://attack.mitre.org/groups/G0034) has sent system information to its C2 server using HTTP.[^19] 	 |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Sandworm Team](https://attack.mitre.org/groups/G0034) leveraged SHARPIVORY, a .NET dropper that writes embedded payload to disk and uses scheduled tasks to persist on victim machines.[^12]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Sandworm Team](https://attack.mitre.org/groups/G0034) exploits public-facing applications for initial access and to acquire infrastructure, such as exploitation of the EXIM mail transfer agent in Linux systems.[^50] [^44]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used stolen credentials to access administrative accounts within the domain.[^16] [^25]  |
| [[NTDS\|T1003.003]] | NTDS | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used `ntdsutil.exe` to back up the Active Directory database, likely for credential access.[^25]  |
| [[Masquerading\|T1036]] | Masquerading | [Sandworm Team](https://attack.mitre.org/groups/G0034) masqueraded malicious installers as Windows update packages to evade defense and entice users to execute binaries.[^44]  |
| [[Spearphishing Link\|T1598.003]] | Spearphishing Link | [Sandworm Team](https://attack.mitre.org/groups/G0034) has crafted spearphishing emails with hyperlinks designed to trick unwitting recipients into revealing their account credentials.[^16]  |
| [[External Remote Services\|T1133]] | External Remote Services | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used Dropbear SSH with a hardcoded backdoor password to maintain persistence within the target network. [Sandworm Team](https://attack.mitre.org/groups/G0034) has also used VPN tunnels established in legitimate software company infrastructure to gain access to internal networks of that software company's users.[^45] [^55] [^47] [^12]  |
| [[Malware\|T1587.001]] | Malware | [Sandworm Team](https://attack.mitre.org/groups/G0034) has developed malware for its operations, including malicious mobile applications and destructive malware such as [NotPetya](https://attack.mitre.org/software/S0368) and [Olympic Destroyer](https://attack.mitre.org/software/S0365).[^16]  |
| [[Software Deployment Tools\|T1072]] | Software Deployment Tools | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used the commercially available tool RemoteExec for agentless remote code execution.[^25]  |
| [[Botnet\|T1584.005]] | Botnet | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used a large-scale botnet to target Small Office/Home Office (SOHO) network devices.[^41]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Sandworm Team](https://attack.mitre.org/groups/G0034) has crafted phishing emails containing malicious hyperlinks.[^16]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used a tool to query Active Directory using LDAP, discovering information about computers listed in AD.[^19] [^36]   |
| [[Employee Names\|T1589.003]] | Employee Names | [Sandworm Team](https://attack.mitre.org/groups/G0034)'s research of potential victim organizations included the identification and collection of employee information.[^16]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Sandworm Team](https://attack.mitre.org/groups/G0034) have used previously acquired legitimate credentials prior to attacks.[^53]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Sandworm Team](https://attack.mitre.org/groups/G0034) has delivered malicious Microsoft Office and ZIP file attachments via spearphishing emails.[^1] [^53] [^19] [^16] [^21] [^12]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Sandworm Team](https://attack.mitre.org/groups/G0034) has tricked unwitting recipients into clicking on spearphishing attachments and enabling malicious macros embedded within files.[^19] [^16]  |
| [[Native API\|T1106]] | Native API | [Sandworm Team](https://attack.mitre.org/groups/G0034) uses [Prestige](https://attack.mitre.org/software/S1058) to disable and restore file system redirection by using the following functions:  `Wow64DisableWow64FsRedirection()` and `Wow64RevertWow64FsRedirection()`.[^25]  |
| [[Tool\|T1588.002]] | Tool | [Sandworm Team](https://attack.mitre.org/groups/G0034) has acquired open-source tools for their operations, including [Invoke-PSImage](https://attack.mitre.org/software/S0231), which was used to establish an encrypted channel from a compromised host to [Sandworm Team](https://attack.mitre.org/groups/G0034)'s C2 server in preparation for the 2018 Winter Olympics attack, as well as [Impacket](https://attack.mitre.org/software/S0357) and RemoteExec, which were used in their 2022 [Prestige](https://attack.mitre.org/software/S1058) operations.[^16] [^25]  Additionally, [Sandworm Team](https://attack.mitre.org/groups/G0034) has used [Empire](https://attack.mitre.org/software/S0363), [Cobalt Strike](https://attack.mitre.org/software/S0154) and [PoshC2](https://attack.mitre.org/software/S0378).[^12]  |
| [[Server\|T1583.004]] | Server | [Sandworm Team](https://attack.mitre.org/groups/G0034) has leased servers from resellers instead of leasing infrastructure directly from hosting companies to enable its operations.[^16]  |
| [[Domain Properties\|T1590.001]] | Domain Properties | [Sandworm Team](https://attack.mitre.org/groups/G0034) conducted technical reconnaissance of the Parliament of Georgia's official internet domain prior to its 2019 attack.[^16]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Sandworm Team](https://attack.mitre.org/groups/G0034) has enumerated files on a compromised host.[^16] [^36]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Sandworm Team](https://attack.mitre.org/groups/G0034) had gathered user, IP address, and server data related to RDP sessions on a compromised host. It has also accessed network diagram files useful for understanding how a host's network was configured.[^16] [^36]   |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Sandworm Team](https://attack.mitre.org/groups/G0034)'s CredRaptor tool can collect saved passwords from various internet browsers.[^19]  |
| [[Service Stop\|T1489]] | Service Stop | [Sandworm Team](https://attack.mitre.org/groups/G0034) attempts to stop the MSSQL Windows service to ensure successful encryption of locked files.[^25]   |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used port 6789 to accept connections on the group's SSH server.[^45]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used backdoors that can delete files used in an attack from an infected system.[^19] [^6] [^48]   |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used [Impacket](https://attack.mitre.org/software/S0357)’s WMIexec module for remote code execution and VBScript to run WMI queries.[^36] [^25]  |
| [[Email Account\|T1087.003]] | Email Account | [Sandworm Team](https://attack.mitre.org/groups/G0034) used malware to enumerate email settings, including usernames and passwords, from the M.E.Doc application.[^6] 	 |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Sandworm Team](https://attack.mitre.org/groups/G0034) has copied payloads to the `ADMIN$` share of remote systems and run `net use` to connect to network shares.[^36] [^25]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Sandworm Team](https://attack.mitre.org/groups/G0034) has tricked unwitting recipients into clicking on malicious hyperlinks within emails crafted to resemble trustworthy senders.[^16]  |
| [[Web Shell\|T1505.003]] | Web Shell | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used webshells including [P.A.S. Webshell](https://attack.mitre.org/software/S0598) to maintain access to victim networks.[^47]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Sandworm Team](https://attack.mitre.org/groups/G0034) used a backdoor which could execute a supplied DLL using rundll32.exe.[^6] 	 |
| [[Endpoint Denial of Service\|T1499]] | Endpoint Denial of Service | [Sandworm Team](https://attack.mitre.org/groups/G0034) temporarily disrupted service to Georgian government, non-government, and private sector websites after compromising a Georgian web hosting provider in 2019.[^16]  |
| [[Compromise Software Supply Chain\|T1195.002]] | Compromise Software Supply Chain | [Sandworm Team](https://attack.mitre.org/groups/G0034) has distributed [NotPetya](https://attack.mitre.org/software/S0368) by compromising the legitimate Ukrainian accounting software M.E.Doc and replacing a legitimate software update with a malicious one.[^2] [^55] [^16]  |
| [[Trusted Relationship\|T1199]] | Trusted Relationship | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used dedicated network connections from one victim organization to gain unauthorized access to a separate organization.[^16]  Additionally, [Sandworm Team](https://attack.mitre.org/groups/G0034) has accessed Internet service providers and telecommunication entities that provide mobile connectivity.[^12]   |
| [[Keylogging\|T1056.001]] | Keylogging | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used a keylogger to capture keystrokes by using the SetWindowsHookEx function.[^19] 	 |
| [[Disk Structure Wipe\|T1561.002]] | Disk Structure Wipe | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used the [BlackEnergy](https://attack.mitre.org/software/S0089) KillDisk component to corrupt the infected system's master boot record.[^53] [^55]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used [Prestige](https://attack.mitre.org/software/S1058) ransomware to encrypt data at targeted organizations in transportation and related logistics industries in Ukraine and Poland.[^25]  |
| [[Software\|T1592.002]] | Software | [Sandworm Team](https://attack.mitre.org/groups/G0034) has researched software code to enable supply-chain operations, most notably for the 2017 [NotPetya](https://attack.mitre.org/software/S0368) attack. [Sandworm Team](https://attack.mitre.org/groups/G0034) also collected a list of computers using specific software as part of its targeting efforts.[^16]  |
| [[External Defacement\|T1491.002]] | External Defacement | [Sandworm Team](https://attack.mitre.org/groups/G0034) defaced approximately 15,000 websites belonging to Georgian government, non-government, and private sector organizations in 2019.[^16] [^17]  |
| [[Acquire Infrastructure\|T1583]] | Acquire Infrastructure | [Sandworm Team](https://attack.mitre.org/groups/G0034) used various third-party email campaign management services to deliver phishing emails.[^44]  |
| [[Remote Access Tools\|T1219]] | Remote Access Tools | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used remote administration tools or remote industrial control system client software for execution and to maliciously release electricity breakers.[^53] [^25]  |
| [[Server\|T1584.004]] | Server | [Sandworm Team](https://attack.mitre.org/groups/G0034) compromised legitimate Linux servers running the EXIM mail transfer agent for use in subsequent campaigns.[^50] [^44]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used its plainpwd tool, a modified version of [Mimikatz](https://attack.mitre.org/software/S0002), and comsvcs.dll to dump Windows credentials from system memory.[^19] [^55] [^25] 	 |
| [[Search Victim-Owned Websites\|T1594]] | Search Victim-Owned Websites | [Sandworm Team](https://attack.mitre.org/groups/G0034) has conducted research against potential victim websites as part of its operational planning.[^16]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used `move` to transfer files to a network share and has copied payloads--such as [Prestige](https://attack.mitre.org/software/S1058) ransomware--to an Active Directory Domain Controller and distributed via the Default Domain Group Policy Object.[^36] [^25]  Additionally, [Sandworm Team](https://attack.mitre.org/groups/G0034) has transferred an ISO file into the OT network to gain initial access.[^48]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used Base64 encoding within malware variants.[^1]  |
| [[Business Relationships\|T1591.002]] | Business Relationships | In preparation for its attack against the 2018 Winter Olympics, [Sandworm Team](https://attack.mitre.org/groups/G0034) conducted online research of partner organizations listed on an official PyeongChang Olympics partnership site.[^16]  |
| [[Email Accounts\|T1585.002]] | Email Accounts | [Sandworm Team](https://attack.mitre.org/groups/G0034) has created email accounts that mimic legitimate organizations for its spearphishing operations.[^16]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used the Telegram Bot API from Telegram Messenger to send and receive commands to its Python backdoor. [Sandworm Team](https://attack.mitre.org/groups/G0034) also used legitimate M.E.Doc software update check requests for sending and receiving commands and hosted malicious payloads on putdrive.com.[^19] [^55]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Sandworm Team](https://attack.mitre.org/groups/G0034) uses [Prestige](https://attack.mitre.org/software/S1058) to delete the backup catalog from the target system using: `C:\Windows\System32\wbadmin.exe delete catalog -quiet` and to delete volume shadow copies using: `C:\Windows\System32\vssadmin.exe delete shadows /all /quiet`. [^25]   |
| [[Domains\|T1583.001]] | Domains | [Sandworm Team](https://attack.mitre.org/groups/G0034) has registered domain names and created URLs that are often designed to mimic or spoof legitimate websites, such as email login pages, online file sharing and storage websites, and password reset pages, while also hosting these items on legitimate, compromised network infrastructure.[^16] [^35]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Sandworm Team](https://attack.mitre.org/groups/G0034)'s VBS backdoor can decode Base64-encoded data and save it to the %TEMP% folder. The group also decrypted received information using the Triple DES algorithm and decompresses it using GZip.[^19] [^6]  |
| [[Data Destruction\|T1485]] | Data Destruction | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used [CaddyWiper](https://attack.mitre.org/software/S0693), [SDelete](https://attack.mitre.org/software/S0195), and the [BlackEnergy](https://attack.mitre.org/software/S0089) KillDisk component to overwrite files on victim systems. [^53] [^55] [^48]  Additionally, [Sandworm Team](https://attack.mitre.org/groups/G0034) has used the JUNKMAIL tool to overwrite files with null bytes.[^12]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Sandworm Team](https://attack.mitre.org/groups/G0034) has created VBScripts to run an SSH server.[^45] [^19] [^55] [^36]   |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Sandworm Team](https://attack.mitre.org/groups/G0034) has pushed additional malicious tools onto an infected system to steal user credentials, move laterally, and destroy data.[^19] [^16]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Sandworm Team](https://attack.mitre.org/groups/G0034) has collected the username from a compromised host.[^16]  |
| [[Email Addresses\|T1589.002]] | Email Addresses | [Sandworm Team](https://attack.mitre.org/groups/G0034) has obtained valid emails addresses while conducting research against target organizations that were subsequently used in spearphishing campaigns.[^16]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Sandworm Team](https://attack.mitre.org/groups/G0034)'s BCS-server tool connects to the designated C2 server via HTTP.[^19] 	 |
| [[Domain Account\|T1087.002]] | Domain Account | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used a tool to query Active Directory using LDAP, discovering information about usernames listed in AD.[^19] 	 |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Sandworm Team](https://attack.mitre.org/groups/G0034) used a backdoor to enumerate information about the infected system's operating system.[^6] [^16] 	 |
| [[Data from Local System\|T1005]] | Data from Local System | [Sandworm Team](https://attack.mitre.org/groups/G0034) has exfiltrated internal documents, files, and other data from compromised hosts.[^16]  |
| [[Supply Chain Compromise\|T1195]] | Supply Chain Compromise | [Sandworm Team](https://attack.mitre.org/groups/G0034) staged compromised versions of legitimate software installers on forums to achieve initial, untargetetd access in victim environments.[^12]   |
| [[Search Open Websites／Domains\|T1593]] | Search Open Websites／Domains | [Sandworm Team](https://attack.mitre.org/groups/G0034) researched Ukraine's unique legal entity identifier (called an "EDRPOU" number), including running queries on the EDRPOU website, in preparation for the [NotPetya](https://attack.mitre.org/software/S0368) attack. [Sandworm Team](https://attack.mitre.org/groups/G0034) has also researched third-party websites to help it craft credible spearphishing emails.[^16]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Sandworm Team](https://attack.mitre.org/groups/G0034) has avoided detection by naming a malicious binary explorer.exe.[^19] [^16]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^36]  |
| [[Impacket\|S0357]] | Impacket | [^25]  |
| [[Empire\|S0363]] | Empire | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used multiple publicly available tools during operations, such as Empire.[^12]  |
| [[PoshC2\|S0378]] | PoshC2 | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used multiple publicly available tools during operations, such as PoshC2.[^12]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^36]  |
| [[Invoke-PSImage\|S0231]] | Invoke-PSImage | [^16]  |
| [[SDelete\|S0195]] | SDelete | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used [SDelete](https://attack.mitre.org/software/S0195) for wartime operations in 2022-2023.[^12]  |
| [[PsExec\|S0029]] | PsExec | [^36]  |
| [[AcidRain\|S1125]] | AcidRain | [Sandworm Team](https://attack.mitre.org/groups/G0034) is linked to [AcidRain](https://attack.mitre.org/software/S1125) deployment during the ViaSat KA-SAT incident in 2022.[^20] [^33]  |
| [[Exaramel for Windows\|S0343]] | Exaramel for Windows | [^13]  |
| [[Exaramel for Linux\|S0401]] | Exaramel for Linux | [^13] [^47]  |
| [[Prestige\|S1058]] | Prestige | [^25] [^12]  |
| [[Bad Rabbit\|S0606]] | Bad Rabbit | [^3]  |
| [[GreyEnergy\|S0342]] | GreyEnergy | [^3]  |
| [[Olympic Destroyer\|S0365]] | Olympic Destroyer | [^42] [^3] [^16] [^17] [^28] [^12]  |
| [[P.A.S. Webshell\|S0598]] | P.A.S. Webshell | [^47]  |
| [[AcidPour\|S1167]] | AcidPour | [AcidPour](https://attack.mitre.org/software/S1167) is associated with [Sandworm Team](https://attack.mitre.org/groups/G0034).[^52]  |
| [[BlackEnergy\|S0089]] | BlackEnergy | [^14] [^54] [^16] [^17] [^3]  |
| [[NotPetya\|S0368]] | NotPetya | [^31] [^16] [^17] [^3] [^28] [^12]  |
| [[VPNFilter\|S1010]] | VPNFilter | [VPNFilter](https://attack.mitre.org/software/S1010) is associated with [Sandworm Team](https://attack.mitre.org/groups/G0034) operations based on reporting on [VPNFilter](https://attack.mitre.org/software/S1010) replacement software, [Cyclops Blink](https://attack.mitre.org/software/S0687).[^37]  |
| [[Industroyer2\|S1072]] | Industroyer2 | [^22] [^12]  |
| [[Kapeka\|S1190]] | Kapeka | [Kapeka](https://attack.mitre.org/software/S1190) is associated with [Sandworm Team](https://attack.mitre.org/groups/G0034) operations and previous malware variants such as [GreyEnergy](https://attack.mitre.org/software/S0342).[^27] [^23]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used multiple publicly available tools during operations, such as Cobalt Strike.[^12]  |
| [[Cyclops Blink\|S0687]] | Cyclops Blink | [^37] [^28]  |
| [[Neo-reGeorg\|S1189]] | Neo-reGeorg | [^48]  |
| [[KillDisk\|S0607]] | KillDisk | [^16] [^3]  |
| [[Industroyer\|S0604]] | Industroyer | [^36] [^43] [^49] [^15] [^12]  |



## References

[^1]: [iSight Sandworm Oct 2014](https://web.archive.org/web/20160503234007/https:/www.isightpartners.com/2014/10/cve-2014-4114/)


[^2]: [Secureworks NotPetya June 2017](https://www.secureworks.com/blog/notpetya-campaign-what-we-know-about-the-latest-global-ransomware-attack)


[^3]: [Secureworks IRON VIKING ](https://www.secureworks.com/research/threat-profiles/iron-viking)


[^4]: [Dragos ELECTRUM](https://www.dragos.com/resource/electrum/)


[^5]: [CrowdStrike VOODOO BEAR](https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-january-voodoo-bear/)


[^6]: [ESET Telebots July 2017](https://www.welivesecurity.com/2017/07/04/analysis-of-telebots-cunning-backdoor/)


[^7]: Sandworm Team


[^8]: IRON VIKING


[^9]: ELECTRUM


[^10]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^11]: APT44


[^12]: [mandiant_apt44_unearthing_sandworm](https://services.google.com/fh/files/misc/apt44-unearthing-sandworm.pdf)


[^13]: [ESET TeleBots Oct 2018](https://www.welivesecurity.com/2018/10/11/new-telebots-backdoor-linking-industroyer-notpetya/)


[^14]: [iSIGHT Sandworm 2014](https://www.fireeye.com/blog/threat-research/2016/01/ukraine-and-sandworm-team.html)


[^15]: [Secureworks IRON VIKING](https://www.secureworks.com/research/threat-profiles/iron-viking)


[^16]: [US District Court Indictment GRU Unit 74455 October 2020](https://www.justice.gov/opa/press-release/file/1328521/download)


[^17]: [UK NCSC Olympic Attacks October 2020](https://www.gov.uk/government/news/uk-exposes-series-of-russian-cyber-attacks-against-olympic-and-paralympic-games)


[^18]: Quedagh


[^19]: [ESET Telebots Dec 2016](https://www.welivesecurity.com/2016/12/13/rise-telebots-analyzing-disruptive-killdisk-attacks/)


[^20]: [Vincens AcidPour 2024](https://cyberscoop.com/viasat-malware-wiper-acidrain/)


[^21]: [Google_WinRAR_vuln_2023](https://blog.google/threat-analysis-group/government-backed-actors-exploiting-winrar-vulnerability/)


[^22]: [Industroyer2 ESET April 2022](https://www.welivesecurity.com/2022/04/12/industroyer2-industroyer-reloaded/)


[^23]: [WithSecure Kapeka 2024](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Research-Kapeka.pdf)


[^24]: IRIDIUM


[^25]: [Microsoft Prestige ransomware October 2022](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)


[^26]: FROZENBARENTS


[^27]: [Microsoft KnuckleTouch 2024](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Backdoor:Win64/KnuckleTouch.A!dha&threatId=-2147067254)


[^28]: [Trend Micro Cyclops Blink March 2022](https://www.trendmicro.com/en_us/research/22/c/cyclops-blink-sets-sights-on-asus-routers--.html)


[^29]: Voodoo Bear


[^30]: [InfoSecurity Sandworm Oct 2014](https://www.infosecurity-magazine.com/news/microsoft-zero-day-traced-russian/)


[^31]: [NCSC Sandworm Feb 2020](https://www.ncsc.gov.uk/news/ncsc-supports-sandworm-advisory)


[^32]: [US District Court Indictment GRU Oct 2018](https://www.justice.gov/opa/page/file/1098481/download)


[^33]: [AcidRain JAGS 2022](https://www.sentinelone.com/labs/acidrain-a-modem-wiper-rains-down-on-europe/)


[^34]: Telebots


[^35]: [Slowik Sandworm 2021](https://www.domaintools.com/resources/blog/centreon-to-exim-and-back-on-the-trail-of-sandworm/)


[^36]: [Dragos Crashoverride 2018](https://www.dragos.com/wp-content/uploads/CRASHOVERRIDE2018.pdf)


[^37]: [NCSC CISA Cyclops Blink Advisory February 2022](https://www.ncsc.gov.uk/news/joint-advisory-shows-new-sandworm-malware-cyclops-blink-replaces-vpnfilter)


[^38]: BlackEnergy (Group)


[^39]: [McAfee Sandworm November 2013](https://www.mcafee.com/blogs/other-blogs/mcafee-labs-detects-zero-day-exploit-targeting-microsoft-office-2)


[^40]: [TrendMicro Sandworm October 2014](https://blog.trendmicro.com/trendlabs-security-intelligence/an-analysis-of-windows-zero-day-vulnerability-cve-2014-4114-aka-sandworm/)


[^41]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)


[^42]: [CrowdStrike GTR 2019](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2019GlobalThreatReport.pdf)


[^43]: [Dragos Crashoverride 2017](https://dragos.com/blog/crashoverride/CrashOverride-01.pdf)


[^44]: [Leonard TAG 2023](https://blog.google/threat-analysis-group/ukraine-remains-russias-biggest-cyber-focus-in-2023/)


[^45]: [ESET BlackEnergy Jan 2016](https://www.welivesecurity.com/2016/01/03/blackenergy-sshbeardoor-details-2015-attacks-ukrainian-news-media-electric-industry/)


[^46]: [USDOJ Sandworm Feb 2020](https://2017-2021.state.gov/the-united-states-condemns-russian-cyber-attack-against-the-country-of-georgia/index.html)


[^47]: [ANSSI Sandworm January 2021](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)


[^48]: [Mandiant-Sandworm-Ukraine-2022](https://www.mandiant.com/resources/blog/sandworm-disrupts-power-ukraine-operational-technology)


[^49]: [ESET Industroyer](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)


[^50]: [NSA Sandworm 2020](https://media.defense.gov/2020/May/28/2002306626/-1/-1/0/CSA%20Sandworm%20Actors%20Exploiting%20Vulnerability%20in%20Exim%20Transfer%20Agent%2020200528.pdf)


[^51]: Seashell Blizzard


[^52]: [SentinelOne AcidPour 2024](https://www.sentinelone.com/labs/acidpour-new-embedded-wiper-variant-of-acidrain-appears-in-ukraine/)


[^53]: [US-CERT Ukraine Feb 2016](https://www.us-cert.gov/ics/alerts/IR-ALERT-H-16-056-01)


[^54]: [F-Secure BlackEnergy 2014](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)


[^55]: [ESET Telebots June 2017](https://www.welivesecurity.com/2017/06/30/telebots-back-supply-chain-attacks-against-ukraine/)


