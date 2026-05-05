---
aliases: 
    - M1026
    
mitre-attack: https://attack.mitre.org/mitigations/M1026
---

## M1026

Privileged Account Management focuses on implementing policies, controls, and tools to securely manage privileged accounts (e.g., SYSTEM, root, or administrative accounts). This includes restricting access, limiting the scope of permissions, monitoring privileged account usage, and ensuring accountability through logging and auditing.This mitigation can be implemented through the following measures:<br><br>Account Permissions and Roles:<br><br>- Implement RBAC and least privilege principles to allocate permissions securely.<br>- Use tools like Active Directory Group Policies to enforce access restrictions.<br><br>Credential Security:<br><br>- Deploy password vaulting tools like CyberArk, HashiCorp Vault, or KeePass for secure storage and rotation of credentials.<br>- Enforce password policies for complexity, uniqueness, and expiration using tools like Microsoft Group Policy Objects (GPO).<br><br>Multi-Factor Authentication (MFA):<br><br>- Enforce MFA for all privileged accounts using Duo Security, Okta, or Microsoft Azure AD MFA.<br><br>Privileged Access Management (PAM):<br><br>- Use PAM solutions like CyberArk, BeyondTrust, or Thycotic to manage, monitor, and audit privileged access.<br><br>Auditing and Monitoring:<br><br>- Integrate activity monitoring into your SIEM (e.g., Splunk or QRadar) to detect and alert on anomalous privileged account usage.<br><br>Just-In-Time Access:<br><br>- Deploy JIT solutions like Azure Privileged Identity Management (PIM) or configure ephemeral roles in AWS and GCP to grant time-limited elevated permissions.<br><br>*Tools for Implementation*<br><br>Privileged Access Management (PAM):<br><br>- CyberArk, BeyondTrust, Thycotic, HashiCorp Vault.<br><br>Credential Management:<br><br>- Microsoft LAPS (Local Admin Password Solution), Password Safe, HashiCorp Vault, KeePass.<br><br>Multi-Factor Authentication:<br><br>- Duo Security, Okta, Microsoft Azure MFA, Google Authenticator.<br><br>Linux Privilege Management:<br><br>- sudo configuration, SELinux, AppArmor.<br><br>Just-In-Time Access:<br><br>- Azure Privileged Identity Management (PIM), AWS IAM Roles with session constraints, GCP Identity-Aware Proxy.

### Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | Configure the Increase Scheduling Priority option to only allow the Administrators group the rights to schedule a priority process. This can be configured through GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Increase scheduling priority. [^10]  |
| [[Pass the Ticket\|T1550.003]] | Pass the Ticket | Limit domain admin account permissions to domain controllers and limited servers. Delegate other admin functions to separate accounts.[^5]  |
| [[Cloud Secrets Management Stores\|T1555.006]] | Cloud Secrets Management Stores | Limit the number of cloud accounts and services with permission to query the secrets manager to only those required. Ensure that accounts and services with permissions to query the secrets manager only have access to the secrets they require. |
| [[IIS Components\|T1505.004]] | IIS Components | Do not allow administrator accounts that have permissions to add IIS components to be used for day-to-day operations that may expose these permissions to potential adversaries and/or other unprivileged systems. |
| [[Reversible Encryption\|T1556.005]] | Reversible Encryption | Audit domain and local accounts as well as their permission levels routinely to look for situations that could allow an adversary to gain wide access by obtaining credentials of a privileged account.[^21] [^14]  These audits should also include if default accounts have been enabled, or if new local accounts are created that have not be authorized. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers.[^22]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | Limit the number of accounts and services with permission to query information from password stores to only those required. Ensure that accounts and services with permissions to query password stores only have access to the secrets they require. |
| [[Service Execution\|T1569.002]] | Service Execution | Ensure that permissions disallow services that run at a higher permissions level from being created or interacted with by a user with a lower permission level. |
| [[Transport Agent\|T1505.002]] | Transport Agent | Do not allow administrator accounts that have permissions to add component software on these services to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems.  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | Prevent credential overlap across systems of administrator and privileged accounts. [^11]  |
| [[Credentials in Registry\|T1552.002]] | Credentials in Registry | If it is necessary that software must store credentials in the Registry, then ensure the associated accounts have limited permissions so they cannot be abused if obtained by an adversary. |
| [[Additional Cloud Roles\|T1098.003]] | Additional Cloud Roles | Ensure that all accounts use the least privileges they require. In Azure AD environments, consider using Privileged Identity Management (PIM) to define roles that require two or more approvals before assignment to users.[^3]  |
| [[Windows Permissions\|T1222.001]] | Windows Permissions | Ensure critical system files as well as those known to be abused by adversaries have restrictive permissions and are owned by an appropriately privileged account, especially if access is not required by users nor will inhibit system functionality. |
| [[Pluggable Authentication Modules\|T1556.003]] | Pluggable Authentication Modules | Limit access to the root account and prevent users from modifying PAM components through proper privilege separation (ex SELinux, grsecurity, AppArmor, etc.) and limiting Privilege Escalation opportunities. |
| [[Windows Remote Management\|T1021.006]] | Windows Remote Management | If the service is necessary, lock down critical enclaves with separate WinRM accounts and permissions. |
| [[System Services\|T1569]] | System Services | Ensure that permissions disallow services that run at a higher permissions level from being created or interacted with by a user with a lower permission level. |
| [[Network Boundary Bridging\|T1599]] | Network Boundary Bridging | Restrict administrator accounts to as few individuals as possible, following least privilege principles.  Prevent credential overlap across systems of administrator and privileged accounts, particularly between network and non-network platforms, such as servers or endpoints. |
| [[／etc／passwd and ／etc／shadow\|T1003.008]] | ／etc／passwd and ／etc／shadow | Follow best practices in restricting access to privileged accounts to avoid hostile programs from accessing such sensitive information. |
| [[Software Deployment Tools\|T1072]] | Software Deployment Tools | Grant access to application deployment systems only to a limited number of authorized administrators. |
| [[Create or Modify System Process\|T1543]] | Create or Modify System Process | Manage the creation, modification, use, and permissions associated to privileged accounts, including SYSTEM and root. |
| [[Code Signing Policy Modification\|T1553.006]] | Code Signing Policy Modification | Limit the usage of local administrator and domain administrator accounts to be used for day-to-day operations that may expose them to potential adversaries. |
| [[Domain or Tenant Policy Modification\|T1484]] | Domain or Tenant Policy Modification | Use least privilege and protect administrative access to the Domain Controller and Active Directory Federation Services (AD FS) server. Do not create service accounts with administrative privileges. |
| [[Kernel Modules and Extensions\|T1547.006]] | Kernel Modules and Extensions | Limit access to the root account and prevent users from loading kernel modules and extensions through proper privilege separation and limiting Privilege Escalation opportunities. |
| [[Make and Impersonate Token\|T1134.003]] | Make and Impersonate Token | Limit permissions so that users and user groups cannot create tokens. This setting should be defined for the local system account only. GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Create a token object. [^8]  Also define who can create a process level token to only the local and network service through GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Replace a process level token.[^6] <br><br>Administrators should log in as a standard user but run their tools with administrator privileges using the built-in access token manipulation command `runas`.[^12]  |
| [[System Firmware\|T1542.001]] | System Firmware | Prevent adversary access to privileged accounts or access necessary to perform this technique. |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | Audit domain account permission levels routinely to look for situations that could allow an adversary to gain wide access by obtaining credentials of a privileged account. Do not put user or admin domain accounts in the local administrator groups across systems unless they are tightly controlled and use of accounts is segmented, as this is often equivalent to having a local administrator account with the same password on all systems. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers. Limit credential overlap across systems to prevent access if account credentials are obtained. |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | Use least privilege for service accounts will limit what permissions the exploited process gets on the rest of the system. |
| [[Cloud Accounts\|T1078.004]] | Cloud Accounts | Review privileged cloud account permission levels routinely to look for those that could allow an adversary to gain wide access, such as Global Administrator and Privileged Role Administrator in Azure AD.[^21] [^14] [^28]  These reviews should also check if new privileged cloud accounts have been created that were not authorized. For example, in Azure AD environments configure alerts to notify when accounts have gone many days without using privileged roles, as these roles may be able to be removed.[^9]  Consider using temporary, just-in-time (JIT) privileged access to Azure AD resources rather than permanently assigning privileged roles.[^28]  |
| [[Local Accounts\|T1078.003]] | Local Accounts | Audit local accounts permission levels routinely to look for situations that could allow an adversary to gain wide access by obtaining credentials of a privileged account. [^21]  [^14]  Limit the usage of local administrator accounts to be used for day-to-day operations that may expose them to potential adversaries. <br><br>For example, audit the use of service accounts in Kubernetes, and avoid automatically granting them access to the Kubernetes API if this is not required.[^13]  Implementing LAPS may also help prevent reuse of local administrator credentials across a domain.[^30]  |
| [[Safe Mode Boot\|T1688]] | Safe Mode Boot | Restrict administrator accounts to as few individuals as possible, following least privilege principles, that may be abused to remotely boot a machine in safe mode.[^15]  |
| [[Silver Ticket\|T1558.002]] | Silver Ticket | Limit service accounts to minimal required privileges, including membership in privileged groups such as Domain Administrators.[^18]  |
| [[Build Image on Host\|T1612]] | Build Image on Host | Ensure containers are not running as root by default. In Kubernetes environments, consider defining Pod Security Standards that prevent pods from running privileged containers.[^23]  |
| [[Trust Modification\|T1484.002]] | Trust Modification | Use the principal of least privilege and protect administrative access to domain trusts and identity tenants. |
| [[Additional Email Delegate Permissions\|T1098.002]] | Additional Email Delegate Permissions | Do not allow domain administrator accounts to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems. |
| [[Container CLI／API\|T1059.013]] | Container CLI／API | Restrict permissions on API access. RBAC in Kubernetes involve permissions that are additive, meaning there are no explicit "deny" rules. These permissions can be defined within a particular namespace or within cluster-scoped resources. Securing the Docker daemon can be done by using SSH or TLS with certificate authorization. Container management tools such as Docker and Podman may offer ways to run containers as rootless, which prevents them from running with privileged permissions. |
| [[NTDS\|T1003.003]] | NTDS | Do not put user or admin domain accounts in the local administrator groups across systems unless they are tightly controlled, as this is often equivalent to having a local administrator account with the same password on all systems. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers. |
| [[Linux and Mac Permissions\|T1222.002]] | Linux and Mac Permissions | Ensure critical system files as well as those known to be abused by adversaries have restrictive permissions and are owned by an appropriately privileged account, especially if access is not required by users nor will inhibit system functionality. |
| [[TFTP Boot\|T1542.005]] | TFTP Boot | Use of Authentication, Authorization, and Accounting (AAA) systems will limit actions administrators can perform and provide a history of user actions to detect unauthorized use and abuse. TACACS+ can keep control over which commands administrators are permitted to use through the configuration of authentication and command authorization. [^29]  [^19]  |
| [[Create Process with Token\|T1134.002]] | Create Process with Token | Limit permissions so that users and user groups cannot create tokens. This setting should be defined for the local system account only. GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Create a token object. [^8]  Also define who can create a process level token to only the local and network service through GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Replace a process level token.[^6] <br><br>Administrators should log in as a standard user but run their tools with administrator privileges using the built-in access token manipulation command `runas`.[^12]  |
| [[Forge Web Credentials\|T1606]] | Forge Web Credentials | Restrict permissions and access to the AD FS server to only originate from privileged access workstations.[^2]  |
| [[Component Object Model\|T1559.001]] | Component Object Model | Modify Registry settings (directly or using Dcomcnfg.exe) in `HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\AppID\\{AppID_GUID}` associated with the process-wide security of individual COM applications.[^7] <br><br>Modify Registry settings (directly or using Dcomcnfg.exe) in `HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Ole` associated with system-wide security defaults for all COM applications that do no set their own process-wide security.[^16]  [^25]  |
| [[Escape to Host\|T1611]] | Escape to Host | Ensure containers are not running as root by default and do not use unnecessary privileges or mounted components. In Kubernetes environments, consider defining Pod Security Standards that prevent pods from running privileged containers.[^23]  |
| [[Cloud Account\|T1136.003]] | Cloud Account | Limit the number of accounts with permissions to create other accounts. Do not allow privileged accounts to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems. |
| [[System Binary Proxy Execution\|T1218]] | System Binary Proxy Execution | Restrict execution of particularly vulnerable binaries to privileged accounts or groups that need to use it to lessen the opportunities for malicious usage. |
| [[Use Alternate Authentication Material\|T1550]] | Use Alternate Authentication Material | Limit credential overlap across systems to prevent the damage of credential compromise and reduce the adversary's ability to perform Lateral Movement between systems. |
| [[Container Orchestration Job\|T1053.007]] | Container Orchestration Job | Ensure containers are not running as root by default. In Kubernetes environments, consider defining Pod Security Standards that prevent pods from running privileged containers.[^23]  |
| [[Subvert Trust Controls\|T1553]] | Subvert Trust Controls | Manage the creation, modification, use, and permissions associated to privileged accounts, including SYSTEM and root. |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | Do not put user or admin domain accounts in the local administrator groups across systems unless they are tightly controlled, as this is often equivalent to having a local administrator account with the same password on all systems. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers. |
| [[Process Injection\|T1055]] | Process Injection | Utilize Yama (ex: /proc/sys/kernel/yama/ptrace_scope) to mitigate ptrace based process injection by restricting the use of ptrace to privileged users only. Other mitigation controls involve the deployment of security kernel modules that provide advanced access control and process restrictions such as SELinux, grsecurity, and AppArmor. |
| [[Abuse Elevation Control Mechanism\|T1548]] | Abuse Elevation Control Mechanism | Remove users from the local administrator group on systems.<br><br>By requiring a password, even if an adversary can get terminal access, they must know the password to run anything in the sudoers file. Setting the timestamp_timeout to 0 will require the user to input their password every time sudo is executed. |
| [[Domain Controller Authentication\|T1556.001]] | Domain Controller Authentication | Audit domain and local accounts as well as their permission levels routinely to look for situations that could allow an adversary to gain wide access by obtaining credentials of a privileged account. [^21]  [^14]  These audits should also include if default accounts have been enabled, or if new local accounts are created that have not be authorized. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers. [^22]  |
| [[Container API\|T1552.007]] | Container API | Use the principle of least privilege for privileged accounts such as the service account in Kubernetes. For example, if a pod is not required to access the Kubernetes API, consider disabling the service account altogether.[^13]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | Audit domain and local accounts as well as their permission levels routinely to look for situations that could allow an adversary to gain wide access by obtaining credentials of a privileged account. [^21]  [^14]  These audits should also include if default accounts have been enabled, or if new local accounts are created that have not been authorized. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers. [^22]  |
| [[Additional Cloud Credentials\|T1098.001]] | Additional Cloud Credentials | Do not allow domain administrator or root accounts to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems. |
| [[Implant Internal Image\|T1525]] | Implant Internal Image | Limit permissions associated with creating and modifying platform images or containers based on the principle of least privilege. |
| [[Scheduled Task／Job\|T1053]] | Scheduled Task／Job | Configure the Increase Scheduling Priority option to only allow the Administrators group the rights to schedule a priority process. This can be can be configured through GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Increase scheduling priority. [^10]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | Remove users from the local administrator group on systems. |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | Deny remote use of local admin credentials to log into systems. Do not allow domain user accounts to be in the local Administrators group multiple systems. |
| [[TCC Manipulation\|T1548.006]] | TCC Manipulation | Remove unnecessary users from the local administrator group on systems. |
| [[Bootkit\|T1542.003]] | Bootkit | Ensure proper permissions are in place to help prevent adversary access to privileged accounts necessary to install a bootkit. |
| [[File and Directory Permissions Modification\|T1222]] | File and Directory Permissions Modification | Ensure critical system files as well as those known to be abused by adversaries have restrictive permissions and are owned by an appropriately privileged account, especially if access is not required by users nor will inhibit system functionality. |
| [[Container Administration Command\|T1609]] | Container Administration Command | Ensure containers are not running as root by default. In Kubernetes environments, consider defining Pod Security Standards that prevent pods from running privileged containers and using the `NodeRestriction` admission controller to deny the kublet access to nodes and pods outside of the node it belongs to.[^23]  [^20]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | Minimize permissions and access for service accounts to limit impact of exploitation. |
| [[Account Manipulation\|T1098]] | Account Manipulation | Do not allow domain administrator accounts to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems. |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | Windows:<br>Do not put user or admin domain accounts in the local administrator groups across systems unless they are tightly controlled, as this is often equivalent to having a local administrator account with the same password on all systems. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers.[^22] <br><br>Linux:<br>Scraping the passwords from memory requires root privileges. Follow best practices in restricting access to privileged accounts to avoid hostile programs from accessing such sensitive regions of memory. |
| [[Event Triggered Execution\|T1546]] | Event Triggered Execution | Manage the creation, modification, use, and permissions associated to privileged accounts, including SYSTEM and root. |
| [[Patch System Image\|T1601.001]] | Patch System Image | Restrict administrator accounts to as few individuals as possible, following least privilege principles.  Prevent credential overlap across systems of administrator and privileged accounts, particularly between network and non-network platforms, such as servers or endpoints. |
| [[Golden Ticket\|T1558.001]] | Golden Ticket | Limit domain admin account permissions to domain controllers and limited servers. Delegate other admin functions to separate accounts. |
| [[Hybrid Identity\|T1556.007]] | Hybrid Identity | Limit on-premises accounts with access to the hybrid identity solution in place. For example, limit Entra ID Global Administrator accounts to only those required, and ensure that these are dedicated cloud-only accounts rather than hybrid ones.[^24]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | Prevent credential overlap across systems of administrator and privileged accounts.[^11]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | Do not put user or admin domain accounts in the local administrator groups across systems unless they are tightly controlled, as this is often equivalent to having a local administrator account with the same password on all systems. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers. |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | When PowerShell is necessary, consider restricting PowerShell execution policy to administrators. Be aware that there are methods of bypassing the PowerShell execution policy, depending on environment configuration.[^17] <br><br>PowerShell JEA (Just Enough Administration) may also be used to sandbox administration and limit what commands admins/users can execute through remote PowerShell sessions.[^26]  |
| [[Web Portal Capture\|T1056.003]] | Web Portal Capture | Do not allow administrator accounts that have permissions to modify the Web content of organization login portals to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems. |
| [[Pass the Hash\|T1550.002]] | Pass the Hash | Limit credential overlap across systems to prevent the damage of credential compromise and reduce the adversary's ability to perform Lateral Movement between systems. |
| [[Downgrade System Image\|T1601.002]] | Downgrade System Image | Restrict administrator accounts to as few individuals as possible, following least privilege principles.  Prevent credential overlap across systems of administrator and privileged accounts, particularly between network and non-network platforms, such as servers or endpoints. |
| [[Pre-OS Boot\|T1542]] | Pre-OS Boot | Ensure proper permissions are in place to help prevent adversary access to privileged accounts necessary to perform these actions |
| [[Create Account\|T1136]] | Create Account | Limit the number of accounts with permissions to create other accounts. Do not allow domain administrator accounts to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems. |
| [[Firmware Corruption\|T1495]] | Firmware Corruption | Prevent adversary access to privileged accounts or access necessary to replace system firmware. |
| [[SAML Tokens\|T1606.002]] | SAML Tokens | Restrict permissions and access to the AD FS server to only originate from privileged access workstations.[^2]  |
| [[RDP Hijacking\|T1563.002]] | RDP Hijacking | Consider removing the local Administrators group from the list of groups allowed to log in through RDP. |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | Limit permissions so that users and user groups cannot create tokens. This setting should be defined for the local system account only. GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Create a token object. [^8]  Also define who can create a process level token to only the local and network service through GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Replace a process level token.[^6] <br><br>Administrators should log in as a standard user but run their tools with administrator privileges using the built-in access token manipulation command `runas`.[^12]  |
| [[Systemd Service\|T1543.002]] | Systemd Service | The creation and modification of systemd service unit files is generally reserved for administrators such as the Linux root user and other users with superuser privileges.  |
| [[Local Account\|T1136.001]] | Local Account | Limit the number of accounts permitted to create other accounts. Limit the usage of local administrator accounts to be used for day-to-day operations that may expose them to potential adversaries. |
| [[Cached Domain Credentials\|T1003.005]] | Cached Domain Credentials | Do not put user or admin domain accounts in the local administrator groups across systems unless they are tightly controlled, as this is often equivalent to having a local administrator account with the same password on all systems. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers. |
| [[Network Device Authentication\|T1556.004]] | Network Device Authentication | Restrict administrator accounts to as few individuals as possible, following least privilege principles.  Prevent credential overlap across systems of administrator and privileged accounts, particularly between network and non-network platforms, such as servers or endpoints. |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers.[^27]  |
| [[Cloud API\|T1059.009]] | Cloud API | Use of proper Identity and Access Management (IAM) with Role Based Access Control (RBAC) policies to limit actions administrators can perform and provide a history of administrative actions to detect unauthorized use and abuse. |
| [[Inter-Process Communication\|T1559]] | Inter-Process Communication | Modify Registry settings (directly or using Dcomcnfg.exe) in `HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\AppID\\{AppID_GUID}` associated with the process-wide security of individual COM applications.[^7] <br><br>Modify Registry settings (directly or using Dcomcnfg.exe) in `HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Ole` associated with system-wide security defaults for all COM applications that do no set their own process-wide security.[^16]  [^25]  |
| [[SQL Stored Procedures\|T1505.001]] | SQL Stored Procedures | Do not allow administrator accounts that have permissions to add component software on these services to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems.  |
| [[Ptrace System Calls\|T1055.008]] | Ptrace System Calls | Utilize Yama (ex: /proc/sys/kernel/yama/ptrace_scope) to mitigate ptrace based process injection by restricting the use of ptrace to privileged users only. Other mitigation controls involve the deployment of security kernel modules that provide advanced access control and process restrictions such as SELinux, grsecurity, and AppArmor.  |
| [[Network Address Translation Traversal\|T1599.001]] | Network Address Translation Traversal | Restrict administrator accounts to as few individuals as possible, following least privilege principles.  Prevent credential overlap across systems of administrator and privileged accounts, particularly between network and non-network platforms, such as servers or endpoints. |
| [[Proc Filesystem\|T1003.007]] | Proc Filesystem | Follow best practices in restricting access to privileged accounts to avoid hostile programs from accessing sensitive information. |
| [[Token Impersonation／Theft\|T1134.001]] | Token Impersonation／Theft | Limit permissions so that users and user groups cannot create tokens. This setting should be defined for the local system account only. GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Create a token object. [^8]  Also define who can create a process level token to only the local and network service through GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Replace a process level token.[^6] <br><br>Administrators should log in as a standard user but run their tools with administrator privileges using the built-in access token manipulation command `runas`.[^12]  |
| [[DCSync\|T1003.006]] | DCSync | Do not put user or admin domain accounts in the local administrator groups across systems unless they are tightly controlled, as this is often equivalent to having a local administrator account with the same password on all systems. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers. |
| [[Modify Authentication Process\|T1556]] | Modify Authentication Process | Audit domain and local accounts as well as their permission levels routinely to look for situations that could allow an adversary to gain wide access by obtaining credentials of a privileged account. [^21]  [^14]  These audits should also include if default accounts have been enabled, or if new local accounts are created that have not be authorized. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers. [^22] <br><br>Limit access to the root account and prevent users from modifying protected components through proper privilege separation (ex SELinux, grsecurity, AppArmor, etc.) and limiting Privilege Escalation opportunities.<br><br>Limit on-premises accounts with access to the hybrid identity solution in place. For example, limit Azure AD Global Administrator accounts to only those required, and ensure that these are dedicated cloud-only accounts rather than hybrid ones.[^24]  |
| [[Cloud Services\|T1021.007]] | Cloud Services | Limit the number of high-privileged domain and cloud accounts, and ensure that these are not used for day-to-day operations. Ensure that on-premises accounts do not have privileged cloud permissions and that isolated, cloud-only accounts are used for managing cloud environments.[^1]  |
| [[Modify System Image\|T1601]] | Modify System Image | Restrict administrator accounts to as few individuals as possible, following least privilege principles.  Prevent credential overlap across systems of administrator and privileged accounts, particularly between network and non-network platforms, such as servers or endpoints. |
| [[At\|T1053.002]] | At | Configure the Increase Scheduling Priority option to only allow the Administrators group the rights to schedule a priority process. This can be configured through GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Increase scheduling priority. [^10]  |
| [[Unsecured Credentials\|T1552]] | Unsecured Credentials | If it is necessary that software must store credentials in the Registry, then ensure the associated accounts have limited permissions so they cannot be abused if obtained by an adversary. |
| [[Remote Service Session Hijacking\|T1563]] | Remote Service Session Hijacking | Do not allow remote access to services as a privileged account unless necessary. |
| [[SSH Hijacking\|T1563.001]] | SSH Hijacking | Do not allow remote access via SSH as root or other privileged accounts. |
| [[PowerShell\|T1059.001]] | PowerShell | When PowerShell is necessary, consider restricting PowerShell execution policy to administrators. Be aware that there are methods of bypassing the PowerShell execution policy, depending on environment configuration.[^17] <br><br>PowerShell JEA (Just Enough Administration) may also be used to sandbox administration and limit what commands admins/users can execute through remote PowerShell sessions.[^26]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | Consider removing the local Administrators group from the list of groups allowed to log in through RDP. |
| [[Systemd Timers\|T1053.006]] | Systemd Timers | Limit access to the root account and prevent users from creating and/or modifying systemd timer unit files.  |
| [[Domain Account\|T1136.002]] | Domain Account | Limit the number of accounts with permissions to create other accounts. Do not allow domain administrator accounts to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems. |
| [[Distributed Component Object Model\|T1021.003]] | Distributed Component Object Model | Modify Registry settings (directly or using Dcomcnfg.exe) in `HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID\{{AppID_GUID}}` associated with the process-wide security of individual COM applications.[^7] <br><br>Modify Registry settings (directly or using Dcomcnfg.exe) in `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole` associated with system-wide security defaults for all COM applications that do not set their own process-wide security.[^16]  [^25]  |
| [[Network Device CLI\|T1059.008]] | Network Device CLI | Use of Authentication, Authorization, and Accounting (AAA) systems will limit actions administrators can perform and provide a history of user actions to detect unauthorized use and abuse. TACACS+ can keep control over which commands administrators are permitted to use through the configuration of authentication and command authorization[^29]  [^19]  |
| [[Msiexec\|T1218.007]] | Msiexec | Restrict execution of Msiexec.exe to privileged accounts or groups that need to use it to lessen the opportunities for malicious usage. |
| [[Server Software Component\|T1505]] | Server Software Component | Do not allow administrator accounts that have permissions to add component software on these services to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems. |
| [[Sudo and Sudo Caching\|T1548.003]] | Sudo and Sudo Caching | By requiring a password, even if an adversary can get terminal access, they must know the password to run anything in the sudoers file. Setting the `timestamp_timeout` to 0 will require the user to input their password every time `sudo` is executed. |
| [[Cloud Administration Command\|T1651]] | Cloud Administration Command | Limit the number of cloud accounts with permissions to remotely execute commands on virtual machines, and ensure that these are not used for day-to-day operations. In Azure, limit the number of accounts with the roles Azure Virtual Machine Contributer and above, and consider using temporary Just-in-Time (JIT) roles to avoid permanently assigning privileged access to virtual machines.[^4]   |
| [[Kerberoasting\|T1558.003]] | Kerberoasting | Limit service accounts to minimal required privileges, including membership in privileged groups such as Domain Administrators.[^18]  |
| [[Steal or Forge Kerberos Tickets\|T1558]] | Steal or Forge Kerberos Tickets | Limit domain admin account permissions to domain controllers and limited servers. Delegate other admin functions to separate accounts.<br><br>Limit service accounts to minimal required privileges, including membership in privileged groups such as Domain Administrators.[^18]  |


## References

[^1]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^2]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^3]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^4]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^5]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^6]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^7]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^8]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^9]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^10]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^11]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^12]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^13]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^14]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^15]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^16]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^17]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^18]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^19]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^20]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^21]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^22]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^23]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^24]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^25]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^26]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^27]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^28]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^29]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^30]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


