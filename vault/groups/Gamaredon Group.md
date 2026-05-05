---
aliases: 
    - Gamaredon Group
    - IRON TILDEN
    - Primitive Bear
    - ACTINIUM
    - Armageddon
    - Shuckworm
    - DEV-0157
    - Aqua Blizzard
    - NastyShrew
mitre-attack: https://attack.mitre.org/groups/G0047
---

## G0047

[Gamaredon Group](https://attack.mitre.org/groups/G0047) is a suspected Russian cyber espionage group that has targeted military, law enforcement, judiciary, non-profit, and non-governmental organizations in Ukraine since at least 2013. The name [Gamaredon Group](https://attack.mitre.org/groups/G0047) derives from a misspelling of the word "Armageddon," found in early campaigns.[^11] [^6] [^26] [^5] [^4] <br><br>In November 2021, the Ukrainian government publicly attributed [Gamaredon Group](https://attack.mitre.org/groups/G0047) to Russia’s Federal Security Service (FSB) Center 18, an assessment later supported by multiple independent cybersecurity researchers. [^24] [^4] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Internal Defacement\|T1491.001]] | Internal Defacement | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has left taunting images and messages on the victims' desktops as proof of system access.[^7]  |
| [[Virtual Private Server\|T1583.003]] | Virtual Private Server | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used VPS hosting providers for infrastructure outside of Russia.[^13] [^19] [^17]   |
| [[Data Obfuscation\|T1001]] | Data Obfuscation | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used obfuscated VBScripts with randomly generated variable names and concatenated strings.[^13]   |
| [[Internal Spearphishing\|T1534]] | Internal Spearphishing | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used an Outlook VBA module on infected systems to send phishing emails with malicious attachments to other employees within the organization.[^26]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used WMI to execute scripts used for discovery and for determining the C2 IP address.[^7] [^13] [^8] [^19]  [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used the following WMI query to search for a ping record: `Select * From Win32_PingStatus where Address = 'mil.gov.ua'`.[^8]   |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used SOCKS5 over port 9050 for C2 communication.[^8]   |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Gamaredon Group](https://attack.mitre.org/groups/G0047) macros can scan for Microsoft Word and Excel files to inject with additional malicious macros. [Gamaredon Group](https://attack.mitre.org/groups/G0047) has also used its backdoors to automatically list interesting files (such as Office documents) found on a system.[^26] [^18] [^19]  Gamaredon Group has also identified directory trees, folders and files on the compromised host.[^8]   |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has replicated to removable media by leveraging the User Assist Reg Key and creating LNKs on all network and removable drives available on the infected host.[^8]   |
| [[Automated Collection\|T1119]] | Automated Collection | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has deployed scripts on compromised systems that automatically scan for interesting documents.[^26]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used legitimate process names to hide malware including `svchosst`.[^18]  Additionally, [Gamaredon Group](https://attack.mitre.org/groups/G0047) disguised malicious ZIP archives as Office documents that are related to the invasion.[^21]  |
| [[Compile After Delivery\|T1027.004]] | Compile After Delivery | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has compiled the source code for a downloader directly on the infected system using the built-in `Microsoft.CSharp.CSharpCodeProvider` class.[^26] 	 |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has downloaded additional malware and tools onto a compromised host.[^11] [^6] [^26] [^4] [^19] [^21]  For example, [Gamaredon Group](https://attack.mitre.org/groups/G0047) uses a backdoor script to retrieve and decode additional payloads once in victim environments.[^13]   |
| [[VNC\|T1021.005]] | VNC | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used VNC tools, including UltraVNC, to remotely interact with compromised hosts.[^5] [^4] [^18]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has obfuscated .NET executables by inserting junk code.[^26] 	 |
| [[Rundll32\|T1218.011]] | Rundll32 | [Gamaredon Group](https://attack.mitre.org/groups/G0047) malware has used rundll32 to launch additional malicious components.[^26]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has delivered spearphishing emails with malicious attachments to targets.[^6] [^26] [^7] [^4] [^18] [^27] [^13] [^19] [^10]  Additionally, [Gamaredon Group](https://attack.mitre.org/groups/G0047) has distributed malicious LNK files compressed in ZIP archives.[^21]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | A [Gamaredon Group](https://attack.mitre.org/groups/G0047) file stealer can gather the victim's computer name and drive serial numbers to send to a C2 server.[^11] [^6] [^7] [^8] [^19]   |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has embedded malicious macros in document templates, which executed VBScript. [Gamaredon Group](https://attack.mitre.org/groups/G0047) has also delivered Microsoft Outlook VBA projects with embedded macros.[^6] [^26] [^7] [^4] [^27] [^19]  Additionally, [Gamaredon Group](https://attack.mitre.org/groups/G0047) has executed VBScript files using wscript.exe.[^8]   |
| [[Screen Capture\|T1113]] | Screen Capture | [Gamaredon Group](https://attack.mitre.org/groups/G0047)'s malware can take screenshots of the compromised computer every minute.[^26] [^8] [^19]    	 |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used PowerShell scripts to identify security software on the victim machine.[^8]   |
| [[Data from Local System\|T1005]] | Data from Local System | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has collected files from infected systems and uploaded them to a C2 server.[^26] [^19]   |
| [[Data from Network Shared Drive\|T1039]] | Data from Network Shared Drive | [Gamaredon Group](https://attack.mitre.org/groups/G0047) malware has collected Microsoft Office documents from mapped network drives.[^26] [^19]   |
| [[Upload Malware\|T1608.001]] | Upload Malware | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has registered domains to stage payloads.[^4] [^18]  |
| [[Compression\|T1027.015]] | Compression | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has delivered malicious payloads within compressed archives and zip files. [^21]  |
| [[One-Way Communication\|T1102.003]] | One-Way Communication | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used Telegram Messenger content to discover the IP address for C2 communications.[^13]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has removed security settings for VBA macro execution by changing registry values `HKCU\Software\Microsoft\Office\&lt;version&gt;\&lt;product&gt;\Security\VBAWarnings` and `HKCU\Software\Microsoft\Office\&lt;version&gt;\&lt;product&gt;\Security\AccessVBOM`.[^26] [^7] [^19]  [Gamaredon Group](https://attack.mitre.org/groups/G0047) has also modified Registry keys to hide folders and system files and to add the C2 address under `HKEY_CURRENT_USER\Console\WindowsUpdate`. [^8]   |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has tested connectivity between a compromised machine and a C2 server using [Ping](https://attack.mitre.org/software/S0097) with commands such as `CSIDL_SYSTEM\cmd.exe /c ping -n 1`.[^5]  [Gamaredon Group](https://attack.mitre.org/groups/G0047) has searched the ping records to obtain the C2 address and has used ping to search for the C2’s status.[^8]   |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used an obfuscated PowerShell script that used `System.Reflection.Assembly` to gather and send victim information to the C2.[^8]   |
| [[Component Object Model\|T1559.001]] | Component Object Model | [Gamaredon Group](https://attack.mitre.org/groups/G0047) malware can insert malicious macros into documents using a `Microsoft.Office.Interop` object.[^26] [^19]  	 |
| [[Query Registry\|T1012]] | Query Registry | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has queried ` HKEY_CURRENT_USER\\Console\\WindowsUpdates` to obtain the C2 addresses.[^8]  [Gamaredon Group](https://attack.mitre.org/groups/G0047) has queried ` HKEY_CURRENT_USER\\Console\\WindowsUpdates` to obtain the C2 addresses.[^8]   |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | A [Gamaredon Group](https://attack.mitre.org/groups/G0047) file stealer has the capability to steal data from newly connected logical volumes on a system, including USB drives.[^11] [^26] [^19]   |
| [[Template Injection\|T1221]] | Template Injection | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used DOCX files to download malicious DOT document templates and has used RTF template injection to download malicious payloads.[^20]  [Gamaredon Group](https://attack.mitre.org/groups/G0047) can also inject malicious macros or remote templates into documents already present on compromised systems.[^6] [^26] [^7] [^4] [^18] [^27] [^19]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has delivered macros which can tamper with Microsoft Office security settings.[^26] [^19]  	 |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Gamaredon Group](https://attack.mitre.org/groups/G0047) tools decrypted additional payloads from the C2. [Gamaredon Group](https://attack.mitre.org/groups/G0047) has also decoded Base64-encoded source code of a downloader.[^6] [^26] [^19]   Additionally, [Gamaredon Group](https://attack.mitre.org/groups/G0047) has decoded Telegram content to reveal the IP address for C2 communications.[^13]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has attempted to get users to click on a link pointing to a malicious HTML file leading to follow-on malicious content.[^13] [^19]    |
| [[Taint Shared Content\|T1080]] | Taint Shared Content | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has injected malicious macros into all Word and Excel documents on mapped network drives.[^26]  |
| [[Native API\|T1106]] | Native API | [Gamaredon Group](https://attack.mitre.org/groups/G0047) malware has used `CreateProcess` to launch additional malicious components.[^26] [^19]   |
| [[Web Services\|T1583.006]] | Web Services | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used Cloudflare’s TryClouldflare service to obtain C2 nodes.[^8]   |
| [[Disk Content Wipe\|T1561.001]] | Disk Content Wipe | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used tools to delete files and folders from victims' desktops and profiles.[^7]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | A [Gamaredon Group](https://attack.mitre.org/groups/G0047) file stealer can gather the victim's username to send to a C2 server.[^11]  |
| [[Digital Certificates\|T1587.003]] | Digital Certificates | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used the same TLS certificate across its infrastructure.[^17]   |
| [[Hidden Window\|T1564.003]] | Hidden Window | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used `hidcon` to run batch files in a hidden console window.[^18]  [Gamaredon Group](https://attack.mitre.org/groups/G0047) has also executed PowerShell in a hidden window.[^21]   |
| [[LNK Icon Smuggling\|T1027.012]] | LNK Icon Smuggling | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used LNK files to hide malicious scripts for execution.[^8] [^21]   |
| [[File Deletion\|T1070.004]] | File Deletion | [Gamaredon Group](https://attack.mitre.org/groups/G0047) tools can delete files used during an operation.[^6] [^5] [^7] [^19]   |
| [[PowerShell\|T1059.001]] | PowerShell | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used obfuscated PowerShell scripts for staging.[^4] [^19]  Additionally, (LinkById : G0047) has used PowerShell based tools later in its attack chain.[^8]  Additionally, [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used the PowerShell cmdlet `Get-Command` to download and execute the next stage payload.[^21]    |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used port 6856 for C2 communications.[^21]  |
| [[Tool\|T1588.002]] | Tool | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used various legitimate tools, such as `mshta.exe` and [Reg](https://attack.mitre.org/software/S0075), and services during operations.[^13] [^19]        |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used modules that automatically upload gathered documents to the C2 server.[^26]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used HTTP and HTTPS for C2 communications.[^11] [^6] [^26] [^5] [^7] [^18] [^13] [^19] [^21]  |
| [[Domains\|T1583.001]] | Domains | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has registered multiple domains to facilitate payload staging and C2.[^4] [^18] [^19] [^8]   |
| [[Fast Flux DNS\|T1568.001]] | Fast Flux DNS | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used fast flux DNS to mask their command and control channel behind rotating IP addresses.[^13] [^19] [^10]  Additionally, [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used a low-frequency variant of the single-flux method.[^17]   |
| [[Process Injection\|T1055]] | Process Injection | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has injected [Remcos](https://attack.mitre.org/software/S0332) into explorer.exe.[^21]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [Gamaredon Group](https://attack.mitre.org/groups/G0047) tools have contained an application to check performance of USB flash drives. [Gamaredon Group](https://attack.mitre.org/groups/G0047) has also used malware to scan for removable drives.[^11] [^26] [^19]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | A [Gamaredon Group](https://attack.mitre.org/groups/G0047) file stealer can transfer collected files to a hardcoded C2 server.[^11] [^19] [^8]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used [Tor](https://attack.mitre.org/software/S0183) for C2 traffic.[^8]   |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has created scheduled tasks to launch executables after a designated number of minutes have passed.[^26] [^7] [^4] [^13] 	 |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has delivered self-extracting 7z archive files within malicious document attachments.[^26]  Additionally, [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used an obfuscated .drv file.[^8]   |
| [[Process Discovery\|T1057]] | Process Discovery | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used tools to enumerate processes on target hosts including Process Explorer.[^5] [^18] [^8]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used obfuscated or encrypted scripts.[^26] [^4] [^8] [^19]     |
| [[Malicious File\|T1204.002]] | Malicious File | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has attempted to get users to click on Office attachments with malicious macros embedded.[^6] [^26] [^5] [^7] [^4] [^18] [^27] [^13]  [Gamaredon Group](https://attack.mitre.org/groups/G0047) has also attempted to get users to click on thematically named files.[^21]   |
| [[Dynamic Resolution\|T1568]] | Dynamic Resolution | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has incorporated dynamic DNS domains in its infrastructure.[^18]  |
| [[Proxy\|T1090]] | Proxy | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used the Cloudflare Tunnel client to proxy C2 traffic.[^19]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Gamaredon Group](https://attack.mitre.org/groups/G0047) tools have registered Run keys in the registry to give malicious VBS files persistence.[^6] [^26] [^7] [^13] [^19]   |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used geoblocking to limit downloads of the malicious file to specific geographic locations.[^13] [^21]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used several ways to try to resolve the C2 server, including: public third-party websites, an adversary-operated Telegraph channel, the [ngrok](https://attack.mitre.org/software/S0508) utility and the TXT record of a hardcoded C2 domain.[^19] [^8]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used various batch scripts to establish C2 and download additional files. [Gamaredon Group](https://attack.mitre.org/groups/G0047)'s backdoor malware has also been written to a batch file.[^11] [^26] [^7] [^18]  |
| [[Mshta\|T1218.005]] | Mshta | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used `mshta.exe` to execute malicious files.[^5] [^13] [^19] [^8]  |
| [[Office Application Startup\|T1137]] | Office Application Startup | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has inserted malicious macros into existing documents, providing persistence when they are reopened. [Gamaredon Group](https://attack.mitre.org/groups/G0047) has loaded the group's previously delivered VBA project by relaunching Microsoft Outlook with the `/altvba` option, once the Application.Startup event is received.[^26]  |
| [[Web Service\|T1102]] | Web Service | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used GitHub repositories for downloaders which will be obtained by the group's .NET executable on the compromised system.[^26] 	 |
| [[System Checks\|T1497.001]] | System Checks | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has checked existing conditions, such as geographic location, device type, or system specification, before the victim is sent a malicious Word document.[^10]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Remcos\|S0332]] | Remcos | [Gamaredon Group](https://attack.mitre.org/groups/G0047) used [Remcos](https://attack.mitre.org/software/S0332) during operations.[^21]  |
| [[Ping\|S0097]] | Ping | [^5]  |
| [[Reg\|S0075]] | Reg | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used [Reg](https://attack.mitre.org/software/S0075) to add Run keys to the Registry.[^13]  |
| [[QuietSieve\|S0686]] | QuietSieve | [^4]  |
| [[Pteranodon\|S0147]] | Pteranodon | [^11] [^5] [^4] [^18] [^27]  |
| [[PowerPunch\|S0685]] | PowerPunch | [^4]  |



## References

[^1]: IRON TILDEN


[^2]: Primitive Bear


[^3]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^4]: [Microsoft Actinium February 2022](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)


[^5]: [Symantec Shuckworm January 2022](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/shuckworm-gamaredon-espionage-ukraine)


[^6]: [TrendMicro Gamaredon April 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/gamaredon-apt-group-use-covid-19-lure-in-campaigns/)


[^7]: [CERT-EE Gamaredon January 2021](https://www.ria.ee/sites/default/files/content-editors/kuberturve/tale_of_gamaredon_infection.pdf)


[^8]: [SymantecCarbonBlack_ShuckwormUSB_Apr2025](https://www.security.com/threat-intelligence/shuckworm-ukraine-gammasteel)


[^9]: DEV-0157


[^10]: [SilentPush_GamaredonFastFlux_Sept2023](https://www.silentpush.com/blog/from-russia-with-a-71/)


[^11]: [Palo Alto Gamaredon Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/)


[^12]: [Cloudflare 2026 Threat Report New Threat Actors March 2026](https://blog.cloudflare.com/2026-threat-report/)


[^13]: [unit42_gamaredon_dec2022](https://unit42.paloaltonetworks.com/trident-ursa/)


[^14]: Aqua Blizzard


[^15]: Armageddon


[^16]: NastyShrew


[^17]: [Huntio_GamaredonFlux_Apr2025](https://hunt.io/blog/state-sponsored-activity-gamaredon-shadowpad)


[^18]: [Unit 42 Gamaredon February 2022](https://unit42.paloaltonetworks.com/gamaredon-primitive-bear-ukraine-update-2021/)


[^19]: [ESET Gamaredon Sept2024](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)


[^20]: [Proofpoint RTF Injection](https://www.proofpoint.com/us/blog/threat-insight/injection-new-black-novel-rtf-template-inject-technique-poised-widespread)


[^21]: [VenereCiscoTalos_Gamaredon_Mar2025](https://blog.talosintelligence.com/gamaredon-campaign-distribute-remcos/)


[^22]: Gamaredon Group


[^23]: ACTINIUM


[^24]: [Bleepingcomputer Gamardeon FSB November 2021](https://www.bleepingcomputer.com/news/security/ukraine-links-members-of-gamaredon-hacker-group-to-russian-fsb/)


[^25]: Shuckworm


[^26]: [ESET Gamaredon June 2020](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)


[^27]: [Secureworks IRON TILDEN Profile](https://www.secureworks.com/research/threat-profiles/iron-tilden)


