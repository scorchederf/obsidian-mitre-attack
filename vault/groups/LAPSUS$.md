---
aliases: 
    - LAPSUS$
    - DEV-0537
    - Strawberry Tempest
mitre-attack: https://attack.mitre.org/groups/G1004
---

## G1004

[LAPSUS$](https://attack.mitre.org/groups/G1004) is cyber criminal threat group that has been active since at least mid-2021. [LAPSUS$](https://attack.mitre.org/groups/G1004) specializes in large-scale social engineering and extortion operations, including destructive attacks without the use of ransomware. The group has targeted organizations globally, including in the government, manufacturing, higher education, energy, healthcare, technology, telecommunications, and media sectors.[^1] [^3] [^5] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Gather Victim Identity Information\|T1589]] | Gather Victim Identity Information | [LAPSUS$](https://attack.mitre.org/groups/G1004) has gathered detailed information of target employees to enhance their social engineering lures.[^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [LAPSUS$](https://attack.mitre.org/groups/G1004) uploaded sensitive files, information, and credentials from a targeted organization for extortion or public release.[^3]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [LAPSUS$](https://attack.mitre.org/groups/G1004) has used the AD Explorer tool to enumerate groups on a victim's network.[^3]  |
| [[Confluence\|T1213.001]] | Confluence | [LAPSUS$](https://attack.mitre.org/groups/G1004) has searched a victim's network for collaboration platforms like Confluence and JIRA to discover further high-privilege account credentials.[^3]  |
| [[Tool\|T1588.002]] | Tool | [LAPSUS$](https://attack.mitre.org/groups/G1004) has obtained tools such as RVTools and AD Explorer for their operations.[^3] [^6]  |
| [[Data Destruction\|T1485]] | Data Destruction | [LAPSUS$](https://attack.mitre.org/groups/G1004) has deleted the target's systems and resources both on-premises and in the cloud.[^3] [^6]  |
| [[Code Repositories\|T1213.003]] | Code Repositories | [LAPSUS$](https://attack.mitre.org/groups/G1004) has searched a victim's network for code repositories like GitLab and GitHub to discover further high-privilege account credentials.[^3] [^6]  |
| [[Sharepoint\|T1213.002]] | Sharepoint | [LAPSUS$](https://attack.mitre.org/groups/G1004) has searched a victim's network for collaboration platforms like SharePoint to discover further high-privilege account credentials.[^3] [^6]  |
| [[Virtual Private Server\|T1583.003]] | Virtual Private Server | [LAPSUS$](https://attack.mitre.org/groups/G1004) has used VPS hosting providers for infrastructure.[^3]  |
| [[Identify Roles\|T1591.004]] | Identify Roles | [LAPSUS$](https://attack.mitre.org/groups/G1004) has gathered detailed knowledge of team structures within a target organization.[^3]  |
| [[Proxy\|T1090]] | Proxy | [LAPSUS$](https://attack.mitre.org/groups/G1004) has leverage NordVPN for its egress points when targeting intended victims.[^3]  |
| [[Domain Account\|T1087.002]] | Domain Account | [LAPSUS$](https://attack.mitre.org/groups/G1004) has used the AD Explorer tool to enumerate users on a victim's network.[^3] [^6]  |
| [[External Remote Services\|T1133]] | External Remote Services | [LAPSUS$](https://attack.mitre.org/groups/G1004) has gained access to internet-facing systems and applications, including virtual private network (VPN), remote desktop protocol (RDP), and virtual desktop infrastructure (VDI) including Citrix. [^3] [^6]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [LAPSUS$](https://attack.mitre.org/groups/G1004) has used compromised credentials and/or session tokens to gain access into a victim's VPN, VDI, RDP, and IAMs.[^3] [^6]  |
| [[Malware\|T1588.001]] | Malware | [LAPSUS$](https://attack.mitre.org/groups/G1004) acquired and used the Redline password stealer in their operations.[^3]  |
| [[Spearphishing Voice\|T1598.004]] | Spearphishing Voice | [LAPSUS$](https://attack.mitre.org/groups/G1004) has called victims' help desk to convince the support personnel to reset a privileged account’s credentials.[^3]  |
| [[User Execution\|T1204]] | User Execution | [LAPSUS$](https://attack.mitre.org/groups/G1004) has recruited target organization employees or contractors who provide credentials and approve an associated MFA prompt, or install remote management software onto a corporate workstation, allowing [LAPSUS$](https://attack.mitre.org/groups/G1004) to take control of an authenticated system.[^3]  |
| [[Chat Messages\|T1552.008]] | Chat Messages | [LAPSUS$](https://attack.mitre.org/groups/G1004) has targeted various collaboration tools like Slack, Teams, JIRA, Confluence, and others to hunt for exposed credentials to support privilege escalation and lateral movement.[^3]  |
| [[Service Stop\|T1489]] | Service Stop | [LAPSUS$](https://attack.mitre.org/groups/G1004) has shut down virtual machines from within a victim's on-premise VMware ESXi infrastructure.[^6]  |
| [[Code Repositories\|T1593.003]] | Code Repositories | [LAPSUS$](https://attack.mitre.org/groups/G1004) has searched public code repositories for exposed credentials.[^3]  |
| [[Cloud Account\|T1136.003]] | Cloud Account | [LAPSUS$](https://attack.mitre.org/groups/G1004) has created global admin accounts in the targeted organization's cloud instances to gain persistence.[^3]  |
| [[Email Forwarding Rule\|T1114.003]] | Email Forwarding Rule | [LAPSUS$](https://attack.mitre.org/groups/G1004) has set an Office 365 tenant level mail transport rule to send all mail in and out of the targeted organization to the newly created account.[^3]  |
| [[Business Relationships\|T1591.002]] | Business Relationships | [LAPSUS$](https://attack.mitre.org/groups/G1004) has gathered detailed knowledge of an organization's supply chain relationships.[^3]  |
| [[Delete Cloud Instance\|T1578.003]] | Delete Cloud Instance | [LAPSUS$](https://attack.mitre.org/groups/G1004) has deleted the target's systems and resources in the cloud to trigger the organization's incident and crisis response process.[^3]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [LAPSUS$](https://attack.mitre.org/groups/G1004) has obtained passwords and session tokens with the use of the Redline password stealer.[^3]  |
| [[Account Access Removal\|T1531]] | Account Access Removal | [LAPSUS$](https://attack.mitre.org/groups/G1004) has removed a targeted organization's global admin accounts to lock the organization out of all access.[^3]  |
| [[Credentials\|T1589.001]] | Credentials | [LAPSUS$](https://attack.mitre.org/groups/G1004) has gathered user identities and credentials to gain initial access to a victim's organization; the group has also called an organization's help desk to reset a target's credentials.[^3] [^6]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [LAPSUS$](https://attack.mitre.org/groups/G1004) has exploited unpatched vulnerabilities on internally accessible servers including JIRA, GitLab, and Confluence for privilege escalation.[^3]  |
| [[Multi-Factor Authentication Request Generation\|T1621]] | Multi-Factor Authentication Request Generation | [LAPSUS$](https://attack.mitre.org/groups/G1004) has spammed target users with MFA prompts in the hope that the legitimate user will grant necessary approval.[^3]  |
| [[Additional Cloud Roles\|T1098.003]] | Additional Cloud Roles | [LAPSUS$](https://attack.mitre.org/groups/G1004) has added the global admin role to accounts they have created in the targeted organization's cloud instances.[^3]  |
| [[DCSync\|T1003.006]] | DCSync | [LAPSUS$](https://attack.mitre.org/groups/G1004) has used DCSync attacks to gather credentials for privilege escalation routines.[^3]  |
| [[Email Accounts\|T1586.002]] | Email Accounts | [LAPSUS$](https://attack.mitre.org/groups/G1004) has payed employees, suppliers, and business partners of target organizations for credentials.[^3] [^6]  |
| [[Messaging Applications\|T1213.005]] | Messaging Applications | [LAPSUS$](https://attack.mitre.org/groups/G1004) has searched a victim's network for organization collaboration channels like MS Teams or Slack to discover further high-privilege account credentials.[^3]  |
| [[Email Addresses\|T1589.002]] | Email Addresses | [LAPSUS$](https://attack.mitre.org/groups/G1004) has gathered employee email addresses, including personal accounts, for social engineering and initial access efforts.[^3]  |
| [[DNS Server\|T1584.002]] | DNS Server | [LAPSUS$](https://attack.mitre.org/groups/G1004) has reconfigured a victim's DNS records to actor-controlled domains and websites.[^6]  |
| [[Impersonation\|T1684.001]] | Impersonation | [LAPSUS$](https://attack.mitre.org/groups/G1004) has called victims' help desk and impersonated legitimate users with previously gathered information in order to gain access to privileged accounts.[^3]  |
| [[NTDS\|T1003.003]] | NTDS | [LAPSUS$](https://attack.mitre.org/groups/G1004) has used Windows built-in tool `ntdsutil` to extract the Active Directory (AD) database.[^3]  |
| [[Password Managers\|T1555.005]] | Password Managers | [LAPSUS$](https://attack.mitre.org/groups/G1004) has accessed local password managers and databases to obtain further credentials from a compromised network.[^6]  |
| [[Trusted Relationship\|T1199]] | Trusted Relationship | [LAPSUS$](https://attack.mitre.org/groups/G1004) has accessed internet-facing identity providers such as Azure Active Directory and Okta to target specific organizations.[^3]  |
| [[Purchase Technical Data\|T1597.002]] | Purchase Technical Data | [LAPSUS$](https://attack.mitre.org/groups/G1004) has purchased credentials and session tokens from criminal underground forums.[^3]  |
| [[Create Cloud Instance\|T1578.002]] | Create Cloud Instance | [LAPSUS$](https://attack.mitre.org/groups/G1004) has created new virtual machines within the target's cloud environment after leveraging credential access to cloud assets.[^3]   |
| [[Cloud Accounts\|T1078.004]] | Cloud Accounts | [LAPSUS$](https://attack.mitre.org/groups/G1004) has used compromised credentials to access cloud assets within a target organization.[^3]  |
| [[Multi-Factor Authentication Interception\|T1111]] | Multi-Factor Authentication Interception | [LAPSUS$](https://attack.mitre.org/groups/G1004) has replayed stolen session token and passwords to trigger simple-approval MFA prompts in hope of the legitimate user will grant necessary approval.[^3]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Mimikatz\|S0002]] | Mimikatz | [^3]  |



## References

[^1]: [BBC LAPSUS Apr 2022](https://www.bbc.com/news/technology-60953527)


[^2]: DEV-0537


[^3]: [MSTIC DEV-0537 Mar 2022](https://www.microsoft.com/security/blog/2022/03/22/dev-0537-criminal-actor-targeting-organizations-for-data-exfiltration-and-destruction/)


[^4]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^5]: [UNIT 42 LAPSUS Mar 2022](https://unit42.paloaltonetworks.com/lapsus-group/)


[^6]: [NCC Group LAPSUS Apr 2022](https://research.nccgroup.com/2022/04/28/lapsus-recent-techniques-tactics-and-procedures/)


[^7]: Strawberry Tempest


