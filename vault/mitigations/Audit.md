---
aliases: 
    - M1047
    
mitre-attack: https://attack.mitre.org/mitigations/M1047
---

## M1047

Auditing is the process of recording activity and systematically reviewing and analyzing the activity and system configurations. The primary purpose of auditing is to detect anomalies and identify potential threats or weaknesses in the environment. Proper auditing configurations can also help to meet compliance requirements. The process of auditing encompasses regular analysis of user behaviors and system logs in support of proactive security measures.<br><br>Auditing is applicable to all systems used within an organization, from the front door of a building to accessing a file on a fileserver. It is considered more critical for regulated industries such as, healthcare, finance and government where compliance requirements demand stringent tracking of user and system activates.This mitigation can be implemented through the following measures: <br><br>System Audit:<br><br>- Use Case: Regularly assess system configurations to ensure compliance with organizational security policies.<br>- Implementation: Use tools to scan for deviations from established benchmarks.<br><br>Permission Audits:<br><br>- Use Case: Review file and folder permissions to minimize the risk of unauthorized access or privilege escalation.<br>- Implementation: Run access reviews to identify users or groups with excessive permissions.<br><br>Software Audits:<br><br>- Use Case: Identify outdated, unsupported, or insecure software that could serve as an attack vector.<br>- Implementation: Use inventory and vulnerability scanning tools to detect outdated versions and recommend secure alternatives.<br><br>Configuration Audits:<br><br>- Use Case: Evaluate system and network configurations to ensure secure settings (e.g., disabled SMBv1, enabled MFA).<br>- Implementation: Implement automated configuration scanning tools like SCAP (Security Content Automation Protocol) to identify non-compliant systems.<br><br>Network Audits:<br><br>- Use Case: Examine network traffic, firewall rules, and endpoint communications to identify unauthorized or insecure connections.<br>- Implementation: Utilize tools such as Wireshark, or Zeek to monitor and log suspicious network behavior.

### Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[Domain or Tenant Policy Modification\|T1484]] | Domain or Tenant Policy Modification | Identify and correct GPO permissions abuse opportunities (ex: GPO modification privileges) using auditing tools such as [BloodHound](https://attack.mitre.org/software/S0521) (version 1.5.1 and later)[^3] . |
| [[Python\|T1059.006]] | Python | Inventory systems for unauthorized Python installations. |
| [[Masquerading\|T1036]] | Masquerading | Audit user accounts to ensure that each one has a defined purpose. |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | Map the trusts within existing domains/forests and keep trust relationships to a minimum. |
| [[Cron\|T1053.003]] | Cron | Review changes to the `cron` schedule. `cron` execution can be reviewed within the `/var/log` directory. To validate the location of the `cron` log file, check the syslog config at `/etc/rsyslog.conf` or `/etc/syslog.conf`. |
| [[Executable Installer File Permissions Weakness\|T1574.005]] | Executable Installer File Permissions Weakness | Use auditing tools capable of detecting file system permissions abuse opportunities on systems within an enterprise and correct them. Toolkits like the PowerSploit framework contain PowerUp modules that can be used to explore systems for service file system permissions weaknesses.[^22]  |
| [[Terminal Services DLL\|T1505.005]] | Terminal Services DLL | Regularly check component software on critical services that adversaries may target for persistence to verify the integrity of the systems and identify if unexpected changes have been made. |
| [[Cloud Firewall\|T1686.001]] | Cloud Firewall | Routinely check account role permissions to ensure only expected users and roles have permission to modify cloud firewalls.  |
| [[Browser Extensions\|T1176.001]] | Browser Extensions |  Ensure extensions that are installed are the intended ones, as many malicious extensions will masquerade as legitimate ones. |
| [[Server Software Component\|T1505]] | Server Software Component | Regularly check component software on critical services that adversaries may target for persistence to verify the integrity of the systems and identify if unexpected changes have been made. |
| [[Pre-OS Boot\|T1542]] | Pre-OS Boot | Perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses. |
| [[Phishing\|T1566]] | Phishing | Perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses. |
| [[Group Policy Modification\|T1484.001]] | Group Policy Modification | Identify and correct GPO permissions abuse opportunities (ex: GPO modification privileges) using auditing tools such as [BloodHound](https://attack.mitre.org/software/S0521) (version 1.5.1 and later).[^3]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | Implement auditing for authentication activities and user logins to detect the use of stolen session cookies. Monitor for impossible travel scenarios and anomalous behavior that could indicate the use of compromised session tokens or cookies. |
| [[SQL Stored Procedures\|T1505.001]] | SQL Stored Procedures | Regularly check component software on critical services that adversaries may target for persistence to verify the integrity of the systems and identify if unexpected changes have been made.  |
| [[Run Virtual Instance\|T1564.006]] | Run Virtual Instance | Periodically audit virtual machines for abnormalities. On ESXi servers, periodically compare the output of `vim-cmd vmsvc/getallvms`, which lists all VMs in vCenter, and `escxli vm process list | grep Display`, which lists all VMs hosted on ESXi.[^37]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | Routinely check account role permissions to ensure only expected users and roles have permission to modify system firewalls. |
| [[Network Device Firewall\|T1686.002]] | Network Device Firewall | Routinely check account role permissions to ensure only expected users and roles have permission to modify system firewalls. |
| [[Path Interception by Unquoted Path\|T1574.009]] | Path Interception by Unquoted Path | Find and eliminate path interception weaknesses in program configuration files, scripts, the PATH environment variable, services, and in shortcuts by surrounding PATH variables with quotation marks when functions allow for them. Be aware of the search order Windows uses for executing or loading binaries and use fully qualified paths wherever appropriate.<br><br>Clean up old Windows Registry keys when software is uninstalled to avoid keys with no associated legitimate binaries. Periodically search for and correct or report path interception weaknesses on systems that may have been introduced using custom or available tools that report software using insecure path configurations.[^14] [^15] [^30]  |
| [[Disable or Modify Windows Event Log\|T1685.001]] | Disable or Modify Windows Event Log | Consider periodic review of `auditpol` settings for Administrator accounts and perform dynamic baselining on SIEM(s) to investigate potential malicious activity. Also ensure that the EventLog service and its threads are properly running. |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | Audit the Remote Desktop Users group membership regularly. Remove unnecessary accounts and groups from Remote Desktop Users groups. |
| [[Email Hiding Rules\|T1564.008]] | Email Hiding Rules | Enterprise email solutions may have monitoring mechanisms that may include the ability to audit inbox rules on a regular basis. <br><br>In an Exchange environment, Administrators can use `Get-InboxRule` / `Remove-InboxRule` and `Get-TransportRule` / `Remove-TransportRule` to discover and remove potentially malicious inbox and transport rules.[^20] [^11]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | Check for common UAC bypass weaknesses on Windows systems to be aware of the risk posture and address issues where appropriate.[^5]  |
| [[AS-REP Roasting\|T1558.004]] | AS-REP Roasting | Kerberos preauthentication is enabled by default. Older protocols might not support preauthentication therefore it is possible to have this setting disabled. Make sure that all accounts have preauthentication whenever possible and audit changes to setting. Windows tools such as PowerShell may be used to easily find which accounts have preauthentication disabled.  [^18] [^29]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | Consider periodic review of common fileless storage locations (such as the Registry or WMI repository) to potentially identify abnormal and malicious data. |
| [[At\|T1053.002]] | At | Toolkits like the PowerSploit framework contain PowerUp modules that can be used to explore systems for permission weaknesses in scheduled tasks that could be used to escalate privileges. [^22]  Windows operating system also creates a registry key specifically associated with the creation of a scheduled task on the destination host at: Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree\At1. [^17]  In Linux and macOS environments, scheduled tasks using `[at](https://attack.mitre.org/software/S0110)` can be audited locally, or through centrally collected logging, using syslog, or auditd events from the host. [^23]  |
| [[Windows Service\|T1543.003]] | Windows Service | Use auditing tools capable of detecting privilege and service abuse opportunities on systems within an enterprise and correct them.  |
| [[Cloud Application Integration\|T1671]] | Cloud Application Integration | Periodically review SaaS integrations for unapproved or potentially malicious applications.   |
| [[Use Alternate Authentication Material\|T1550]] | Use Alternate Authentication Material | Perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses. |
| [[Group Policy Preferences\|T1552.006]] | Group Policy Preferences | Search SYSVOL for any existing GGPs that may contain credentials and remove them.[^16]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | Periodically verify that tools are functioning appropriately – for example, that all expected hosts with EDRs or monitoring agents are checking in to the central console. Check EDRs to ensure that no unexpected exclusion paths have been added. In Microsoft Defender for Endpoint, exclusions can be reviewed with the `Get-MpPreference` cmdlet.[^33]  |
| [[Steal Application Access Token\|T1528]] | Steal Application Access Token | Administrators should audit all cloud and container accounts to ensure that they are necessary and that the permissions granted to them are appropriate.  Additionally, administrators should perform an audit of all OAuth applications and the permissions they have been granted to access organizational data. This should be done extensively on all applications in order to establish a baseline, followed up on with periodic audits of new or updated applications. Suspicious applications should be investigated and removed. |
| [[Hijack Execution Flow\|T1574]] | Hijack Execution Flow | Use auditing tools capable of detecting hijacking opportunities on systems within an enterprise and correct them. Toolkits like the PowerSploit framework contain PowerUp modules that can be used to explore systems for hijacking weaknesses.[^22] <br><br>Use the program sxstrace.exe that is included with Windows along with manual inspection to check manifest files for side-loading vulnerabilities in software.<br><br>Find and eliminate path interception weaknesses in program configuration files, scripts, the PATH environment variable, services, and in shortcuts by surrounding PATH variables with quotation marks when functions allow for them. Be aware of the search order Windows uses for executing or loading binaries and use fully qualified paths wherever appropriate.<br><br>Clean up old Windows Registry keys when software is uninstalled to avoid keys with no associated legitimate binaries. Periodically search for and correct or report path interception weaknesses on systems that may have been introduced using custom or available tools that report software using insecure path configurations.[^14] [^15] [^30]  |
| [[Deploy Container\|T1610]] | Deploy Container | Scan images before deployment, and block those that are not in compliance with security policies. In Kubernetes environments, the admission controller can be used to validate images after a container deployment request is authenticated but before the container is deployed.[^34]  |
| [[Web Cookies\|T1606.001]] | Web Cookies | Administrators should perform an audit of all access lists and the permissions they have been granted to access web applications and services. This should be done extensively on all resources in order to establish a baseline, followed up on with periodic audits of new or updated resources. Suspicious accounts/credentials should be investigated and removed. |
| [[Confluence\|T1213.001]] | Confluence | Consider periodic review of accounts and privileges for critical and sensitive Confluence repositories. |
| [[Messaging Applications\|T1213.005]] | Messaging Applications | Preemptively search through communication services to find inappropriately shared data, and take actions to reduce exposure when found.  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | Audit applications and their permissions to ensure access to data and resources are limited based upon necessity and principle of least privilege. |
| [[LC_LOAD_DYLIB Addition\|T1546.006]] | LC_LOAD_DYLIB Addition | Binaries can also be baselined for what dynamic libraries they require, and if an app requires a new dynamic library that wasn't included as part of an update, it should be investigated. |
| [[Hide Artifacts\|T1564]] | Hide Artifacts | Periodically audit virtual machines for abnormalities. |
| [[Create or Modify System Process\|T1543]] | Create or Modify System Process | Use auditing tools capable of detecting privilege and service abuse opportunities on systems within an enterprise and correct them. |
| [[Ccache Files\|T1558.005]] | Ccache Files | Enable and perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses.[^4]  For example, use `auditd` to audit access to hashes, machine tickets, or `/tmp` files. If using sssd and Vintela, ensure kerberos is disabled if not being used.[^8]  |
| [[Sharepoint\|T1213.002]] | Sharepoint | Consider periodic review of accounts and privileges for critical and sensitive SharePoint repositories. |
| [[Network Provider DLL\|T1556.008]] | Network Provider DLL | Periodically review for new and unknown network provider DLLs within the Registry (`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\<NetworkProviderName>\NetworkProvider\ProviderPath`).<br><br>Ensure only valid network provider DLLs are registered. The name of these can be found in the Registry key at `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\NetworkProvider\Order`, and have corresponding service subkey pointing to a DLL at `HKEY_LOCAL_MACHINE\SYSTEM\CurrentC ontrolSet\Services\<NetworkProviderName>\NetworkProvider`. |
| [[RDP Hijacking\|T1563.002]] | RDP Hijacking | Audit the Remote Desktop Users group membership regularly. Remove unnecessary accounts and groups from Remote Desktop Users groups. |
| [[Remote Services\|T1021]] | Remote Services | Perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses. |
| [[Create Snapshot\|T1578.001]] | Create Snapshot | Routinely check user permissions to ensure only the expected users have the capability to create snapshots and backups. |
| [[VNC\|T1021.005]] | VNC | Inventory workstations for unauthorized VNC server software. |
| [[IDE Extensions\|T1176.002]] | IDE Extensions | Ensure extensions that are installed are the intended ones, as many malicious extensions may masquerade as legitimate ones.  |
| [[Chat Messages\|T1552.008]] | Chat Messages | Preemptively search through communication services to find shared unsecured credentials. Searching for common patterns like "`password is `", “`password=`” and take actions to reduce exposure when found.  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | Enable auditing and monitoring for email attachments and file transfers to detect and investigate suspicious activity. Regularly review logs for anomalies related to attachments containing potentially malicious content, as well as any attempts to execute or interact with these files. This practice helps identify spearphishing attempts before they can lead to further compromise. |
| [[Clear Mailbox Data\|T1070.008]] | Clear Mailbox Data | In an Exchange environment, Administrators can use `Get-TransportRule` / `Remove-TransportRule` to discover and remove potentially malicious transport rules.[^11]  |
| [[Lua\|T1059.011]] | Lua | Inventory systems for unauthorized Lua installations. |
| [[Application Access Token\|T1550.001]] | Application Access Token | Administrators should audit all cloud and container accounts to ensure that they are necessary and that the permissions granted to them are appropriate. Where possible, the ability to request temporary account tokens on behalf of another accounts should be disabled. Additionally, administrators can leverage audit tools to monitor actions that can be conducted as a result of OAuth 2.0 access. For instance, audit reports enable admins to identify privilege escalation actions such as role creations or policy modifications, which could be actions performed after initial access. |
| [[Social Engineering\|T1684]] | Social Engineering | Enables correlation of email/identity/SaaS/endpoint activity that appears legitimate.[^31] [^39]  |
| [[SAML Tokens\|T1606.002]] | SAML Tokens | Enable advanced auditing on AD FS. Check the success and failure audit options in the AD FS Management snap-in. Enable Audit Application Generated events on the AD FS farm via Group Policy Object.[^6]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | Periodically investigate ESXi hosts for open VMCI ports. Running the `lsof -A` command and inspecting results with a type of `SOCKET_VMCI` will reveal processes that have open VMCI ports.[^24]  |
| [[Cloud Account\|T1087.004]] | Cloud Account | Routinely check user permissions to ensure only the expected users have the ability to list IAM identities or otherwise discover cloud accounts. |
| [[Multi-Factor Authentication\|T1556.006]] | Multi-Factor Authentication | Review MFA actions alongside authentication logs to ensure that MFA-based logins are functioning as intended. Review user accounts to ensure that all accounts have MFA enabled.[^38]  |
| [[Modify Cloud Compute Infrastructure\|T1578]] | Modify Cloud Compute Infrastructure | Routinely monitor user permissions to ensure only the expected users have the capability to modify cloud compute infrastructure components. |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | System scans can be performed to identify unauthorized archival utilities. |
| [[Abuse Elevation Control Mechanism\|T1548]] | Abuse Elevation Control Mechanism | Check for common UAC bypass weaknesses on Windows systems to be aware of the risk posture and address issues where appropriate.[^5]  |
| [[Browser Fingerprint\|T1036.012]] | Browser Fingerprint | Review and limit the fingerprinting surface to only necessary information on each browser to make the browser less unique. For example, the available fonts may be limited to a standard font list. [^9]  |
| [[Code Repositories\|T1213.003]] | Code Repositories | Consider periodic reviews of accounts and privileges for critical and sensitive code repositories. Scan code repositories for exposed credentials or other sensitive information. |
| [[Disable or Modify Linux Audit System Log\|T1685.004]] | Disable or Modify Linux Audit System Log | Routinely check account role permissions to ensure only expected users and roles have permission to modify logging settings.<br><br>To ensure Audit rules can not be modified at runtime, add the `auditctl -e 2` as the last command in the audit.rules files. Once started, any attempt to change the configuration in this mode will be audited and denied. The configuration can only be changed by rebooting the machine. |
| [[Modify Cloud Compute Configurations\|T1578.005]] | Modify Cloud Compute Configurations | Routinely monitor user permissions to ensure only the expected users have the capability to request quota adjustments or modify tenant-level compute settings. |
| [[Spearphishing via Service\|T1566.003]] | Spearphishing via Service | Implement auditing and logging for interactions with third-party messaging services or collaboration platforms. Monitor user activity and review logs for signs of suspicious links, downloads, or file exchanges that could indicate spearphishing attempts. Effective auditing allows for the quick identification of malicious activity originating from compromised service accounts. |
| [[Credentials in Registry\|T1552.002]] | Credentials in Registry | Proactively search for credentials within the Registry and attempt to remediate the risk. |
| [[Scheduled Task／Job\|T1053]] | Scheduled Task／Job | Toolkits like the PowerSploit framework contain PowerUp modules that can be used to explore systems for permission weaknesses in scheduled tasks that could be used to escalate privileges. [^22]  |
| [[Services File Permissions Weakness\|T1574.010]] | Services File Permissions Weakness | Use auditing tools capable of detecting file system permissions abuse opportunities on systems within an enterprise and correct them. Toolkits like the PowerSploit framework contain PowerUp modules that can be used to explore systems for service file system permissions weaknesses.[^22]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | System scans can be performed to identify unauthorized archival utilities. |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | Consider periodic review of common fileless storage locations (such as the Registry or WMI repository) to potentially identify abnormal and malicious data. |
| [[IIS Components\|T1505.004]] | IIS Components | Regularly check installed IIS components to verify the integrity of the web server and identify if unexpected changes have been made. |
| [[Software Extensions\|T1176]] | Software Extensions | Ensure extensions that are installed are the intended ones, as many malicious extensions may masquerade as legitimate ones.  |
| [[Customer Relationship Management Software\|T1213.004]] | Customer Relationship Management Software | Consider periodic review of accounts and privileges for critical and sensitive CRM data. |
| [[Hybrid Identity\|T1556.007]] | Hybrid Identity | Periodically review the hybrid identity solution in use for any discrepancies. For example, review all PTA agents in the Entra ID Management Portal to identify any unwanted or unapproved ones.[^12]  If ADFS is in use, review DLLs and executable files in the AD FS and Global Assembly Cache directories to ensure that they are signed by Microsoft. Note that in some cases binaries may be catalog-signed, which may cause the file to appear unsigned when viewing file properties.[^35]  |
| [[Unsecured Credentials\|T1552]] | Unsecured Credentials | Preemptively search for files containing passwords or other credentials and take actions to reduce the exposure risk when found. |
| [[Create Cloud Instance\|T1578.002]] | Create Cloud Instance | Routinely check user permissions to ensure only the expected users have the capability to create new instances. |
| [[Path Interception by Search Order Hijacking\|T1574.008]] | Path Interception by Search Order Hijacking | Find and eliminate path interception weaknesses in program configuration files, scripts, the PATH environment variable, services, and in shortcuts by surrounding PATH variables with quotation marks when functions allow for them. Be aware of the search order Windows uses for executing or loading binaries and use fully qualified paths wherever appropriate.<br><br>Clean up old Windows Registry keys when software is uninstalled to avoid keys with no associated legitimate binaries. Periodically search for and correct or report path interception weaknesses on systems that may have been introduced using custom or available tools that report software using insecure path configurations.[^14] [^15] [^30]  |
| [[ROMMONkit\|T1542.004]] | ROMMONkit | Periodically check the integrity of system image to ensure it has not been modified. [^19]  [^13]  [^7]   |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | Toolkits like the PowerSploit framework contain PowerUp modules that can be used to explore systems for permission weaknesses in scheduled tasks that could be used to escalate privileges. [^22]  |
| [[DLL\|T1574.001]] | DLL | Use auditing tools capable of detecting DLL search order hijacking opportunities on systems within an enterprise and correct them. Toolkits like the PowerSploit framework contain PowerUp modules that can be used to explore systems for DLL hijacking weaknesses.[^22] <br><br>Use the program `sxstrace.exe` that is included with Windows, along with manual inspection, to check manifest files for side-by-side problems in software.[^26]  |
| [[Malicious Image\|T1204.003]] | Malicious Image | Audit images deployed within the environment to ensure they do not contain any malicious components. |
| [[Delete Cloud Instance\|T1578.003]] | Delete Cloud Instance | Routinely check user permissions to ensure only the expected users have the capability to delete new instances. |
| [[Build Image on Host\|T1612]] | Build Image on Host | Audit images deployed within the environment to ensure they do not contain any malicious components. |
| [[Transport Agent\|T1505.002]] | Transport Agent | Regularly check component software on critical services that adversaries may target for persistence to verify the integrity of the systems and identify if unexpected changes have been made.  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | Inventory systems for unauthorized command and scripting interpreter installations. |
| [[Power Settings\|T1653]] | Power Settings | Periodically inspect systems for abnormal and unexpected power settings that may indicate malicious activty. |
| [[Modify Cloud Resource Hierarchy\|T1666]] | Modify Cloud Resource Hierarchy | Periodically audit resource groups in the cloud management console to ensure that only expected items exist, especially close to the top of the hierarchy (e.g., AWS accounts and Azure subscriptions). Typically, top-level accounts (such as the AWS management account) should not contain any workloads or resources.[^40]  |
| [[Path Interception by PATH Environment Variable\|T1574.007]] | Path Interception by PATH Environment Variable | Find and eliminate path interception weaknesses in program configuration files, scripts, the PATH environment variable, services, and in shortcuts by surrounding PATH variables with quotation marks when functions allow for them. Be aware of the search order Windows uses for executing or loading binaries and use fully qualified paths wherever appropriate.<br><br>Clean up old Windows Registry keys when software is uninstalled to avoid keys with no associated legitimate binaries. Periodically search for and correct or report path interception weaknesses on systems that may have been introduced using custom or available tools that report software using insecure path configurations.[^14] [^15] [^30]  |
| [[Masquerade Account Name\|T1036.010]] | Masquerade Account Name | Audit user accounts to ensure that each one has a defined purpose.   |
| [[Email Forwarding Rule\|T1114.003]] | Email Forwarding Rule | Enterprise email solutions have monitoring mechanisms that may include the ability to audit auto-forwarding rules on a regular basis.<br><br>In an Exchange environment, Administrators can use `Get-InboxRule` / `Remove-InboxRule` and `Get-TransportRule` / `Remove-TransportRule` to discover and remove potentially malicious auto-fowarding and transport rules.[^21] [^11] [^20]  In addition to this, a MAPI Editor can be utilized to examine the underlying database structure and discover any modifications/tampering of the properties of auto-forwarding rules.[^27]  |
| [[Steal or Forge Authentication Certificates\|T1649]] | Steal or Forge Authentication Certificates | Check and remediate unneeded existing authentication certificates as well as common abusable misconfigurations of CA settings and permissions, such as AD CS certificate enrollment permissions and published overly permissive certificate templates (which define available settings for created certificates). For example, available AD CS certificate templates can be checked via the Certificate Authority MMC snap-in (`certsrv.msc`). `certutil.exe` can also be used to examine various information within an AD CS CA database.[^32] [^2] [^10]  |
| [[Email Collection\|T1114]] | Email Collection | Enterprise email solutions have monitoring mechanisms that may include the ability to audit auto-forwarding rules on a regular basis.<br><br>In an Exchange environment, Administrators can use Get-InboxRule to discover and remove potentially malicious auto-forwarding rules.[^21]   |
| [[Forge Web Credentials\|T1606]] | Forge Web Credentials | Administrators should perform an audit of all access lists and the permissions they have been granted to access web applications and services. This should be done extensively on all resources in order to establish a baseline, followed up on with periodic audits of new or updated resources. Suspicious accounts/credentials should be investigated and removed.<br> <br>Enable advanced auditing on ADFS. Check the success and failure audit options in the ADFS Management snap-in. Enable Audit Application Generated events on the AD FS farm via Group Policy Object.[^6]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | Preemptively search for files containing passwords and take actions to reduce the exposure risk when found. |
| [[TCC Manipulation\|T1548.006]] | TCC Manipulation | Routinely check applications using Automation under Security & Privacy System Preferences. To reset permissions, user's can utilize the `tccutil reset` command. When using Mobile Device Management (MDM), review the list of enabled or disabled applications in the `MDMOverrides.plist` which overrides the TCC database.[^1]  |
| [[Data from Cloud Storage\|T1530]] | Data from Cloud Storage | Frequently check permissions on cloud storage to ensure proper permissions are set to deny open or unprivileged access to resources.[^28]  |
| [[Launch Daemon\|T1543.004]] | Launch Daemon | Use auditing tools capable of detecting folder permissions abuse opportunities on systems, especially reviewing changes made to folders by third-party software. |
| [[Search Open Websites／Domains\|T1593]] | Search Open Websites／Domains | Scan public code repositories for exposed credentials or other sensitive information before making commits. Ensure that any leaked credentials are removed from the commit history, not just the current latest version of the code. |
| [[Data from Information Repositories\|T1213]] | Data from Information Repositories | Consider periodic review of accounts and privileges for critical and sensitive repositories. Ensure that repositories such as cloud-hosted databases are not unintentionally exposed to the public, and that security groups assigned to them permit only necessary and authorized hosts.[^25]  |
| [[Private Keys\|T1552.004]] | Private Keys | Ensure only authorized keys are allowed access to critical resources and audit access lists regularly. |
| [[TFTP Boot\|T1542.005]] | TFTP Boot | Periodically check the integrity of the running configuration and system image to ensure they have not been modified. [^13]  [^19]  [^7]   |
| [[Modify Authentication Process\|T1556]] | Modify Authentication Process | Review authentication logs to ensure that mechanisms such as enforcement of MFA are functioning as intended.<br><br>Periodically review the hybrid identity solution in use for any discrepancies. For example, review all Pass Through Authentication (PTA) agents in the Azure Management Portal to identify any unwanted or unapproved ones.[^12]  If ADFS is in use, review DLLs and executable files in the AD FS and Global Assembly Cache directories to ensure that they are signed by Microsoft. Note that in some cases binaries may be catalog-signed, which may cause the file to appear unsigned when viewing file properties.[^35] <br><br>Periodically review for new and unknown network provider DLLs within the Registry (`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\<NetworkProviderName>\NetworkProvider\ProviderPath`). Ensure only valid network provider DLLs are registered. The name of these can be found in the Registry key at `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\NetworkProvider\Order`, and have corresponding service subkey pointing to a DLL at `HKEY_LOCAL_MACHINE\SYSTEM\CurrentC ontrolSet\Services\<NetworkProviderName>\NetworkProvider`. |
| [[Steal or Forge Kerberos Tickets\|T1558]] | Steal or Forge Kerberos Tickets | Perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses. |
| [[Windows Host Firewall\|T1686.003]] | Windows Host Firewall | Routinely check account role permissions to ensure only expected users and roles have permission to modify system firewalls. |
| [[Implant Internal Image\|T1525]] | Implant Internal Image | Periodically check the integrity of images and containers used in cloud deployments to ensure they have not been modified to include malicious software. |
| [[Databases\|T1213.006]] | Databases | Consider periodic review of accounts and privileges for critical and sensitive databases.  |
| [[vSphere Installation Bundles\|T1505.006]] | vSphere Installation Bundles | Periodically audit ESXi hosts to ensure that only approved VIBs are installed. The command `esxcli software vib list` lists installed VIBs, while the command `esxcli software vib signature verify` verifies the signatures of installed VIBs.[^36]  |
| [[Code Repositories\|T1593.003]] | Code Repositories | Scan public code repositories for exposed credentials or other sensitive information before making commits. Ensure that any leaked credentials are removed from the commit history, not just the current latest version of the code. |


## References

[^1]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^2]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^3]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^4]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^5]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^6]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^7]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^8]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^9]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^10]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^11]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^12]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^13]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^14]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^15]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^16]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^17]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^18]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^19]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^20]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^21]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^22]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^23]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^24]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^25]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^26]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^27]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^28]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^29]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^30]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^31]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^32]: [SpecterOps Certified Pre Owned](https://web.archive.org/web/20220818094600/https://specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^33]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^34]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^35]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^36]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^37]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^38]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^39]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^40]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


