---
aliases: 
    - S0256
    
mitre-attack: https://attack.mitre.org/software/S0256
---

## S0256

[Mosquito](https://attack.mitre.org/software/S0256) is a Win32 backdoor that has been used by [Turla](https://attack.mitre.org/groups/G0010). [Mosquito](https://attack.mitre.org/software/S0256) is made up of three parts: the installer, the launcher, and the backdoor. The main backdoor is called CommanderDLL and is launched by the loader program. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Mosquito](https://attack.mitre.org/software/S0256)'s installer uses WMI to search for antivirus display names.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Mosquito](https://attack.mitre.org/software/S0256) runs `whoami` on the victim’s machine.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Mosquito](https://attack.mitre.org/software/S0256)'s launcher uses rundll32.exe in a Registry Key value to start the main backdoor capability.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Mosquito](https://attack.mitre.org/software/S0256) deletes files using DeleteFileW API call.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Mosquito](https://attack.mitre.org/software/S0256) uses a custom encryption algorithm, which consists of XOR and a stream that is similar to the Blum Blum Shub algorithm.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Mosquito](https://attack.mitre.org/software/S0256)'s installer searches the Registry and system to see if specific antivirus tools are installed on the system.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Mosquito](https://attack.mitre.org/software/S0256) can launch PowerShell Scripts.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Mosquito](https://attack.mitre.org/software/S0256) can modify Registry keys under `HKCU\Software\Microsoft\[dllname]` to store configuration values. [Mosquito](https://attack.mitre.org/software/S0256) also modifies Registry keys under `HKCR\CLSID\...\InprocServer32` with a path to the launcher.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Mosquito](https://attack.mitre.org/software/S0256) can upload and download files to the victim.[^1]  |
| [[Component Object Model Hijacking\|T1546.015]] | Component Object Model Hijacking | [Mosquito](https://attack.mitre.org/software/S0256) uses COM hijacking as a method of persistence.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Mosquito](https://attack.mitre.org/software/S0256)’s installer is obfuscated with a custom crypter to obfuscate the installer.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Mosquito](https://attack.mitre.org/software/S0256) runs `tasklist` to obtain running processes.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Mosquito](https://attack.mitre.org/software/S0256) uses the `ipconfig` command.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Mosquito](https://attack.mitre.org/software/S0256) executes cmd.exe and uses a pipe to read the results and send back the output to the C2 server.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Mosquito](https://attack.mitre.org/software/S0256) establishes persistence under the Registry key `HKCU\Software\Run auto_update`.[^1]  |
| [[Native API\|T1106]] | Native API | [Mosquito](https://attack.mitre.org/software/S0256) leverages the CreateProcess() and LoadLibrary() calls to execute files with the .dll and .exe extensions.[^1]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [Mosquito](https://attack.mitre.org/software/S0256) stores configuration values under the Registry key `HKCU\Software\Microsoft\[dllname]`.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Turla\|G0010]] | Turla |



## References

[^1]: [ESET Turla Mosquito Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)


[^2]: [Secureworks IRON HUNTER Profile](http://www.secureworks.com/research/threat-profiles/iron-hunter)


[^3]: Mosquito


[^4]: [ESET Turla Mosquito May 2018](https://www.welivesecurity.com/2018/05/22/turla-mosquito-shift-towards-generic-tools/)


