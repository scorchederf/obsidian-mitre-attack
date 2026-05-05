---
aliases: 
    - APT28
    - IRON TWILIGHT
    - SNAKEMACKEREL
    - Swallowtail
    - Group 74
    - Sednit
    - Sofacy
    - Pawn Storm
    - Fancy Bear
    - STRONTIUM
    - Tsar Team
    - Threat Group-4127
    - TG-4127
    - Forest Blizzard
    - FROZENLAKE
    - GruesomeLarch
mitre-attack: https://attack.mitre.org/groups/G0007
---

## G0007

[APT28](https://attack.mitre.org/groups/G0007) is a threat group that has been attributed to Russia's General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (GTsSS) military unit 26165.[^33] [^4]  This group has been active since at least 2004.[^51] [^66] [^44] [^37] [^46] [^20] [^18] [^52] [^34] [^68] [^57] <br><br>[APT28](https://attack.mitre.org/groups/G0007) reportedly compromised the Hillary Clinton campaign, the Democratic National Committee, and the Democratic Congressional Campaign Committee in 2016 in an attempt to interfere with the U.S. presidential election.[^44]  In 2018, the US indicted five GRU Unit 26165 officers associated with [APT28](https://attack.mitre.org/groups/G0007) for cyber operations (including close-access operations) conducted between 2014 and 2018 against the World Anti-Doping Agency (WADA), the US Anti-Doping Agency, a US nuclear facility, the Organization for the Prohibition of Chemical Weapons (OPCW), the Spiez Swiss Chemicals Laboratory, and other organizations.[^45]  Some of these were conducted with the assistance of GRU Unit 74455, which is also referred to as [Sandworm Team](https://attack.mitre.org/groups/G0034). 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[NTDS\|T1003.003]] | NTDS | [APT28](https://attack.mitre.org/groups/G0007) has used the ntdsutil.exe utility to export the Active Directory database for credential access.[^4]  |
| [[Credentials\|T1589.001]] | Credentials | [APT28](https://attack.mitre.org/groups/G0007) has harvested user's login credentials.[^73]  |
| [[Gather Victim Org Information\|T1591]] | Gather Victim Org Information | [APT28](https://attack.mitre.org/groups/G0007) has used large language models (LLMs) to gather information about satellite capabilities.[^74] [^25]   |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [APT28](https://attack.mitre.org/groups/G0007) has saved files with hidden file attributes.[^53] [^53]  |
| [[Virtual Private Server\|T1583.003]] | Virtual Private Server | [APT28](https://attack.mitre.org/groups/G0007) hosted phishing domains on free services for brief periods of time during campaigns.[^56]  |
| [[Search Open Technical Databases\|T1596]] | Search Open Technical Databases | [APT28](https://attack.mitre.org/groups/G0007) has used large language models (LLMs) to assist in script development and deployment.[^74] [^25]   |
| [[Domains\|T1583.001]] | Domains | [APT28](https://attack.mitre.org/groups/G0007) registered domains imitating NATO, OSCE security websites, Caucasus information resources, and other organizations.[^37] [^45] [^71]  |
| [[Timestomp\|T1070.006]] | Timestomp | [APT28](https://attack.mitre.org/groups/G0007) has performed timestomping on victim files.[^44]  |
| [[External Proxy\|T1090.002]] | External Proxy | [APT28](https://attack.mitre.org/groups/G0007) used other victims as proxies to relay command traffic, for instance using a compromised Georgian military email server as a hop point to NATO victims. The group has also used a tool that acts as a proxy to allow C2 even if the victim is behind a router. [APT28](https://attack.mitre.org/groups/G0007) has also used a machine to relay and obscure communications between [CHOPSTICK](https://attack.mitre.org/software/S0023) and their server.[^37] [^26] [^51]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [APT28](https://attack.mitre.org/groups/G0007) sent spearphishing emails containing malicious Microsoft Office and RAR attachments.[^5] [^52] [^34] [^51] [^70] [^16] [^40] [^48] [^36]  |
| [[PowerShell\|T1059.001]] | PowerShell | [APT28](https://attack.mitre.org/groups/G0007) downloads and executes PowerShell scripts and performs PowerShell commands.[^34] [^40] [^4]  |
| [[Exfiltration Over Asymmetric Encrypted Non-C2 Protocol\|T1048.002]] | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | [APT28](https://attack.mitre.org/groups/G0007) has exfiltrated archives of collected data previously staged on a target's OWA server via HTTPS.[^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [APT28](https://attack.mitre.org/groups/G0007) has deployed malware that has copied itself to the startup directory for persistence.[^40]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [APT28](https://attack.mitre.org/groups/G0007) encrypted a .dll payload using RTL and a custom encryption algorithm. [APT28](https://attack.mitre.org/groups/G0007) has also obfuscated payloads with base64, XOR, and RC4.[^26] [^5] [^34] [^53] [^16]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [APT28](https://attack.mitre.org/groups/G0007) has exploited Microsoft Office vulnerability CVE-2017-0262 for execution.[^70]  |
| [[Email Accounts\|T1586.002]] | Email Accounts | [APT28](https://attack.mitre.org/groups/G0007) has used compromised email accounts to send credential phishing emails.[^71]  |
| [[Remote Email Collection\|T1114.002]] | Remote Email Collection | [APT28](https://attack.mitre.org/groups/G0007) has collected emails from victim Microsoft Exchange servers.[^51] [^4]  |
| [[Web Shell\|T1505.003]] | Web Shell | [APT28](https://attack.mitre.org/groups/G0007) has used a modified and obfuscated version of the reGeorg web shell to maintain persistence on a target's Outlook Web Access (OWA) server.[^4]  |
| [[Network Devices\|T1584.008]] | Network Devices | [APT28](https://attack.mitre.org/groups/G0007) compromised Ubiquiti network devices to act as collection devices for credentials compromised via phishing webpages.[^56]  |
| [[Pass the Hash\|T1550.002]] | Pass the Hash | [APT28](https://attack.mitre.org/groups/G0007) has used pass the hash for lateral movement.[^17]  |
| [[Logon Script (Windows)\|T1037.001]] | Logon Script (Windows) | An [APT28](https://attack.mitre.org/groups/G0007) loader Trojan adds the Registry key `HKCU\Environment\UserInitMprLogonScript` to establish persistence.[^69]  |
| [[Tool\|T1588.002]] | Tool | [APT28](https://attack.mitre.org/groups/G0007) has obtained and used open-source tools like [Koadic](https://attack.mitre.org/software/S0250), [Mimikatz](https://attack.mitre.org/software/S0002), and [Responder](https://attack.mitre.org/software/S0174).[^34] [^70] [^55]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [APT28](https://attack.mitre.org/groups/G0007) has used the WindowStyle parameter to conceal [PowerShell](https://attack.mitre.org/techniques/T1059/001) windows.[^34]  [^23]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [APT28](https://attack.mitre.org/groups/G0007) has routed traffic over [Tor](https://attack.mitre.org/software/S0183) and VPN servers to obfuscate their activities.[^40]  |
| [[Exfiltration Over Web Service\|T1567]] | Exfiltration Over Web Service | [APT28](https://attack.mitre.org/groups/G0007) can exfiltrate data over Google Drive.[^40]   |
| [[Keylogging\|T1056.001]] | Keylogging | [APT28](https://attack.mitre.org/groups/G0007) has used tools to perform keylogging.[^17] [^51] [^40]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [APT28](https://attack.mitre.org/groups/G0007) has used [Forfiles](https://attack.mitre.org/software/S0193) to locate PDF, Excel, and Word documents during collection. The group also searched a compromised DCCC computer for specific terms.[^19] [^51]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [APT28](https://attack.mitre.org/groups/G0007) has used a variety of public exploits, including CVE 2020-0688 and CVE 2020-17144, to gain execution on vulnerable Microsoft Exchange; they have also conducted SQL injection attacks against external websites.[^45] [^4]  |
| [[Wi-Fi Networks\|T1669]] | Wi-Fi Networks | [APT28](https://attack.mitre.org/groups/G0007) has exploited open Wi-Fi access points for initial access to target devices using the network.[^12] [^28]  |
| [[Data from Network Shared Drive\|T1039]] | Data from Network Shared Drive | [APT28](https://attack.mitre.org/groups/G0007) has collected files from network shared drives.[^4]  |
| [[Screen Capture\|T1113]] | Screen Capture | [APT28](https://attack.mitre.org/groups/G0007) has used tools to take screenshots from victims.[^39] [^15] [^51] [^48]  |
| [[Password Guessing\|T1110.001]] | Password Guessing | [APT28](https://attack.mitre.org/groups/G0007) has used a brute-force/password-spray tooling that operated in two modes: in brute-force mode it typically sent over 300 authentication attempts per hour per targeted account over the course of several hours or days.[^65]  [APT28](https://attack.mitre.org/groups/G0007) has also used a Kubernetes cluster to conduct distributed, large-scale password guessing attacks.[^4]  |
| [[Web Services\|T1583.006]] | Web Services | [APT28](https://attack.mitre.org/groups/G0007) has used newly-created Blogspot pages for credential harvesting operations.[^71]  |
| [[Process Discovery\|T1057]] | Process Discovery | An [APT28](https://attack.mitre.org/groups/G0007) loader Trojan will enumerate the victim's processes searching for explorer.exe if its current process does not have necessary permissions.[^69]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [APT28](https://attack.mitre.org/groups/G0007) has compromised targets via strategic web compromise utilizing custom exploit kits.[^48]  [APT28](https://attack.mitre.org/groups/G0007) used reflected cross-site scripting (XSS) against government websites to redirect users to phishing webpages.[^56]  |
| [[Vulnerability Scanning\|T1595.002]] | Vulnerability Scanning | [APT28](https://attack.mitre.org/groups/G0007) has performed large-scale scans in an attempt to find vulnerable servers.[^22]  |
| [[Component Object Model Hijacking\|T1546.015]] | Component Object Model Hijacking | [APT28](https://attack.mitre.org/groups/G0007) has used COM hijacking for persistence by replacing the legitimate `MMDeviceEnumerator` object with a payload.[^62] [^57]  |
| [[Trusted Relationship\|T1199]] | Trusted Relationship | Once [APT28](https://attack.mitre.org/groups/G0007) gained access to the DCCC network, the group then proceeded to use that access to compromise the DNC network.[^51]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [APT28](https://attack.mitre.org/groups/G0007) uses a module to receive a notification every time a USB mass storage device is inserted into a victim.[^17]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | An [APT28](https://attack.mitre.org/groups/G0007) loader Trojan uses a cmd.exe and batch script to run its payload.[^69]  The group has also used macros to execute payloads.[^53] [^1] [^16] [^40]  |
| [[Evil Twin\|T1557.004]] | Evil Twin | [APT28](https://attack.mitre.org/groups/G0007) has used a Wi-Fi Pineapple to set up Evil Twin Wi-Fi Poisoning for the purposes of capturing victim credentials or planting espionage-oriented malware.[^45]  |
| [[Network Denial of Service\|T1498]] | Network Denial of Service | In 2016, [APT28](https://attack.mitre.org/groups/G0007) conducted a distributed denial of service (DDoS) attack against the World Anti-Doping Agency.[^45]  |
| [[File Deletion\|T1070.004]] | File Deletion | [APT28](https://attack.mitre.org/groups/G0007) has intentionally deleted computer files to cover their tracks, including with use of the program CCleaner.[^51]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [APT28](https://attack.mitre.org/groups/G0007) used a publicly available tool to gather and compress multiple documents on the DCCC and DNC networks.[^51]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [APT28](https://attack.mitre.org/groups/G0007) has downloaded additional files, including by using a first-stage downloader to contact the C2 server to obtain the second-stage implant.[^26] [^69] [^16] [^40] [^4]  |
| [[Phishing for Information\|T1598]] | Phishing for Information | [APT28](https://attack.mitre.org/groups/G0007) has used spearphishing to compromise credentials.[^73] [^48]  |
| [[Dynamic Data Exchange\|T1559.002]] | Dynamic Data Exchange | [APT28](https://attack.mitre.org/groups/G0007) has delivered [JHUHUGIT](https://attack.mitre.org/software/S0044) and [Koadic](https://attack.mitre.org/software/S0250) by executing PowerShell commands through DDE in Word documents.[^23] [^47] [^34]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [APT28](https://attack.mitre.org/groups/G0007) has changed extensions on files containing exfiltrated data to make them appear benign, and renamed a web shell instance to appear as a legitimate OWA page.[^4]  |
| [[Automated Collection\|T1119]] | Automated Collection | [APT28](https://attack.mitre.org/groups/G0007) used a publicly available tool to gather and compress multiple documents on the DCCC and DNC networks.[^51]  |
| [[Cloud Accounts\|T1078.004]] | Cloud Accounts | [APT28](https://attack.mitre.org/groups/G0007) has used compromised Office 365 service accounts with Global Administrator privileges to collect email from user inboxes.[^4]  |
| [[Template Injection\|T1221]] | Template Injection | [APT28](https://attack.mitre.org/groups/G0007) used weaponized Microsoft Word documents abusing the remote template function to retrieve a malicious macro. [^63]  |
| [[Data from Local System\|T1005]] | Data from Local System | [APT28](https://attack.mitre.org/groups/G0007) has retrieved internal documents from machines inside victim environments, including by using [Forfiles](https://attack.mitre.org/software/S0193) to stage documents before exfiltration.[^19] [^51] [^22] [^4]  |
| [[Sharepoint\|T1213.002]] | Sharepoint | [APT28](https://attack.mitre.org/groups/G0007) has collected information from Microsoft SharePoint services within target networks.[^29]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [APT28](https://attack.mitre.org/groups/G0007) has used legitimate credentials to gain initial access, maintain access, and exfiltrate data from a victim network. The group has specifically used credentials stolen through a spearphishing email to login to the DCCC network. The group has also leveraged default manufacturer's passwords to gain initial access to corporate networks via IoT devices such as a VOIP phone, printer, and video decoder.[^72] [^51] [^13] [^4]  |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | An [APT28](https://attack.mitre.org/groups/G0007) backdoor may collect the entire contents of an inserted USB device.[^17]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | Later implants used by [APT28](https://attack.mitre.org/groups/G0007), such as [CHOPSTICK](https://attack.mitre.org/software/S0023), use a blend of HTTP, HTTPS, and other legitimate channels for C2, depending on module configuration.[^37] [^4]  |
| [[Data from Information Repositories\|T1213]] | Data from Information Repositories | [APT28](https://attack.mitre.org/groups/G0007) has collected files from various information repositories.[^4]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [APT28](https://attack.mitre.org/groups/G0007) executed [CHOPSTICK](https://attack.mitre.org/software/S0023) by using rundll32 commands such as `rundll32.exe “C:\Windows\twain_64.dll”`. [APT28](https://attack.mitre.org/groups/G0007) also executed a .dll for a first stage dropper using rundll32.exe. An [APT28](https://attack.mitre.org/groups/G0007) loader Trojan saved a batch script that uses rundll32 to execute a DLL payload.[^44] [^26] [^34] [^69] [^57] [^4]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [APT28](https://attack.mitre.org/groups/G0007) has used a variety of utilities, including WinRAR, to archive collected data with password protection.[^4]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | An [APT28](https://attack.mitre.org/groups/G0007) macro uses the command `certutil -decode` to decode contents of a .txt file storing the base64 encoded payload.[^5] [^34]  |
| [[Spearphishing Link\|T1598.003]] | Spearphishing Link | [APT28](https://attack.mitre.org/groups/G0007) has conducted credential phishing campaigns with links that redirect to credential harvesting sites.[^71] [^51] [^57] [^45] [^48]  |
| [[Bootkit\|T1542.003]] | Bootkit | [APT28](https://attack.mitre.org/groups/G0007) has deployed a bootkit along with [Downdelph](https://attack.mitre.org/software/S0134) to ensure its persistence on the victim. The bootkit shares code with some variants of [BlackEnergy](https://attack.mitre.org/software/S0089).[^21]  |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [APT28](https://attack.mitre.org/groups/G0007) has used IMAP, POP3, and SMTP for a communication channel in various implants, including using self-registered Google Mail accounts and later compromised email servers of its victims.[^37] [^4]  |
| [[Masquerading\|T1036]] | Masquerading | [APT28](https://attack.mitre.org/groups/G0007) has renamed the WinRAR utility to avoid detection.[^4]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [APT28](https://attack.mitre.org/groups/G0007) exploited a Windows SMB Remote Code Execution Vulnerability to conduct lateral movement.[^37] [^55] [^67]  |
| [[Rootkit\|T1014]] | Rootkit | [APT28](https://attack.mitre.org/groups/G0007) has used a UEFI (Unified Extensible Firmware Interface) rootkit known as [LoJax](https://attack.mitre.org/software/S0397).[^68] [^32]  |
| [[Malicious File\|T1204.002]] | Malicious File | [APT28](https://attack.mitre.org/groups/G0007) attempted to get users to click on Microsoft Office attachments containing malicious macro scripts.[^5] [^16] [^48] [^36]  |
| [[Application Access Token\|T1550.001]] | Application Access Token | [APT28](https://attack.mitre.org/groups/G0007) has used several malicious applications that abused OAuth access tokens to gain access to target email accounts, including Gmail and Yahoo Mail.[^59]  |
| [[Data Transfer Size Limits\|T1030]] | Data Transfer Size Limits | [APT28](https://attack.mitre.org/groups/G0007) has split archived exfiltration files into chunks smaller than 1MB.[^4]  |
| [[Token Impersonation／Theft\|T1134.001]] | Token Impersonation／Theft | [APT28](https://attack.mitre.org/groups/G0007) has used CVE-2015-1701 to access the SYSTEM token and copy it into the current process as part of privilege escalation.[^58]  |
| [[Remote Data Staging\|T1074.002]] | Remote Data Staging | [APT28](https://attack.mitre.org/groups/G0007) has staged archives of collected data on a target's Outlook Web Access (OWA) server.[^4]  |
| [[Communication Through Removable Media\|T1092]] | Communication Through Removable Media | [APT28](https://attack.mitre.org/groups/G0007) uses a tool that captures information from air-gapped computers via an infected USB and transfers it to network-connected computer when the USB is inserted.[^17]  |
| [[Additional Email Delegate Permissions\|T1098.002]] | Additional Email Delegate Permissions | [APT28](https://attack.mitre.org/groups/G0007) has used a Powershell cmdlet to grant the `ApplicationImpersonation` role to a compromised account.[^4]  |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | [APT28](https://attack.mitre.org/groups/G0007) regularly deploys both publicly available (ex: [Mimikatz](https://attack.mitre.org/software/S0002)) and custom password retrieval tools on victims.[^39] [^51] [^45] 	 |
| [[Network Sniffing\|T1040]] | Network Sniffing | [APT28](https://attack.mitre.org/groups/G0007) deployed the open source tool Responder to conduct NetBIOS Name Service poisoning, which captured usernames and hashed passwords that allowed access to legitimate credentials.[^37] [^55]  [APT28](https://attack.mitre.org/groups/G0007) close-access teams have used Wi-Fi pineapples to intercept Wi-Fi signals and user credentials.[^45]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [APT28](https://attack.mitre.org/groups/G0007) has exploited CVE-2014-4076, CVE-2015-2387, CVE-2015-1701, CVE-2017-0263, and CVE-2022-38028 to escalate privileges.[^26] [^17] [^70] [^12]  |
| [[Office Test\|T1137.002]] | Office Test | [APT28](https://attack.mitre.org/groups/G0007) has used the Office Test persistence mechanism within Microsoft Office by adding the Registry key `HKCU\Software\Microsoft\Office test\Special\Perf` to execute code.[^60]  |
| [[Steal Application Access Token\|T1528]] | Steal Application Access Token | [APT28](https://attack.mitre.org/groups/G0007) has used several malicious applications to steal user OAuth access tokens including applications masquerading as "Google Defender" "Google Email Protection," and "Google Scanner" for Gmail users. They also targeted Yahoo users with applications masquerading as "Delivery Service" and "McAfee Email Protection".[^59]  |
| [[Password Spraying\|T1110.003]] | Password Spraying | [APT28](https://attack.mitre.org/groups/G0007) has used a brute-force/password-spray tooling that operated in two modes: in password-spraying mode it conducted approximately four authentication attempts per hour per targeted account over the course of several days or weeks.[^65] [^73]  [APT28](https://attack.mitre.org/groups/G0007) has also used a Kubernetes cluster to conduct distributed, large-scale password spray attacks.[^4]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [APT28](https://attack.mitre.org/groups/G0007) has tricked unwitting recipients into clicking on malicious hyperlinks within emails crafted to resemble trustworthy senders.[^45] [^48]  |
| [[External Remote Services\|T1133]] | External Remote Services | [APT28](https://attack.mitre.org/groups/G0007) has used [Tor](https://attack.mitre.org/software/S0183) and a variety of commercial VPN services to route brute force authentication attempts.[^4]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [APT28](https://attack.mitre.org/groups/G0007) has used Google Drive for C2.[^40]  |
| [[Junk Data\|T1001.001]] | Junk Data | [APT28](https://attack.mitre.org/groups/G0007) added "junk data" to each encoded string, preventing trivial decoding without knowledge of the junk removal algorithm. Each implant was given a "junk length" value when created, tracked by the controller software to allow seamless communication but prevent analysis of the command protocol on the wire.[^37]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [APT28](https://attack.mitre.org/groups/G0007) has cleared event logs, including by using the commands `wevtutil cl System` and `wevtutil cl Security`.[^44] [^51]  |
| [[Exploitation for Stealth\|T1211]] | Exploitation for Stealth | [APT28](https://attack.mitre.org/groups/G0007) has used CVE-2015-4902 to bypass security features.[^26] [^17]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [APT28](https://attack.mitre.org/groups/G0007) regularly deploys both publicly available (ex: [Mimikatz](https://attack.mitre.org/software/S0002)) and custom password retrieval tools on victims.[^39] [^51]  They have also dumped the LSASS process memory using the MiniDump function.[^4]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [APT28](https://attack.mitre.org/groups/G0007) installed a Delphi backdoor that used a custom algorithm for C2 communications.[^57]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [APT28](https://attack.mitre.org/groups/G0007) has stored captured credential information in a file named pi.log.[^17]  |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [APT28](https://attack.mitre.org/groups/G0007) uses a tool to infect connected USB devices and transmit itself to air-gapped computers when the infected USB device is inserted.[^17]  |
| [[Artificial Intelligence\|T1588.007]] | Artificial Intelligence | [APT28](https://attack.mitre.org/groups/G0007) has deployed [LAMEHUG](https://attack.mitre.org/software/S9035) which can can query an LLM to generate and return commands for post compromise activity on targeted systems.[^24]  |
| [[Brute Force\|T1110]] | Brute Force | [APT28](https://attack.mitre.org/groups/G0007) can perform brute force attacks to obtain credentials.[^22] [^40] [^73]  |
| [[Impersonation\|T1684.001]] | Impersonation | [LAMEHUG](https://attack.mitre.org/software/S9035) has sent spearphishing emails impersonating Ukrainian government officials. [^36]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [APT28](https://attack.mitre.org/groups/G0007) has mapped network drives using [Net](https://attack.mitre.org/software/S0039) and administrator credentials.[^4]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^4]  |
| [[certutil\|S0160]] | certutil | [^5] [^4]  |
| [[Forfiles\|S0193]] | Forfiles | [^19]  |
| [[Winexe\|S0191]] | Winexe | [^19] [^48]  |
| [[Responder\|S0174]] | Responder | [^55] [^45]   |
| [[Mimikatz\|S0002]] | Mimikatz | [^3]  |
| [[Koadic\|S0250]] | Koadic | [^34]  |
| [[cipher.exe\|S1205]] | cipher.exe | [^12]  |
| [[Tor\|S0183]] | Tor | [^4]  |
| [[Wevtutil\|S0645]] | Wevtutil | [^44]  |
| [[Downdelph\|S0134]] | Downdelph | [^21] [^48]  |
| [[reGeorg\|S1187]] | reGeorg | [^6]  |
| [[OLDBAIT\|S0138]] | OLDBAIT | [^37]  |
| [[Fysbis\|S0410]] | Fysbis | [^41]  |
| [[XAgentOSX\|S0161]] | XAgentOSX | [^15] [^68] [^45]  |
| [[CORESHELL\|S0137]] | CORESHELL | [^37] [^48]  |
| [[XTunnel\|S0117]] | XTunnel | [^21] [^68] [^45] [^48]  |
| [[JHUHUGIT\|S0044]] | JHUHUGIT | [^20] [^3] [^70] [^45] [^48]  |
| [[DealersChoice\|S0243]] | DealersChoice | [^52] [^48]  |
| [[Drovorub\|S0502]] | Drovorub | [^33]  |
| [[Zebrocy\|S0251]] | Zebrocy | [^34] [^1] [^70] [^63] [^57]  |
| [[USBStealer\|S0136]] | USBStealer | [^21]  |
| [[LoJax\|S0397]] | LoJax | [^32]  |
| [[LAMEHUG\|S9035]] | LAMEHUG | [APT28](https://attack.mitre.org/groups/G0007) has used [LAMEHUG](https://attack.mitre.org/software/S9035) against targets in Ukraine.[^24] [^36]  |
| [[CHOPSTICK\|S0023]] | CHOPSTICK | [^37] [^3] [^70] [^48]  |
| [[Cannon\|S0351]] | Cannon | [^1] [^63]  |
| [[HIDEDRV\|S0135]] | HIDEDRV | [^21]  |
| [[Komplex\|S0162]] | Komplex | [^15] [^27] [^48]  |
| [[ADVSTORESHELL\|S0045]] | ADVSTORESHELL | [^3] [^70]  |



## References

[^1]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)


[^2]: Threat Group-4127


[^3]: [Kaspersky Sofacy](https://securelist.com/sofacy-apt-hits-high-profile-targets-with-updated-toolset/72924/)


[^4]: [Cybersecurity Advisory GRU Brute Force Campaign July 2021](https://media.defense.gov/2021/Jul/01/2002753896/-1/-1/1/CSA_GRU_GLOBAL_BRUTE_FORCE_CAMPAIGN_UOO158036-21.PDF)


[^5]: [Unit 42 Sofacy Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-sofacy-attacks-multiple-government-entities/)


[^6]: [Security Affairs ANSSI APT28 OCT 2023](https://securityaffairs.com/153131/apt/france-anssi-apt28.html)


[^7]: Fancy Bear


[^8]: Swallowtail


[^9]: SNAKEMACKEREL


[^10]: FROZENLAKE


[^11]: Pawn Storm


[^12]: [Nearest Neighbor Volexity](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/)


[^13]: [Microsoft STRONTIUM Aug 2019](https://msrc-blog.microsoft.com/2019/08/05/corporate-iot-a-path-to-intrusion/)


[^14]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^15]: [XAgentOSX 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-xagentosx-sofacys-xagent-macos-tool/)


[^16]: [Accenture SNAKEMACKEREL Nov 2018](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)


[^17]: [Microsoft SIR Vol 19](http://download.microsoft.com/download/4/4/C/44CDEF0E-7924-4787-A56A-16261691ACE3/Microsoft_Security_Intelligence_Report_Volume_19_English.pdf)


[^18]: [GRIZZLY STEPPE JAR](https://www.us-cert.gov/sites/default/files/publications/JAR_16-20296A_GRIZZLY%20STEPPE-2016-1229.pdf)


[^19]: [Überwachung APT28 Forfiles June 2015](https://netzpolitik.org/2015/digital-attack-on-german-parliament-investigative-report-on-the-hack-of-the-left-party-infrastructure-in-bundestag/)


[^20]: [FireEye APT28 January 2017](https://www.mandiant.com/sites/default/files/2021-09/APT28-Center-of-Storm-2017.pdf)


[^21]: [ESET Sednit Part 3](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part3.pdf)


[^22]: [TrendMicro Pawn Storm 2019](https://documents.trendmicro.com/assets/white_papers/wp-pawn-storm-in-2019.pdf)


[^23]: [McAfee APT28 DDE1 Nov 2017](https://securingtomorrow.mcafee.com/mcafee-labs/apt28-threat-group-adopts-dde-technique-nyc-attack-theme-in-latest-campaign/)


[^24]: [Nov AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)


[^25]: [OpenAI-CTI](https://openai.com/index/disrupting-malicious-uses-of-ai-by-state-affiliated-threat-actors/)


[^26]: [Bitdefender APT28 Dec 2015](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)


[^27]: [Sofacy Komplex Trojan](https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/)


[^28]: [DOJ GRU Charges 2018](https://www.justice.gov/archives/opa/pr/us-charges-russian-gru-officers-international-hacking-and-related-influence-and)


[^29]: [RSAC 2015 Abu Dhabi Stefano Maccaglia](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2015/2015.11.04_Evolving_Threats/cct-w08_evolving-threats-dissection-of-a-cyber-espionage-attack.pdf)


[^30]: Group 74


[^31]: Tsar Team


[^32]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^33]: [NSA/FBI Drovorub August 2020](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF)


[^34]: [Palo Alto Sofacy 06-2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-sofacy-groups-parallel-attacks/)


[^35]: [Secureworks IRON TWILIGHT Profile](https://www.secureworks.com/research/threat-profiles/iron-twilight)


[^36]: [Cato LAMEHUG JUL 2025](https://www.catonetworks.com/blog/cato-ctrl-threat-research-analyzing-lamehug/)


[^37]: [FireEye APT28](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)


[^38]: Sednit


[^39]: [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)


[^40]: [TrendMicro Pawn Storm Dec 2020](https://www.trendmicro.com/en_us/research/20/l/pawn-storm-lack-of-sophistication-as-a-strategy.html)


[^41]: [Fysbis Palo Alto Analysis](https://researchcenter.paloaltonetworks.com/2016/02/a-look-into-fysbis-sofacys-linux-backdoor/)


[^42]: APT28


[^43]: IRON TWILIGHT


[^44]: [Crowdstrike DNC June 2016](https://www.crowdstrike.com/blog/bears-midst-intrusion-democratic-national-committee/)


[^45]: [US District Court Indictment GRU Oct 2018](https://www.justice.gov/opa/page/file/1098481/download)


[^46]: [SecureWorks TG-4127](https://www.secureworks.com/research/threat-group-4127-targets-hillary-clinton-presidential-campaign)


[^47]: [McAfee APT28 DDE2 Nov 2017](http://securityaffairs.co/wordpress/65318/hacking/dde-attack-apt28.html)


[^48]: [Secureworks IRON TWILIGHT Active Measures March 2017](https://www.secureworks.com/research/iron-twilight-supports-active-measures)


[^49]: STRONTIUM


[^50]: Forest Blizzard


[^51]: [DOJ GRU Indictment Jul 2018](https://cdn.cnn.com/cnn/2018/images/07/13/gru.indictment.pdf)


[^52]: [Sofacy DealersChoice](https://researchcenter.paloaltonetworks.com/2018/03/unit42-sofacy-uses-dealerschoice-target-european-government-agency/)


[^53]: [Talos Seduploader Oct 2017](https://blog.talosintelligence.com/2017/10/cyber-conflict-decoy-document.html)


[^54]: TG-4127


[^55]: [FireEye APT28 Hospitality Aug 2017](https://web.archive.org/web/20171202185937/https://www.fireeye.com/blog/threat-research/2017/08/apt28-targets-hospitality-sector.html)


[^56]: [Leonard TAG 2023](https://blog.google/threat-analysis-group/ukraine-remains-russias-biggest-cyber-focus-in-2023/)


[^57]: [ESET Zebrocy May 2019](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)


[^58]: [FireEye Op RussianDoll](https://www.fireeye.com/blog/threat-research/2015/04/probable_apt28_useo.html)


[^59]: [Trend Micro Pawn Storm OAuth 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/pawn-storm-abuses-open-authentication-advanced-social-engineering-attacks)


[^60]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^61]: Sofacy


[^62]: [ESET Sednit Part 1](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part1.pdf)


[^63]: [Unit42 Sofacy Dec 2018](https://unit42.paloaltonetworks.com/dear-joohn-sofacy-groups-global-campaign/)


[^64]: GruesomeLarch


[^65]: [Microsoft STRONTIUM New Patterns Cred Harvesting Sept 2020](https://www.microsoft.com/security/blog/2020/09/10/strontium-detecting-new-patters-credential-harvesting/)


[^66]: [Ars Technica GRU indictment Jul 2018](https://arstechnica.com/information-technology/2018/07/from-bitly-to-x-agent-how-gru-hackers-targeted-the-2016-presidential-election/)


[^67]: [MS17-010 March 2017](https://docs.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010)


[^68]: [Symantec APT28 Oct 2018](https://www.symantec.com/blogs/election-security/apt28-espionage-military-government)


[^69]: [Unit 42 Playbook Dec 2017](https://pan-unit42.github.io/playbook_viewer/)


[^70]: [Securelist Sofacy Feb 2018](https://securelist.com/a-slice-of-2017-sofacy-activity/83930/)


[^71]: [Google TAG Ukraine Threat Landscape March 2022](https://blog.google/threat-analysis-group/update-threat-landscape-ukraine)


[^72]: [Trend Micro Pawn Storm April 2017](https://documents.trendmicro.com/assets/wp/wp-two-years-of-pawn-storm.pdf)


[^73]: [Microsoft Targeting Elections September 2020](https://blogs.microsoft.com/on-the-issues/2020/09/10/cyberattacks-us-elections-trump-biden/)


[^74]: [MSFT-AI](https://www.microsoft.com/en-us/security/blog/2024/02/14/staying-ahead-of-threat-actors-in-the-age-of-ai/)


