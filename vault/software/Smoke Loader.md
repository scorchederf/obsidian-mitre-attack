---
aliases: 
    - S0226
    
mitre-attack: https://attack.mitre.org/software/S0226
---

## S0226

[Smoke Loader](https://attack.mitre.org/software/S0226) is a malicious bot application that can be used to load other malware.<br>[Smoke Loader](https://attack.mitre.org/software/S0226) has been seen in the wild since at least 2011 and has included a number of different payloads. It is notorious for its use of deception and self-protection. It also comes with several plug-ins. [^1]  [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Smoke Loader](https://attack.mitre.org/software/S0226) deobfuscates its code.[^5]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [Smoke Loader](https://attack.mitre.org/software/S0226) searches for files named logins.json to parse for credentials.[^5]  |
| [[Local Email Collection\|T1114.001]] | Local Email Collection | [Smoke Loader](https://attack.mitre.org/software/S0226) searches through Outlook files and directories (e.g., inbox, sent, templates, drafts, archives, etc.).[^5]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Smoke Loader](https://attack.mitre.org/software/S0226) adds a Visual Basic script in the Startup folder to deploy the payload.[^1]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Smoke Loader](https://attack.mitre.org/software/S0226) searches for credentials stored from web browsers.[^5]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Smoke Loader](https://attack.mitre.org/software/S0226) uses HTTP for C2.[^1]  |
| [[System Checks\|T1497.001]] | System Checks | [Smoke Loader](https://attack.mitre.org/software/S0226) scans processes to perform anti-VM checks. [^5]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Smoke Loader](https://attack.mitre.org/software/S0226) downloads a new version of itself once it has installed. It also downloads additional plugins.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Smoke Loader](https://attack.mitre.org/software/S0226) adds a Registry Run key for persistence and adds a script in the Startup folder to deploy the payload.[^1]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Smoke Loader](https://attack.mitre.org/software/S0226) spawns a new copy of c:\windows\syswow64\explorer.exe and then replaces the executable code in memory with malware.[^1] [^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Smoke Loader](https://attack.mitre.org/software/S0226) uses a simple one-byte XOR method to obfuscate values in the malware.[^1] [^5]  |
| [[Process Injection\|T1055]] | Process Injection | [Smoke Loader](https://attack.mitre.org/software/S0226) injects into the Internet Explorer process.[^5]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Smoke Loader](https://attack.mitre.org/software/S0226) launches a scheduled task.[^5]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Smoke Loader](https://attack.mitre.org/software/S0226) recursively searches through directories for files.[^5]  |




## References

[^1]: [Malwarebytes SmokeLoader 2016](https://blog.malwarebytes.com/threat-analysis/2016/08/smoke-loader-downloader-with-a-smokescreen-still-alive/)


[^2]: Dofoil


[^3]: [Microsoft Dofoil 2018](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/07/behavior-monitoring-combined-with-machine-learning-spoils-a-massive-dofoil-coin-mining-campaign/)


[^4]: Smoke Loader


[^5]: [Talos Smoke Loader July 2018](https://blog.talosintelligence.com/2018/07/smoking-guns-smoke-loader-learned-new.html#more)


