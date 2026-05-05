---
aliases: 
    - INC Ransom
    - GOLD IONIC
mitre-attack: https://attack.mitre.org/groups/G1032
---

## G1032

[INC Ransom](https://attack.mitre.org/groups/G1032) is a ransomware and data extortion threat group associated with the deployment of [INC Ransomware](https://attack.mitre.org/software/S1139) that has been active since at least July 2023. [INC Ransom](https://attack.mitre.org/groups/G1032)  has targeted organizations worldwide most commonly in the industrial, healthcare, and education sectors in the US and Europe.[^1] [^7] [^6] [^4] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [INC Ransom](https://attack.mitre.org/groups/G1032) has used [INC Ransomware](https://attack.mitre.org/software/S1139) to encrypt victim's data.[^4] [^8] [^1] [^6] [^7] [^2]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | <br>[INC Ransom](https://attack.mitre.org/groups/G1032) has used RDP to move laterally.[^7] [^8] [^2] [^5]  |
| [[Financial Theft\|T1657]] | Financial Theft | [INC Ransom](https://attack.mitre.org/groups/G1032) has stolen and encrypted victim's data in order to extort payment for keeping it private or decrypting it.[^7] [^1] [^6] [^2] [^4]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [INC Ransom](https://attack.mitre.org/groups/G1032) has used WMIC to deploy ransomware.[^7] [^8] [^2]  |
| [[Phishing\|T1566]] | Phishing | [INC Ransom](https://attack.mitre.org/groups/G1032) has used phishing to gain initial access.[^2] [^4] <br> |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [INC Ransom](https://attack.mitre.org/groups/G1032) has used `cmd.exe` to launch malicious payloads.[^8]  |
| [[Transfer Data to Cloud Account\|T1537]] | Transfer Data to Cloud Account | [INC Ransom](https://attack.mitre.org/groups/G1032) has used Megasync to exfiltrate data to the cloud.[^6]  |
| [[Domain Account\|T1087.002]] | Domain Account | [INC Ransom](https://attack.mitre.org/groups/G1032) has scanned for domain admin accounts in compromised environments.[^2]  |
| [[Data Staged\|T1074]] | Data Staged | [INC Ransom](https://attack.mitre.org/groups/G1032) has staged data on compromised hosts prior to exfiltration.[^8] [^2]  |
| [[Application Layer Protocol\|T1071]] | Application Layer Protocol | [INC Ransom](https://attack.mitre.org/groups/G1032) has used valid accounts over RDP to connect to targeted systems.[^8]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [INC Ransom](https://attack.mitre.org/groups/G1032) has used NETSCAN.EXE for internal reconnaissance.[^2] [^4]  |
| [[Service Execution\|T1569.002]] | Service Execution | [INC Ransom](https://attack.mitre.org/groups/G1032) has run a file encryption executable via `Service Control Manager/7045;winupd,%SystemRoot%\winupd.exe,user mode service,demand start,LocalSystem`.[^8]  |
| [[Remote Access Tools\|T1219]] | Remote Access Tools | <br>[INC Ransom](https://attack.mitre.org/groups/G1032) has used AnyDesk and PuTTY on compromised systems.[^8] [^2] [^5] [^4]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [INC Ransom](https://attack.mitre.org/groups/G1032) can use SystemSettingsAdminFlows.exe, a native Windows utility, to disable Windows Defender.[^5]  |
| [[Tool\|T1588.002]] | Tool | [INC Ransom](https://attack.mitre.org/groups/G1032) has acquired and used several tools including MegaSync, AnyDesk,  [esentutl](https://attack.mitre.org/software/S0404) and [PsExec](https://attack.mitre.org/software/S0029).[^7] [^8] [^2] [^5] [^4]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [INC Ransom](https://attack.mitre.org/groups/G1032) has named a [PsExec](https://attack.mitre.org/software/S0029) executable winupd to mimic a legitimate Windows update file.[^8] [^2]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | <br>[INC Ransom](https://attack.mitre.org/groups/G1032) has used a rapid succession of copy commands to install a file encryption executable across multiple endpoints within compromised infrastructure.[^8] [^6]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [INC Ransom](https://attack.mitre.org/groups/G1032) has enumerated domain groups on targeted hosts.[^8]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [INC Ransom](https://attack.mitre.org/groups/G1032) has used Internet Explorer to view folders on other systems.[^8]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [INC Ransom](https://attack.mitre.org/groups/G1032) has exploited known vulnerabilities including CVE-2023-3519 in Citrix NetScaler for initial access.[^2] [^4]  |
| [[File Deletion\|T1070.004]] | File Deletion | <br>[INC Ransom](https://attack.mitre.org/groups/G1032) has uninstalled tools from compromised endpoints after use.[^5]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | <br>[INC Ransom](https://attack.mitre.org/groups/G1032) has used compromised valid accounts for access to victim environments.[^7] [^8] [^2] [^5]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [INC Ransom](https://attack.mitre.org/groups/G1032) has downloaded tools to compromised servers including Advanced IP Scanner. [^8] [^5]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [INC Ransom](https://attack.mitre.org/groups/G1032) has used 7-Zip and WinRAR to archive collected data prior to exfiltration.[^8] [^6] [^2] [^5]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [INC Ransom](https://attack.mitre.org/groups/G1032) has used RDP to test network connections.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^5]  |
| [[Rclone\|S1040]] | Rclone | [^5]  |
| [[Nltest\|S0359]] | Nltest | [^8]  |
| [[esentutl\|S0404]] | esentutl | [^2] [^4]  |
| [[Tor\|S0183]] | Tor | [^6] [^2] [^4]  |
| [[AdFind\|S0552]] | AdFind | [^6]  |
| [[PsExec\|S0029]] | PsExec | [^7] [^8] [^6] [^2]  |
| [[INC Ransomware\|S1139]] | INC Ransomware | [^7] [^6]  |



## References

[^1]: [Bleeping Computer INC Ransomware March 2024](https://www.bleepingcomputer.com/news/security/inc-ransom-threatens-to-leak-3tb-of-nhs-scotland-stolen-data/)


[^2]: [SOCRadar INC Ransom January 2024](https://socradar.io/dark-web-profile-inc-ransom/)


[^3]: GOLD IONIC


[^4]: [SentinelOne INC Ransomware](https://www.sentinelone.com/anthology/inc-ransom/)


[^5]: [Huntress INC Ransomware May 2024](https://www.huntress.com/blog/lolbin-to-inc-ransomware)


[^6]: [Secureworks GOLD IONIC April 2024](https://www.secureworks.com/blog/gold-ionic-deploys-inc-ransomware)


[^7]: [Cybereason INC Ransomware November 2023](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)


[^8]: [Huntress INC Ransom Group August 2023](https://www.huntress.com/blog/investigating-new-inc-ransom-group-activity)


