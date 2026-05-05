---
aliases: 
    - T1555
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/credential_access
    - attack/type/technique
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1555-Credentials_from_Password_Stores
tactic: 
     - Credential Access
platforms:
     - IaaS - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may search for common password storage locations to obtain user credentials.[^10]  Passwords are stored in several places on a system, depending on the operating system or application holding the credentials. There are also specific applications and services that store passwords to make them easier for users to manage and maintain, such as password managers and cloud secrets vaults. Once credentials are obtained, they can be used to perform lateral movement and access restricted information.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0002-Mimikatz\|S0002]] | Mimikatz | [[kb/mitre/attack/software/S0002-Mimikatz\|Mimikatz]] performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from the credential vault and DPAPI.[^4] [^1] [^8] [^5] [^9] 	 |
| [[kb/mitre/attack/software/S0192-Pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can use Lazagne for harvesting credentials.[^11]  |
| [[kb/mitre/attack/software/S0262-QuasarRAT\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can obtain passwords from common FTP clients.[^6] [^3]  |
| [[kb/mitre/attack/software/S0349-LaZagne\|S0349]] | LaZagne | [[kb/mitre/attack/software/S0349-LaZagne\|LaZagne]] can obtain credentials from databases, mail, and WiFi across multiple platforms.[^2]  |
| [[kb/mitre/attack/software/S0378-PoshC2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] can decrypt passwords stored in the RDCMan configuration file.[^7]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1026-Privileged_Account_Management\|M1026]] | Privileged Account Management | Limit the number of accounts and services with permission to query information from password stores to only those required. Ensure that accounts and services with permissions to query password stores only have access to the secrets they require. |
| [[kb/mitre/attack/mitigations/M1027-Password_Policies\|M1027]] | Password Policies | The password for the user's login keychain can be changed from the user's login password. This increases the complexity for an adversary because they need to know an additional password.<br><br>Organizations may consider weighing the risk of storing credentials in password stores and web browsers. If system, software, or web browser credential disclosure is a significant concern, technical controls, policy, and user training may be used to prevent storage of credentials in improper locations. |
| [[kb/mitre/attack/mitigations/M1051-Update_Software\|M1051]] | Update Software | Perform regular software updates to mitigate exploitation risk. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1555.001-Keychain\|T1555.001]] | Keychain |
| [[kb/mitre/attack/techniques/T1555.002-Securityd_Memory\|T1555.002]] | Securityd Memory |
| [[kb/mitre/attack/techniques/T1555.003-Credentials_from_Web_Browsers\|T1555.003]] | Credentials from Web Browsers |
| [[kb/mitre/attack/techniques/T1555.004-Windows_Credential_Manager\|T1555.004]] | Windows Credential Manager |
| [[kb/mitre/attack/techniques/T1555.005-Password_Managers\|T1555.005]] | Password Managers |
| [[kb/mitre/attack/techniques/T1555.006-Cloud_Secrets_Management_Stores\|T1555.006]] | Cloud Secrets Management Stores |




> [!info]- References
> [^1]: [GitHub Mimikatz lsadump Module](https://github.com/gentilkiwi/mimikatz/wiki/module-~-lsadump)

> [^2]: [GitHub LaZagne Dec 2018](https://github.com/AlessandroZ/LaZagne)

> [^3]: [Volexity Patchwork June 2018](https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/)

> [^4]: [Deply Mimikatz](https://github.com/gentilkiwi/mimikatz)

> [^5]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)

> [^6]: [GitHub QuasarRAT](https://github.com/quasar/QuasarRAT)

> [^7]: [SecureWorks August 2019](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)

> [^8]: [Directory Services Internals DPAPI Backup Keys Oct 2015](https://www.dsinternals.com/en/retrieving-dpapi-backup-keys-from-active-directory/)

> [^9]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)

> [^10]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)

> [^11]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)


