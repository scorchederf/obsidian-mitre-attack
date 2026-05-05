---
aliases: 
    - S0630
    
mitre-attack: https://attack.mitre.org/software/S0630
---

## S0630

[Nebulae](https://attack.mitre.org/software/S0630) Is a backdoor that has been used by [Naikon](https://attack.mitre.org/groups/G0019)  since at least 2020.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Nebulae](https://attack.mitre.org/software/S0630) can download files from C2.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Nebulae](https://attack.mitre.org/software/S0630) can discover logical drive information including the drive type, free space, and volume information.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Nebulae](https://attack.mitre.org/software/S0630) has the capability to upload collected files to C2.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Nebulae](https://attack.mitre.org/software/S0630) can use TCP in C2 communications.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Nebulae](https://attack.mitre.org/software/S0630) can achieve persistence through a Registry Run key.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Nebulae](https://attack.mitre.org/software/S0630) can enumerate processes on a target system.[^1]  |
| [[Native API\|T1106]] | Native API | [Nebulae](https://attack.mitre.org/software/S0630) has the ability to use `CreateProcess` to execute a process.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Nebulae](https://attack.mitre.org/software/S0630) has created a service named "Windows Update Agent1" to appear legitimate.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Nebulae](https://attack.mitre.org/software/S0630) has the ability to delete files and directories.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Nebulae](https://attack.mitre.org/software/S0630) can create a service to establish persistence.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Nebulae](https://attack.mitre.org/software/S0630) uses functions named `StartUserModeBrowserInjection` and `StopUserModeBrowserInjection` indicating that it's trying to imitate chrome_frame_helper.dll.[^1]  |
| [[DLL\|T1574.001]] | DLL | [Nebulae](https://attack.mitre.org/software/S0630) can use DLL side-loading to gain execution.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Nebulae](https://attack.mitre.org/software/S0630) can use CMD to execute a process.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Nebulae](https://attack.mitre.org/software/S0630) can list files and directories on a compromised host.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Nebulae](https://attack.mitre.org/software/S0630) can use RC4 and XOR to encrypt C2 communications.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Naikon\|G0019]] | Naikon |



## References

[^1]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)


