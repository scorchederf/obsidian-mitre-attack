---
aliases: 
    - Scattered Spider
    - Roasted 0ktapus
    - Octo Tempest
    - Storm-0875
    - UNC3944
mitre-attack: https://attack.mitre.org/groups/G1015
---

## G1015

[Scattered Spider](https://attack.mitre.org/groups/G1015) is a native English-speaking cybercriminal group active since at least 2022. [^6]  [^2]  The group initially targeted customer relationship management (CRM) providers, business process outsourcing (BPO) firms, and telecommunications and technology companies before expanding in 2023 to gaming, hospitality, retail, managed service provider (MSP), manufacturing, and financial sectors. [^2] <br>[Scattered Spider](https://attack.mitre.org/groups/G1015) relies heavily on social engineering, including impersonating IT and help-desk staff, to gain initial access, bypass multi-factor authentication (MFA), and compromise enterprise networks. The group has adapted its tooling to evade endpoint detection and response (EDR) defenses and used ransomware for financial gain. [^15]  [^7]  [^12] <br>[Scattered Spider](https://attack.mitre.org/groups/G1015) had expanded into hybrid cloud and identity environments, using help-desk impersonation and MFA bypass to obtain administrator access in Okta, AWS, and Office 365. [^3] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Phishing for Information\|T1598]] | Phishing for Information | [Scattered Spider](https://attack.mitre.org/groups/G1015) has used a combination of credential phishing and social engineering to capture one-time-password (OTP) codes.[^7]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Scattered Spider](https://attack.mitre.org/groups/G1015) has uninstalled and disabled security tools.[^3]   |
| [[Code Signing\|T1553.002]] | Code Signing | [Scattered Spider](https://attack.mitre.org/groups/G1015) has used self-signed and stolen certificates originally issued to NVIDIA and Global Software LLC.[^7]  |
| [[Conditional Access Policies\|T1556.009]] | Conditional Access Policies | [Scattered Spider](https://attack.mitre.org/groups/G1015) has added additional trusted locations to Azure AD conditional access policies. [^2]  |
| [[Cloud Infrastructure Discovery\|T1580]] | Cloud Infrastructure Discovery | [Scattered Spider](https://attack.mitre.org/groups/G1015) enumerates cloud environments including Amazon Web Services (AWS) S3 buckets to identify server and backup management infrastructure, resource access, databases and storage containers .[^2] [^3] [^9]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Scattered Spider](https://attack.mitre.org/groups/G1015) has downloaded the Teleport remote access tool to compromised VMware vCenter Servers.[^10]  |
| [[Email Forwarding Rule\|T1114.003]] | Email Forwarding Rule | [Scattered Spider](https://attack.mitre.org/groups/G1015) has redirected emails notifying users of suspicious account activity.[^9]  |
| [[Spearphishing Link\|T1598.003]] | Spearphishing Link | [Scattered Spider](https://attack.mitre.org/groups/G1015) has used domains mirroring corporate login portals to socially engineer victims into providing credentials.[^14]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Scattered Spider](https://attack.mitre.org/groups/G1015) has used compromised credentials for initial access.[^3] [^10]  |
| [[NTDS\|T1003.003]] | NTDS | [Scattered Spider](https://attack.mitre.org/groups/G1015) has extracted the `NTDS.dit` file by creating volume shadow copies of virtual domain controller disks.[^2] [^9] [^10]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Scattered Spider](https://attack.mitre.org/groups/G1015) has exfiltrated data from compromised VMware vCenter servers through an established C2 channel using the Teleport remote access tool.[^10]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Scattered Spider](https://attack.mitre.org/groups/G1015) has enumerated legitimate domain accounts which are used in the targeted environment.[^15] [^2] [^9] [^10]  |
| [[Trust Modification\|T1484.002]] | Trust Modification | [Scattered Spider](https://attack.mitre.org/groups/G1015) adds a federated identity provider to the victim’s SSO tenant and activates automatic account linking.[^15]  |
| [[Account Discovery\|T1087]] | Account Discovery | [Scattered Spider](https://attack.mitre.org/groups/G1015) has identified vSphere administrator accounts.[^10] <br> |
| [[Email Hiding Rules\|T1564.008]] | Email Hiding Rules | [Scattered Spider](https://attack.mitre.org/groups/G1015) creates inbound rules on the compromised email accounts of security personnel to automatically delete emails from vendor security products.[^2]  |
| [[Social Media Accounts\|T1585.001]] | Social Media Accounts | [Scattered Spider](https://attack.mitre.org/groups/G1015) has created matching fake social media profiles to support new accounts created in victim environments.[^15]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [Scattered Spider](https://attack.mitre.org/groups/G1015) retrieves browser cookies via Raccoon Stealer.[^15]  |
| [[Tool\|T1588.002]] | Tool | [Scattered Spider](https://attack.mitre.org/groups/G1015) has obtained tools for use throughout the attack lifecycle to include remote access software, protocol tunneling and proxy tools, exploitation frameworks, and reconnaissance tools.[^3] [^9] [^14] [^15]  |
| [[Private Keys\|T1552.004]] | Private Keys | [Scattered Spider](https://attack.mitre.org/groups/G1015) enumerate and exfiltrate code-signing certificates from a compromised host.[^15]  |
| [[Gather Victim Identity Information\|T1589]] | Gather Victim Identity Information | [Scattered Spider](https://attack.mitre.org/groups/G1015) has used information from previous data breaches to identify employee names to be used in social engineering.[^10]  |
| [[Cloud Service Dashboard\|T1538]] | Cloud Service Dashboard | [Scattered Spider](https://attack.mitre.org/groups/G1015) abused AWS Systems Manager Inventory to identify targets on the compromised network prior to lateral movement.[^15]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Scattered Spider](https://attack.mitre.org/groups/G1015) has used [BlackCat](https://attack.mitre.org/software/S1068) and DragonForce ransomware to encrypt files including on VMWare ESXi servers.[^15] [^2] [^9] [^10] [^14]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Scattered Spider](https://attack.mitre.org/groups/G1015) has used the command shell to upload and install the Teleport remote access tool to a compromised vCenter Server Appliance.[^10]  |
| [[External Remote Services\|T1133]] | External Remote Services | [Scattered Spider](https://attack.mitre.org/groups/G1015) has leveraged legitimate remote management tools to maintain persistent access.[^7]  |
| [[SSH\|T1021.004]] | SSH | [Scattered Spider](https://attack.mitre.org/groups/G1015) has used SSH to move laterally in victim environments and to access the vSphere vCenter Server GUI.[^3] [^10] <br> |
| [[User Execution\|T1204]] | User Execution | [Scattered Spider](https://attack.mitre.org/groups/G1015) has impersonated organization IT and helpdesk staff to instruct victims to execute commercial remote access tools to gain initial access.[^15]  |
| [[Multi-Factor Authentication\|T1556.006]] | Multi-Factor Authentication | After compromising user accounts, [Scattered Spider](https://attack.mitre.org/groups/G1015) registers their own MFA tokens.[^15]  |
| [[Impersonation\|T1684.001]] | Impersonation | [Scattered Spider](https://attack.mitre.org/groups/G1015) utilized social engineering to compel IT help desk personnel to reset passwords and MFA tokens.[^15] [^2]  [Scattered Spider](https://attack.mitre.org/groups/G1015) has also used Microsoft Teams to pose as internal IT support or help desk personnel.[^3]   |
| [[Domains\|T1583.001]] | Domains | [Scattered Spider](https://attack.mitre.org/groups/G1015) has registered domains to spoof legitimate corporate login portals.[^14]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Scattered Spider](https://attack.mitre.org/groups/G1015) has used network reconnaissance commands for discovery including `ping` and `nltest`.[^3]    |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Scattered Spider](https://attack.mitre.org/groups/G1015) Spider enumerates a target organization for files and directories of interest, including source code, user provisioning, MFA device registration, network diagrams, and shared credentials in documents or spreadsheets.[^15] [^2] [^3] [^9] [^10]  |
| [[Systemd Service\|T1543.002]] | Systemd Service | [Scattered Spider](https://attack.mitre.org/groups/G1015) has run `SYSTEMD_UNIT_PATH="/lib/systemd/<br>system/teleport.service` to establish persistence for the Teleport remote access tool.[^10]  |
| [[Remote Desktop Software\|T1219.002]] | Remote Desktop Software | In addition to directing victims to run remote software, [Scattered Spider](https://attack.mitre.org/groups/G1015) members themselves also deploy RMM software including TeamViewer, AnyDesk, LogMeIn, [ngrok](https://attack.mitre.org/software/S0508), and [ConnectWise](https://attack.mitre.org/software/S0591) to establish persistence on the compromised network.[^15] [^4] [^3] [^9] [^14]  |
| [[Financial Theft\|T1657]] | Financial Theft | [Scattered Spider](https://attack.mitre.org/groups/G1015) has deployed ransomware on compromised hosts and threatened to leak stolen data for financial gain.[^15] [^4] [^9]  |
| [[Code Repositories\|T1213.003]] | Code Repositories | [Scattered Spider](https://attack.mitre.org/groups/G1015) enumerates data stored within victim code repositories, such as internal GitHub repositories.[^15] [^2]  |
| [[Additional Cloud Roles\|T1098.003]] | Additional Cloud Roles | [Scattered Spider](https://attack.mitre.org/groups/G1015) has assigned user access admin roles in order to gain Tenant Root Group management permissions in Azure.[^2]  |
| [[Permission Groups Discovery\|T1069]] | Permission Groups Discovery | [Scattered Spider](https://attack.mitre.org/groups/G1015) has enumerated the vSphere Admins and ESX Admins groups in targeted environments.[^10]  |
| [[Multi-Factor Authentication Request Generation\|T1621]] | Multi-Factor Authentication Request Generation | [Scattered Spider](https://attack.mitre.org/groups/G1015) has used multifactor authentication (MFA) fatigue by sending repeated MFA authentication requests to targets.[^7] [^14]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Scattered Spider](https://attack.mitre.org/groups/G1015) has executed scripts to identify the underlying operating system to ensure it uses the correct installation package for malicious payloads.[^10]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Scattered Spider](https://attack.mitre.org/groups/G1015) has used RDP to enable lateral movement.[^3]   |
| [[Account Manipulation\|T1098]] | Account Manipulation | [Scattered Spider](https://attack.mitre.org/groups/G1015) has added accounts to the ESX Admins group to grant them full admin rights in vSphere.[^10]  |
| [[Messaging Applications\|T1213.005]] | Messaging Applications | [Scattered Spider](https://attack.mitre.org/groups/G1015) threat actors search the victim’s Slack and Microsoft Teams for conversations about the intrusion and incident response.[^15]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [Scattered Spider](https://attack.mitre.org/groups/G1015) has deployed a malicious kernel driver through exploitation of CVE-2015-2291 in the Intel Ethernet diagnostics driver for Windows (iqvw64.sys).[^7]  |
| [[Proxy\|T1090]] | Proxy | [Scattered Spider](https://attack.mitre.org/groups/G1015) has used proxy networks to hamper detection and has installed legitimate proxy tools on VMware vCenter and adversary-controlled VMs.[^9] [^15]  |
| [[Data from Cloud Storage\|T1530]] | Data from Cloud Storage | [Scattered Spider](https://attack.mitre.org/groups/G1015) enumerates data stored in cloud resources for collection and exfiltration purposes.[^15]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [Scattered Spider](https://attack.mitre.org/groups/G1015) retrieves browser histories via infostealer malware such as Raccoon Stealer.[^15]  |
| [[Direct Volume Access\|T1006]] | Direct Volume Access | [Scattered Spider](https://attack.mitre.org/groups/G1015) has created volume shadow copies of virtual domain controller disks to extract the `NTDS.dit` file.[^2]  |
| [[Create Account\|T1136]] | Create Account | [Scattered Spider](https://attack.mitre.org/groups/G1015) creates new user identities within the compromised organization.[^15]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Scattered Spider](https://attack.mitre.org/groups/G1015) has stopped the Volume Shadow Copy service on compromised hosts.[^3]   |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Scattered Spider](https://attack.mitre.org/groups/G1015) can enumerate remote systems, such as VMware vCenter infrastructure.[^15]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | <br>[Scattered Spider](https://attack.mitre.org/groups/G1015) has enumerated Active Directory security groups including through the use of ADExplorer, ADRecon.ps1, and Get-ADUser.[^9] [^10] <br> |
| [[PowerShell\|T1059.001]] | PowerShell | [Scattered Spider](https://attack.mitre.org/groups/G1015) has used the PowerShell cmdlet Get-ADUser.[^9]  |
| [[Password Managers\|T1555.005]] | Password Managers | [Scattered Spider](https://attack.mitre.org/groups/G1015) has searched for credentials in password vaults and Privileged Access Management (PAM) solutions including HashiCorp Vault.[^3] [^10]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Scattered Spider](https://attack.mitre.org/groups/G1015) has exfiltrated victim data to the MEGA file sharing site, SnowFlake, and AWS S3 buckets.[^15] [^2] [^9]  |
| [[Spearphishing Voice\|T1598.004]] | Spearphishing Voice | [Scattered Spider](https://attack.mitre.org/groups/G1015) has used help desk voice-based phishing and also called employees at target organizations and compelled them to navigate to fake login portals using adversary-in-the-middle toolkits.[^2] [^9] [^10]  |
| [[Data Staged\|T1074]] | Data Staged | [Scattered Spider](https://attack.mitre.org/groups/G1015) stages data in a centralized database prior to exfiltration.[^15]  |
| [[Cloud Accounts\|T1078.004]] | Cloud Accounts | [Scattered Spider](https://attack.mitre.org/groups/G1015) has used compromised Microsoft Entra ID accounts to pivot in victim environments.[^9]  |
| [[Clear Mailbox Data\|T1070.008]] | Clear Mailbox Data | [Scattered Spider](https://attack.mitre.org/groups/G1015) has manually deleted emails notifying users of suspicious account activity.  [^9]  |
| [[Cloud Services\|T1021.007]] | Cloud Services | [Scattered Spider](https://attack.mitre.org/groups/G1015) has also leveraged pre-existing AWS EC2 instances for lateral movement and data collection purposes.[^15]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Scattered Spider](https://attack.mitre.org/groups/G1015) has installed protocol-tunneling tools on VMware vCenter and adversary-controlled VMs, including Teleport.sh, Chisel (configured to communicate with trycloudflare[.]com subdomains), MobaXterm, ngrok, Pinggy, and Teleport.[^9] [^15]  |
| [[Create Cloud Instance\|T1578.002]] | Create Cloud Instance | [Scattered Spider](https://attack.mitre.org/groups/G1015) has created Amazon EC2 instances within the victim's environment.[^15]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [Scattered Spider](https://attack.mitre.org/groups/G1015) Spider searches for credential storage documentation on a compromised host.[^15] [^3] [^9]  |
| [[Email Collection\|T1114]] | Email Collection | [Scattered Spider](https://attack.mitre.org/groups/G1015) searched the victim’s Microsoft Exchange for emails about the intrusion and incident response.[^15]  |
| [[Malware\|T1588.001]] | Malware | [Scattered Spider](https://attack.mitre.org/groups/G1015) has obtained malware to use at multiple stages of operations including information stealers, remote access tools, and ransomware.[^3] [^14]   |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[ngrok\|S0508]] | ngrok | [Scattered Spider](https://attack.mitre.org/groups/G1015) has used [ngrok](https://attack.mitre.org/software/S0508) to create secure tunnels to remote web servers.[^15] [^9] [^14]  |
| [[Rclone\|S1040]] | Rclone | [^3]    |
| [[ConnectWise\|S0591]] | ConnectWise | [Scattered Spider](https://attack.mitre.org/groups/G1015) has used [ConnectWise](https://attack.mitre.org/software/S0591) to maintain persistence.[^3] [^14]  |
| [[Mimikatz\|S0002]] | Mimikatz | [Scattered Spider](https://attack.mitre.org/groups/G1015) has gathered credentials using [Mimikatz](https://attack.mitre.org/software/S0002).[^15] [^2] [^3] [^14]  |
| [[LaZagne\|S0349]] | LaZagne | [Scattered Spider](https://attack.mitre.org/groups/G1015) can obtain credential information using [LaZagne](https://attack.mitre.org/software/S0349).[^2]  |
| [[Tor\|S0183]] | Tor | [Scattered Spider](https://attack.mitre.org/groups/G1015) has used [Tor](https://attack.mitre.org/software/S0183) to communicate with targeted organizations.[^15]  |
| [[BlackCat\|S1068]] | BlackCat | [Scattered Spider](https://attack.mitre.org/groups/G1015) has deployed [BlackCat](https://attack.mitre.org/software/S1068) ransomware to victim environments for financial gain.[^15] [^2] [^3] [^14]  |
| [[Raccoon Stealer\|S1148]] | Raccoon Stealer | [^14]  |
| [[WarzoneRAT\|S0670]] | WarzoneRAT | [Scattered Spider](https://attack.mitre.org/groups/G1015) has utilized [WarzoneRAT](https://attack.mitre.org/software/S0670) to remotely access a compromised system.[^15] [^14]  |



## References

[^1]: UNC3944


[^2]: [MSTIC Octo Tempest Operations October 2023](https://www.microsoft.com/en-us/security/blog/2023/10/25/octo-tempest-crosses-boundaries-to-facilitate-extortion-encryption-and-destruction/)


[^3]: [Mandiant UNC3944 May 2025](https://cloud.google.com/blog/topics/threat-intelligence/unc3944-proactive-hardening-recommendations)


[^4]: [Trellix Scattered Spider MO August 2023](https://www.trellix.com/blogs/research/scattered-spider-the-modus-operandi/)


[^5]: Octo Tempest


[^6]: [CrowdStrike Scattered Spider Profile](https://www.crowdstrike.com/adversaries/scattered-spider/)


[^7]: [CrowdStrike Scattered Spider BYOVD January 2023](https://www.crowdstrike.com/blog/scattered-spider-attempts-to-avoid-detection-with-bring-your-own-vulnerable-driver-tactic/)


[^8]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^9]: [CrowdStrike Scattered Spider JUL 2025](https://www.crowdstrike.com/en-us/blog/crowdstrike-services-observes-scattered-spider-escalate-attacks/)


[^10]: [Mandiant VMware vSphere JUL 2025](https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944)


[^11]: Roasted 0ktapus


[^12]: [Crowdstrike TELCO BPO Campaign December 2022](https://www.crowdstrike.com/blog/analysis-of-intrusion-campaign-targeting-telecom-and-bpo-companies/)


[^13]: Storm-0875


[^14]: [Check Point Scattered Spider JUL 2025](https://blog.checkpoint.com/research/exposing-scattered-spider-new-indicators-highlight-growing-threat-to-enterprises-and-aviation/)


[^15]: [CISA Scattered Spider Advisory November 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)


