---
aliases: 
    - Ke3chang
    - APT15
    - Mirage
    - Vixen Panda
    - GREF
    - Playful Dragon
    - RoyalAPT
    - NICKEL
    - Nylon Typhoon
mitre-attack: https://attack.mitre.org/groups/G0004
---

## G0004

[Ke3chang](https://attack.mitre.org/groups/G0004) is a threat group attributed to actors operating out of China. [Ke3chang](https://attack.mitre.org/groups/G0004) has targeted oil, government, diplomatic, military, and NGOs in Central and South America, the Caribbean, Europe, and North America since at least 2010.[^12] [^8] [^10] [^15] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Remote Email Collection\|T1114.002]] | Remote Email Collection | [Ke3chang](https://attack.mitre.org/groups/G0004) has used compromised credentials and a .NET tool to dump data from Microsoft Exchange mailboxes.[^8] [^15]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Ke3chang](https://attack.mitre.org/groups/G0004) has used tools to download files to compromised machines.[^15]  |
| [[Local Account\|T1087.001]] | Local Account | [Ke3chang](https://attack.mitre.org/groups/G0004) performs account discovery using commands such as `net localgroup administrators` and `net group "REDACTED" /domain` on specific permissions groups.[^12]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Ke3chang](https://attack.mitre.org/groups/G0004) has used implants capable of collecting the signed-in username.[^15]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [Ke3chang](https://attack.mitre.org/groups/G0004) has used implants to collect the system language ID of a compromised machine.[^15]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Ke3chang](https://attack.mitre.org/groups/G0004) performs account discovery using commands such as `net localgroup administrators` and `net group "REDACTED" /domain` on specific permissions groups.[^12]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Ke3chang](https://attack.mitre.org/groups/G0004) has deobfuscated Base64-encoded shellcode strings prior to loading them.[^15]  |
| [[Golden Ticket\|T1558.001]] | Golden Ticket | [Ke3chang](https://attack.mitre.org/groups/G0004) has used [Mimikatz](https://attack.mitre.org/software/S0002) to generate Kerberos golden tickets.[^8]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Ke3chang](https://attack.mitre.org/groups/G0004) actors have been known to copy files to the network shares of other computers to move laterally.[^12] [^8]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Ke3chang](https://attack.mitre.org/groups/G0004) transferred compressed and encrypted RAR files containing exfiltration through the established backdoor command and control channel during operations.[^12]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Ke3chang](https://attack.mitre.org/groups/G0004) has performed frequent and scheduled data collection from victim networks.[^15]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Ke3chang](https://attack.mitre.org/groups/G0004) uses command-line interaction to search files and directories.[^12] [^15]  |
| [[External Remote Services\|T1133]] | External Remote Services | [Ke3chang](https://attack.mitre.org/groups/G0004) has gained access through VPNs including with compromised accounts and stolen VPN certificates.[^8] [^15]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Ke3chang](https://attack.mitre.org/groups/G0004) has used network scanning and enumeration tools, including [Ping](https://attack.mitre.org/software/S0097).[^8]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [Ke3chang](https://attack.mitre.org/groups/G0004) has dumped credentials, including by using gsecdump.[^12] [^8]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Ke3chang](https://attack.mitre.org/groups/G0004) has performed local network configuration discovery using `ipconfig`.[^12] [^8] [^15]  |
| [[Tool\|T1588.002]] | Tool | [Ke3chang](https://attack.mitre.org/groups/G0004) has obtained and used tools such as [Mimikatz](https://attack.mitre.org/software/S0002).[^8]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [Ke3chang](https://attack.mitre.org/groups/G0004) has performed  frequent and scheduled data exfiltration from compromised networks.[^15]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Ke3chang](https://attack.mitre.org/groups/G0004) performs service discovery using `net start` commands.[^12]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Ke3chang](https://attack.mitre.org/groups/G0004) backdoor RoyalDNS established persistence through adding a service called `Nwsapagent`.[^8]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Ke3chang](https://attack.mitre.org/groups/G0004) has compromised networks by exploiting Internet-facing applications, including vulnerable Microsoft Exchange and SharePoint servers.[^15]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Ke3chang](https://attack.mitre.org/groups/G0004) has dropped their malware into legitimate installed software paths including: `C:\ProgramFiles\Realtek\Audio\HDA\AERTSr.exe`, `C:\Program Files (x86)\Foxit Software\Foxit Reader\FoxitRdr64.exe`, `C:\Program Files (x86)\Adobe\Flash Player\AddIns\airappinstaller\airappinstall.exe`, and `C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd64.exe`.[^15]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Ke3chang](https://attack.mitre.org/groups/G0004) has used a tool known as RemoteExec (similar to [PsExec](https://attack.mitre.org/software/S0029)) to remotely execute batch scripts and binaries.[^8]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Ke3chang](https://attack.mitre.org/groups/G0004) gathered information and files from local directories for exfiltration.[^12] [^15]  |
| [[DNS\|T1071.004]] | DNS | [Ke3chang](https://attack.mitre.org/groups/G0004) malware RoyalDNS has used DNS for C2.[^8]  |
| [[Sharepoint\|T1213.002]] | Sharepoint | [Ke3chang](https://attack.mitre.org/groups/G0004) used a SharePoint enumeration and data dumping tool known as spwebmember.[^8]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Ke3chang](https://attack.mitre.org/groups/G0004) has used Base64-encoded shellcode strings.[^15]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | Malware used by [Ke3chang](https://attack.mitre.org/groups/G0004) can run commands on the command-line interface.[^12] [^8]  |
| [[Right-to-Left Override\|T1036.002]] | Right-to-Left Override | [Ke3chang](https://attack.mitre.org/groups/G0004) has used the right-to-left override character in spearphishing attachment names to trick targets into executing .scr and .exe files.[^12]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | The [Ke3chang](https://attack.mitre.org/groups/G0004) group has been known to compress data before exfiltration.[^12]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [Ke3chang](https://attack.mitre.org/groups/G0004) performs discovery of permission groups `net group /domain`.[^12]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Ke3chang](https://attack.mitre.org/groups/G0004) is known to use 7Zip and RAR with passwords to encrypt data prior to exfiltration.[^12] [^15]  |
| [[NTDS\|T1003.003]] | NTDS | [Ke3chang](https://attack.mitre.org/groups/G0004) has used NTDSDump and other password dumping tools to gather credentials.[^15]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Ke3chang](https://attack.mitre.org/groups/G0004) performs process discovery using `tasklist` commands.[^12] [^8]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Ke3chang](https://attack.mitre.org/groups/G0004) has dumped credentials, including by using [Mimikatz](https://attack.mitre.org/software/S0002).[^12] [^8] [^15]  |
| [[Malware\|T1587.001]] | Malware | [Ke3chang](https://attack.mitre.org/groups/G0004) has developed custom malware that allowed them to maintain persistence on victim networks.[^15]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Ke3chang](https://attack.mitre.org/groups/G0004) malware including RoyalCli and BS2005 have communicated over HTTP with the C2 server through Internet Explorer (IE) by using the COM interface IWebBrowser2.[^8] [^15]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Ke3chang](https://attack.mitre.org/groups/G0004) has used batch scripts in its malware to install persistence mechanisms.[^8]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Ke3chang](https://attack.mitre.org/groups/G0004) has used credential dumpers or stealers to obtain legitimate credentials, which they used to gain access to victim accounts.[^15]  |
| [[Botnet\|T1583.005]] | Botnet | [Ke3chang](https://attack.mitre.org/groups/G0004) has utilized an ORB (operational relay box) network for reconnaissance and vulnerability exploitation.[^5]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | Several [Ke3chang](https://attack.mitre.org/groups/G0004) backdoors achieved persistence by adding a Run key.[^8]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Ke3chang](https://attack.mitre.org/groups/G0004) performs local network connection discovery using `netstat`.[^12] [^8]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Ke3chang](https://attack.mitre.org/groups/G0004) has used keyloggers.[^8] [^15]  |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | [Ke3chang](https://attack.mitre.org/groups/G0004) has dumped credentials, including by using gsecdump.[^12] [^8]  |
| [[Cloud Accounts\|T1078.004]] | Cloud Accounts | [Ke3chang](https://attack.mitre.org/groups/G0004) has used compromised credentials to sign into victims’ Microsoft 365 accounts.[^15]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Ke3chang](https://attack.mitre.org/groups/G0004) performs operating system information discovery using `systeminfo` and has used implants to identify the system language and computer name.[^12] [^8] [^15]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^12] [^8]  |
| [[ipconfig\|S0100]] | ipconfig | [^12] [^8]  |
| [[Tasklist\|S0057]] | Tasklist | [^8]  |
| [[spwebmember\|S0227]] | spwebmember | [^8]  |
| [[netstat\|S0104]] | netstat | [^12] [^8]  |
| [[Systeminfo\|S0096]] | Systeminfo | [^12] [^8]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^8] [^15]  |
| [[Ping\|S0097]] | Ping | [^8]  |
| [[Okrum\|S0439]] | Okrum | [^3]  |
| [[Neoichor\|S0691]] | Neoichor | [^15]  |
| [[MirageFox\|S0280]] | MirageFox | [^10]  |



## References

[^1]: Vixen Panda


[^2]: GREF


[^3]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)


[^4]: APT15


[^5]: [ORB Mandiant](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-espionage-orb-networks)


[^6]: NICKEL


[^7]: Ke3chang


[^8]: [NCC Group APT15 Alive and Strong](https://research.nccgroup.com/2018/03/10/apt15-is-alive-and-strong-an-analysis-of-royalcli-and-royaldns/)


[^9]: Mirage


[^10]: [APT15 Intezer June 2018](https://web.archive.org/web/20180615122133/https://www.intezer.com/miragefox-apt15-resurfaces-with-new-tools-based-on-old-ones/)


[^11]: Playful Dragon


[^12]: [Mandiant Operation Ke3chang November 2014](https://www.mandiant.com/resources/operation-ke3chang-targeted-attacks-against-ministries-of-foreign-affairs)


[^13]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^14]: [Villeneuve et al 2014](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-operation-ke3chang.pdf)


[^15]: [Microsoft NICKEL December 2021](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)


[^16]: RoyalAPT


[^17]: Nylon Typhoon


