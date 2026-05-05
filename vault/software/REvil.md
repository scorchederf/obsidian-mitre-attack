---
aliases: 
    - S0496
    
mitre-attack: https://attack.mitre.org/software/S0496
---

## S0496

[REvil](https://attack.mitre.org/software/S0496) is a ransomware family that has been linked to the [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) group and operated as ransomware-as-a-service (RaaS) since at least April 2019. [REvil](https://attack.mitre.org/software/S0496), which as been used against organizations in the manufacturing, transportation, and electric sectors, is highly configurable and shares code similarities with the GandCrab RaaS.[^12] [^19] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [REvil](https://attack.mitre.org/software/S0496) can encrypt files on victim systems and demands a ransom to decrypt the files.[^4] [^8] [^14] [^2] [^19] [^11] [^12] [^9]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [REvil](https://attack.mitre.org/software/S0496) can use the Windows command line to delete volume shadow copies and disable recovery.[^8] [^14] [^11] [^12]  |
| [[PowerShell\|T1059.001]] | PowerShell | [REvil](https://attack.mitre.org/software/S0496) has used PowerShell to delete volume shadow copies and download files.[^16] [^14] [^19] [^3]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [REvil](https://attack.mitre.org/software/S0496) has encrypted C2 communications with the ECIES algorithm.[^4]  |
| [[Process Injection\|T1055]] | Process Injection | [REvil](https://attack.mitre.org/software/S0496) can inject itself into running processes on a compromised host.[^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [REvil](https://attack.mitre.org/software/S0496) can mimic the names of known executables.[^11]  |
| [[Modify Registry\|T1112]] | Modify Registry | [REvil](https://attack.mitre.org/software/S0496) can modify the Registry to save encryption parameters and system information.[^8] [^16] [^18] [^19] [^12]  |
| [[Data Destruction\|T1485]] | Data Destruction | [REvil](https://attack.mitre.org/software/S0496) has the capability to destroy files and folders.[^4] [^16] [^18] [^18] [^19] [^11] [^12]  |
| [[Query Registry\|T1012]] | Query Registry | [REvil](https://attack.mitre.org/software/S0496) can query the Registry to get random file extensions to append to encrypted files.[^12]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [REvil](https://attack.mitre.org/software/S0496) has used obfuscated VBA macros for execution.[^1] [^11]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [REvil](https://attack.mitre.org/software/S0496) can exfiltrate host and malware information to C2 servers.[^12]  |
| [[Service Stop\|T1489]] | Service Stop | [REvil](https://attack.mitre.org/software/S0496) has the capability to stop services and kill processes.[^19] [^12]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [REvil](https://attack.mitre.org/software/S0496) can identify the username, machine name, system language, keyboard layout, and OS version on a compromised host.[^4] [^8] [^16] [^18] [^18] [^19] [^3] [^12]  |
| [[Native API\|T1106]] | Native API | [REvil](https://attack.mitre.org/software/S0496) can use Native API for execution and to retrieve active services.[^12] [^19]  |
| [[Malicious File\|T1204.002]] | Malicious File | [REvil](https://attack.mitre.org/software/S0496) has been executed via malicious MS Word e-mail attachments.[^1] [^2] [^11]  |
| [[Create Process with Token\|T1134.002]] | Create Process with Token | [REvil](https://attack.mitre.org/software/S0496) can launch an instance of itself with administrative rights using runas.[^12]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [REvil](https://attack.mitre.org/software/S0496) can connect to and disable the Symantec server on the victim's network.[^8]  |
| [[Mutual Exclusion\|T1480.002]] | Mutual Exclusion | [REvil](https://attack.mitre.org/software/S0496) attempts to create a mutex using a hard-coded value to ensure that no other instances of itself are running on the host.[^15]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [REvil](https://attack.mitre.org/software/S0496) has the ability to identify specific files and directories that are not to be encrypted.[^4] [^8] [^16] [^18] [^19] [^12]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [REvil](https://attack.mitre.org/software/S0496) has used encrypted strings and configuration files.[^1] [^16] [^18] [^19] [^3] [^11] [^12]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [REvil](https://attack.mitre.org/software/S0496) has infected victim machines through compromised websites and exploit kits.[^12] [^18] [^11] [^16]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [REvil](https://attack.mitre.org/software/S0496) can enumerate active services.[^19]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [REvil](https://attack.mitre.org/software/S0496) can use WMI to monitor for and kill specific processes listed in its configuration file.[^16] [^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [REvil](https://attack.mitre.org/software/S0496) can decode encrypted strings to enable execution of commands and payloads.[^1] [^4] [^8] [^18] [^19] [^12]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [REvil](https://attack.mitre.org/software/S0496) has been distributed via malicious e-mail attachments including MS Word Documents.[^1] [^8] [^12] [^18] [^11]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [REvil](https://attack.mitre.org/software/S0496) can download a copy of itself from an attacker controlled IP address to the victim machine.[^14] [^18] [^11]  |
| [[Safe Mode Boot\|T1688]] | Safe Mode Boot | [REvil](https://attack.mitre.org/software/S0496) can force a reboot in safe mode with networking.[^20]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [REvil](https://attack.mitre.org/software/S0496) can identify system drive information on a compromised host.[^4] [^8] [^16] [^18] [^18] [^19] [^3] [^12]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [REvil](https://attack.mitre.org/software/S0496) can check the system language using `GetUserDefaultUILanguage` and `GetSystemDefaultUILanguage`. If the language is found in the list, the process terminates.[^4] <br> |
| [[Token Impersonation／Theft\|T1134.001]] | Token Impersonation／Theft | [REvil](https://attack.mitre.org/software/S0496) can obtain the token from the user that launched the explorer.exe process to avoid affecting the desktop of the SYSTEM user.[^18]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [REvil](https://attack.mitre.org/software/S0496) has used HTTP and HTTPS in communication with C2.[^8] [^16] [^18] [^19] [^12]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [REvil](https://attack.mitre.org/software/S0496) can identify the domain membership of a compromised host.[^4] [^18] [^12]  |
| [[File Deletion\|T1070.004]] | File Deletion | [REvil](https://attack.mitre.org/software/S0496) can mark its binary code for deletion after reboot.[^19]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [REvil](https://attack.mitre.org/software/S0496) can use vssadmin to delete volume shadow copies and bcdedit to disable recovery features.[^4] [^8] [^16] [^14] [^18] [^19] [^11] [^12] [^9]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [REvil](https://attack.mitre.org/software/S0496) can save encryption parameters and system information in the Registry.[^8] [^16] [^18] [^19] [^12]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN7\|G0046]] | FIN7 |
| [[GOLD SOUTHFIELD\|G0115]] | GOLD SOUTHFIELD |



## References

[^1]: [G Data Sodinokibi June 2019](https://www.gdatasoftware.com/blog/2019/06/31724-strange-bits-sodinokibi-spam-cinarat-and-fake-g-data)


[^2]: [McAfee REvil October 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-crescendo/)


[^3]: [Group IB Ransomware May 2020](https://www.group-ib.com/whitepapers/ransomware-uncovered.html)


[^4]: [Kaspersky Sodin July 2019](https://securelist.com/sodin-ransomware/91473/)


[^5]: [CrowdStrike Carbon Spider August 2021](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)


[^6]: Sodin


[^7]: Sodinokibi


[^8]: [Cylance Sodinokibi July 2019](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)


[^9]: [Tetra Defense Sodinokibi March 2020](https://web.archive.org/web/20210414101816/https://tetradefense.com/incident-response-services/cause-and-effect-sodinokibi-ransomware-analysis/)


[^10]: [IBM Ransomware Trends September 2020](https://securityintelligence.com/posts/ransomware-2020-attack-trends-new-techniques-affecting-organizations-worldwide/)


[^11]: [Picus Sodinokibi January 2020](https://www.picussecurity.com/blog/a-brief-history-and-further-technical-analysis-of-sodinokibi-ransomware)


[^12]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)


[^13]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^14]: [Talos Sodinokibi April 2019](https://blog.talosintelligence.com/2019/04/sodinokibi-ransomware-exploits-weblogic.html)


[^15]: [SecureWorks September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)


[^16]: [Secureworks GandCrab and REvil September 2019](https://www.secureworks.com/blog/revil-the-gandcrab-connection)


[^17]: [FBI Flash FIN7 USB](https://therecord.media/fbi-fin7-hackers-target-us-companies-with-badusb-devices-to-install-ransomware/)


[^18]: [McAfee Sodinokibi October 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)


[^19]: [Intel 471 REvil March 2020](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)


[^20]: [BleepingComputer REvil 2021](https://www.bleepingcomputer.com/news/security/revil-ransomware-has-a-new-windows-safe-mode-encryption-mode/)


