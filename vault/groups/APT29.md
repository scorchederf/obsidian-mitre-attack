---
aliases: 
    - APT29
    - IRON RITUAL
    - IRON HEMLOCK
    - NobleBaron
    - Dark Halo
    - NOBELIUM
    - UNC2452
    - YTTRIUM
    - The Dukes
    - Cozy Bear
    - CozyDuke
    - SolarStorm
    - Blue Kitsune
    - UNC3524
    - Midnight Blizzard
mitre-attack: https://attack.mitre.org/groups/G0016
---

## G0016

[APT29](https://attack.mitre.org/groups/G0016) is threat group that has been attributed to Russia's Foreign Intelligence Service (SVR).[^66] [^44]  They have operated since at least 2008, often targeting government networks in Europe and NATO member countries, research institutes, and think tanks. [APT29](https://attack.mitre.org/groups/G0016) reportedly compromised the Democratic National Committee starting in the summer of 2015.[^31] [^13] [^32] [^36] <br><br>In April 2021, the US and UK governments attributed the [SolarWinds Compromise](https://attack.mitre.org/campaigns/C0024) to the SVR; public statements included citations to [APT29](https://attack.mitre.org/groups/G0016), Cozy Bear, and The Dukes.[^64] [^58]  Industry reporting also referred to the actors involved in this campaign as UNC2452, NOBELIUM, StellarParticle, Dark Halo, and SolarStorm.[^9] [^40] [^30] [^28] [^20] [^54] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Multi-Factor Authentication Request Generation\|T1621]] | Multi-Factor Authentication Request Generation | [APT29](https://attack.mitre.org/groups/G0016) has used repeated MFA requests to gain access to victim accounts.[^12] [^55]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [APT29](https://attack.mitre.org/groups/G0016) has used the `reg save` command to save registry hives.[^53]  |
| [[Tool\|T1588.002]] | Tool | [APT29](https://attack.mitre.org/groups/G0016) has obtained and used a variety of tools including [Mimikatz](https://attack.mitre.org/software/S0002), [SDelete](https://attack.mitre.org/software/S0195), [Tor](https://attack.mitre.org/software/S0183), [meek](https://attack.mitre.org/software/S0175), and [Cobalt Strike](https://attack.mitre.org/software/S0154).[^46] [^31] [^53]  |
| [[Domain Fronting\|T1090.004]] | Domain Fronting | [APT29](https://attack.mitre.org/groups/G0016) has used the meek domain fronting plugin for [Tor](https://attack.mitre.org/software/S0183) to hide the destination of C2 traffic.[^46]  |
| [[Steal Application Access Token\|T1528]] | Steal Application Access Token | [APT29](https://attack.mitre.org/groups/G0016) uses stolen tokens to access victim accounts, without needing a password.[^55]  |
| [[Dynamic Resolution\|T1568]] | Dynamic Resolution | [APT29](https://attack.mitre.org/groups/G0016) has used Dynamic DNS providers for their malware C2 infrastructure.[^53]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [APT29](https://attack.mitre.org/groups/G0016) has exploited CVE-2021-36934 to escalate privileges on a compromised host.[^38]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [APT29](https://attack.mitre.org/groups/G0016) has used WMI event subscriptions for persistence.[^46]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [APT29](https://attack.mitre.org/groups/G0016) added Registry Run keys to establish persistence.[^46]  |
| [[Cloud Account\|T1136.003]] | Cloud Account | [APT29](https://attack.mitre.org/groups/G0016) can create new users through Azure AD.[^26]  |
| [[Device Registration\|T1098.005]] | Device Registration | [APT29](https://attack.mitre.org/groups/G0016) has enrolled their own devices into compromised cloud tenants, including enrolling a device in MFA to an Azure AD environment following a successful password guessing attack against a dormant account.[^52] [^55]  |
| [[Digital Certificates\|T1587.003]] | Digital Certificates | [APT29](https://attack.mitre.org/groups/G0016) has created self-signed digital certificates to enable mutual TLS authentication for malware.[^51] [^35]  |
| [[Data from Local System\|T1005]] | Data from Local System | [APT29](https://attack.mitre.org/groups/G0016) has stolen data from compromised hosts.[^53]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [APT29](https://attack.mitre.org/groups/G0016) has downloaded additional tools and malware onto compromised networks.[^46] [^51] [^31] [^53]  |
| [[Cloud Administration Command\|T1651]] | Cloud Administration Command | [APT29](https://attack.mitre.org/groups/G0016) has used Azure Run Command and Azure Admin-on-Behalf-of (AOBO) to execute code on virtual machines.[^26]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [APT29](https://attack.mitre.org/groups/G0016) has used spearphishing emails with an attachment to deliver files with exploits to initial victims.[^31] [^65] [^38] [^27]  |
| [[Cloud Accounts\|T1078.004]] | Cloud Accounts | [APT29](https://attack.mitre.org/groups/G0016) has gained access to a global administrator account in Azure AD and has used `Service Principal` credentials in Exchange.[^52] [^53]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [APT29](https://attack.mitre.org/groups/G0016) has used named and hijacked scheduled tasks to establish persistence.[^46]  |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [APT29](https://attack.mitre.org/groups/G0016) has ensured web servers in a victim environment are Internet accessible before copying tools or malware to it.[^53]  |
| [[Malware\|T1587.001]] | Malware | [APT29](https://attack.mitre.org/groups/G0016) has used unique malware in many of their operations.[^31] [^46] [^43] [^53]  |
| [[Web Services\|T1583.006]] | Web Services | [APT29](https://attack.mitre.org/groups/G0016) has registered algorithmically generated Twitter handles that are used for C2 by malware, such as [HAMMERTOSS](https://attack.mitre.org/software/S0037). [APT29](https://attack.mitre.org/groups/G0016) has also used legitimate web services such as Dropbox and Constant Contact in their operations.[^11] [^65]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | A backdoor used by [APT29](https://attack.mitre.org/groups/G0016) created a [Tor](https://attack.mitre.org/software/S0183) hidden service to forward traffic from the [Tor](https://attack.mitre.org/software/S0183) client to local ports 3389 (RDP), 139 (Netbios), and 445 (SMB) enabling full remote access from outside the network and has also used TOR.[^46] [^26]  |
| [[Boot or Logon Initialization Scripts\|T1037]] | Boot or Logon Initialization Scripts | [APT29](https://attack.mitre.org/groups/G0016) has hijacked legitimate application-specific startup scripts to enable malware to execute on system startup.[^53]  |
| [[HTML Smuggling\|T1027.006]] | HTML Smuggling | [APT29](https://attack.mitre.org/groups/G0016) has embedded an ISO file within an HTML attachment that contained JavaScript code to initiate malware execution.[^38]   |
| [[File Deletion\|T1070.004]] | File Deletion | [APT29](https://attack.mitre.org/groups/G0016) has used [SDelete](https://attack.mitre.org/software/S0195) to remove artifacts from victim networks.[^46]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [APT29](https://attack.mitre.org/groups/G0016) has used multiple software exploits for common client software, like Microsoft Word, Exchange, and Adobe Reader, to gain code execution.[^31] [^20] [^65]  |
| [[Pass the Ticket\|T1550.003]] | Pass the Ticket | [APT29](https://attack.mitre.org/groups/G0016) used Kerberos ticket attacks for lateral movement.[^46]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [APT29](https://attack.mitre.org/groups/G0016) has used various forms of spearphishing attempting to get a user to click on a malicious link.[^65] [^16]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [APT29](https://attack.mitre.org/groups/G0016) has renamed malicious DLLs with legitimate names to appear benign; they have also created an Azure AD certificate with a Common Name that matched the display name of the compromised service principal.[^18] [^52]  |
| [[Password Spraying\|T1110.003]] | Password Spraying | [APT29](https://attack.mitre.org/groups/G0016) has conducted brute force password spray attacks.[^5] [^26] [^55]  |
| [[Remote Email Collection\|T1114.002]] | Remote Email Collection | [APT29](https://attack.mitre.org/groups/G0016) has collected emails from targeted mailboxes within a compromised Azure AD tenant and compromised Exchange servers, including via Exchange Web Services (EWS) API requests.[^52] [^53]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [APT29](https://attack.mitre.org/groups/G0016) used large size files to avoid detection by security solutions with hardcoded size limits.[^18]  |
| [[Hybrid Identity\|T1556.007]] | Hybrid Identity | [APT29](https://attack.mitre.org/groups/G0016) has edited the `Microsoft.IdentityServer.Servicehost.exe.config` file to load a malicious DLL into the AD FS process, thereby enabling persistent access to any service federated with AD FS for a user with a specified User Principal Name.[^60]  |
| [[PowerShell\|T1059.001]] | PowerShell | [APT29](https://attack.mitre.org/groups/G0016) has used encoded PowerShell scripts uploaded to [CozyCar](https://attack.mitre.org/software/S0046) installations to download and install [SeaDuke](https://attack.mitre.org/software/S0053).[^29] [^46] [^38] [^27]  |
| [[External Remote Services\|T1133]] | External Remote Services | [APT29](https://attack.mitre.org/groups/G0016) has used compromised identities to access networks via VPNs and Citrix.[^57] [^52]  |
| [[RC Scripts\|T1037.004]] | RC Scripts | [APT29](https://attack.mitre.org/groups/G0016) has installed a run command on a compromised system to enable malware execution on system startup.[^53]  |
| [[Cloud Services\|T1021.007]] | Cloud Services | [APT29](https://attack.mitre.org/groups/G0016) has leveraged compromised high-privileged on-premises accounts synced to Office 365 to move laterally into a cloud environment, including through the use of Azure AD PowerShell.[^23]  |
| [[Vulnerability Scanning\|T1595.002]] | Vulnerability Scanning | [APT29](https://attack.mitre.org/groups/G0016) has conducted widespread scanning of target environments to identify vulnerabilities for exploit.[^20]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [APT29](https://attack.mitre.org/groups/G0016) has used spearphishing with a link to trick victims into clicking on a link to a zip file containing malicious files.[^46] [^65] [^16]  |
| [[Timestomp\|T1070.006]] | Timestomp | [APT29](https://attack.mitre.org/groups/G0016) has used timestomping to alter the Standard Information timestamps on their web shells to match other files in the same directory.[^53]  |
| [[Cloud Accounts\|T1586.003]] | Cloud Accounts | [APT29](https://attack.mitre.org/groups/G0016) has used residential proxies, including Azure Virtual Machines, to obfuscate their access to victim environments.[^52]  |
| [[External Proxy\|T1090.002]] | External Proxy | [APT29](https://attack.mitre.org/groups/G0016) uses compromised residential endpoints as proxies for defense evasion and network access.[^55]  |
| [[Encrypted Channel\|T1573]] | Encrypted Channel | [APT29](https://attack.mitre.org/groups/G0016) has used multiple layers of encryption within malware to protect C2 communication.[^27]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [APT29](https://attack.mitre.org/groups/G0016) used WMI to steal credentials and execute backdoors at a future time.[^46]  |
| [[Password Guessing\|T1110.001]] | Password Guessing | [APT29](https://attack.mitre.org/groups/G0016) has successfully conducted password guessing attacks against a list of mailboxes.[^52]  |
| [[Trusted Relationship\|T1199]] | Trusted Relationship | [APT29](https://attack.mitre.org/groups/G0016) has compromised IT, cloud services, and managed services providers to gain broad access to multiple customers for subsequent operations.[^26]  |
| [[Spearphishing via Service\|T1566.003]] | Spearphishing via Service | [APT29](https://attack.mitre.org/groups/G0016) has used the legitimate mailing service Constant Contact to send phishing e-mails.[^65]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [APT29](https://attack.mitre.org/groups/G0016) has used a compromised account to access an organization's VPN infrastructure.[^52]  |
| [[Web Shell\|T1505.003]] | Web Shell | [APT29](https://attack.mitre.org/groups/G0016) has installed web shells on exploited Microsoft Exchange servers.[^20] [^53]  |
| [[Python\|T1059.006]] | Python | [APT29](https://attack.mitre.org/groups/G0016) has developed malware variants written in Python.[^29]  |
| [[Hide Infrastructure\|T1665]] | Hide Infrastructure | [APT29](https://attack.mitre.org/groups/G0016) uses compromised residential endpoints, typically within the same ISP IP address range, as proxies to hide the true source of C2 traffic.[^55]  |
| [[Mshta\|T1218.005]] | Mshta | [APT29](https://attack.mitre.org/groups/G0016) has use `mshta` to execute malicious scripts on a compromised host.[^38]  |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | [APT29](https://attack.mitre.org/groups/G0016) has used the `reg save` command to extract LSA secrets offline.[^53]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [APT29](https://attack.mitre.org/groups/G0016) has exploited CVE-2019-19781 for Citrix, CVE-2019-11510 for Pulse Secure VPNs, CVE-2018-13379 for FortiGate VPNs, and CVE-2019-9670 in Zimbra software to gain access.[^20] [^57]  |
| [[Mark-of-the-Web Bypass\|T1553.005]] | Mark-of-the-Web Bypass | [APT29](https://attack.mitre.org/groups/G0016) has embedded ISO images and VHDX files in HTML to evade Mark-of-the-Web.[^38]  |
| [[Steal or Forge Authentication Certificates\|T1649]] | Steal or Forge Authentication Certificates | [APT29](https://attack.mitre.org/groups/G0016) has abused misconfigured AD CS certificate templates to impersonate admin users and create additional authentication certificates.[^63]  |
| [[Cloud Account\|T1087.004]] | Cloud Account | [APT29](https://attack.mitre.org/groups/G0016) has conducted enumeration of Azure AD accounts.[^26]  |
| [[Additional Email Delegate Permissions\|T1098.002]] | Additional Email Delegate Permissions | [APT29](https://attack.mitre.org/groups/G0016) has used a compromised global administrator account in Azure AD to backdoor a service principal with `ApplicationImpersonation` rights to start collecting emails from targeted mailboxes; [APT29](https://attack.mitre.org/groups/G0016) has also used compromised accounts holding `ApplicationImpersonation` rights in Exchange to collect emails.[^52] [^53]  |
| [[Local Accounts\|T1078.003]] | Local Accounts | [APT29](https://attack.mitre.org/groups/G0016) targets dormant or inactive user accounts, accounts belonging to individuals no longer at the organization but whose accounts remain on the system, for access and persistence.[^55]  |
| [[Accessibility Features\|T1546.008]] | Accessibility Features | [APT29](https://attack.mitre.org/groups/G0016) used sticky-keys to obtain unauthenticated, privileged console access.[^46] [^37]  |
| [[Cloud API\|T1059.009]] | Cloud API | [APT29](https://attack.mitre.org/groups/G0016) has leveraged the Microsoft Graph API to perform various actions across Azure and M365 environments. They have also utilized AADInternals PowerShell Modules to access the API [^43]  |
| [[Email Accounts\|T1586.002]] | Email Accounts | [APT29](https://attack.mitre.org/groups/G0016) has compromised email accounts to further enable phishing campaigns and taken control of dormant accounts.[^14] [^52]  |
| [[Malicious File\|T1204.002]] | Malicious File | [APT29](https://attack.mitre.org/groups/G0016) has used various forms of spearphishing attempting to get a user to open attachments, including, but not limited to, malicious Microsoft Word documents, .pdf, and .lnk files. [^31] [^38] [^27]  |
| [[Disable or Modify Cloud Log\|T1685.002]] | Disable or Modify Cloud Log | [APT29](https://attack.mitre.org/groups/G0016) has disabled Purview Audit on targeted accounts prior to stealing emails from  Microsoft 365 tenants.[^52]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [APT29](https://attack.mitre.org/groups/G0016) has bypassed UAC.[^46]  |
| [[Software Packing\|T1027.002]] | Software Packing | [APT29](https://attack.mitre.org/groups/G0016) used UPX to pack files.[^46]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^49]  |
| [[BloodHound\|S0521]] | BloodHound | [^38]  |
| [[Sliver\|S0633]] | Sliver | [^20] [^27]  |
| [[Impacket\|S0357]] | Impacket | [^53]  |
| [[ipconfig\|S0100]] | ipconfig | [^49]  |
| [[AADInternals\|S0677]] | AADInternals | [^26]  |
| [[Tasklist\|S0057]] | Tasklist | [^49]  |
| [[meek\|S0175]] | meek | [^46]  |
| [[ROADTools\|S0684]] | ROADTools | [^26]  |
| [[Systeminfo\|S0096]] | Systeminfo | [^49]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^31] [^3] [^48]  |
| [[SDelete\|S0195]] | SDelete | [^46]  |
| [[Tor\|S0183]] | Tor | [^46]  |
| [[AdFind\|S0552]] | AdFind | [^42] [^48] [^38]  |
| [[PsExec\|S0029]] | PsExec | [^31] [^21]  |
| [[PowerDuke\|S0139]] | PowerDuke | [^7]  |
| [[reGeorg\|S1187]] | reGeorg | [^53]  |
| [[GeminiDuke\|S0049]] | GeminiDuke | [^31]  |
| [[HAMMERTOSS\|S0037]] | HAMMERTOSS | [^31] [^27]  |
| [[CosmicDuke\|S0050]] | CosmicDuke | [^31] [^27]  |
| [[EnvyScout\|S0634]] | EnvyScout | [^43]  |
| [[TEARDROP\|S0560]] | TEARDROP | [^9] [^65] [^43] [^6]  |
| [[WellMess\|S0514]] | WellMess | [^51] [^35] [^41] [^57] [^20]  |
| [[PolyglotDuke\|S0518]] | PolyglotDuke | [^21] [^27]  |
| [[RegDuke\|S0511]] | RegDuke | [^21] [^27]  |
| [[QUIETEXIT\|S1084]] | QUIETEXIT | [^53]  |
| [[Raindrop\|S0565]] | Raindrop | [^59] [^43] [^6]  |
| [[FatDuke\|S0512]] | FatDuke | [^21] [^27]  |
| [[GoldMax\|S0588]] | GoldMax | [^40] [^20] [^65] [^43] [^6]  |
| [[POSHSPY\|S0150]] | POSHSPY | [^10]  |
| [[MiniDuke\|S0051]] | MiniDuke | [^31] [^21] [^27]  |
| [[SeaDuke\|S0053]] | SeaDuke | [^31] [^27] [^29]  |
| [[FoggyWeb\|S0661]] | FoggyWeb | [^39]  |
| [[WellMail\|S0515]] | WellMail | [^24] [^57] [^20]  |
| [[LiteDuke\|S0513]] | LiteDuke | [^21] [^27]  |
| [[VaporRage\|S0636]] | VaporRage | [^43]  |
| [[Sibot\|S0589]] | Sibot | [^40] [^20] [^43] [^6]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^9] [^20] [^65] [^43] [^18] [^38] [^6] [^16]  |
| [[SUNBURST\|S0559]] | SUNBURST | [^9] [^65] [^6]  |
| [[PinchDuke\|S0048]] | PinchDuke | [^31]  |
| [[OnionDuke\|S0052]] | OnionDuke | [^31] [^21] [^27]  |
| [[NativeZone\|S0637]] | NativeZone | [^18]  |
| [[GoldFinder\|S0597]] | GoldFinder | [^40] [^20] [^43] [^6]  |
| [[TrailBlazer\|S0682]] | TrailBlazer | [^48]  |
| [[SUNSPOT\|S0562]] | SUNSPOT | [^30] [^43]  |
| [[BoomBox\|S0635]] | BoomBox | [^43]  |
| [[CloudDuke\|S0054]] | CloudDuke | [^31]  |
| [[SoreFang\|S0516]] | SoreFang | [^57] [^49]  |
| [[CozyCar\|S0046]] | CozyCar | [^31] [^27]  |



## References

[^1]: IRON HEMLOCK


[^2]: The Dukes


[^3]: [Microsoft 365 Defender Solorigate](https://www.microsoft.com/security/blog/2020/12/28/using-microsoft-365-defender-to-coordinate-protection-against-solorigate/)


[^4]: Blue Kitsune


[^5]: [MSRC Nobelium June 2021](https://msrc-blog.microsoft.com/2021/06/25/new-nobelium-activity/)


[^6]: [Secureworks IRON RITUAL Profile](https://www.sophos.com/en-us/threat-profiles/iron-ritual)


[^7]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)


[^8]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^9]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)


[^10]: [FireEye POSHSPY April 2017](https://www.fireeye.com/blog/threat-research/2017/03/dissecting_one_ofap.html)


[^11]: [FireEye APT29](https://services.google.com/fh/files/misc/rpt-apt29-hammertoss-stealthy-tactics-define-en.pdf)


[^12]: [Suspected Russian Activity Targeting Government and Business Entities Around the Globe](https://www.mandiant.com/resources/russian-targeting-gov-business)


[^13]: [GRIZZLY STEPPE JAR](https://www.us-cert.gov/sites/default/files/publications/JAR_16-20296A_GRIZZLY%20STEPPE-2016-1229.pdf)


[^14]: [ANSSI Nobelium Phishing December 2021](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-011.pdf)


[^15]: APT29


[^16]: [Secureworks IRON RITUAL USAID Phish May 2021](https://www.secureworks.com/blog/usaid-themed-phishing-campaign-leverages-us-elections-lure)


[^17]: UNC2452


[^18]: [SentinelOne NobleBaron June 2021](https://labs.sentinelone.com/noblebaron-new-poisoned-installers-could-be-used-in-supply-chain-attacks/)


[^19]: Cozy Bear


[^20]: [Cybersecurity Advisory SVR TTP May 2021](https://www.ncsc.gov.uk/files/Advisory-further-TTPs-associated-with-SVR-cyber-actors.pdf)


[^21]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)


[^22]: Dark Halo


[^23]: [Mandiant Remediation and Hardening Strategies for Microsoft 365](https://www.mandiant.com/sites/default/files/2022-08/remediation-hardening-strategies-for-m365-defend-against-apt29-white-paper.pdf)


[^24]: [CISA WellMail July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)


[^25]: SolarStorm


[^26]: [MSTIC Nobelium Oct 2021](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks/)


[^27]: [Secureworks IRON HEMLOCK Profile](http://www.secureworks.com/research/threat-profiles/iron-hemlock)


[^28]: [Volexity SolarWinds](https://www.volexity.com/blog/2020/12/14/dark-halo-leverages-solarwinds-compromise-to-breach-organizations/)


[^29]: [Symantec Seaduke 2015](http://www.symantec.com/connect/blogs/forkmeiamfamous-seaduke-latest-weapon-duke-armory)


[^30]: [CrowdStrike SUNSPOT Implant January 2021](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)


[^31]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)


[^32]: [Crowdstrike DNC June 2016](https://www.crowdstrike.com/blog/bears-midst-intrusion-democratic-national-committee/)


[^33]: YTTRIUM


[^34]: NOBELIUM


[^35]: [PWC WellMess C2 August 2020](https://www.pwc.co.uk/issues/cyber-security-services/insights/wellmess-analysis-command-control.html)


[^36]: [UK Gov UK Exposes Russia SolarWinds April 2021](https://www.gov.uk/government/news/russia-uk-exposes-russian-involvement-in-solarwinds-cyber-compromise)


[^37]: [FireEye APT29 Domain Fronting](https://www.fireeye.com/blog/threat-research/2017/03/apt29_domain_frontin.html)


[^38]: [ESET T3 Threat Report 2021](https://www.welivesecurity.com/wp-content/uploads/2022/02/eset_threat_report_t32021.pdf)


[^39]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)


[^40]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)


[^41]: [CISA WellMess July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198b)


[^42]: [Microsoft Analyzing Solorigate Dec 2020](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)


[^43]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)


[^44]: [UK Gov Malign RIS Activity April 2021](https://www.gov.uk/government/news/russia-uk-and-us-expose-global-campaigns-of-malign-activity-by-russian-intelligence-services)


[^45]: Midnight Blizzard


[^46]: [Mandiant No Easy Breach](https://www.slideshare.net/slideshow/no-easy-breach-derby-con-2016/66447908)


[^47]: IRON RITUAL


[^48]: [CrowdStrike StellarParticle January 2022](https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/)


[^49]: [CISA SoreFang July 2016](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)


[^50]: [Microsoft Unidentified Dec 2018](https://www.microsoft.com/security/blog/2018/12/03/analysis-of-cyberattack-on-u-s-think-tanks-non-profits-public-sector-by-unidentified-attackers/)


[^51]: [PWC WellMess July 2020](https://www.pwc.co.uk/issues/cyber-security-services/insights/cleaning-up-after-wellmess.html)


[^52]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^53]: [Mandiant APT29 Eye Spy Email Nov 22](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)


[^54]: [Unit 42 SolarStorm December 2020](https://unit42.paloaltonetworks.com/solarstorm-supply-chain-attack-timeline/)


[^55]: [NCSC et al APT29 2024](https://www.ic3.gov/Media/News/2024/240226.pdf)


[^56]: UNC3524


[^57]: [NCSC APT29 July 2020](https://www.ncsc.gov.uk/files/Advisory-APT29-targets-COVID-19-vaccine-development-V1-1.pdf)


[^58]: [UK NSCS Russia SolarWinds April 2021](https://www.ncsc.gov.uk/news/uk-and-us-call-out-russia-for-solarwinds-compromise)


[^59]: [Symantec RAINDROP January 2021](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/solarwinds-raindrop-malware)


[^60]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^61]: [FireEye APT29 Nov 2018](https://www.fireeye.com/blog/threat-research/2018/11/not-so-cozy-an-uncomfortable-examination-of-a-suspected-apt29-phishing-campaign.html)


[^62]: NobleBaron


[^63]: [Mandiant APT29 Trello](https://www.mandiant.com/resources/tracking-apt29-phishing-campaigns)


[^64]: [NSA Joint Advisory SVR SolarWinds April 2021](https://media.defense.gov/2021/Apr/15/2002621240/-1/-1/0/CSA_SVR_TARGETS_US_ALLIES_UOO13234021.PDF/CSA_SVR_TARGETS_US_ALLIES_UOO13234021.PDF)


[^65]: [MSTIC NOBELIUM May 2021](https://www.microsoft.com/security/blog/2021/05/27/new-sophisticated-email-based-attack-from-nobelium/)


[^66]: [White House Imposing Costs RU Gov April 2021](https://www.whitehouse.gov/briefing-room/statements-releases/2021/04/15/fact-sheet-imposing-costs-for-harmful-foreign-activities-by-the-russian-government/)


[^67]: CozyDuke


