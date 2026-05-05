---
aliases: 
    - S1053
    
mitre-attack: https://attack.mitre.org/software/S1053
---

## S1053

[AvosLocker](https://attack.mitre.org/software/S1053) is ransomware written in C++ that has been offered via the Ransomware-as-a-Service (RaaS) model. It was first observed in June 2021 and has been used against financial services, critical manufacturing, government facilities, and other critical infrastructure sectors in the United States. As of March 2022, [AvosLocker](https://attack.mitre.org/software/S1053) had also been used against organizations in Belgium, Canada, China, Germany, Saudi Arabia, Spain, Syria, Taiwan, Turkey, the United Arab Emirates, and the United Kingdom.[^5] [^3] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Native API\|T1106]] | Native API | [AvosLocker](https://attack.mitre.org/software/S1053) has used a variety of Windows API calls, including `NtCurrentPeb` and `GetLogicalDrives`.[^5]  |
| [[Safe Mode Boot\|T1688]] | Safe Mode Boot | [AvosLocker](https://attack.mitre.org/software/S1053) can restart a compromised machine in safe mode.[^3] [^4]   |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [AvosLocker](https://attack.mitre.org/software/S1053) has encrypted files and network resources using AES-256 and added an `.avos`, `.avos2`, or `.AvosLinux` extension to filenames.[^5] [^3] [^2] [^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [AvosLocker](https://attack.mitre.org/software/S1053) has been executed via the `RunOnce` Registry key to run itself on safe mode.[^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [AvosLocker](https://attack.mitre.org/software/S1053) has deobfuscated XOR-encoded strings.[^5]  |
| [[Dynamic API Resolution\|T1027.007]] | Dynamic API Resolution | [AvosLocker](https://attack.mitre.org/software/S1053) has used obfuscated API calls that are retrieved by their checksums.[^5]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [AvosLocker](https://attack.mitre.org/software/S1053) has searched for files and directories on a compromised network.[^5] [^3]  |
| [[Masquerade File Type\|T1036.008]] | Masquerade File Type | [AvosLocker](https://attack.mitre.org/software/S1053) has been disguised as a .jpg file.[^3]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [AvosLocker](https://attack.mitre.org/software/S1053) has hidden its console window by using the `ShowWindow` API function.[^5]  |
| [[Service Stop\|T1489]] | Service Stop | [AvosLocker](https://attack.mitre.org/software/S1053) has terminated specific processes before encryption.[^5]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [AvosLocker](https://attack.mitre.org/software/S1053) has enumerated shared drives on a compromised network.[^5] [^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [AvosLocker](https://attack.mitre.org/software/S1053) has used XOR-encoded strings.[^5]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [AvosLocker](https://attack.mitre.org/software/S1053) has checked the system time before and after encryption.[^5]  |
| [[Process Discovery\|T1057]] | Process Discovery | [AvosLocker](https://attack.mitre.org/software/S1053) has discovered system processes by calling `RmGetList`.[^5]  |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [AvosLocker](https://attack.mitre.org/software/S1053)’s Linux variant has terminated ESXi virtual machines.[^3]  |




## References

[^1]: [Joint CSA AvosLocker Mar 2022](https://www.ic3.gov/Media/News/2022/220318.pdf)


[^2]: [Cisco Talos Avos Jun 2022](https://blog.talosintelligence.com/avoslocker-new-arsenal/)


[^3]: [Trend Micro AvosLocker Apr 2022](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-avoslocker)


[^4]: [Costa AvosLocker May 2022](https://www.linkedin.com/pulse/raas-avoslocker-incident-response-analysis-fl%C3%A1vio-costa?trk=articles_directory)


[^5]: [Malwarebytes AvosLocker Jul 2021](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)


