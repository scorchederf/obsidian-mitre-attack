---
aliases: 
    - Play
mitre-attack: https://attack.mitre.org/groups/G1040
---

## G1040

[Play](https://attack.mitre.org/groups/G1040) is a ransomware group that has been active since at least 2022 deploying  [Playcrypt](https://attack.mitre.org/software/S1162) ransomware against the business, government, critical infrastructure, healthcare, and media sectors in North America, South America, and Europe. [Play](https://attack.mitre.org/groups/G1040) actors employ a double-extortion model, encrypting systems after exfiltrating data, and are presumed by security researchers to operate as a closed group.[^1] [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Data Transfer Size Limits\|T1030]] | Data Transfer Size Limits | [Play](https://attack.mitre.org/groups/G1040) has split victims' files into chunks for exfiltration.[^1] [^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | <br>[Play](https://attack.mitre.org/groups/G1040) has used the information-stealing tool Grixba to enumerate network information.[^1] <br> |
| [[Exfiltration Over Alternative Protocol\|T1048]] | Exfiltration Over Alternative Protocol | [Play](https://attack.mitre.org/groups/G1040) has used WinSCP to exfiltrate data to actor-controlled accounts.[^1] [^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Play](https://attack.mitre.org/groups/G1040) has used tools including [Wevtutil](https://attack.mitre.org/software/S0645) to remove malicious files from compromised hosts.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | <br>[Play](https://attack.mitre.org/groups/G1040) has used a batch script to remove indicators of its presence on compromised hosts.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Play](https://attack.mitre.org/groups/G1040) has used Base64-encoded PowerShell scripts to disable Microsoft Defender.[^2]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | <br>[Play](https://attack.mitre.org/groups/G1040) has used WinRAR to compress files prior to exfiltration.[^1] [^2]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Play](https://attack.mitre.org/groups/G1040) has used tools such as [AdFind](https://attack.mitre.org/software/S0552), [Nltest](https://attack.mitre.org/software/S0359), and [BloodHound](https://attack.mitre.org/software/S0521) to enumerate shares and hostnames on compromised networks.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | <br>[Play](https://attack.mitre.org/groups/G1040) has used the information stealer Grixba to check for a list of security processes.[^2]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Play](https://attack.mitre.org/groups/G1040) has used Base64-encoded PowerShell scripts for post exploit activities on compromised hosts.[^2]  |
| [[Malware\|T1587.001]] | Malware | [Play](https://attack.mitre.org/groups/G1040) developed and employ [Playcrypt](https://attack.mitre.org/software/S1162) ransomware.[^2] [^1]  |
| [[Local Accounts\|T1078.003]] | Local Accounts | [Play](https://attack.mitre.org/groups/G1040) has used valid  local accounts to gain initial access.[^2]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Play](https://attack.mitre.org/groups/G1040) has used [Cobalt Strike](https://attack.mitre.org/software/S0154) to move laterally via SMB.[^2]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [Play](https://attack.mitre.org/groups/G1040) has used tools to remove log files on targeted systems.[^1] [^2]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Play](https://attack.mitre.org/groups/G1040) has used valid VPN accounts to achieve initial access.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Play](https://attack.mitre.org/groups/G1040) has used [Cobalt Strike](https://attack.mitre.org/software/S0154) to download files to compromised machines.[^2]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [Play](https://attack.mitre.org/groups/G1040) has used valid domain accounts for access.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | <br>[Play](https://attack.mitre.org/groups/G1040) has leveraged tools to enumerate system information.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Play](https://attack.mitre.org/groups/G1040) has used the Grixba information stealer to list security files and processes.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | <br>[Play](https://attack.mitre.org/groups/G1040) has used the information-stealing tool Grixba to scan for anti-virus software.[^1] <br> |
| [[External Remote Services\|T1133]] | External Remote Services | <br>[Play](https://attack.mitre.org/groups/G1040) has used Remote Desktop Protocol (RDP) and Virtual Private Networks (VPN) for initial access.[^1] [^2]  |
| [[Tool\|T1588.002]] | Tool | [Play](https://attack.mitre.org/groups/G1040) has used multiple tools for discovery and defense evasion purposes on compromised hosts.[^1]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Play](https://attack.mitre.org/groups/G1040) has exploited known vulnerabilities for initial access including CVE-2018-13379 and CVE-2020-12812 in FortiOS and CVE-2022-41082 and CVE-2022-41040 ("ProxyNotShell") in Microsoft Exchange.[^1] [^2]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Play](https://attack.mitre.org/groups/G1040) has used [Mimikatz](https://attack.mitre.org/software/S0002) and the Windows Task Manager to dump LSASS process memory.[^2]  |
| [[Financial Theft\|T1657]] | Financial Theft | [Play](https://attack.mitre.org/groups/G1040) demands ransom payments from victims to unencrypt filesystems and to not publish sensitive data exfiltrated from victim networks.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | <br>[Play](https://attack.mitre.org/groups/G1040) has used tools including GMER, IOBit, and PowerTool to disable antivirus software.[^1] [^2] <br> |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[BloodHound\|S0521]] | BloodHound | [^2]  |
| [[Empire\|S0363]] | Empire | [^2]  |
| [[Nltest\|S0359]] | Nltest | [^2]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^2]  |
| [[AdFind\|S0552]] | AdFind | [^1] [^2]  |
| [[Wevtutil\|S0645]] | Wevtutil | [^2]  |
| [[PsExec\|S0029]] | PsExec | [^1]  |
| [[Playcrypt\|S1162]] | Playcrypt | [^1] [^2]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^2]  |



## References

[^1]: [CISA Play Ransomware Advisory December 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a)


[^2]: [Trend Micro Ransomware Spotlight Play July 2023](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)


