---
aliases: 
    - menuPass
    - Cicada
    - POTASSIUM
    - Stone Panda
    - APT10
    - Red Apollo
    - CVNX
    - HOGFISH
    - BRONZE RIVERSIDE
mitre-attack: https://attack.mitre.org/groups/G0045
---

## G0045

[menuPass](https://attack.mitre.org/groups/G0045) is a threat group that has been active since at least 2006. Individual members of [menuPass](https://attack.mitre.org/groups/G0045) are known to have acted in association with the Chinese Ministry of State Security's (MSS) Tianjin State Security Bureau and worked for the Huaying Haitai Science and Technology Development Company.[^1] [^4] <br><br>[menuPass](https://attack.mitre.org/groups/G0045) has targeted healthcare, defense, aerospace, finance, maritime, biotechnology, energy, and government sectors globally, with an emphasis on Japanese organizations. In 2016 and 2017, the group is known to have targeted managed IT service providers (MSPs), manufacturing and mining companies, and a university.[^2] [^21] [^13] [^15] [^5] [^1] [^4] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [menuPass](https://attack.mitre.org/groups/G0045) uses scripts to enumerate IP ranges on the victim network. [menuPass](https://attack.mitre.org/groups/G0045) has also issued the command `net view /domain` to a [PlugX](https://attack.mitre.org/software/S0013) implant to gather information about remote systems on the network.[^7] [^5]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [menuPass](https://attack.mitre.org/groups/G0045) has used a modified version of pentesting script wmiexec.vbs, which logs into a remote machine using WMI.[^7] [^22] [^14]  |
| [[Masquerading\|T1036]] | Masquerading | [menuPass](https://attack.mitre.org/groups/G0045) has used [esentutl](https://attack.mitre.org/software/S0404) to change file extensions to their true type that were masquerading as .txt files.[^23]   |
| [[File Deletion\|T1070.004]] | File Deletion | A [menuPass](https://attack.mitre.org/groups/G0045) macro deletes files after it has decoded and decompressed them.[^18] [^4]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [menuPass](https://attack.mitre.org/groups/G0045) has used tcping.exe, similar to [Ping](https://attack.mitre.org/software/S0097), to probe port status on systems of interest.[^7]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [menuPass](https://attack.mitre.org/groups/G0045) has used `net use` to conduct connectivity checks to machines.[^15]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [menuPass](https://attack.mitre.org/groups/G0045) has compressed files before exfiltration using TAR and RAR.[^15] [^7] [^14]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [menuPass](https://attack.mitre.org/groups/G0045) has sent malicious Office documents via email as part of spearphishing campaigns as well as executables disguised as documents.[^7] [^5] [^23] [^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [menuPass](https://attack.mitre.org/groups/G0045) has installed updates and new malware on victims.[^15] [^4]  |
| [[Tool\|T1588.002]] | Tool | [menuPass](https://attack.mitre.org/groups/G0045) has used and modified open-source tools like [Impacket](https://attack.mitre.org/software/S0357), [Mimikatz](https://attack.mitre.org/software/S0002), and [pwdump](https://attack.mitre.org/software/S0006).[^7]  |
| [[Malicious File\|T1204.002]] | Malicious File | [menuPass](https://attack.mitre.org/groups/G0045) has attempted to get victims to open malicious files such as Windows Shortcuts (.lnk) and/or Microsoft Office documents, sent via email as part of spearphishing campaigns.[^7] [^5] [^18] [^23] [^4]  |
| [[External Proxy\|T1090.002]] | External Proxy | [menuPass](https://attack.mitre.org/groups/G0045) has used a global service provider's IP as a proxy for C2 traffic from a victim.[^5] [^23]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [menuPass](https://attack.mitre.org/groups/G0045) has used valid accounts including shared between Managed Service Providers and clients to move between the two environments.[^15] [^14] [^4] [^11]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [menuPass](https://attack.mitre.org/groups/G0045) has used several tools to scan for open NetBIOS nameservers and enumerate NetBIOS sessions.[^7]  |
| [[Fast Flux DNS\|T1568.001]] | Fast Flux DNS | [menuPass](https://attack.mitre.org/groups/G0045) has used dynamic DNS service providers to host malicious domains.[^4]  |
| [[Rename Legitimate Utilities\|T1036.003]] | Rename Legitimate Utilities | [menuPass](https://attack.mitre.org/groups/G0045) has renamed [certutil](https://attack.mitre.org/software/S0160) and moved it to a different location on the system to avoid detection based on use of the tool.[^23]  |
| [[Keylogging\|T1056.001]] | Keylogging | [menuPass](https://attack.mitre.org/groups/G0045) has used key loggers to steal usernames and passwords.[^4]  |
| [[Domain Account\|T1087.002]] | Domain Account | [menuPass](https://attack.mitre.org/groups/G0045) has used the Microsoft administration tool csvde.exe to export Active Directory data.[^7]  |
| [[NTDS\|T1003.003]] | NTDS | [menuPass](https://attack.mitre.org/groups/G0045) has used Ntdsutil to dump credentials.[^14]  |
| [[InstallUtil\|T1218.004]] | InstallUtil | [menuPass](https://attack.mitre.org/groups/G0045) has used `InstallUtil.exe` to execute malicious software.[^7]  |
| [[Native API\|T1106]] | Native API | [menuPass](https://attack.mitre.org/groups/G0045) has used native APIs including `GetModuleFileName`, `lstrcat`, `CreateFile`, and `ReadFile`.[^14]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [menuPass](https://attack.mitre.org/groups/G0045) has used a modified version of pentesting tools wmiexec.vbs and secretsdump.py to dump credentials.[^7] [^22]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [menuPass](https://attack.mitre.org/groups/G0045) has encoded strings in its malware with base64 as well as with a simple, single-byte XOR obfuscation using key 0x40.[^18] [^23] [^14]  |
| [[Trusted Relationship\|T1199]] | Trusted Relationship | [menuPass](https://attack.mitre.org/groups/G0045) has used legitimate access granted to Managed Service Providers in order to access victims of interest.[^7] [^5] [^14] [^1] [^4]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [menuPass](https://attack.mitre.org/groups/G0045) has leveraged vulnerabilities in Pulse Secure VPNs to hijack sessions.[^11]  |
| [[Remote Data Staging\|T1074.002]] | Remote Data Staging | [menuPass](https://attack.mitre.org/groups/G0045) has staged data on remote MSP systems or other victim networks prior to exfiltration.[^15] [^14]  |
| [[Clear Command History\|T1070.003]] | Clear Command History | [menuPass](https://attack.mitre.org/groups/G0045) has used [Wevtutil](https://attack.mitre.org/software/S0645) to remove PowerShell execution logs.[^11]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [menuPass](https://attack.mitre.org/groups/G0045) has used [certutil](https://attack.mitre.org/software/S0160) in a macro to decode base64-encoded content contained in a dropper document attached to an email. The group has also used `certutil -decode` to decode files on the victim’s machine when dropping [UPPERCUT](https://attack.mitre.org/software/S0275).[^18] [^23]  |
| [[Code Signing\|T1553.002]] | Code Signing | [menuPass](https://attack.mitre.org/groups/G0045) has resized and added data to the certificate table to enable the signing of modified files with legitimate signatures.[^11]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [menuPass](https://attack.mitre.org/groups/G0045) has used a script (atexec.py) to execute a command on a target machine via Task Scheduler.[^7]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [menuPass](https://attack.mitre.org/groups/G0045) has used process hollowing in iexplore.exe to load the [RedLeaves](https://attack.mitre.org/software/S0153) implant.[^18]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [menuPass](https://attack.mitre.org/groups/G0045) stages data prior to exfiltration in multi-part archives, often saved in the Recycle Bin.[^15]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [menuPass](https://attack.mitre.org/groups/G0045) has used RDP connections to move across the victim network.[^15] [^4]  |
| [[Data from Network Shared Drive\|T1039]] | Data from Network Shared Drive | [menuPass](https://attack.mitre.org/groups/G0045) has collected data from remote systems by mounting network shares with `net use` and using Robocopy to transfer data.[^15]  |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | [menuPass](https://attack.mitre.org/groups/G0045) has used a modified version of pentesting tools wmiexec.vbs and secretsdump.py to dump credentials.[^7] [^22]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [menuPass](https://attack.mitre.org/groups/G0045) has searched compromised systems for folders of interest including those related to HR, audit and expense, and meeting memos.[^14]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [menuPass](https://attack.mitre.org/groups/G0045) has been seen changing malicious files to appear legitimate.[^4]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [menuPass](https://attack.mitre.org/groups/G0045) has encrypted files and information before exfiltration.[^1] [^4]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [menuPass](https://attack.mitre.org/groups/G0045) executes commands using a command-line interface and reverse shell. The group has used a modified version of pentesting script wmiexec.vbs to execute commands.[^15] [^7] [^22] [^23]  [menuPass](https://attack.mitre.org/groups/G0045) has used malicious macros embedded inside Office documents to execute files.[^18] [^23]  |
| [[Data from Local System\|T1005]] | Data from Local System | [menuPass](https://attack.mitre.org/groups/G0045) has collected various files from the compromised computers.[^1] [^14] <br> |
| [[PowerShell\|T1059.001]] | PowerShell | [menuPass](https://attack.mitre.org/groups/G0045) uses [PowerSploit](https://attack.mitre.org/software/S0194) to inject shellcode into PowerShell.[^7] [^14]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [menuPass](https://attack.mitre.org/groups/G0045) has used tools to exploit the ZeroLogon vulnerability (CVE-2020-1472).[^14]  |
| [[SSH\|T1021.004]] | SSH | [menuPass](https://attack.mitre.org/groups/G0045) has used Putty Secure Copy Client (PSCP) to transfer data.[^15]  |
| [[Automated Collection\|T1119]] | Automated Collection | [menuPass](https://attack.mitre.org/groups/G0045) has used the Csvde tool to collect Active Directory files and data.[^14]  |
| [[Domains\|T1583.001]] | Domains | [menuPass](https://attack.mitre.org/groups/G0045) has registered malicious domains for use in intrusion campaigns.[^1] [^4]  |
| [[DLL\|T1574.001]] | DLL | [menuPass](https://attack.mitre.org/groups/G0045) has used DLL side-loading to launch versions of Mimikatz and PwDump6 as well as [UPPERCUT](https://attack.mitre.org/software/S0275).[^7] [^23] [^14]  [menuPass](https://attack.mitre.org/groups/G0045) has also used DLL search order hijacking.[^15]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^7]  |
| [[certutil\|S0160]] | certutil | [^18] [^23] [^14]  |
| [[PowerSploit\|S0194]] | PowerSploit | [^7]  |
| [[Impacket\|S0357]] | Impacket | [^7]  |
| [[pwdump\|S0006]] | pwdump | [^7]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^7]  |
| [[Ping\|S0097]] | Ping | [^7] [^5]  |
| [[cmd\|S0106]] | cmd | [^7]  |
| [[esentutl\|S0404]] | esentutl | [^23]  |
| [[QuasarRAT\|S0262]] | QuasarRAT | [^1] [^14] [^11]  |
| [[AdFind\|S0552]] | AdFind | [^14]  |
| [[PsExec\|S0029]] | PsExec | [^7] [^5]  |
| [[RedLeaves\|S0153]] | RedLeaves | [^7] [^1]  |
| [[Ecipekac\|S0624]] | Ecipekac | [^11]  |
| [[EvilGrab\|S0152]] | EvilGrab | [^7]  |
| [[SNUGRIDE\|S0159]] | SNUGRIDE | [^5]  |
| [[FYAnti\|S0628]] | FYAnti | [^11]  |
| [[HUI Loader\|S1097]] | HUI Loader | [^9]  |
| [[PlugX\|S0013]] | PlugX | [^7] [^5] [^1]  |
| [[P8RAT\|S0626]] | P8RAT | [^11]  |
| [[SodaMaster\|S0627]] | SodaMaster | [^11]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^11]  |
| [[PoisonIvy\|S0012]] | PoisonIvy | [^7] [^4]  |
| [[ChChes\|S0144]] | ChChes | [^7]  |
| [[UPPERCUT\|S0275]] | UPPERCUT | [menuPass](https://attack.mitre.org/groups/G0045) has used [UPPERCUT](https://attack.mitre.org/software/S0275) during operations.[^23]  |



## References

[^1]: [DOJ APT10 Dec 2018](https://www.justice.gov/opa/pr/two-chinese-hackers-associated-ministry-state-security-charged-global-computer-intrusion)


[^2]: [Palo Alto menuPass Feb 2017](http://researchcenter.paloaltonetworks.com/2017/02/unit42-menupass-returns-new-malware-new-attacks-japanese-academics-organizations/)


[^3]: APT10


[^4]: [District Court of NY APT10 Indictment December 2018](https://www.justice.gov/opa/page/file/1122671/download)


[^5]: [FireEye APT10 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/apt10_menupass_grou.html)


[^6]: Stone Panda


[^7]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^8]: POTASSIUM


[^9]: [SecureWorks BRONZE STARLIGHT Ransomware Operations June 2022](https://www.secureworks.com/research/bronze-starlight-ransomware-operations-use-hui-loader)


[^10]: CVNX


[^11]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)


[^12]: BRONZE RIVERSIDE


[^13]: [FireEye Poison Ivy](https://www.mandiant.com/sites/default/files/2021-09/rpt-poison-ivy.pdf)


[^14]: [Symantec Cicada November 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/cicada-apt10-japan-espionage)


[^15]: [PWC Cloud Hopper April 2017](https://web.archive.org/web/20220224041316/https:/www.pwc.co.uk/cyber-security/pdf/cloud-hopper-report-final-v4.pdf)


[^16]: Cicada


[^17]: HOGFISH


[^18]: [Accenture Hogfish April 2018](http://web.archive.org/web/20220810112638/https:/www.accenture.com/t20180423T055005Z_w_/se-en/_acnmedia/PDF-76/Accenture-Hogfish-Threat-Analysis.pdf)


[^19]: Red Apollo


[^20]: menuPass


[^21]: [Crowdstrike CrowdCast Oct 2013](https://www.slideshare.net/slideshow/crowd-casts-monthly-you-have-an-adversary-problem/27262315)


[^22]: [Github AD-Pentest-Script](https://github.com/Twi1ight/AD-Pentest-Script/blob/master/wmiexec.vbs)


[^23]: [FireEye APT10 Sept 2018](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)


