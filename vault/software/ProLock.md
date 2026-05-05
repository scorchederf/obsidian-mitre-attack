---
aliases: 
    - S0654
    
mitre-attack: https://attack.mitre.org/software/S0654
---

## S0654

[ProLock](https://attack.mitre.org/software/S0654) is a ransomware strain that has been used in Big Game Hunting (BGH) operations since at least 2020, often obtaining initial access with [QakBot](https://attack.mitre.org/software/S0650). [ProLock](https://attack.mitre.org/software/S0654) is the successor to PwndLocker ransomware which was found to contain a bug allowing decryption without ransom payment in 2019.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File Deletion\|T1070.004]] | File Deletion | [ProLock](https://attack.mitre.org/software/S0654) can remove files containing its payload after they are executed.[^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [ProLock](https://attack.mitre.org/software/S0654) can encrypt files on a compromised host with RC6, and encrypts the key with RSA-1024.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [ProLock](https://attack.mitre.org/software/S0654) can use WMIC to execute scripts on targeted hosts.[^1]  |
| [[BITS Jobs\|T1197]] | BITS Jobs | [ProLock](https://attack.mitre.org/software/S0654) can use BITS jobs to download its malicious payload.[^1]  |
| [[Steganography\|T1027.003]] | Steganography | [ProLock](https://attack.mitre.org/software/S0654) can use .jpg and .bmp files to store its payload.[^1]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [ProLock](https://attack.mitre.org/software/S0654) can use CVE-2019-0859 to escalate privileges on a compromised host.[^1]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [ProLock](https://attack.mitre.org/software/S0654) can use vssadmin.exe to remove volume shadow copies.[^1]  |




## References

[^1]: [Group IB Ransomware September 2020](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)


