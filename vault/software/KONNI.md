---
aliases: 
    - S0356
    
mitre-attack: https://attack.mitre.org/software/S0356
---

## S0356

[KONNI](https://attack.mitre.org/software/S0356) is a remote access tool that security researchers assess has been used by North Korean cyber actors since at least 2014. [KONNI](https://attack.mitre.org/software/S0356) has significant code overlap with the [NOKKI](https://attack.mitre.org/software/S0353) malware family, and has been linked to several suspected North Korean campaigns targeting political organizations in Russia, East Asia, Europe and the Middle East; there is some evidence potentially linking [KONNI](https://attack.mitre.org/software/S0356) to [APT37](https://attack.mitre.org/groups/G0067).[^4] [^5] [^6] [^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [KONNI](https://attack.mitre.org/software/S0356) has used certutil to download and decode base64 encoded strings and has also devoted a custom section to performing all the components of the deobfuscation process.[^1] [^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [KONNI](https://attack.mitre.org/software/S0356) has relied on a victim to enable malicious macros within an attachment delivered via email.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [KONNI](https://attack.mitre.org/software/S0356) can gather the OS version, architecture information, hostname, and RAM size information from the victim’s machine and has used `cmd /c systeminfo` command to get a snapshot of the current system state of the target machine.[^4] [^1] [^2]  |
| [[Component Object Model Hijacking\|T1546.015]] | Component Object Model Hijacking | [KONNI](https://attack.mitre.org/software/S0356) has modified ComSysApp service to load the malicious DLL payload.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [KONNI](https://attack.mitre.org/software/S0356) can collect the IP address from the victim’s machine.[^4]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [KONNI](https://attack.mitre.org/software/S0356) has used FTP to exfiltrate reconnaissance data out.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [KONNI](https://attack.mitre.org/software/S0356) has used `net session` on the victim's machine.[^2]   |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [KONNI](https://attack.mitre.org/software/S0356) can steal profiles (containing credential information) from Firefox, Chrome, and Opera.[^4]  |
| [[Data from Local System\|T1005]] | Data from Local System | [KONNI](https://attack.mitre.org/software/S0356) has stored collected information and discovered processes in a tmp file.[^2]  |
| [[Parent PID Spoofing\|T1134.004]] | Parent PID Spoofing | [KONNI](https://attack.mitre.org/software/S0356) has used parent PID spoofing to spawn a new `cmd` process using `CreateProcessW` and a handle to `Taskmgr.exe`.[^2]   |
| [[Software Packing\|T1027.002]] | Software Packing | [KONNI](https://attack.mitre.org/software/S0356) has been packed for obfuscation.[^7]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [KONNI](https://attack.mitre.org/software/S0356) has bypassed UAC by performing token impersonation as well as an RPC-based method, this included bypassing UAC set to “AlwaysNotify".[^1] [^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [KONNI](https://attack.mitre.org/software/S0356) has used HTTP POST for C2.[^4] [^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [KONNI](https://attack.mitre.org/software/S0356) can collect the username from the victim’s machine.[^4]  |
| [[File Deletion\|T1070.004]] | File Deletion | [KONNI](https://attack.mitre.org/software/S0356) can delete files.[^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | A version of [KONNI](https://attack.mitre.org/software/S0356) has dropped a Windows shortcut into the Startup folder to establish persistence.[^4]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [KONNI](https://attack.mitre.org/software/S0356) is heavily obfuscated and includes encrypted configuration files.[^2]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [KONNI](https://attack.mitre.org/software/S0356) had a feature to steal data from the clipboard.[^4]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [KONNI](https://attack.mitre.org/software/S0356) has pretended to be the xmlProv Network Provisioning service.[^2]   |
| [[Process Discovery\|T1057]] | Process Discovery | [KONNI](https://attack.mitre.org/software/S0356) has used the command `cmd /c tasklist` to get a snapshot of the current processes on the target machine.[^1] [^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [KONNI](https://attack.mitre.org/software/S0356) used PowerShell to download and execute a specific 64-bit version of the malware.[^4] [^2]   |
| [[Modify Registry\|T1112]] | Modify Registry | [KONNI](https://attack.mitre.org/software/S0356) has modified registry keys of ComSysApp, Svchost, and xmlProv on the machine to gain persistence.[^1] [^2]   |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [KONNI](https://attack.mitre.org/software/S0356) can gather information on connected drives and disk space from the victim’s machine.[^4] [^1] [^2]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [KONNI](https://attack.mitre.org/software/S0356) has encrypted data and files prior to exfiltration.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [KONNI](https://attack.mitre.org/software/S0356) can download files and execute them on the victim’s machine.[^4] [^2]   |
| [[Native API\|T1106]] | Native API | [KONNI](https://attack.mitre.org/software/S0356) has hardcoded API calls within its functions to use on the victim's machine.[^2]   |
| [[Windows Service\|T1543.003]] | Windows Service | [KONNI](https://attack.mitre.org/software/S0356) has registered itself as a service using its export function.[^2]   |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [KONNI](https://attack.mitre.org/software/S0356) has used a custom base64 key to encode stolen data before exfiltration.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [KONNI](https://attack.mitre.org/software/S0356) can take screenshots of the victim’s machine.[^4]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [KONNI](https://attack.mitre.org/software/S0356) has used cmd.exe to execute arbitrary commands on the infected host across different stages of the infection chain.[^4] [^1] [^2]   |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [KONNI](https://attack.mitre.org/software/S0356) has been delivered via spearphishing campaigns through a malicious Word document.[^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [KONNI](https://attack.mitre.org/software/S0356) has used Rundll32 to execute its loader for privilege escalation purposes.[^1] [^2]  |
| [[Create Process with Token\|T1134.002]] | Create Process with Token | [KONNI](https://attack.mitre.org/software/S0356) has duplicated the token of a high integrity process to spawn an instance of cmd.exe under an impersonated user.[^1] [^2]   |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [KONNI](https://attack.mitre.org/software/S0356) has sent data and files to its C2 server.[^4] [^2] [^7]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [KONNI](https://attack.mitre.org/software/S0356) has used AES to encrypt C2 traffic.[^7]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | A version of [KONNI](https://attack.mitre.org/software/S0356) searches for filenames created with a previous version of the malware, suggesting different versions targeted the same victims and the versions may work together.[^4]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | A version of [KONNI](https://attack.mitre.org/software/S0356) drops a Windows shortcut on the victim’s machine to establish persistence.[^4]  |
| [[Keylogging\|T1056.001]] | Keylogging | [KONNI](https://attack.mitre.org/software/S0356) has the capability to perform keylogging.[^4]  |
| [[JavaScript\|T1059.007]] | JavaScript | [KONNI](https://attack.mitre.org/software/S0356) has executed malicious JavaScript code.[^2]   |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [KONNI](https://attack.mitre.org/software/S0356) has created a shortcut called "Anti virus service.lnk" in an apparent attempt to masquerade as a legitimate file.[^4]  |




## References

[^1]: [Medium KONNI Jan 2020](https://medium.com/d-hunter/a-look-into-konni-2019-campaign-b45a0f321e9b)


[^2]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)


[^3]: KONNI


[^4]: [Talos Konni May 2017](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)


[^5]: [Unit 42 NOKKI Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)


[^6]: [Unit 42 Nokki Oct 2018](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)


[^7]: [Malwarebytes KONNI Evolves Jan 2022](https://blog.malwarebytes.com/threat-intelligence/2022/01/konni-evolves-into-stealthier-rat/)


