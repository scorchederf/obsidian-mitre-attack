---
aliases: 
    - S0168
    
mitre-attack: https://attack.mitre.org/software/S0168
---

## S0168

[Gazer](https://attack.mitre.org/software/S0168) is a backdoor used by [Turla](https://attack.mitre.org/groups/G0010) since at least 2016. [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Winlogon Helper DLL\|T1547.004]] | Winlogon Helper DLL | [Gazer](https://attack.mitre.org/software/S0168) can establish persistence by setting the value “Shell” with “explorer.exe, %malware_pathfile%” under the Registry key `HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon`.[^3]  |
| [[Timestomp\|T1070.006]] | Timestomp | For early [Gazer](https://attack.mitre.org/software/S0168) versions, the compilation timestamp was faked.[^3]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Gazer](https://attack.mitre.org/software/S0168) uses custom encryption for C2 that uses RSA.[^3] [^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Gazer](https://attack.mitre.org/software/S0168) can establish persistence by creating a .lnk file in the Start menu.[^3] [^4]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Gazer](https://attack.mitre.org/software/S0168) communicates with its C2 servers over HTTP.[^3]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [Gazer](https://attack.mitre.org/software/S0168) can establish persistence by creating a .lnk file in the Start menu or by modifying existing .lnk files to execute the malware through cmd.exe.[^3] [^4]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Gazer](https://attack.mitre.org/software/S0168) has commands to delete files and persistence mechanisms from the victim.[^3] [^4]  |
| [[Thread Execution Hijacking\|T1055.003]] | Thread Execution Hijacking | [Gazer](https://attack.mitre.org/software/S0168) performs thread execution hijacking to inject its orchestrator into a running thread from a remote process.[^3] [^4]  |
| [[Process Injection\|T1055]] | Process Injection | [Gazer](https://attack.mitre.org/software/S0168) injects its communication module into an Internet accessible process through which it performs C2.[^3] [^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Gazer](https://attack.mitre.org/software/S0168) can execute a task to download a file.[^3] [^4]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Gazer](https://attack.mitre.org/software/S0168) uses custom encryption for C2 that uses 3DES.[^3] [^4]  |
| [[Screensaver\|T1546.002]] | Screensaver | [Gazer](https://attack.mitre.org/software/S0168) can establish persistence through the system screensaver by configuring it to execute the malware.[^3]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Gazer](https://attack.mitre.org/software/S0168) versions are signed with various valid certificates; one was likely faked and issued by Comodo for "Solid Loop Ltd," and another was issued for "Ultimate Computer Support Ltd."[^3] [^4]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Gazer](https://attack.mitre.org/software/S0168) obtains the current user's security identifier.[^4]  |
| [[NTFS File Attributes\|T1564.004]] | NTFS File Attributes | [Gazer](https://attack.mitre.org/software/S0168) stores configuration items in alternate data streams (ADSs) if the Registry is not accessible.[^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Gazer](https://attack.mitre.org/software/S0168) logs its actions into files that are encrypted with 3DES. It also uses RSA to encrypt resources.[^4]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Gazer](https://attack.mitre.org/software/S0168) can establish persistence by creating a scheduled task.[^3] [^4]  |
| [[Mutual Exclusion\|T1480.002]] | Mutual Exclusion | [Gazer](https://attack.mitre.org/software/S0168) creates a mutex using the hard-coded value `{531511FA-190D-5D85-8A4A-279F2F592CC7}` to ensure that only one instance of itself is running.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Turla\|G0010]] | Turla |



## References

[^1]: [ESET Crutch December 2020](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)


[^2]: WhiteBear


[^3]: [ESET Gazer Aug 2017](https://www.welivesecurity.com/wp-content/uploads/2017/08/eset-gazer.pdf)


[^4]: [Securelist WhiteBear Aug 2017](https://securelist.com/introducing-whitebear/81638/)


[^5]: Gazer


