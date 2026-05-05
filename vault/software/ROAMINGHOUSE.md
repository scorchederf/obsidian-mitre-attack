---
aliases: 
    - S9026
    
mitre-attack: https://attack.mitre.org/software/S9026
---

## S9026

[ROAMINGHOUSE](https://attack.mitre.org/software/S9026) is a dropper malware used by [MirrorFace](https://attack.mitre.org/groups/G1054) to extract and execute embedded payloads including [UPPERCUT](https://attack.mitre.org/software/S0275) components.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [ROAMINGHOUSE](https://attack.mitre.org/software/S9026) can decode and drop a malicious ZIP file prior to execution.[^2]  |
| [[Office Template Macros\|T1137.001]] | Office Template Macros | [ROAMINGHOUSE](https://attack.mitre.org/software/S9026) has been loaded as a Word Template file when victims opened a decoy document placed in `%APPDATA%\Microsoft\Templates` alongside a [ROAMINGHOUSE](https://attack.mitre.org/software/S9026) macro.[^1]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [ROAMINGHOUSE](https://attack.mitre.org/software/S9026) has been distributed through phishing emails containing malicious OneDrive links.[^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) used malicious files to drop [ROAMINGHOUSE](https://attack.mitre.org/software/S9026).[^1]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [ROAMINGHOUSE](https://attack.mitre.org/software/S9026) has been executed through luring victims into clicking links to download malicious ZIP files.[^2]  |
| [[User Activity Based Checks\|T1497.002]] | User Activity Based Checks | [ROAMINGHOUSE](https://attack.mitre.org/software/S9026) can check for specific mouse movements and user activity before initiating malicious activity.[^1]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [ROAMINGHOUSE](https://attack.mitre.org/software/S9026) can change its execution method to create a batch file in the startup folder that executes a legitimate executable if a McAfee product is detected.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [ROAMINGHOUSE](https://attack.mitre.org/software/S9026) can embed a ZIP file containing [UPPERCUT](https://attack.mitre.org/software/S0275) components into three base64 encoded parts.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [ROAMINGHOUSE](https://attack.mitre.org/software/S9026) can identify McAfee applications on compromised hosts and change its execution method if one is detected.[^2]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [ROAMINGHOUSE](https://attack.mitre.org/software/S9026) can use WMI to launch a legitimate executable later used to enable DLL sideloading.[^2] [^1]  |
| [[DLL\|T1574.001]] | DLL | [ROAMINGHOUSE](https://attack.mitre.org/software/S9026) can use a legitimate EXE to sideload a malicious DLL named JSFC.dll.[^2]  [ROAMINGHOUSE](https://attack.mitre.org/software/S9026) has also used ScnCfg32.exe to sideload vsodscpl.dll to enable [UPPERCUT](https://attack.mitre.org/software/S0275) execution.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MirrorFace\|G1054]] | MirrorFace |



## References

[^1]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)


[^2]: [Trend Micro Earth Kasha Updates APR 2025](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)


