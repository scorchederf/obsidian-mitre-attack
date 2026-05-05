---
aliases: 
    - S1202
    
mitre-attack: https://attack.mitre.org/software/S1202
---

## S1202

[LockBit 3.0](https://attack.mitre.org/software/S1202) is an evolution of the LockBit Ransomware-as-a-Service (RaaS) offering with similarities to BlackMatter and [BlackCat](https://attack.mitre.org/software/S1068) ransomware. [LockBit 3.0](https://attack.mitre.org/software/S1202) has been in use since at least June 2022 and features enhanced defense evasion and exfiltration tactics, robust encryption methods for Windows and VMware ESXi systems, and a more refined RaaS structure over its predecessors such as [LockBit 2.0](https://attack.mitre.org/software/S1199).[^3] [^1] [^2] [^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | The [LockBit 3.0](https://attack.mitre.org/software/S1202) payload is decrypted at runtime.[^3] [^2] [^5]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [LockBit 3.0](https://attack.mitre.org/software/S1202) can encrypt C2 communications with AES.[^2]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [LockBit 3.0](https://attack.mitre.org/software/S1202) can bypass UAC to execute code with elevated privileges through an elevated Component Object Model (COM) interface.[^2]  |
| [[Group Policy Modification\|T1484.001]] | Group Policy Modification | [LockBit 3.0](https://attack.mitre.org/software/S1202) can enable options for propogation through Group Policy Objects.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [LockBit 3.0](https://attack.mitre.org/software/S1202) can use PowerShell to apply Group Policy changes.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [LockBit 3.0](https://attack.mitre.org/software/S1202) can change the Registry values for Group Policy refresh time, to disable SmartScreen, and to disable Windows Defender.[^2] [^5] <br><br> |
| [[Mutual Exclusion\|T1480.002]] | Mutual Exclusion | [LockBit 3.0](https://attack.mitre.org/software/S1202) can create and check for a mutex containing a hash of the `MachineGUID` value at execution to prevent running more than one instance.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | The [LockBit 3.0](https://attack.mitre.org/software/S1202) payload includes an encrypted main component.[^3] [^2]  |
| [[Software Packing\|T1027.002]] | Software Packing | [LockBit 3.0](https://attack.mitre.org/software/S1202) can use code packing to hinder analysis.[^3] [^5]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [LockBit 3.0](https://attack.mitre.org/software/S1202) can enumerate local drive configuration.[^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | [LockBit 3.0](https://attack.mitre.org/software/S1202) can install system services for persistence.[^3]  |
| [[Service Execution\|T1569.002]] | Service Execution | [LockBit 3.0](https://attack.mitre.org/software/S1202) can use [PsExec](https://attack.mitre.org/software/S0029) to execute commands and payloads.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [LockBit 3.0](https://attack.mitre.org/software/S1202) can use HTTP to send victim host information to C2.[^2] [^5]  |
| [[Native API\|T1106]] | Native API | [LockBit 3.0](https://attack.mitre.org/software/S1202) has the ability to directly call native Windows API items during execution.[^3] [^5]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [LockBit 3.0](https://attack.mitre.org/software/S1202) can make execution dependent on specific parameters including a unique passphrase and the system language of the targeted host not being found on a set exclusion list. [^1] [^3] [^2]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [LockBit 3.0](https://attack.mitre.org/software/S1202) can delete log files on targeted systems.[^1] [^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [LockBit 3.0](https://attack.mitre.org/software/S1202) can delete itself from disk.[^1] [^2]  |
| [[CMSTP\|T1218.003]] | CMSTP | [LockBit 3.0](https://attack.mitre.org/software/S1202) can attempt a CMSTP UAC bypass if it does not have administrative privileges.[^3]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [LockBit 3.0](https://attack.mitre.org/software/S1202) can disable security tools to evade detection including Windows Defender.[^1] [^2] [^5]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [LockBit 3.0](https://attack.mitre.org/software/S1202) can exclude files associated with core system functions from encryption.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [LockBit 3.0](https://attack.mitre.org/software/S1202) can enumerate system hostname and domain.[^2]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [LockBit 3.0](https://attack.mitre.org/software/S1202) can identify network shares on compromised systems.[^2]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [LockBit 3.0](https://attack.mitre.org/software/S1202) can Base64-encode C2 communication.[^2]  |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [LockBit 3.0](https://attack.mitre.org/software/S1202) can check heap memory parameters for indications of a debugger and stop the flow of events to the attached debugger in order to hinder dynamic analysis.[^3]  |
| [[Service Stop\|T1489]] | Service Stop | [LockBit 3.0](https://attack.mitre.org/software/S1202) can terminate targeted processes and services related to security, backup, database management, and other applications that could stop or interfere with encryption.[^1] [^3] [^2] [^5]  |
| [[Winlogon Helper DLL\|T1547.004]] | Winlogon Helper DLL | [LockBit 3.0](https://attack.mitre.org/software/S1202) can enable automatic logon through the `SOFTWARE\Microsoft\Windows<br>NT\CurrentVersion\Winlogon` Registry key.[^2] <br> |
| [[Process Discovery\|T1057]] | Process Discovery | [LockBit 3.0](https://attack.mitre.org/software/S1202) can identify and terminate specific services.[^3] [^1]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [LockBit 3.0](https://attack.mitre.org/software/S1202) will not affect machines with language settings matching a defined exlusion list of mainly Eastern European languages.[^1] [^2]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [LockBit 3.0](https://attack.mitre.org/software/S1202) has the ability to discover external storage devices.[^2]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [LockBit 3.0](https://attack.mitre.org/software/S1202) can encrypt targeted data using the AES-256, ChaCha20, or RSA-2048 algorithms.[^1] [^3] [^2] [^5]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [LockBit 3.0](https://attack.mitre.org/software/S1202) can use SMB for lateral movement.[^2]  |
| [[Safe Mode Boot\|T1688]] | Safe Mode Boot | [LockBit 3.0](https://attack.mitre.org/software/S1202) can reboot the infected host into Safe Mode.[^2]  |
| [[Local Accounts\|T1078.003]] | Local Accounts | [LockBit 3.0](https://attack.mitre.org/software/S1202) can use a compromised local account for lateral movement.[^2]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [LockBit 3.0](https://attack.mitre.org/software/S1202) can delete volume shadow copies.[^1] [^2] [^5]  |




## References

[^1]: [Joint Cybersecurity Advisory LockBit JUN 2023](https://www.cisa.gov/sites/default/files/2023-06/aa23-165a_understanding_TA_LockBit_0.pdf)


[^2]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)


[^3]: [Sentinel Labs LockBit 3.0 JUL 2022](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques)


[^4]: LockBit Black


[^5]: [INCIBE-CERT LockBit MAR 2024](https://www.incibe.es/en/incibe-cert/blog/lockbit-response-and-recovery-actions)


