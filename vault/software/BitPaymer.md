---
aliases: 
    - S0570
    
mitre-attack: https://attack.mitre.org/software/S0570
---

## S0570

[BitPaymer](https://attack.mitre.org/software/S0570) is a ransomware variant first observed in August 2017 targeting hospitals in the U.K. [BitPaymer](https://attack.mitre.org/software/S0570) uses a unique encryption key, ransom note, and contact information for each operation. [BitPaymer](https://attack.mitre.org/software/S0570) has several indicators suggesting overlap with the [Dridex](https://attack.mitre.org/software/S0384) malware and is often delivered via [Dridex](https://attack.mitre.org/software/S0384).[^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [BitPaymer](https://attack.mitre.org/software/S0570) can use `net view` to discover remote systems.[^5]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [BitPaymer](https://attack.mitre.org/software/S0570) compares file names and paths to a list of excluded names and directory names during encryption.[^5]  |
| [[Windows Permissions\|T1222.001]] | Windows Permissions | [BitPaymer](https://attack.mitre.org/software/S0570) can use `icacls /reset` and `takeown /F` to reset a targeted executable's permissions and then take ownership.[^5]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [BitPaymer](https://attack.mitre.org/software/S0570) can import a hard-coded RSA 1024-bit public key, generate a 128-bit RC4 key for each file, and encrypt the file in place, appending `.locked` to the filename.[^5]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [BitPaymer](https://attack.mitre.org/software/S0570) has used RC4-encrypted strings and string hashes to avoid identifiable strings within the binary.[^5]  |
| [[Timestomp\|T1070.006]] | Timestomp | [BitPaymer](https://attack.mitre.org/software/S0570) can modify the timestamp of an executable so that it can be identified and restored by the decryption tool.[^5]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [BitPaymer](https://attack.mitre.org/software/S0570) has set the run key `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` for persistence.[^5]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [BitPaymer](https://attack.mitre.org/software/S0570) can search for network shares on the domain or workgroup using `net view <host>`.[^5]  |
| [[Token Impersonation／Theft\|T1134.001]] | Token Impersonation／Theft | [BitPaymer](https://attack.mitre.org/software/S0570) can use the tokens of users to create processes on infected systems.[^5]  |
| [[Query Registry\|T1012]] | Query Registry | [BitPaymer](https://attack.mitre.org/software/S0570) can use the RegEnumKeyW to iterate through Registry keys.[^5]   |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [BitPaymer](https://attack.mitre.org/software/S0570) attempts to remove the backup shadow files from the host using `vssadmin.exe Delete Shadows /All /Quiet`.[^5]  |
| [[Windows Service\|T1543.003]] | Windows Service | [BitPaymer](https://attack.mitre.org/software/S0570) has attempted to install itself as a service to maintain persistence.[^5]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [BitPaymer](https://attack.mitre.org/software/S0570) can suppress UAC prompts by setting the `HKCU\Software\Classes\ms-settings\shell\open\command` registry key on Windows 10 or `HKCU\Software\Classes\mscfile\shell\open\command` on Windows 7 and launching the `eventvwr.msc` process, which launches [BitPaymer](https://attack.mitre.org/software/S0570) with elevated privileges.[^5]  |
| [[NTFS File Attributes\|T1564.004]] | NTFS File Attributes | [BitPaymer](https://attack.mitre.org/software/S0570) has copied itself to the `:bin` alternate data stream of a newly created file.[^5]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [BitPaymer](https://attack.mitre.org/software/S0570) can enumerate existing Windows services on the host that are configured to run as LocalSystem.[^5]  |
| [[Local Account\|T1087.001]] | Local Account | [BitPaymer](https://attack.mitre.org/software/S0570) can enumerate the sessions for each user logged onto the infected host.[^5]  |
| [[Modify Registry\|T1112]] | Modify Registry | [BitPaymer](https://attack.mitre.org/software/S0570) can set values in the Registry to help in execution.[^5]   |
| [[Native API\|T1106]] | Native API | [BitPaymer](https://attack.mitre.org/software/S0570) has used dynamic API resolution to avoid identifiable strings within the binary, including `RegEnumKeyW`.[^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Indrik Spider\|G0119]] | Indrik Spider |



## References

[^1]: wp_encrypt


[^2]: BitPaymer


[^3]: [Crowdstrike EvilCorp March 2021](https://www.crowdstrike.com/blog/hades-ransomware-successor-to-indrik-spiders-wastedlocker/)


[^4]: FriedEx


[^5]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)


