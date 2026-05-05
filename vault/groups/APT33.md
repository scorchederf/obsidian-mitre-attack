---
aliases: 
    - APT33
    - HOLMIUM
    - Elfin
    - Peach Sandstorm
mitre-attack: https://attack.mitre.org/groups/G0064
---

## G0064

[APT33](https://attack.mitre.org/groups/G0064) is a suspected Iranian threat group that has carried out operations since at least 2013. The group has targeted organizations across multiple industries in the United States, Saudi Arabia, and South Korea, with a particular interest in the aviation and energy sectors.[^3] [^11] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [APT33](https://attack.mitre.org/groups/G0064) has used a variety of publicly available tools like [LaZagne](https://attack.mitre.org/software/S0349) to gather credentials.[^4] [^10]  |
| [[Cached Domain Credentials\|T1003.005]] | Cached Domain Credentials | [APT33](https://attack.mitre.org/groups/G0064) has used a variety of publicly available tools like [LaZagne](https://attack.mitre.org/software/S0349) to gather credentials.[^4] [^10]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [APT33](https://attack.mitre.org/groups/G0064) has used WinRAR to compress data prior to exfil.[^4] 	<br> |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [APT33](https://attack.mitre.org/groups/G0064) has used a variety of publicly available tools like [LaZagne](https://attack.mitre.org/software/S0349) to gather credentials.[^4] [^10]  |
| [[Group Policy Preferences\|T1552.006]] | Group Policy Preferences | [APT33](https://attack.mitre.org/groups/G0064) has used a variety of publicly available tools like Gpppassword to gather credentials.[^4] [^10]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [APT33](https://attack.mitre.org/groups/G0064) has used base64 to encode payloads.[^10]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [APT33](https://attack.mitre.org/groups/G0064) has sent spearphishing e-mails with archive attachments.[^5]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [APT33](https://attack.mitre.org/groups/G0064) has used a variety of publicly available tools like [LaZagne](https://attack.mitre.org/software/S0349), [Mimikatz](https://attack.mitre.org/software/S0002), and ProcDump to dump credentials.[^4] [^10]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [APT33](https://attack.mitre.org/groups/G0064) has sent spearphishing emails containing links to .hta files.[^3] [^4]  |
| [[Password Spraying\|T1110.003]] | Password Spraying | [APT33](https://attack.mitre.org/groups/G0064) has used password spraying to gain access to target systems.[^10] [^5]  |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | [APT33](https://attack.mitre.org/groups/G0064) has used a variety of publicly available tools like [LaZagne](https://attack.mitre.org/software/S0349) to gather credentials.[^4] [^10]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [APT33](https://attack.mitre.org/groups/G0064) has created a scheduled task to execute a .vbe file multiple times a day.[^4]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [APT33](https://attack.mitre.org/groups/G0064) has used a variety of publicly available tools like [LaZagne](https://attack.mitre.org/software/S0349) to gather credentials.[^4] [^10]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [APT33](https://attack.mitre.org/groups/G0064) has attempted to use WMI event subscriptions to establish persistence on compromised hosts.[^5]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [APT33](https://attack.mitre.org/groups/G0064) has downloaded additional files and programs from its C2 server.[^4] [^5] 	<br> |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [APT33](https://attack.mitre.org/groups/G0064) has used FTP to exfiltrate files (separately from the C2 channel).[^4]  |
| [[Tool\|T1588.002]] | Tool | [APT33](https://attack.mitre.org/groups/G0064) has obtained and leveraged publicly-available tools for early intrusion activities.[^10] [^4]  |
| [[Network Sniffing\|T1040]] | Network Sniffing | [APT33](https://attack.mitre.org/groups/G0064) has used SniffPass to collect credentials by sniffing network traffic.[^4]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [APT33](https://attack.mitre.org/groups/G0064) has used HTTP for command and control.[^4]  |
| [[PowerShell\|T1059.001]] | PowerShell | [APT33](https://attack.mitre.org/groups/G0064) has utilized PowerShell to download files from the C2 server and run various scripts. [^4] [^5]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [APT33](https://attack.mitre.org/groups/G0064) has deployed a tool known as [DarkComet](https://attack.mitre.org/software/S0334) to the Startup folder of a victim, and used Registry run keys to gain persistence.[^4] [^5]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [APT33](https://attack.mitre.org/groups/G0064) has used valid accounts for initial access and privilege escalation.[^11] [^10]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [APT33](https://attack.mitre.org/groups/G0064) has used AES for encryption of command and control traffic.[^10]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [APT33](https://attack.mitre.org/groups/G0064) has used VBScript to initiate the delivery of payloads.[^5]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [APT33](https://attack.mitre.org/groups/G0064) has used base64 to encode command and control traffic.[^10]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [APT33](https://attack.mitre.org/groups/G0064) has used HTTP over TCP ports 808 and 880 for command and control.[^4]  |
| [[Cloud Accounts\|T1078.004]] | Cloud Accounts | [APT33](https://attack.mitre.org/groups/G0064) has used compromised Office 365 accounts in tandem with [Ruler](https://attack.mitre.org/software/S0358) in an attempt to gain control of endpoints.[^5]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [APT33](https://attack.mitre.org/groups/G0064) has attempted to exploit a known vulnerability in WinRAR (CVE-2018-20250), and attempted to gain remote code execution via a security bypass vulnerability (CVE-2017-11774).[^4] [^5]  |
| [[Malicious File\|T1204.002]] | Malicious File | [APT33](https://attack.mitre.org/groups/G0064) has used malicious e-mail attachments to lure victims into executing malware.[^5]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [APT33](https://attack.mitre.org/groups/G0064) has lured users to click links to malicious HTML applications delivered via spearphishing emails.[^3] [^4]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [APT33](https://attack.mitre.org/groups/G0064) has used a publicly available exploit for CVE-2017-0213 to escalate privileges on a local system.[^10]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^4]  |
| [[PowerSploit\|S0194]] | PowerSploit | [^10]  |
| [[Empire\|S0363]] | Empire | [^10] [^4]  |
| [[PoshC2\|S0378]] | PoshC2 | [^10] [^4]  |
| [[Ruler\|S0358]] | Ruler | [^10] [^5]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^4]  |
| [[LaZagne\|S0349]] | LaZagne | [^4]  |
| [[Pupy\|S0192]] | Pupy | [^10]  |
| [[ftp\|S0095]] | ftp | [^4]  |
| [[NETWIRE\|S0198]] | NETWIRE | [^3] [^11]  |
| [[StoneDrill\|S0380]] | StoneDrill | [^3]  |
| [[NanoCore\|S0336]] | NanoCore | [^11]  |
| [[TURNEDUP\|S0199]] | TURNEDUP | [^3] [^11] [^4]  |
| [[POWERTON\|S0371]] | POWERTON | [^10] [^5]  |
| [[DEADWOOD\|S1134]] | DEADWOOD | [DEADWOOD](https://attack.mitre.org/software/S1134) was previously linked to [APT33](https://attack.mitre.org/groups/G0064) operations in 2019.[^6]  |
| [[AutoIt backdoor\|S0129]] | AutoIt backdoor | [^4]  |



## References

[^1]: APT33


[^2]: Elfin


[^3]: [FireEye APT33 Sept 2017](https://www.fireeye.com/blog/threat-research/2017/09/apt33-insights-into-iranian-cyber-espionage.html)


[^4]: [Symantec Elfin Mar 2019](https://www.symantec.com/blogs/threat-intelligence/elfin-apt33-espionage)


[^5]: [Microsoft Holmium June 2020](https://www.microsoft.com/security/blog/2020/06/18/inside-microsoft-threat-protection-mapping-attack-chains-from-cloud-to-endpoint/)


[^6]: [RecordedFuture IranianResponse 2020](https://www.recordedfuture.com/blog/iranian-cyber-response)


[^7]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^8]: Peach Sandstorm


[^9]: HOLMIUM


[^10]: [FireEye APT33 Guardrail](https://www.fireeye.com/blog/threat-research/2018/12/overruled-containing-a-potentially-destructive-adversary.html)


[^11]: [FireEye APT33 Webinar Sept 2017](https://www.brighttalk.com/webcast/10703/275683)


