---
aliases: 
    - S1247
    
mitre-attack: https://attack.mitre.org/software/S1247
---

## S1247

[Embargo](https://attack.mitre.org/software/S1247) is a ransomware variant written in Rust that has been active since at least May 2024.[^4] [^2]   [Embargo](https://attack.mitre.org/software/S1247) ransomware operations are associated with “double extortion” ransomware activity, where data is exfiltrated from victim environments prior to encryption, with threats to publish files if a ransom is not paid.[^4] [^2]   [Embargo](https://attack.mitre.org/software/S1247) ransomware has been known to be delivered through a loader known as MDeployer which also leverages a malware component known as MS4Killer that facilitates termination of processes operating on the victim hosts.[^2]  [Embargo](https://attack.mitre.org/software/S1247) is also reportedly a Ransomware as a Service (RaaS).[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Service Stop\|T1489]] | Service Stop | [Embargo](https://attack.mitre.org/software/S1247) has terminated active processes and services based on a hardcoded list using the `CloseServiceHandle()` function.[^4]  [Embargo](https://attack.mitre.org/software/S1247) has also leveraged MS4Killer to terminate processes contained in an embedded list of security software process names that were XOR-encrypted.[^2]  |
| [[Mutual Exclusion\|T1480.002]] | Mutual Exclusion | [Embargo](https://attack.mitre.org/software/S1247) has utilized a hardcoded mutex name of “LoadUpOnGunsBringYourFriends” using the `CreateMutexW()` function.[^4]  [Embargo](https://attack.mitre.org/software/S1247) has also utilized a hardcoded mutex name of “IntoTheFloodAgainSameOldTrip."[^2]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [Embargo](https://attack.mitre.org/software/S1247) has leveraged MS4Killer to deliver a vulnerable driver to the victim device, sometimes referred to as Bring Your Own Vulnerable Driver (BYOVD).[^2]  [Embargo](https://attack.mitre.org/software/S1247) has utilized the vulnerable driver probmon.sys version 3.0.0.4 which had a revoked certificated from “ITM System Co.,LTD.”[^2]  |
| [[Financial Theft\|T1657]] | Financial Theft | [Embargo](https://attack.mitre.org/software/S1247) has been leveraged in double-extortion ransomware, exfiltrating files then encrypting them, to prompt victims to pay a ransom.[^4] [^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Embargo](https://attack.mitre.org/software/S1247) has searched for folders, subfolders and other networked or mounted drives for follow on encryption actions.[^4]  [Embargo](https://attack.mitre.org/software/S1247) has also iterated device volumes using `FindFirstVolumeW()` and `FindNextVolumeW()` functions and then calls the `GetVolumePathNamesForVolumeNameW()` function to retrieve a list of drive letters and mounted folder paths for each specified volume.[^4]  |
| [[Safe Mode Boot\|T1688]] | Safe Mode Boot | [Embargo](https://attack.mitre.org/software/S1247) has used a DLL variant of MDeployer to disable security solutions through Safe Mode.[^2]  |
| [[Native API\|T1106]] | Native API | [Embargo](https://attack.mitre.org/software/S1247) has leveraged Windows Native API functions to execute its operations.[^4]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Embargo](https://attack.mitre.org/software/S1247) has utilized MS4Killer to detect running processes on the victim device.[^2]  [Embargo](https://attack.mitre.org/software/S1247) has also captured a snapshot of active running processes using the Windows API `CreateToolHelp32Snapshot()`.[^4]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Embargo](https://attack.mitre.org/software/S1247) has modified and deleted Registry keys to add services, and to disable Security Solutions such as Windows Defender.[^2]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Embargo](https://attack.mitre.org/software/S1247) has cleared files from the recycle bin by invoking `SHEmptyRecycleBinW()` and disabled Windows recovery through `C:\Windows\System32\cmd.exe /q /c bcdedit /set {default} recoveryenabled no`.[^4]  |
| [[Selective Exclusion\|T1679]] | Selective Exclusion | [Embargo](https://attack.mitre.org/software/S1247) has avoided encrypting specific files and directories by leveraging a regular expression within the ransomware binary.[^4]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Embargo](https://attack.mitre.org/software/S1247) has utilized MDeployer to decrypt two payloads that contain MS4Killer toolkit b.cache and the [Embargo](https://attack.mitre.org/software/S1247) ransomware executable a.cache with a hardcoded RC4 key `wlQYLoPCil3niI7x8CvR9EtNtL/aeaHrZ23LP3fAsJogVTIzdnZ5Pi09ZVeHFkiB`.[^2]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Embargo](https://attack.mitre.org/software/S1247) has searched for folders, subfolders and other networked or mounted drives for follow-on encryption actions.[^4]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Embargo](https://attack.mitre.org/software/S1247) has encrypted both MDeployer and MS4 Killer payloads with RC4.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Embargo](https://attack.mitre.org/software/S1247) has utilized a BAT script to disable security solutions.[^2]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Embargo](https://attack.mitre.org/software/S1247) has obtained active services running on the victim’s system through the functions `OpenSCManagerW()` and `EnumServicesStatusExW()`.[^4]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Embargo](https://attack.mitre.org/software/S1247) has obtained persistence of the loader MDeployer by creating a scheduled task named “Perf_sys.”[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Embargo](https://attack.mitre.org/software/S1247) has leveraged MDeployer to terminate the MS4Killer process, delete the decrypted payload files and a driver file dropped by MS4killer, and reboot the system.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Embargo](https://attack.mitre.org/software/S1247) has modified the Windows Registry to start a custom service named irnagentd in Safe Mode.[^2]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Embargo](https://attack.mitre.org/software/S1247) has created a service named irnagentd that executed the MDeployer loader after the system is rebooted in Safe Mode.[^2]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Embargo](https://attack.mitre.org/software/S1247) has the ability to encrypt files with the ChaCha20 and Curve25519 cryptographic algorithms.[^4]  [Embargo](https://attack.mitre.org/software/S1247) also has the ability to encrypt system data and add a random six-letter extension consisting of hexadecimal characters such as ".b58eeb" or “.3d828a” to encrypted files.[^2]   |
| [[Windows Service\|T1543.003]] | Windows Service | [Embargo](https://attack.mitre.org/software/S1247) has created persistence through the DLL variant of the MDeployer toolkit by creating a service called irnagentd that launches after the system is rebooted in Safe Mode.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Storm-0501\|G1053]] | Storm-0501 |



## References

[^1]: [Microsoft Storm-501 Sabbath Ransomware Embargo September 2024](https://www.microsoft.com/en-us/security/blog/2024/09/26/storm-0501-ransomware-attacks-expanding-to-hybrid-cloud-environments/)


[^2]: [ESET Embargo Ransomware October 2024](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)


[^3]: [Microsoft Storm-0501 Embargo Ransomware August 2025](https://www.microsoft.com/en-us/security/blog/2025/08/27/storm-0501s-evolving-techniques-lead-to-cloud-based-ransomware/)


[^4]: [Cyble Embargo Ransomware May 2024](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)


