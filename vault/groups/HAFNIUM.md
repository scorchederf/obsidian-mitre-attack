---
aliases: 
    - HAFNIUM
    - Operation Exchange Marauder
    - Silk Typhoon
mitre-attack: https://attack.mitre.org/groups/G0125
---

## G0125

[HAFNIUM](https://attack.mitre.org/groups/G0125) is a likely state-sponsored cyber espionage group operating out of China that has been active since at least January 2021. [HAFNIUM](https://attack.mitre.org/groups/G0125) primarily targets entities in the US across a number of industry sectors, including infectious disease researchers, law firms, higher education institutions, defense contractors, policy think tanks, and NGOs. [HAFNIUM](https://attack.mitre.org/groups/G0125) has targeted remote management tools and cloud software for intial access and has demonstrated an ability to quickly operationalize exploits for identified vulnerabilities in edge devices.[^6] [^4] [^5] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Client Configurations\|T1592.004]] | Client Configurations | [HAFNIUM](https://attack.mitre.org/groups/G0125) has interacted with Office 365 tenants to gather details regarding target's environments.[^6]  |
| [[Password Spraying\|T1110.003]] | Password Spraying | [HAFNIUM](https://attack.mitre.org/groups/G0125) has gained initial access through password spray attacks.[^5]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [HAFNIUM](https://attack.mitre.org/groups/G0125) has downloaded malware and tools--including Nishang and PowerCat--onto a compromised host.[^6] [^1]   |
| [[Web Services\|T1583.006]] | Web Services | [HAFNIUM](https://attack.mitre.org/groups/G0125) has acquired web services for use in C2 and exfiltration.[^6]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used 7-Zip and WinRAR to compress stolen files for exfiltration.[^6] [^4]  |
| [[Data from Local System\|T1005]] | Data from Local System | [HAFNIUM](https://attack.mitre.org/groups/G0125) has collected data and files from a compromised machine.[^1] [^5]  |
| [[Botnet\|T1583.005]] | Botnet | [HAFNIUM](https://attack.mitre.org/groups/G0125) has incorporated leased devices into covert networks to obfuscate communications.[^5]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used `whoami` to gather user information.[^1]  |
| [[Sharepoint\|T1213.002]] | Sharepoint | [HAFNIUM](https://attack.mitre.org/groups/G0125) has abused compromised credentials to exfiltrate data from SharePoint.[^5]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [HAFNIUM](https://attack.mitre.org/groups/G0125) has targeted unpatched applications to elevate access in targeted organizations.[^5]  |
| [[Botnet\|T1584.005]] | Botnet | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used compromised devices in covert networks to obfuscate communications.[^5]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used `cmd.exe` to execute commands on the victim's machine.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used `tasklist` to enumerate processes.[^1]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used `procdump` to dump the LSASS process memory.[^6] [^4] [^1]  |
| [[Data from Cloud Storage\|T1530]] | Data from Cloud Storage | [HAFNIUM](https://attack.mitre.org/groups/G0125) has exfitrated data from OneDrive.[^5]  |
| [[Automated Collection\|T1119]] | Automated Collection | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used MSGraph to exfiltrate data from email, OneDrive, and SharePoint.[^5]  |
| [[Gather Victim Network Information\|T1590]] | Gather Victim Network Information | [HAFNIUM](https://attack.mitre.org/groups/G0125) gathered the fully qualified domain names (FQDNs) for targeted Exchange servers in the victim's environment.[^4]  |
| [[Web Shell\|T1505.003]] | Web Shell | [HAFNIUM](https://attack.mitre.org/groups/G0125) has deployed multiple web shells on compromised servers including SIMPLESEESHARP, SPORTSBALL, [China Chopper](https://attack.mitre.org/software/S0020), and [ASPXSpy](https://attack.mitre.org/software/S0073).[^6] [^4] [^8] [^2] [^1] [^5]  |
| [[Email Addresses\|T1589.002]] | Email Addresses | [HAFNIUM](https://attack.mitre.org/groups/G0125) has collected e-mail addresses for users they intended to target.[^4]  |
| [[Cloud Secrets Management Stores\|T1555.006]] | Cloud Secrets Management Stores | [HAFNIUM](https://attack.mitre.org/groups/G0125) has moved laterally from on-premises environments to steal passwords from Azure key vaults.[^5]  |
| [[Code Repositories\|T1593.003]] | Code Repositories | [HAFNIUM](https://attack.mitre.org/groups/G0125) has discovered leaked corporate credentials on public repositories including GitHub.[^5]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [HAFNIUM](https://attack.mitre.org/groups/G0125) has exfiltrated data to file sharing sites, including MEGA.[^6]  |
| [[Remote Email Collection\|T1114.002]] | Remote Email Collection | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used web shells and MSGraph to export mailbox data.[^6] [^4] [^5] <br> |
| [[Rundll32\|T1218.011]] | Rundll32 | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used `rundll32` to load malicious DLLs.[^4]  |
| [[Local Accounts\|T1078.003]] | Local Accounts | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used the NT AUTHORITY\SYSTEM account to create files on Exchange servers.[^8]  |
| [[PowerShell\|T1059.001]] | PowerShell | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used the Exchange Power Shell module `Set-OabVirtualDirectoryPowerShell` to export mailbox data.[^6] [^4]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [HAFNIUM](https://attack.mitre.org/groups/G0125) has hidden files on a compromised host.[^1]  |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [HAFNIUM](https://attack.mitre.org/groups/G0125) has checked for network connectivity from a compromised host using `ping`, including attempts to contact `google[.]com`.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [HAFNIUM](https://attack.mitre.org/groups/G0125) has collected IP information via IPInfo.[^1]  |
| [[IP Addresses\|T1590.005]] | IP Addresses | [HAFNIUM](https://attack.mitre.org/groups/G0125) has obtained IP addresses for publicly-accessible Exchange servers.[^4]  |
| [[Trusted Relationship\|T1199]] | Trusted Relationship | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used stolen API keys and credentials associated with privilege access management (PAM), cloud app providers, and cloud data management companies to access downstream customer environments.[^5]  |
| [[Cloud Accounts\|T1078.004]] | Cloud Accounts | [HAFNIUM](https://attack.mitre.org/groups/G0125) has abused service principals in compromised environments to enable data exfiltration.[^5]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [HAFNIUM](https://attack.mitre.org/groups/G0125) has searched file contents on a compromised host.[^1]  |
| [[NTDS\|T1003.003]] | NTDS | [HAFNIUM](https://attack.mitre.org/groups/G0125) has stolen copies of the Active Directory database (NTDS.DIT).[^4] [^5]  |
| [[Account Manipulation\|T1098]] | Account Manipulation | [HAFNIUM](https://attack.mitre.org/groups/G0125) has granted privileges to domain accounts and reset the password for default admin accounts.[^4] [^5]  |
| [[Domain Account\|T1136.002]] | Domain Account | [HAFNIUM](https://attack.mitre.org/groups/G0125) has created domain accounts.[^4] [^5]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used open-source C2 frameworks, including [Covenant](https://attack.mitre.org/software/S1155).[^6]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [HAFNIUM](https://attack.mitre.org/groups/G0125) has enumerated domain controllers using `net group "Domain computers"` and `nltest /dclist`.[^1]  |
| [[Application Access Token\|T1550.001]] | Application Access Token | [HAFNIUM](https://attack.mitre.org/groups/G0125) has abused service principals with administrative permissions for data exfiltration.[^5]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [HAFNIUM](https://attack.mitre.org/groups/G0125) has cleared actor-performed actions from logs.[^5]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [HAFNIUM](https://attack.mitre.org/groups/G0125) has exploited multiple vulnerabilities to compromise edge devices and on-premises versions of Microsoft Exchange Server.[^6] [^4] [^8] [^2] [^3] [^5]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used TCP for C2.[^6]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used ASCII encoding for C2 traffic.[^6]  |
| [[Virtual Private Server\|T1583.003]] | Virtual Private Server | [HAFNIUM](https://attack.mitre.org/groups/G0125) has operated from leased virtual private servers (VPS) in the United States.[^6]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Covenant\|S1155]] | Covenant | [HAFNIUM](https://attack.mitre.org/groups/G0125) used [Covenant](https://attack.mitre.org/software/S1155) for command and control following compromise of internet-facing servers.[^6] [^5]  |
| [[Impacket\|S0357]] | Impacket | [^2]  |
| [[PsExec\|S0029]] | PsExec | [^4]  |
| [[ASPXSpy\|S0073]] | ASPXSpy | [^4]  |
| [[China Chopper\|S0020]] | China Chopper | [^4] [^8] [^1]  |
| [[Tarrask\|S1011]] | Tarrask | [^2]   |



## References

[^1]: [Rapid7 HAFNIUM Mar 2021](https://www.rapid7.com/blog/post/2021/03/23/defending-against-the-zero-day-analyzing-attacker-behavior-post-exploitation-of-microsoft-exchange/)


[^2]: [Tarrask scheduled task](https://www.microsoft.com/security/blog/2022/04/12/tarrask-malware-uses-scheduled-tasks-for-defense-evasion/)


[^3]: [Microsoft Log4j Vulnerability Exploitation December 2021](https://www.microsoft.com/en-us/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/)


[^4]: [Volexity Exchange Marauder March 2021](https://www.volexity.com/blog/2021/03/02/active-exploitation-of-microsoft-exchange-zero-day-vulnerabilities/)


[^5]: [Microsoft Silk Typhoon MAR 2025](https://www.microsoft.com/en-us/security/blog/2025/03/05/silk-typhoon-targeting-it-supply-chain/)


[^6]: [Microsoft HAFNIUM March 2020](https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/)


[^7]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^8]: [FireEye Exchange Zero Days March 2021](https://www.fireeye.com/blog/threat-research/2021/03/detection-response-to-exploitation-of-microsoft-exchange-zero-day-vulnerabilities.html)


[^9]: Operation Exchange Marauder


[^10]: Silk Typhoon


