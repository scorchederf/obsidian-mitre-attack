---
aliases: 
    - M1054
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/type/mitigation
    
mitre-attack: kb/mitre/attack/mitigations/M1054-Software_Configuration
---

## Description

Software configuration refers to making security-focused adjustments to the settings of applications, middleware, databases, or other software to mitigate potential threats. These changes help reduce the attack surface, enforce best practices, and protect sensitive data. This mitigation can be implemented through the following measures:<br><br>Conduct a Security Review of Application Settings:<br><br>- Review the software documentation to identify recommended security configurations.<br>- Compare default settings against organizational policies and compliance requirements.<br><br>Implement Access Controls and Permissions:<br><br>- Restrict access to sensitive features or data within the software.<br>- Enforce least privilege principles for all roles and accounts interacting with the software.<br><br>Enable Logging and Monitoring:<br><br>- Configure detailed logging for key application events such as authentication failures, configuration changes, or unusual activity.<br>- Integrate logs with a centralized monitoring solution, such as a SIEM.<br><br>Update and Patch Software Regularly:<br><br>- Ensure the software is kept up-to-date with the latest security patches to address known vulnerabilities.<br>- Use automated patch management tools to streamline the update process.<br><br>Disable Unnecessary Features or Services:<br><br>- Turn off unused functionality or components that could introduce vulnerabilities, such as debugging interfaces or deprecated APIs.<br><br>Test Configuration Changes:<br><br>- Perform configuration changes in a staging environment before applying them in production.<br>- Conduct regular audits to ensure that settings remain aligned with security policies.<br><br>*Tools for Implementation*<br><br>Configuration Management Tools:<br><br>- Ansible: Automates configuration changes across multiple applications and environments.<br>- Chef: Ensures consistent application settings through code-based configuration management.<br>- Puppet: Automates software configurations and audits changes for compliance.<br><br>Security Benchmarking Tools:<br><br>- CIS-CAT: Provides benchmarks and audits for secure software configurations.<br>- Aqua Security Trivy: Scans containerized applications for configuration issues.<br><br>Vulnerability Management Solutions:<br><br>- Nessus: Identifies misconfigurations and suggests corrective actions.<br><br>Logging and Monitoring Tools:<br><br>- Splunk: Aggregates and analyzes application logs to detect suspicious activity.

## Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1137-Office_Application_Startup\|T1137]] | Office Application Startup | For the Office Test method, create the Registry key used to execute it and set the permissions to "Read Control" to prevent easy access to the key without administrator permissions or requiring Privilege Escalation. [^2]  |
| [[kb/mitre/attack/techniques/T1137.002-Office_Test\|T1137.002]] | Office Test | Create the Registry key used to execute it and set the permissions to "Read Control" to prevent easy access to the key without administrator permissions or requiring Privilege Escalation.[^2]  |
| [[kb/mitre/attack/techniques/T1213-Data_from_Information_Repositories\|T1213]] | Data from Information Repositories | Consider implementing data retention policies to automate periodically archiving and/or deleting data that is no longer needed.   |
| [[kb/mitre/attack/techniques/T1213.004-Customer_Relationship_Management_Software\|T1213.004]] | Customer Relationship Management Software | Consider implementing data retention policies to automate periodically archiving and/or deleting data that is no longer needed.    |
| [[kb/mitre/attack/techniques/T1213.006-Databases\|T1213.006]] | Databases | Consider implementing data retention policies to automate periodically archiving and/or deleting data that is no longer needed.  |
| [[kb/mitre/attack/techniques/T1535-Unused_Unsupported_Cloud_Regions\|T1535]] | Unused／Unsupported Cloud Regions | Cloud service providers may allow customers to deactivate unused regions.[^3]  |
| [[kb/mitre/attack/techniques/T1537-Transfer_Data_to_Cloud_Account\|T1537]] | Transfer Data to Cloud Account | Configure appropriate data sharing restrictions in cloud services. For example, external sharing in Microsoft SharePoint and Google Drive can be turned off altogether, blocked for certain domains, or restricted to certain users.[^8]  [^17]  |
| [[kb/mitre/attack/techniques/T1539-Steal_Web_Session_Cookie\|T1539]] | Steal Web Session Cookie | Configure browsers or tasks to regularly delete persistent cookies.<br><br>Additionally, minimize the length of time a web cookie is viable to potentially reduce the impact of stolen cookies while also increasing the needed frequency of cookie theft attempts – providing defenders with additional chances at detection.[^15]  For example, use non-persistent cookies to limit the duration a session ID will remain on the web client cache where an attacker could obtain it.[^6]  |
| [[kb/mitre/attack/techniques/T1543-Create_or_Modify_System_Process\|T1543]] | Create or Modify System Process | Where possible, consider enforcing the use of container services in rootless mode to limit the possibility of privilege escalation or malicious effects on the host running the container. |
| [[kb/mitre/attack/techniques/T1543.005-Container_Service\|T1543.005]] | Container Service | Where possible, consider enforcing the use of container services in rootless mode to limit the possibility of privilege escalation or malicious effects on the host running the container.   |
| [[kb/mitre/attack/techniques/T1546.013-PowerShell_Profile\|T1546.013]] | PowerShell Profile | Avoid PowerShell profiles if not needed. Use the -No Profile flag with when executing PowerShell scripts remotely to prevent local profiles and scripts from being executed. |
| [[kb/mitre/attack/techniques/T1550.004-Web_Session_Cookie\|T1550.004]] | Web Session Cookie | Configure browsers or tasks to regularly delete persistent cookies. |
| [[kb/mitre/attack/techniques/T1553-Subvert_Trust_Controls\|T1553]] | Subvert Trust Controls | HTTP Public Key Pinning (HPKP) is one method to mitigate potential [[kb/mitre/attack/techniques/T1557-Adversary-in-the-Middle\|Adversary-in-the-Middle]] situations where and adversary uses a mis-issued or fraudulent certificate to intercept encrypted communications by enforcing use of an expected certificate. [^10]  |
| [[kb/mitre/attack/techniques/T1553.004-Install_Root_Certificate\|T1553.004]] | Install Root Certificate | HTTP Public Key Pinning (HPKP) is one method to mitigate potential [[kb/mitre/attack/techniques/T1557-Adversary-in-the-Middle\|Adversary-in-the-Middle]] situations where and adversary uses a mis-issued or fraudulent certificate to intercept encrypted communications by enforcing use of an expected certificate. [^10]  |
| [[kb/mitre/attack/techniques/T1555.005-Password_Managers\|T1555.005]] | Password Managers | Consider re-locking password managers after a short timeout to limit the time plaintext credentials live in memory from decrypted databases. |
| [[kb/mitre/attack/techniques/T1559-Inter-Process_Communication\|T1559]] | Inter-Process Communication | Consider disabling embedded files in Office programs, such as OneNote, that do not work with Protected View.[^4] [^5]  |
| [[kb/mitre/attack/techniques/T1559.002-Dynamic_Data_Exchange\|T1559.002]] | Dynamic Data Exchange | Consider disabling embedded files in Office programs, such as OneNote, that do not work with Protected View.[^4] [^5]  |
| [[kb/mitre/attack/techniques/T1566-Phishing\|T1566]] | Phishing | Use anti-spoofing and email authentication mechanisms to filter messages based on validity checks of the sender domain (using SPF) and integrity of messages (using DKIM). Enabling these mechanisms within an organization (through policies such as DMARC) may enable recipients (intra-org and cross domain) to perform similar message filtering and validation.[^18] [^1]  |
| [[kb/mitre/attack/techniques/T1566.001-Spearphishing_Attachment\|T1566.001]] | Spearphishing Attachment | Use anti-spoofing and email authentication mechanisms to filter messages based on validity checks of the sender domain (using SPF) and integrity of messages (using DKIM). Enabling these mechanisms within an organization (through policies such as DMARC) may enable recipients (intra-org and cross domain) to perform similar message filtering and validation.[^18] [^1]  |
| [[kb/mitre/attack/techniques/T1566.002-Spearphishing_Link\|T1566.002]] | Spearphishing Link | Use anti-spoofing and email authentication mechanisms to filter messages based on validity checks of the sender domain (using SPF) and integrity of messages (using DKIM). Enabling these mechanisms within an organization (through policies such as DMARC) may enable recipients (intra-org and cross domain) to perform similar message filtering and validation.[^18] [^1] .<br><br>Furthermore, policies may enforce / install browser extensions that protect against IDN and homograph attacks. |
| [[kb/mitre/attack/techniques/T1590.002-DNS\|T1590.002]] | DNS | Consider implementing policies for DNS servers, such as Zone Transfer Policies, that enforce a list of validated servers permitted for zone transfers.[^16]  |
| [[kb/mitre/attack/techniques/T1598-Phishing_for_Information\|T1598]] | Phishing for Information | Use anti-spoofing and email authentication mechanisms to filter messages based on validity checks of the sender domain (using SPF) and integrity of messages (using DKIM). Enabling these mechanisms within an organization (through policies such as DMARC) may enable recipients (intra-org and cross domain) to perform similar message filtering and validation.[^18] [^1]  |
| [[kb/mitre/attack/techniques/T1598.002-Spearphishing_Attachment\|T1598.002]] | Spearphishing Attachment | Use anti-spoofing and email authentication mechanisms to filter messages based on validity checks of the sender domain (using SPF) and integrity of messages (using DKIM). Enabling these mechanisms within an organization (through policies such as DMARC) may enable recipients (intra-org and cross domain) to perform similar message filtering and validation.[^18] [^1]  |
| [[kb/mitre/attack/techniques/T1598.003-Spearphishing_Link\|T1598.003]] | Spearphishing Link | Use anti-spoofing and email authentication mechanisms to filter messages based on validity checks of the sender domain (using SPF) and integrity of messages (using DKIM). Enabling these mechanisms within an organization (through policies such as DMARC) may enable recipients (intra-org and cross domain) to perform similar message filtering and validation.[^18] [^1] <br><br>Furthermore, policies may enforce / install browser extensions that protect against IDN and homograph attacks. Browser password managers may also be configured to only populate credential fields when the URL matches that of the original, legitimate site.  |
| [[kb/mitre/attack/techniques/T1602-Data_from_Configuration_Repository\|T1602]] | Data from Configuration Repository | Allowlist MIB objects and implement SNMP views.[^7]  |
| [[kb/mitre/attack/techniques/T1602.001-SNMP_MIB_Dump\|T1602.001]] | SNMP (MIB Dump) | Allowlist MIB objects and implement SNMP views.[^7]  |
| [[kb/mitre/attack/techniques/T1602.002-Network_Device_Configuration_Dump\|T1602.002]] | Network Device Configuration Dump | Allowlist MIB objects and implement SNMP views. Disable Smart Install (SMI) if not used.[^7] [^9]   |
| [[kb/mitre/attack/techniques/T1606-Forge_Web_Credentials\|T1606]] | Forge Web Credentials | Configure browsers/applications to regularly delete persistent web credentials (such as cookies). |
| [[kb/mitre/attack/techniques/T1606.001-Web_Cookies\|T1606.001]] | Web Cookies | Configure browsers/applications to regularly delete persistent web cookies. |
| [[kb/mitre/attack/techniques/T1666-Modify_Cloud_Resource_Hierarchy\|T1666]] | Modify Cloud Resource Hierarchy | In Azure environments, consider setting a policy to block subscription transfers.[^14]  In AWS environments, consider using Service Control Policies to prevent the use of the `LeaveOrganization` API call.[^13]  |
| [[kb/mitre/attack/techniques/T1667-Email_Bombing\|T1667]] | Email Bombing | Use anti-spoofing and email authentication mechanisms to filter messages based on validity checks of the sender domain (using SPF) and integrity of messages (using DKIM). Enabling these mechanisms within an organization (through policies such as DMARC) may enable recipients (intra-org and cross domain) to perform similar message filtering and validation.[^18] [^1]  Note that additional filtering may be necessary if emails are coming from legitimate sources.  |
| [[kb/mitre/attack/techniques/T1677-Poisoned_Pipeline_Execution\|T1677]] | Poisoned Pipeline Execution | Where possible, avoid allowing pipelines to run unreviewed code. Where this is necessary, ensure that these pipelines are executed on isolated nodes without access to secrets. In GitHub, avoid using the `pull_request_target` trigger if possible, do not treat user-controlled inputs (such as branch names) as trusted, and do not use self-hosted runners on public repositories.   |
| [[kb/mitre/attack/techniques/T1684.002-Email_Spoofing\|T1684.002]] | Email Spoofing | Use anti-spoofing and email authentication mechanisms to filter messages based on validity checks of the sender domain (using SPF) and integrity of messages (using DKIM). Enabling these mechanisms within an organization (through policies such as DMARC) may enable recipients (intra-org and cross domain) to perform similar message filtering and validation.[^18] [^1]  |
| [[kb/mitre/attack/techniques/T1685-Disable_or_Modify_Tools\|T1685]] | Disable or Modify Tools | Consider automatically relaunching forwarding mechanisms at recurring intervals (ex: temporal, on-logon, etc.) as well as applying appropriate change management to firewall rules and other related system configurations. |
| [[kb/mitre/attack/techniques/T1688-Safe_Mode_Boot\|T1688]] | Safe Mode Boot | Ensure that endpoint defenses run in safe mode.[^11]  |
| [[kb/mitre/attack/techniques/T1689-Downgrade_Attack\|T1689]] | Downgrade Attack | Consider implementing policies on internal web servers, such HTTP Strict Transport Security, that enforce the use of HTTPS/network traffic encryption to prevent insecure connections.[^12]  |



> [!info]- References
> [^1]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)

> [^2]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)

> [^3]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)

> [^4]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)

> [^5]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)

> [^6]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)

> [^7]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)

> [^8]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)

> [^9]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)

> [^10]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)

> [^11]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)

> [^12]: [Chromium HSTS](https://www.chromium.org/hsts/)

> [^13]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)

> [^14]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)

> [^15]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)

> [^16]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)

> [^17]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)

> [^18]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


