---
aliases: 
    - T1556
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/credential_access
    - attack/tactic/defense_impairment
    - attack/tactic/persistence
    - attack/type/technique
    - platform/iaas
    - platform/identity_provider
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1556-Modify_Authentication_Process
tactic: 
     - Defense Impairment - Persistence - Credential Access
platforms:
     - IaaS - Identity Provider - Linux - macOS - Network Devices - Office Suite - SaaS - Windows
permissions required:
     - none
---

## Description

Adversaries may modify authentication mechanisms and processes to access user credentials or enable otherwise unwarranted access to accounts. The authentication process is handled by mechanisms, such as the Local Security Authentication Server (LSASS) process and the Security Accounts Manager (SAM) on Windows, pluggable authentication modules (PAM) on Unix-based systems, and authorization plugins on MacOS systems, responsible for gathering, storing, and validating credentials. By modifying an authentication process, an adversary may be able to authenticate to a service or system without using [[kb/mitre/attack/techniques/T1078-Valid_Accounts\|Valid Accounts]].<br><br>Adversaries may maliciously modify a part of this process to either reveal credentials or bypass authentication mechanisms. Compromised credentials or access may be used to bypass access controls placed on various resources on systems within the network and may even be used for persistent access to remote systems and externally available services, such as VPNs, Outlook Web Access and remote desktop.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can create a backdoor in KeePass using a malicious config file and in TortoiseSVN using a registry hook.[^6]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Ensure that proper policies are implemented to dictate the the secure enrollment and deactivation of authentication mechanisms, such as MFA, for user accounts. |
| [[kb/mitre/attack/mitigations/M1022-Restrict_File_and_Directory_Permissions\|M1022]] | Restrict File and Directory Permissions | Restrict write access to the `/Library/Security/SecurityAgentPlugins` directory. |
| [[kb/mitre/attack/mitigations/M1024-Restrict_Registry_Permissions\|M1024]] | Restrict Registry Permissions | Restrict Registry permissions to disallow the modification of sensitive Registry keys such as `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\NetworkProvider\Order`. |
| [[kb/mitre/attack/mitigations/M1025-Privileged_Process_Integrity\|M1025]] | Privileged Process Integrity | Enabled features, such as Protected Process Light (PPL), for LSA.[^3]  |
| [[kb/mitre/attack/mitigations/M1026-Privileged_Account_Management\|M1026]] | Privileged Account Management | Audit domain and local accounts as well as their permission levels routinely to look for situations that could allow an adversary to gain wide access by obtaining credentials of a privileged account. [^9]  [^4]  These audits should also include if default accounts have been enabled, or if new local accounts are created that have not be authorized. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers. [^7] <br><br>Limit access to the root account and prevent users from modifying protected components through proper privilege separation (ex SELinux, grsecurity, AppArmor, etc.) and limiting Privilege Escalation opportunities.<br><br>Limit on-premises accounts with access to the hybrid identity solution in place. For example, limit Azure AD Global Administrator accounts to only those required, and ensure that these are dedicated cloud-only accounts rather than hybrid ones.[^8]  |
| [[kb/mitre/attack/mitigations/M1027-Password_Policies\|M1027]] | Password Policies | Ensure that `AllowReversiblePasswordEncryption` property is set to disabled unless there are application requirements.[^2]  |
| [[kb/mitre/attack/mitigations/M1028-Operating_System_Configuration\|M1028]] | Operating System Configuration | Ensure only valid password filters are registered. Filter DLLs must be present in Windows installation directory (`C:\Windows\System32\` by default) of a domain controller and/or local computer with a corresponding entry in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Notification Packages`. <br><br>Starting in Windows 11 22H2, the `EnableMPRNotifications` policy can be disabled through Group Policy or through a configuration service provider to prevent Winlogon from sending credentials to network providers.[^5]  |
| [[kb/mitre/attack/mitigations/M1032-Multi-factor_Authentication\|M1032]] | Multi-factor Authentication | Integrating multi-factor authentication (MFA) as part of organizational policy can greatly reduce the risk of an adversary gaining control of valid credentials that may be used for additional tactics such as initial access, lateral movement, and collecting information. MFA can also be used to restrict access to cloud resources and APIs.  |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Review authentication logs to ensure that mechanisms such as enforcement of MFA are functioning as intended.<br><br>Periodically review the hybrid identity solution in use for any discrepancies. For example, review all Pass Through Authentication (PTA) agents in the Azure Management Portal to identify any unwanted or unapproved ones.[^1]  If ADFS is in use, review DLLs and executable files in the AD FS and Global Assembly Cache directories to ensure that they are signed by Microsoft. Note that in some cases binaries may be catalog-signed, which may cause the file to appear unsigned when viewing file properties.[^8] <br><br>Periodically review for new and unknown network provider DLLs within the Registry (`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\<NetworkProviderName>\NetworkProvider\ProviderPath`). Ensure only valid network provider DLLs are registered. The name of these can be found in the Registry key at `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\NetworkProvider\Order`, and have corresponding service subkey pointing to a DLL at `HKEY_LOCAL_MACHINE\SYSTEM\CurrentC ontrolSet\Services\<NetworkProviderName>\NetworkProvider`. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1556.001-Domain_Controller_Authentication\|T1556.001]] | Domain Controller Authentication |
| [[kb/mitre/attack/techniques/T1556.002-Password_Filter_DLL\|T1556.002]] | Password Filter DLL |
| [[kb/mitre/attack/techniques/T1556.003-Pluggable_Authentication_Modules\|T1556.003]] | Pluggable Authentication Modules |
| [[kb/mitre/attack/techniques/T1556.004-Network_Device_Authentication\|T1556.004]] | Network Device Authentication |
| [[kb/mitre/attack/techniques/T1556.005-Reversible_Encryption\|T1556.005]] | Reversible Encryption |
| [[kb/mitre/attack/techniques/T1556.006-Multi-Factor_Authentication\|T1556.006]] | Multi-Factor Authentication |
| [[kb/mitre/attack/techniques/T1556.007-Hybrid_Identity\|T1556.007]] | Hybrid Identity |
| [[kb/mitre/attack/techniques/T1556.008-Network_Provider_DLL\|T1556.008]] | Network Provider DLL |
| [[kb/mitre/attack/techniques/T1556.009-Conditional_Access_Policies\|T1556.009]] | Conditional Access Policies |




> [!info]- References
> [^1]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)

> [^2]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)

> [^3]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)

> [^4]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)

> [^5]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)

> [^6]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^7]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)

> [^8]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)

> [^9]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


