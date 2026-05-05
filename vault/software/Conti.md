---
aliases: 
    - S0575
    
mitre-attack: https://attack.mitre.org/software/S0575
---

## S0575

[Conti](https://attack.mitre.org/software/S0575) is a Ransomware-as-a-Service (RaaS) that was first observed in December 2019. [Conti](https://attack.mitre.org/software/S0575) has been deployed via [TrickBot](https://attack.mitre.org/software/S0266) and used against major corporations and government agencies, particularly those in North America. As with other ransomware families, actors using [Conti](https://attack.mitre.org/software/S0575) steal sensitive files and information from compromised networks, and threaten to publish this data unless the ransom is paid.[^7] [^6] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Conti](https://attack.mitre.org/software/S0575) can spread via SMB and encrypts files on different hosts, potentially compromising an entire network.[^7] [^6]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Conti](https://attack.mitre.org/software/S0575) can enumerate remote open SMB network shares using `NetShareEnum()`.[^6] [^8]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Conti](https://attack.mitre.org/software/S0575) has decrypted its payload using a hardcoded AES-256 key.[^7] [^6]  |
| [[Service Stop\|T1489]] | Service Stop | [Conti](https://attack.mitre.org/software/S0575) can stop up to 146 Windows services related to security, backup, database, and email solutions through the use of `net stop`.[^6]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Conti](https://attack.mitre.org/software/S0575) can discover files on a local system.[^6]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Conti](https://attack.mitre.org/software/S0575) can retrieve the ARP cache from the local system by using the `GetIpNetTable()` API call and check to ensure IP addresses it connects to are for local, non-Internet, systems.[^6]   |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Conti](https://attack.mitre.org/software/S0575) can use `CreateIoCompletionPort()`, `PostQueuedCompletionStatus()`, and `GetQueuedCompletionPort()` to rapidly encrypt files, excluding those with the extensions of .exe, .dll, and .lnk. It has used a different AES-256 encryption key per file with a bundled RAS-4096 public encryption key that is unique for each victim. [Conti](https://attack.mitre.org/software/S0575) can use “Windows Restart Manager” to ensure files are unlocked and open for encryption.[^7] [^6] [^1] [^8] [^3]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | <br>[Conti](https://attack.mitre.org/software/S0575) has the ability to discover hosts on a target network.[^8]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Conti](https://attack.mitre.org/software/S0575) can use compiler-based obfuscation for its code, encrypt DLLs, and hide Windows API calls.[^6] [^7] [^8]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Conti](https://attack.mitre.org/software/S0575) can delete Windows Volume Shadow Copies using `vssadmin`.[^6]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Conti](https://attack.mitre.org/software/S0575) can enumerate routine network connections from a compromised host.[^6]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Conti](https://attack.mitre.org/software/S0575) has loaded an encrypted DLL into memory and then executes it.[^7] [^6]  |
| [[Taint Shared Content\|T1080]] | Taint Shared Content | [Conti](https://attack.mitre.org/software/S0575) can spread itself by infecting other remote machines via network shared drives.[^7] [^6]   |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Conti](https://attack.mitre.org/software/S0575) can utilize command line options to allow an attacker control over how it scans and encrypts files.[^6] [^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Conti](https://attack.mitre.org/software/S0575) can enumerate through all open processes to search for any that have the string “sql” in their process name.[^6]  |
| [[Native API\|T1106]] | Native API | [Conti](https://attack.mitre.org/software/S0575) has used API calls during execution.[^7] [^6]   |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Wizard Spider\|G0102]] | Wizard Spider |



## References

[^1]: [Cybleinc Conti January 2020](https://cybleinc.com/2021/01/21/conti-ransomware-resurfaces-targeting-government-large-organizations/)


[^2]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^3]: [DFIR Conti Bazar Nov 2021](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)


[^4]: Conti


[^5]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^6]: [CarbonBlack Conti July 2020](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)


[^7]: [Cybereason Conti Jan 2021](https://www.cybereason.com/blog/cybereason-vs.-conti-ransomware)


[^8]: [CrowdStrike Wizard Spider October 2020](https://www.crowdstrike.com/blog/wizard-spider-adversary-update/)


