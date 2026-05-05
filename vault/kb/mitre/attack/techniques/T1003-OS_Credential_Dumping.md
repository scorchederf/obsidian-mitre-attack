---
aliases: 
    - T1003
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/credential_access
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1003-OS_Credential_Dumping
tactic: 
     - Credential Access
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may attempt to dump credentials to obtain account login and credential material, normally in the form of a hash or a clear text password. Credentials can be obtained from OS caches, memory, or structures.[^10]  Credentials can then be used to perform [[kb/mitre/attack/tactics/TA0008-Lateral_Movement\|Lateral Movement]] and access restricted information.<br><br>Several of the tools mentioned in associated sub-techniques may be used by both adversaries and professional security testers. Additional custom tools likely exist as well.<br>




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1015-Active_Directory_Configuration\|M1015]] | Active Directory Configuration | <br>Manage the access control list for “Replicating Directory Changes All” and other permissions associated with domain controller replication. [^9]  [^7]  Consider adding users to the "Protected Users" Active Directory security group. This can help limit the caching of users' plaintext credentials.[^13]  |
| [[kb/mitre/attack/mitigations/M1017-User_Training\|M1017]] | User Training | Limit credential overlap across accounts and systems by training users and administrators not to use the same password for multiple accounts. |
| [[kb/mitre/attack/mitigations/M1025-Privileged_Process_Integrity\|M1025]] | Privileged Process Integrity | <br>On Windows 8.1 and Windows Server 2012 R2, enable Protected Process Light for LSA.[^11]  |
| [[kb/mitre/attack/mitigations/M1026-Privileged_Account_Management\|M1026]] | Privileged Account Management | Windows:<br>Do not put user or admin domain accounts in the local administrator groups across systems unless they are tightly controlled, as this is often equivalent to having a local administrator account with the same password on all systems. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers.[^2] <br><br>Linux:<br>Scraping the passwords from memory requires root privileges. Follow best practices in restricting access to privileged accounts to avoid hostile programs from accessing such sensitive regions of memory. |
| [[kb/mitre/attack/mitigations/M1027-Password_Policies\|M1027]] | Password Policies | Ensure that local administrator accounts have complex, unique passwords across all systems on the network. |
| [[kb/mitre/attack/mitigations/M1028-Operating_System_Configuration\|M1028]] | Operating System Configuration | <br>Consider disabling or restricting NTLM.[^18]  Consider disabling WDigest authentication.[^14]  |
| [[kb/mitre/attack/mitigations/M1040-Behavior_Prevention_on_Endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to secure LSASS and prevent credential stealing. [^1]  |
| [[kb/mitre/attack/mitigations/M1041-Encrypt_Sensitive_Information\|M1041]] | Encrypt Sensitive Information | Ensure Domain Controller backups are properly secured. |
| [[kb/mitre/attack/mitigations/M1043-Credential_Access_Protection\|M1043]] | Credential Access Protection | With Windows 10, Microsoft implemented new protections called Credential Guard to protect the LSA secrets that can be used to obtain credentials through forms of credential dumping. It is not configured by default and has hardware and firmware system requirements. [^3]  It also does not protect against all forms of credential dumping. [^19]  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1003.001-LSASS_Memory\|T1003.001]] | LSASS Memory |
| [[kb/mitre/attack/techniques/T1003.002-Security_Account_Manager\|T1003.002]] | Security Account Manager |
| [[kb/mitre/attack/techniques/T1003.003-NTDS\|T1003.003]] | NTDS |
| [[kb/mitre/attack/techniques/T1003.004-LSA_Secrets\|T1003.004]] | LSA Secrets |
| [[kb/mitre/attack/techniques/T1003.005-Cached_Domain_Credentials\|T1003.005]] | Cached Domain Credentials |
| [[kb/mitre/attack/techniques/T1003.006-DCSync\|T1003.006]] | DCSync |
| [[kb/mitre/attack/techniques/T1003.007-Proc_Filesystem\|T1003.007]] | Proc Filesystem |
| [[kb/mitre/attack/techniques/T1003.008-etc_passwd_and_etc_shadow\|T1003.008]] | ／etc／passwd and ／etc／shadow |




> [!info]- References
> [^1]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)

> [^2]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)

> [^3]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)

> [^4]: [Microsoft GetNCCChanges](https://msdn.microsoft.com/library/dd207691.aspx)

> [^5]: [Microsoft DRSR Dec 2017](https://msdn.microsoft.com/library/cc228086.aspx)

> [^6]: [Powersploit](https://github.com/mattifestation/PowerSploit)

> [^7]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)

> [^8]: [Microsoft SAMR](https://msdn.microsoft.com/library/cc245496.aspx)

> [^9]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)

> [^10]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)

> [^11]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)

> [^12]: [Medium Detecting Attempts to Steal Passwords from Memory](https://medium.com/threatpunter/detecting-attempts-to-steal-passwords-from-memory-558f16dce4ea)

> [^13]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)

> [^14]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)

> [^15]: [Microsoft NRPC Dec 2017](https://msdn.microsoft.com/library/cc237008.aspx)

> [^16]: [Samba DRSUAPI](https://wiki.samba.org/index.php/DRSUAPI)

> [^17]: [Harmj0y DCSync Sept 2015](http://www.harmj0y.net/blog/redteaming/mimikatz-and-dcsync-and-extrasids-oh-my/)

> [^18]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)

> [^19]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


