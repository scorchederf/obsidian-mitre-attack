---
aliases: 
    - S0349
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0349-LaZagne
---

## Description

[[kb/mitre/attack/software/S0349-LaZagne\|LaZagne]] is a post-exploitation, open-source tool used to recover stored passwords on a system. It has modules for Windows, Linux, and OSX, but is mainly focused on Windows systems. [[kb/mitre/attack/software/S0349-LaZagne\|LaZagne]] is publicly available on GitHub.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.001-LSASS_Memory\|T1003.001]] | LSASS Memory | [[kb/mitre/attack/software/S0349-LaZagne\|LaZagne]] can perform credential dumping from memory to obtain account and password information.[^1]  |
| [[kb/mitre/attack/techniques/T1003.004-LSA_Secrets\|T1003.004]] | LSA Secrets | [[kb/mitre/attack/software/S0349-LaZagne\|LaZagne]] can perform credential dumping from LSA secrets to obtain account and password information.[^1]  |
| [[kb/mitre/attack/techniques/T1003.005-Cached_Domain_Credentials\|T1003.005]] | Cached Domain Credentials | [[kb/mitre/attack/software/S0349-LaZagne\|LaZagne]] can perform credential dumping from MSCache to obtain account and password information.[^1]  |
| [[kb/mitre/attack/techniques/T1003.007-Proc_Filesystem\|T1003.007]] | Proc Filesystem | [[kb/mitre/attack/software/S0349-LaZagne\|LaZagne]] can use the `<PID>/maps` and `<PID>/mem` files to identify regex patterns to dump cleartext passwords from the browser's process memory.[^1] [^4]  |
| [[kb/mitre/attack/techniques/T1003.008-etc_passwd_and_etc_shadow\|T1003.008]] | ／etc／passwd and ／etc／shadow | [[kb/mitre/attack/software/S0349-LaZagne\|LaZagne]] can obtain credential information from /etc/shadow using the shadow.py module.[^1]  |
| [[kb/mitre/attack/techniques/T1552.001-Credentials_In_Files\|T1552.001]] | Credentials In Files | [[kb/mitre/attack/software/S0349-LaZagne\|LaZagne]] can obtain credentials from chats, databases, mail, and WiFi.[^1]  |
| [[kb/mitre/attack/techniques/T1555-Credentials_from_Password_Stores\|T1555]] | Credentials from Password Stores | [[kb/mitre/attack/software/S0349-LaZagne\|LaZagne]] can obtain credentials from databases, mail, and WiFi across multiple platforms.[^1]  |
| [[kb/mitre/attack/techniques/T1555.001-Keychain\|T1555.001]] | Keychain | [[kb/mitre/attack/software/S0349-LaZagne\|LaZagne]] can obtain credentials from macOS Keychains.[^1] 	 |
| [[kb/mitre/attack/techniques/T1555.003-Credentials_from_Web_Browsers\|T1555.003]] | Credentials from Web Browsers | [[kb/mitre/attack/software/S0349-LaZagne\|LaZagne]] can obtain credentials from web browsers such as Google Chrome, Internet Explorer, and Firefox.[^1]  |
| [[kb/mitre/attack/techniques/T1555.004-Windows_Credential_Manager\|T1555.004]] | Windows Credential Manager | [[kb/mitre/attack/software/S0349-LaZagne\|LaZagne]] can obtain credentials from Vault files.[^1] 	 |





> [!info]- References
> [^1]: [GitHub LaZagne Dec 2018](https://github.com/AlessandroZ/LaZagne)

> [^2]: [GitHub LaZange Dec 2018](https://github.com/AlessandroZ/LaZagne)

> [^3]: LaZagne

> [^4]: [Picus Labs Proc cump 2022](https://www.picussecurity.com/resource/the-mitre-attck-t1003-os-credential-dumping-technique-and-its-adversary-use)


