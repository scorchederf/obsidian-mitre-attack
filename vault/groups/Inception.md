---
aliases: 
    - Inception
    - Inception Framework
    - Cloud Atlas
mitre-attack: https://attack.mitre.org/groups/G0100
---

## G0100

[Inception](https://attack.mitre.org/groups/G0100) is a cyber espionage group active since at least 2014. The group has targeted multiple industries and governmental entities primarily in Russia, but has also been active in the United States and throughout Europe, Asia, Africa, and the Middle East.[^7] [^4] [^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Inception](https://attack.mitre.org/groups/G0100) has encrypted malware payloads dropped on victim machines with AES and RC4 encryption.[^1]  |
| [[Tool\|T1588.002]] | Tool | [Inception](https://attack.mitre.org/groups/G0100) has obtained and used open-source tools such as [LaZagne](https://attack.mitre.org/software/S0349).[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Inception](https://attack.mitre.org/groups/G0100) has maintained persistence by modifying Registry run key value <br> `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run\`.[^1]  |
| [[Web Service\|T1102]] | Web Service | [Inception](https://attack.mitre.org/groups/G0100) has incorporated at least five different cloud service providers into their C2 infrastructure including CloudMe.[^1] [^4]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [Inception](https://attack.mitre.org/groups/G0100) used chains of compromised routers to proxy C2 communications between them and cloud service providers.[^4]  |
| [[Software Discovery\|T1518]] | Software Discovery | [Inception](https://attack.mitre.org/groups/G0100) has enumerated installed software on compromised systems.[^4]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Inception](https://attack.mitre.org/groups/G0100) used a file listing plugin to collect information about file and directories both on local and remote drives.[^4]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Inception](https://attack.mitre.org/groups/G0100) has used weaponized documents attached to spearphishing emails for reconnaissance and initial compromise.[^1] [^4] [^7] [^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Inception](https://attack.mitre.org/groups/G0100) has used a reconnaissance module to gather information about the operating system and hardware on the infected host.[^4]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Inception](https://attack.mitre.org/groups/G0100) has used PowerShell to execute malicious commands and payloads.[^7] [^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Inception](https://attack.mitre.org/groups/G0100) lured victims into clicking malicious files for machine reconnaissance and to execute malware.[^1] [^2] [^4] [^7]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Inception](https://attack.mitre.org/groups/G0100) has used HTTP, HTTPS, and WebDav in network communications.[^1] [^7]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Inception](https://attack.mitre.org/groups/G0100) used a file hunting plugin to collect .txt, .pdf, .xls or .doc files from the infected host.[^2]  |
| [[Mshta\|T1218.005]] | Mshta | [Inception](https://attack.mitre.org/groups/G0100) has used malicious HTA files to drop and execute malware.[^2]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Inception](https://attack.mitre.org/groups/G0100) used a browser plugin to steal passwords and sessions from Internet Explorer, Chrome, Opera, Firefox, Torch, and Yandex.[^4]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Inception](https://attack.mitre.org/groups/G0100) has exploited CVE-2012-0158, CVE-2014-1761, CVE-2017-11882 and CVE-2018-0802 for execution.[^2] [^1] [^4] [^7]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [Inception](https://attack.mitre.org/groups/G0100) has used specific malware modules to gather domain membership.[^4]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Inception](https://attack.mitre.org/groups/G0100) has used VBScript to execute malicious commands and payloads.[^7] [^1]  |
| [[Template Injection\|T1221]] | Template Injection | [Inception](https://attack.mitre.org/groups/G0100) has used decoy documents to load malicious remote payloads via HTTP.[^7]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Inception](https://attack.mitre.org/groups/G0100) has ensured persistence at system boot by setting the value `regsvr32 %path%\ctfmonrn.dll /s`.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Inception](https://attack.mitre.org/groups/G0100) has encrypted network communications with AES.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Inception](https://attack.mitre.org/groups/G0100) has used a reconnaissance module to identify active processes and other associated loaded modules.[^4]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[LaZagne\|S0349]] | LaZagne | [^2]  |
| [[PowerShower\|S0441]] | PowerShower | [^7]  |
| [[VBShower\|S0442]] | VBShower | [^2]  |



## References

[^1]: [Kaspersky Cloud Atlas December 2014](https://securelist.com/cloud-atlas-redoctober-apt-is-back-in-style/68083/)


[^2]: [Kaspersky Cloud Atlas August 2019](https://securelist.com/recent-cloud-atlas-activity/92016/)


[^3]: Inception Framework


[^4]: [Symantec Inception Framework March 2018](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/inception-framework-hiding-behind-proxies)


[^5]: Inception


[^6]: Cloud Atlas


[^7]: [Unit 42 Inception November 2018](https://unit42.paloaltonetworks.com/unit42-inception-attackers-target-europe-year-old-office-vulnerability/)


