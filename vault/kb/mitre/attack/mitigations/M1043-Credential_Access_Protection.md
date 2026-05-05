---
aliases: 
    - M1043
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/type/mitigation
    
mitre-attack: kb/mitre/attack/mitigations/M1043-Credential_Access_Protection
---

## Description

Credential Access Protection focuses on implementing measures to prevent adversaries from obtaining credentials, such as passwords, hashes, tokens, or keys, that could be used for unauthorized access. This involves restricting access to credential storage mechanisms, hardening configurations to block credential dumping methods, and using monitoring tools to detect suspicious credential-related activity. This mitigation can be implemented through the following measures:<br><br>Restrict Access to Credential Storage:<br><br>- Use Case: Prevent adversaries from accessing the SAM (Security Account Manager) database on Windows systems.<br>- Implementation: Enforce least privilege principles and restrict administrative access to credential stores such as `C:\Windows\System32\config\SAM`.<br><br>Use Credential Guard:<br><br>- Use Case: Isolate LSASS (Local Security Authority Subsystem Service) memory to prevent credential dumping.<br>- Implementation: Enable Windows Defender Credential Guard on enterprise endpoints to isolate secrets and protect them from unauthorized access.<br><br>Monitor for Credential Dumping Tools:<br><br>- Use Case: Detect and block known tools like Mimikatz or Windows Credential Editor.<br>- Implementation: Flag suspicious process behavior related to credential dumping.<br><br>Disable Cached Credentials:<br><br>- Use Case: Prevent adversaries from exploiting cached credentials on endpoints.<br>- Implementation: Configure group policy to reduce or eliminate the use of cached credentials (e.g., set Interactive logon: Number of previous logons to cache to 0).<br><br>Enable Secure Boot and Memory Protections:<br><br>- Use Case: Prevent memory-based attacks used to extract credentials.<br>- Implementation: Configure Secure Boot and enforce hardware-based security features like DEP (Data Execution Prevention) and ASLR (Address Space Layout Randomization).

## Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003-OS_Credential_Dumping\|T1003]] | OS Credential Dumping | With Windows 10, Microsoft implemented new protections called Credential Guard to protect the LSA secrets that can be used to obtain credentials through forms of credential dumping. It is not configured by default and has hardware and firmware system requirements. [^7]  It also does not protect against all forms of credential dumping. [^5]  |
| [[kb/mitre/attack/techniques/T1003.001-LSASS_Memory\|T1003.001]] | LSASS Memory | With Windows 10, Microsoft implemented new protections called Credential Guard to protect the LSA secrets that can be used to obtain credentials through forms of credential dumping. It is not configured by default and has hardware and firmware system requirements. It also does not protect against all forms of credential dumping.[^7] [^5]  |
| [[kb/mitre/attack/techniques/T1547.008-LSASS_Driver\|T1547.008]] | LSASS Driver | On Windows 10 and Server 2016, enable Windows Defender Credential Guard [^2]  to run lsass.exe in an isolated virtualized environment without any device drivers. [^3]  |
| [[kb/mitre/attack/techniques/T1558-Steal_or_Forge_Kerberos_Tickets\|T1558]] | Steal or Forge Kerberos Tickets | On Linux systems, protect resources with Security Enhanced Linux (SELinux) by defining entry points, process types, and file labels.[^1]   |
| [[kb/mitre/attack/techniques/T1558.005-Ccache_Files\|T1558.005]] | Ccache Files | Protect resources with Security Enhanced Linux (SELinux) by defining entry points, process types, and file labels.[^1]   |
| [[kb/mitre/attack/techniques/T1599-Network_Boundary_Bridging\|T1599]] | Network Boundary Bridging | Some embedded network devices are capable of storing passwords for local accounts in either plain-text or encrypted formats.  Ensure that, where available, local passwords are always encrypted, per vendor recommendations.[^4]  |
| [[kb/mitre/attack/techniques/T1599.001-Network_Address_Translation_Traversal\|T1599.001]] | Network Address Translation Traversal | Some embedded network devices are capable of storing passwords for local accounts in either plain-text or encrypted formats.  Ensure that, where available, local passwords are always encrypted, per vendor recommendations. [^4]  |
| [[kb/mitre/attack/techniques/T1601-Modify_System_Image\|T1601]] | Modify System Image | Some embedded network devices are capable of storing passwords for local accounts in either plain-text or encrypted formats.  Ensure that, where available, local passwords are always encrypted, per vendor recommendations. [^6]  |
| [[kb/mitre/attack/techniques/T1601.001-Patch_System_Image\|T1601.001]] | Patch System Image | Some embedded network devices are capable of storing passwords for local accounts in either plain-text or encrypted formats.  Ensure that, where available, local passwords are always encrypted, per vendor recommendations. [^6]  |
| [[kb/mitre/attack/techniques/T1601.002-Downgrade_System_Image\|T1601.002]] | Downgrade System Image | Some embedded network devices are capable of storing passwords for local accounts in either plain-text or encrypted formats.  Ensure that, where available, local passwords are always encrypted, per vendor recommendations. [^6]  |



> [!info]- References
> [^1]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)

> [^2]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)

> [^3]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)

> [^4]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)

> [^5]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)

> [^6]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)

> [^7]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


