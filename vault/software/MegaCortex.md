---
aliases: 
    - S0576
    
mitre-attack: https://attack.mitre.org/software/S0576
---

## S0576

[MegaCortex](https://attack.mitre.org/software/S0576) is ransomware that first appeared in May 2019. [^1]  [MegaCortex](https://attack.mitre.org/software/S0576) has mainly targeted industrial organizations. [^3] [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [MegaCortex](https://attack.mitre.org/software/S0576) was used to kill endpoint security processes.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [MegaCortex](https://attack.mitre.org/software/S0576) has used `rundll32.exe` to load a DLL for file encryption.[^1]  |
| [[System Checks\|T1497.001]] | System Checks | [MegaCortex](https://attack.mitre.org/software/S0576) has checked the number of CPUs in the system to avoid being run in a sandbox or emulator.[^1]   |
| [[Code Signing Certificates\|T1588.003]] | Code Signing Certificates | [MegaCortex](https://attack.mitre.org/software/S0576) has used code signing certificates issued to fake companies to bypass security controls.[^1]  |
| [[Account Access Removal\|T1531]] | Account Access Removal | [MegaCortex](https://attack.mitre.org/software/S0576) has changed user account passwords and logged users off the system.[^1]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [MegaCortex](https://attack.mitre.org/software/S0576) has deleted volume shadow copies using `vssadmin.exe`.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [MegaCortex](https://attack.mitre.org/software/S0576) can parse the available drives and directories to determine which files to encrypt.[^1]   |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [MegaCortex](https://attack.mitre.org/software/S0576) loads `injecthelper.dll` into a newly created `rundll32.exe` process.[^1]  |
| [[Service Stop\|T1489]] | Service Stop | [MegaCortex](https://attack.mitre.org/software/S0576) can stop and disable services on the system.[^1]   |
| [[Modify Registry\|T1112]] | Modify Registry | [MegaCortex](https://attack.mitre.org/software/S0576) has added entries to the Registry for ransom contact information.[^1]  |
| [[Disk Content Wipe\|T1561.001]] | Disk Content Wipe | [MegaCortex](https://attack.mitre.org/software/S0576) can wipe deleted data from all drives using `[cipher.exe](https://attack.mitre.org/software/S1205)`.[^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [MegaCortex](https://attack.mitre.org/software/S0576) has used the open-source library, Mbed Crypto, and generated AES keys to carry out the file encryption process.[^1] [^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [MegaCortex](https://attack.mitre.org/software/S0576) has used `.cmd` scripts on the victim's system.[^1]   |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [MegaCortex](https://attack.mitre.org/software/S0576) has used a Base64 key to decode its components.[^1]  |
| [[Native API\|T1106]] | Native API | After escalating privileges, [MegaCortex](https://attack.mitre.org/software/S0576) calls `TerminateProcess()`, `CreateRemoteThread`, and other Win32 APIs.[^1]  |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [MegaCortex](https://attack.mitre.org/software/S0576) can enable `SeDebugPrivilege` and adjust token privileges.[^1]  |




## References

[^1]: [IBM MegaCortex](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)


[^2]: [mbed-crypto](https://github.com/ARMmbed/mbed-crypto)


[^3]: [FireEye Ransomware Disrupt Industrial Production](https://www.fireeye.com/blog/threat-research/2020/02/ransomware-against-machine-learning-to-disrupt-industrial-production.html)


[^4]: [FireEye Financial Actors Moving into OT](https://www.fireeye.com/blog/threat-research/2020/07/financially-motivated-actors-are-expanding-access-into-ot.html)


