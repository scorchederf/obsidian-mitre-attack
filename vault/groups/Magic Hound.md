---
aliases: 
    - Magic Hound
    - TA453
    - COBALT ILLUSION
    - Charming Kitten
    - ITG18
    - Phosphorus
    - Newscaster
    - APT35
    - Mint Sandstorm
mitre-attack: https://attack.mitre.org/groups/G0059
---

## G0059

[Magic Hound](https://attack.mitre.org/groups/G0059) is an Iranian-sponsored threat group that conducts long term, resource-intensive cyber espionage operations, likely on behalf of the Islamic Revolutionary Guard Corps. They have targeted European, U.S., and Middle Eastern government and military personnel, academics, journalists, and organizations such as the World Health Organization (WHO), via complex social engineering campaigns since at least 2014.[^34] [^6] [^9] [^20] [^25] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Keylogging\|T1056.001]] | Keylogging | [Magic Hound](https://attack.mitre.org/groups/G0059) malware is capable of keylogging.[^28]  |
| [[Exfiltration Over Web Service\|T1567]] | Exfiltration Over Web Service | [Magic Hound](https://attack.mitre.org/groups/G0059) has used the Telegram API `sendMessage` to relay data on compromised devices.[^16]  |
| [[Credentials\|T1589.001]] | Credentials | [Magic Hound](https://attack.mitre.org/groups/G0059) gathered credentials from two victims that they then attempted to validate across 75 different websites. [Magic Hound](https://attack.mitre.org/groups/G0059) has also collected credentials from over 900 Fortinet VPN servers in the US, Europe, and Israel.[^10] [^33]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Magic Hound](https://attack.mitre.org/groups/G0059) malware has used Registry Run keys to establish persistence.[^28] [^2] [^33]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Magic Hound](https://attack.mitre.org/groups/G0059) has used PowerShell for execution and privilege escalation.[^28] [^34] [^21] [^2] [^33]  |
| [[Wi-Fi Discovery\|T1016.002]] | Wi-Fi Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) has collected names and passwords of all Wi-Fi networks to which a device has previously connected.[^31]  |
| [[Tool\|T1588.002]] | Tool | [Magic Hound](https://attack.mitre.org/groups/G0059) has obtained and used tools like [Havij](https://attack.mitre.org/software/S0224), [sqlmap](https://attack.mitre.org/software/S0225), Metasploit, [Mimikatz](https://attack.mitre.org/software/S0002), and Plink.[^7] [^34] [^31] [^2] [^33]  |
| [[Domains\|T1584.001]] | Domains | [Magic Hound](https://attack.mitre.org/groups/G0059) has used compromised domains to host links targeted to specific phishing victims.[^6] [^25] [^9] [^16]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Magic Hound](https://attack.mitre.org/groups/G0059) has used the command-line interface for code execution.[^28] [^21] [^2]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Magic Hound](https://attack.mitre.org/groups/G0059) has used Plink to tunnel RDP over SSH.[^2]  |
| [[Email Accounts\|T1585.002]] | Email Accounts | [Magic Hound](https://attack.mitre.org/groups/G0059) has established email accounts using fake personas for spearphishing operations.[^10] [^11]  |
| [[Determine Physical Locations\|T1591.001]] | Determine Physical Locations | [Magic Hound](https://attack.mitre.org/groups/G0059) has collected location information from visitors to their phishing sites.[^16]  |
| [[Application Layer Protocol\|T1071]] | Application Layer Protocol | [Magic Hound](https://attack.mitre.org/groups/G0059) malware has used IRC for C2.[^28] [^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Magic Hound](https://attack.mitre.org/groups/G0059) has used HTTP for C2.[^28] [^21] [^2]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Magic Hound](https://attack.mitre.org/groups/G0059) has used BitLocker and DiskCryptor to encrypt targeted workstations. [^2] [^33]  |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) has conducted a network call out to a specific website as part of their initial discovery activity.[^2]   |
| [[Email Accounts\|T1586.002]] | Email Accounts | [Magic Hound](https://attack.mitre.org/groups/G0059) has compromised personal email accounts through the use of legitimate credentials and gathered additional victim information.[^10]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Magic Hound](https://attack.mitre.org/groups/G0059) has used scheduled tasks to establish persistence and execution.[^21] [^2]  |
| [[Software\|T1592.002]] | Software | [Magic Hound](https://attack.mitre.org/groups/G0059) has captured the user-agent strings from visitors to their phishing sites.[^16]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Magic Hound](https://attack.mitre.org/groups/G0059) has used Remote Desktop Services to copy tools on targeted systems.[^21] [^2]  |
| [[Email Account\|T1087.003]] | Email Account | [Magic Hound](https://attack.mitre.org/groups/G0059) has used Powershell to discover email accounts.[^21]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Magic Hound](https://attack.mitre.org/groups/G0059) has downloaded additional code and files from servers onto victims.[^28] [^21] [^2] [^33]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Magic Hound](https://attack.mitre.org/groups/G0059) has exploited the Log4j utility (CVE-2021-44228), on-premises MS Exchange servers via "ProxyShell" (CVE-2021-34473, CVE-2021-34523, CVE-2021-31207), and Fortios SSL VPNs (CVE-2018-13379).[^31] [^21] [^4] [^2] [^33] [^13]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Magic Hound](https://attack.mitre.org/groups/G0059) has attempted to lure victims into opening malicious email attachments.[^6]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Magic Hound](https://attack.mitre.org/groups/G0059) has used rundll32.exe to execute MiniDump from comsvcs.dll when dumping LSASS memory.[^21]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Magic Hound](https://attack.mitre.org/groups/G0059) has used base64-encoded commands.[^28] [^33]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) has used KPortScan 3.0 to perform SMB, RDP, and LDAP scanning.[^2]  |
| [[IP Addresses\|T1590.005]] | IP Addresses | [Magic Hound](https://attack.mitre.org/groups/G0059) has captured the IP addresses of visitors to their phishing sites.[^16]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Magic Hound](https://attack.mitre.org/groups/G0059) malware can take a screenshot and upload the file to its C2 server.[^28]  |
| [[Encrypted Channel\|T1573]] | Encrypted Channel | [Magic Hound](https://attack.mitre.org/groups/G0059) has used an encrypted http proxy in C2 communications.[^2]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Magic Hound](https://attack.mitre.org/groups/G0059) malware has used VBS scripts for execution.[^28]  |
| [[Disable or Modify Windows Event Log\|T1685.001]] | Disable or Modify Windows Event Log | [Magic Hound](https://attack.mitre.org/groups/G0059) has executed scripts to disable the event log service.[^2]  |
| [[Vulnerability Scanning\|T1595.002]] | Vulnerability Scanning | [Magic Hound](https://attack.mitre.org/groups/G0059) has conducted widespread scanning to identify public-facing systems vulnerable to CVE-2021-44228 in Log4j and ProxyShell vulnerabilities; CVE-2021-26855, CVE-2021-26857, CVE-2021-26858, and CVE-2021-27065 in on-premises MS Exchange Servers; and CVE-2018-13379 in Fortinet FortiOS SSL VPNs.[^31] [^33]  |
| [[Masquerade Account Name\|T1036.010]] | Masquerade Account Name | [Magic Hound](https://attack.mitre.org/groups/G0059) has created local accounts named `help` and `DefaultAccount` on compromised machines.[^21] [^33]  |
| [[Email Addresses\|T1589.002]] | Email Addresses | [Magic Hound](https://attack.mitre.org/groups/G0059) has identified high-value email accounts in academia, journalism, NGO's, foreign policy, and national security for targeting.[^25] [^16]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Magic Hound](https://attack.mitre.org/groups/G0059) has attempted to lure victims into opening malicious links embedded in emails.[^6] [^9]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [Magic Hound](https://attack.mitre.org/groups/G0059) malware can use a SOAP Web service to communicate with its C2 server.[^28]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) malware has obtained the victim username and sent it to the C2 server.[^28] [^21] [^2]  |
| [[Additional Email Delegate Permissions\|T1098.002]] | Additional Email Delegate Permissions | [Magic Hound](https://attack.mitre.org/groups/G0059) granted compromised email accounts read access to the email boxes of additional targeted accounts. The group then was able to authenticate to the intended victim's OWA (Outlook Web Access) portal and read hundreds of email communications for information on Middle East organizations.[^34]   |
| [[File Deletion\|T1070.004]] | File Deletion | [Magic Hound](https://attack.mitre.org/groups/G0059) has deleted and overwrote files to cover tracks.[^28] [^34] [^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Magic Hound](https://attack.mitre.org/groups/G0059) malware has used base64-encoded files and has also encrypted embedded strings with AES.[^28] [^33]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Magic Hound](https://attack.mitre.org/groups/G0059) has sent malicious URL links through email to victims. In some cases the URLs were shortened or linked to Word documents with malicious macros that executed PowerShells scripts to download [Pupy](https://attack.mitre.org/software/S0192).[^18] [^6] [^9] [^33]  |
| [[Default Accounts\|T1078.001]] | Default Accounts | [Magic Hound](https://attack.mitre.org/groups/G0059) enabled and used the default system managed account, DefaultAccount, via `"powershell.exe" /c net user DefaultAccount /active:yes` to connect to a targeted Exchange server over RDP.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) malware can list a victim's logical drives and the type, as well the total/free space of the fixed devices. Other malware can list a directory's contents.[^28]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) malware gathers the victim's local IP address, MAC address, and external IP address.[^28] [^21] [^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Magic Hound](https://attack.mitre.org/groups/G0059) has used `dllhost.exe` to mask Fast Reverse Proxy (FRP) and `MicrosoftOutLookUpdater.exe` for Plink.[^21] [^2] [^33]  |
| [[Additional Local or Domain Groups\|T1098.007]] | Additional Local or Domain Groups | [Magic Hound](https://attack.mitre.org/groups/G0059) has added a user named DefaultAccount to the Administrators and Remote Desktop Users groups.[^21]  |
| [[Spearphishing Link\|T1598.003]] | Spearphishing Link | [Magic Hound](https://attack.mitre.org/groups/G0059) has used SMS and email messages with links designed to steal credentials or track victims.[^9] [^6] [^11] [^25] [^16] [^33]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) has used quser.exe to identify existing RDP connections.[^21]  |
| [[Email Collection\|T1114]] | Email Collection | [Magic Hound](https://attack.mitre.org/groups/G0059) has compromised email credentials in order to steal sensitive data.[^9]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Magic Hound](https://attack.mitre.org/groups/G0059) has stolen domain credentials by dumping LSASS process memory using Task Manager, comsvcs.dll, and from a Microsoft Active Directory Domain Controller using [Mimikatz](https://attack.mitre.org/software/S0002).[^34] [^21] [^2] [^33]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Magic Hound](https://attack.mitre.org/groups/G0059) has copied tools within a compromised network using RDP.[^2]  |
| [[Local Account\|T1136.001]] | Local Account | [Magic Hound](https://attack.mitre.org/groups/G0059) has created local accounts named `help` and `DefaultAccount` on compromised machines.[^21] [^33]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) malware can list running processes.[^28]  |
| [[Remote Email Collection\|T1114.002]] | Remote Email Collection | [Magic Hound](https://attack.mitre.org/groups/G0059) has exported emails from compromised Exchange servers including through use of the cmdlet `New-MailboxExportRequest.`[^21] [^2]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [Magic Hound](https://attack.mitre.org/groups/G0059) malware has communicated with its C2 server over TCP ports 4443 and 10151 using HTTP.[^28] [^2]  |
| [[Windows Host Firewall\|T1686.003]] | Windows Host Firewall | [Magic Hound](https://attack.mitre.org/groups/G0059) has added the following rule to a victim's Windows firewall to allow RDP traffic - `"netsh" advfirewall firewall add rule name="Terminal Server" dir=in action=allow protocol=TCP localport=3389`.[^21] [^2]  |
| [[Clear Command History\|T1070.003]] | Clear Command History | [Magic Hound](https://attack.mitre.org/groups/G0059) has removed mailbox export requests from compromised Exchange servers.[^21]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) malware has used a PowerShell command to check the victim system architecture to determine if it is an x64 machine. Other malware has obtained the OS version, UUID, and computer/host name to send to the C2 server.[^28] [^21] [^2]  |
| [[Local Email Collection\|T1114.001]] | Local Email Collection | [Magic Hound](https://attack.mitre.org/groups/G0059) has collected .PST archives.[^34]  |
| [[Web Shell\|T1505.003]] | Web Shell | [Magic Hound](https://attack.mitre.org/groups/G0059) has used multiple web shells to gain execution.[^21] [^2]  |
| [[Proxy\|T1090]] | Proxy | [Magic Hound](https://attack.mitre.org/groups/G0059) has used Fast Reverse Proxy (FRP) for RDP traffic.[^2]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Magic Hound](https://attack.mitre.org/groups/G0059) has named a malicious script CacheTask.bat to mimic a legitimate task.[^2]  |
| [[Domains\|T1583.001]] | Domains | [Magic Hound](https://attack.mitre.org/groups/G0059) has registered fraudulent domains such as "mail-newyorker.com" and "news12.com.recover-session-service.site" to target specific victims with phishing attacks.[^9]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) has used [Ping](https://attack.mitre.org/software/S0097) for discovery on targeted networks.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Magic Hound](https://attack.mitre.org/groups/G0059) has modified Registry settings for security tools.[^21]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) has used a web shell to execute `nltest /trusted_domains` to identify trust relationships.[^2]  |
| [[Gather Victim Identity Information\|T1589]] | Gather Victim Identity Information | [Magic Hound](https://attack.mitre.org/groups/G0059) has acquired mobile phone numbers of potential targets, possibly for mobile malware or additional phishing operations.[^25]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [Magic Hound](https://attack.mitre.org/groups/G0059) has used domain administrator accounts after dumping LSASS process memory.[^2]  |
| [[Spearphishing via Service\|T1566.003]] | Spearphishing via Service | [Magic Hound](https://attack.mitre.org/groups/G0059) used various social media channels (such as LinkedIn) as well as messaging services (such as WhatsApp) to spearphish victims.[^32] [^27] [^6]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Magic Hound](https://attack.mitre.org/groups/G0059) has used gzip to archive dumped LSASS process memory and RAR to stage and compress local folders.[^34] [^21] [^2]  |
| [[Social Media Accounts\|T1585.001]] | Social Media Accounts | [Magic Hound](https://attack.mitre.org/groups/G0059) has created fake LinkedIn and other social media accounts to contact targets and convince them--through messages and voice communications--to open malicious links.[^6]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [Magic Hound](https://attack.mitre.org/groups/G0059) malware has a function to determine whether the C2 server wishes to execute the newly dropped file in a hidden window.[^28]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Magic Hound](https://attack.mitre.org/groups/G0059) has used a web shell to exfiltrate a ZIP file containing a dump of LSASS memory on a compromised machine.[^21] [^2]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Magic Hound](https://attack.mitre.org/groups/G0059) has used a tool to run `cmd /c wmic computersystem get domain` for discovery.[^21]  |
| [[Web Services\|T1583.006]] | Web Services | [Magic Hound](https://attack.mitre.org/groups/G0059) has acquired Amazon S3 buckets to use in C2.[^31]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Magic Hound](https://attack.mitre.org/groups/G0059) has disabled antivirus services on targeted systems in order to upload malicious payloads.[^21]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Magic Hound](https://attack.mitre.org/groups/G0059) has conducted watering-hole attacks through media and magazine websites.[^6]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^21] [^2]  |
| [[Impacket\|S0357]] | Impacket | [^2]  |
| [[ipconfig\|S0100]] | ipconfig | [^21] [^2]  |
| [[FRP\|S1144]] | FRP | [^2]  |
| [[netsh\|S0108]] | netsh | [^21]  |
| [[Systeminfo\|S0096]] | Systeminfo | [^2]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^34]  |
| [[Ping\|S0097]] | Ping | [^2]  |
| [[Pupy\|S0192]] | Pupy | [^28] [^34] [^18]  |
| [[PsExec\|S0029]] | PsExec | [^34]  |
| [[PowerLess\|S1012]] | PowerLess | [^4]  |
| [[CharmPower\|S0674]] | CharmPower | [^31]  |
| [[DownPaper\|S0186]] | DownPaper | [^1]  |



## References

[^1]: [ClearSky Charming Kitten Dec 2017](http://www.clearskysec.com/wp-content/uploads/2017/12/Charming_Kitten_2017.pdf)


[^2]: [DFIR Phosphorus November 2021](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)


[^3]: APT35


[^4]: [Cybereason PowerLess February 2022](https://www.cybereason.com/blog/research/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage)


[^5]: Phosphorus


[^6]: [ClearSky Kittens Back 3 August 2020](https://www.clearskysec.com/wp-content/uploads/2020/08/The-Kittens-are-Back-in-Town-3.pdf)


[^7]: [Check Point Rocket Kitten](https://blog.checkpoint.com/wp-content/uploads/2015/11/rocket-kitten-report.pdf)


[^8]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^9]: [Certfa Charming Kitten January 2021](https://blog.certfa.com/posts/charming-kitten-christmas-gift/)


[^10]: [IBM ITG18 2020](https://securityintelligence.com/posts/new-research-exposes-iranian-threat-group-operations/)


[^11]: [Proofpoint TA453 March 2021](https://www.proofpoint.com/us/blog/threat-insight/badblood-ta453-targets-us-and-israeli-medical-research-personnel-credential)


[^12]: [Microsoft Phosphorus Oct 2020](https://blogs.microsoft.com/on-the-issues/2020/10/28/cyberattacks-phosphorus-t20-munich-security-conference/)


[^13]: [Microsoft Log4j Vulnerability Exploitation December 2021](https://www.microsoft.com/en-us/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/)


[^14]: [US District Court of DC Phosphorus Complaint 2019](https://noticeofpleadings.com/phosphorus/files/Complaint.pdf)


[^15]: Charming Kitten


[^16]: [Google Iran Threats October 2021](https://blog.google/threat-analysis-group/countering-threats-iran/)


[^17]: COBALT ILLUSION


[^18]: [Secureworks Cobalt Gypsy Feb 2017](https://www.secureworks.com/blog/iranian-pupyrat-bites-middle-eastern-organizations)


[^19]: Newscaster


[^20]: [Secureworks COBALT ILLUSION Threat Profile](https://www.secureworks.com/research/threat-profiles/cobalt-illusion)


[^21]: [DFIR Report APT35 ProxyShell March 2022](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)


[^22]: ITG18


[^23]: [ClearSky Kittens Back 2 Oct 2019](https://www.clearskysec.com/wp-content/uploads/2019/10/The-Kittens-Are-Back-in-Town-2-1.pdf)


[^24]: Mint Sandstorm


[^25]: [Proofpoint TA453 July2021](https://www.proofpoint.com/us/blog/threat-insight/operation-spoofedscholars-conversation-ta453)


[^26]: TA453


[^27]: [Microsoft Phosphorus Mar 2019](https://blogs.microsoft.com/on-the-issues/2019/03/27/new-steps-to-protect-customers-from-hacking/)


[^28]: [Unit 42 Magic Hound Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/)


[^29]: [Eweek Newscaster and Charming Kitten May 2014](https://www.eweek.com/security/newscaster-threat-uses-social-media-for-intelligence-gathering)


[^30]: Magic Hound


[^31]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)


[^32]: [SecureWorks Mia Ash July 2017](https://www.secureworks.com/research/the-curious-case-of-mia-ash)


[^33]: [Microsoft Iranian Threat Actor Trends November 2021](https://www.microsoft.com/en-us/security/blog/2021/11/16/evolving-trends-in-iranian-threat-actor-activity-mstic-presentation-at-cyberwarcon-2021)


[^34]: [FireEye APT35 2018](https://static.carahsoft.com/concrete/files/1015/2779/3571/M-Trends-2018-Report.pdf)


