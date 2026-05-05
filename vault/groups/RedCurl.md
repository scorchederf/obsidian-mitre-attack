---
aliases: 
    - RedCurl
mitre-attack: https://attack.mitre.org/groups/G1039
---

## G1039

[RedCurl](https://attack.mitre.org/groups/G1039) is a threat actor active since 2018 notable for corporate espionage targeting a variety of locations, including Ukraine, Canada and the United Kingdom, and a variety of industries, including but not limited to travel agencies, insurance companies, and banks.[^2]  [RedCurl](https://attack.mitre.org/groups/G1039) is allegedly a Russian-speaking threat actor.[^2] [^1]  The group’s operations typically start with spearphishing emails to gain initial access, then the group executes discovery and collection commands and scripts to find corporate data. The group concludes operations by exfiltrating files to the C2 servers. 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [RedCurl](https://attack.mitre.org/groups/G1039) has used malware with string encryption.[^3]  [RedCurl](https://attack.mitre.org/groups/G1039) has also encrypted data and has encoded PowerShell commands using Base64.[^2] [^1]  [RedCurl](https://attack.mitre.org/groups/G1039) has used `PyArmor` to obfuscate code execution of [LaZagne](https://attack.mitre.org/software/S0349). [^2]  Additionally, [RedCurl](https://attack.mitre.org/groups/G1039) has obfuscated downloaded files by renaming them as commonly used tools and has used `echo`, instead of file names themselves, to execute files.[^4]  <br> |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [RedCurl](https://attack.mitre.org/groups/G1039) added the “hidden” file attribute to original files, manipulating victims to click on malicious LNK files.[^2] [^1]  |
| [[Web Service\|T1102]] | Web Service | [RedCurl](https://attack.mitre.org/groups/G1039) has used web services to download malicious files.[^2] [^1]  |
| [[Local Email Collection\|T1114.001]] | Local Email Collection | [RedCurl](https://attack.mitre.org/groups/G1039) has collected emails to use in future phishing campaigns.[^2]  |
| [[Data from Network Shared Drive\|T1039]] | Data from Network Shared Drive | [RedCurl](https://attack.mitre.org/groups/G1039) has collected data about network drives.[^2] [^1]  |
| [[Taint Shared Content\|T1080]] | Taint Shared Content | [RedCurl](https://attack.mitre.org/groups/G1039) has placed modified LNK files on network drives for lateral movement.[^2] [^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [RedCurl](https://attack.mitre.org/groups/G1039) has used malicious files to infect the victim machines.[^2] [^1] [^4]   |
| [[Data from Local System\|T1005]] | Data from Local System | [RedCurl](https://attack.mitre.org/groups/G1039) has collected data from the local disk of compromised hosts.[^2] [^1]  |
| [[Automated Collection\|T1119]] | Automated Collection | [RedCurl](https://attack.mitre.org/groups/G1039) has used batch scripts to collect data.[^2] [^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [RedCurl](https://attack.mitre.org/groups/G1039) has searched for and collected files on local and network drives.[^3] [^2] [^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [RedCurl](https://attack.mitre.org/groups/G1039) has used the Windows Command Prompt to execute commands.[^2] [^1] [^4]  |
| [[PowerShell\|T1059.001]] | PowerShell | [RedCurl](https://attack.mitre.org/groups/G1039) has used PowerShell to execute commands and to download malware.[^2] [^1] [^4]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [RedCurl](https://attack.mitre.org/groups/G1039) mimicked legitimate file names and scheduled tasks, e.g. ` MicrosoftCurrentupdatesCheck` and<br>`MdMMaintenenceTask` to mask malicious files and scheduled tasks.[^2] [^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [RedCurl](https://attack.mitre.org/groups/G1039) has used phishing emails with malicious files to gain initial access.[^2] [^4]   |
| [[Visual Basic\|T1059.005]] | Visual Basic | [RedCurl](https://attack.mitre.org/groups/G1039) has used VBScript to run malicious files.[^2] [^1]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [RedCurl](https://attack.mitre.org/groups/G1039) has downloaded 7-Zip to decompress password protected archives.[^4]   |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [RedCurl](https://attack.mitre.org/groups/G1039) has used AES-128 CBC to encrypt C2 communications.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [RedCurl](https://attack.mitre.org/groups/G1039) has used HTTP, HTTPS and Webdav protocls for C2 communications.[^2] [^1]   |
| [[Email Account\|T1087.003]] | Email Account | [RedCurl](https://attack.mitre.org/groups/G1039) has collected information about email accounts.[^2] [^1]  |
| [[Malware\|T1587.001]] | Malware | [RedCurl](https://attack.mitre.org/groups/G1039) has created its own tools to use during operations.[^3]  |
| [[Local Account\|T1087.001]] | Local Account | [RedCurl](https://attack.mitre.org/groups/G1039) has collected information about local accounts.[^2] [^1]  |
| [[GUI Input Capture\|T1056.002]] | GUI Input Capture | [RedCurl](https://attack.mitre.org/groups/G1039) prompts the user for credentials through a Microsoft Outlook pop-up.[^2] [^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [RedCurl](https://attack.mitre.org/groups/G1039) has collected information about the target system, such as system information and list of network connections.[^2] [^1]    |
| [[Malicious Link\|T1204.001]] | Malicious Link | [RedCurl](https://attack.mitre.org/groups/G1039) has used malicious links to infect the victim machines.[^2] [^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [RedCurl](https://attack.mitre.org/groups/G1039) has used HTTPS for C2 communication.[^2] [^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [RedCurl](https://attack.mitre.org/groups/G1039) has created scheduled tasks for persistence.[^2] [^1] [^4]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [RedCurl](https://attack.mitre.org/groups/G1039) has used batch scripts to exfiltrate data.[^2] [^1]  |
| [[Trusted Relationship\|T1199]] | Trusted Relationship | [RedCurl](https://attack.mitre.org/groups/G1039) has gained access to a contractor to pivot to the victim’s infrastructure.[^3]  |
| [[Transfer Data to Cloud Account\|T1537]] | Transfer Data to Cloud Account | [RedCurl](https://attack.mitre.org/groups/G1039) has used cloud storage to exfiltrate data, in particular the megatools utilities were used to exfiltrate data to Mega, a file storage service.[^2] [^1]  |
| [[Indirect Command Execution\|T1202]] | Indirect Command Execution | [RedCurl](https://attack.mitre.org/groups/G1039) has used pcalua.exe to obfuscate binary execution and remote connections.[^4]   |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [RedCurl](https://attack.mitre.org/groups/G1039) used [LaZagne](https://attack.mitre.org/software/S0349) to obtain passwords in files.[^2] [^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [RedCurl](https://attack.mitre.org/groups/G1039) has used rundll32.exe to execute malicious files.[^2] [^1] [^4]   |
| [[Domain Account\|T1087.002]] | Domain Account | [RedCurl](https://attack.mitre.org/groups/G1039) has collected information about domain accounts using SysInternal’s AdExplorer functionality   .[^2] [^1]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [RedCurl](https://attack.mitre.org/groups/G1039) has used phishing emails with malicious links to gain initial access.[^2] [^1]  |
| [[Credentials in Registry\|T1552.002]] | Credentials in Registry | [RedCurl](https://attack.mitre.org/groups/G1039) used [LaZagne](https://attack.mitre.org/software/S0349) to obtain passwords in the Registry.[^2] [^1]       |
| [[File Deletion\|T1070.004]] | File Deletion | [RedCurl](https://attack.mitre.org/groups/G1039) has deleted files after execution.[^2] [^1] [^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [RedCurl](https://attack.mitre.org/groups/G1039) has established persistence by creating entries in `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`.[^2] [^1]    |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [RedCurl](https://attack.mitre.org/groups/G1039) used [LaZagne](https://attack.mitre.org/software/S0349) to obtain passwords from web browsers.[^2] [^1]  |
| [[Python\|T1059.006]] | Python | [RedCurl](https://attack.mitre.org/groups/G1039) has used a Python script to establish outbound communication and to execute commands using SMB port 445.[^4]   |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [RedCurl](https://attack.mitre.org/groups/G1039) used [LaZagne](https://attack.mitre.org/software/S0349) to obtain passwords from memory.[^2] [^1]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [RedCurl](https://attack.mitre.org/groups/G1039) has used netstat to check if port 4119 is open.[^4]   |




## References

[^1]: [group-ib_redcurl2](https://www.group-ib.com/resources/research-hub/red-curl-2/)


[^2]: [group-ib_redcurl1](https://www.group-ib.com/resources/research-hub/red-curl/)


[^3]: [therecord_redcurl](https://therecord.media/redcurl-hackers-russian-bank-australian-company)


[^4]: [trendmicro_redcurl](https://www.trendmicro.com/en_us/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)


