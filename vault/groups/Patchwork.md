---
aliases: 
    - Patchwork
    - Hangover Group
    - Dropping Elephant
    - Chinastrats
    - MONSOON
    - Operation Hangover
mitre-attack: https://attack.mitre.org/groups/G0040
---

## G0040

[Patchwork](https://attack.mitre.org/groups/G0040) is a cyber espionage group that was first observed in December 2015. While the group has not been definitively attributed, circumstantial evidence suggests the group may be a pro-Indian or Indian entity. [Patchwork](https://attack.mitre.org/groups/G0040) has been seen targeting industries related to diplomatic and government agencies. Much of the code used by this group was copied and pasted from online forums. [Patchwork](https://attack.mitre.org/groups/G0040) was also seen operating spearphishing campaigns targeting U.S. think tank groups in March and April of 2018.[^10]  [^11] [^13] [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Patchwork](https://attack.mitre.org/groups/G0040) used Visual Basic Scripts (VBS) on victim machines.[^13] [^2]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Patchwork](https://attack.mitre.org/groups/G0040) encrypted the collected files' path with AES and then encoded them with base64.[^13]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | A [Patchwork](https://attack.mitre.org/groups/G0040) payload has searched all fixed drives on the victim for files matching a specified list of extensions.[^10] [^13]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Patchwork](https://attack.mitre.org/groups/G0040) has signed malware with self-signed certificates from fictitious and spoofed legitimate software companies.[^14]  |
| [[DLL\|T1574.001]] | DLL | A [Patchwork](https://attack.mitre.org/groups/G0040) .dll that contains [BADNEWS](https://attack.mitre.org/software/S0128) is loaded and executed using DLL side-loading.[^13]  |
| [[Modify Registry\|T1112]] | Modify Registry | A [Patchwork](https://attack.mitre.org/groups/G0040) payload deletes Resiliency Registry keys created by Microsoft Office applications in an apparent effort to trick users into thinking there were no issues during application runs.[^13]  |
| [[BITS Jobs\|T1197]] | BITS Jobs | [Patchwork](https://attack.mitre.org/groups/G0040) has used BITS jobs to download malicious payloads.[^14]  |
| [[Indicator Removal from Tools\|T1027.005]] | Indicator Removal from Tools | [Patchwork](https://attack.mitre.org/groups/G0040) apparently altered [NDiskMonitor](https://attack.mitre.org/software/S0272) samples by adding four bytes of random letters in a likely attempt to change the file hashes.[^13]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Patchwork](https://attack.mitre.org/groups/G0040) dumped the login data database from `\AppData\Local\Google\Chrome\User Data\Default\Login Data`.[^10]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | A [Patchwork](https://attack.mitre.org/groups/G0040) file stealer can run a TaskScheduler DLL to add persistence.[^13]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Patchwork](https://attack.mitre.org/groups/G0040) used Base64 to encode C2 traffic.[^10]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | A [Patchwork](https://attack.mitre.org/groups/G0040) payload uses process hollowing to hide the UAC bypass vulnerability exploitation inside svchost.exe.[^10]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Patchwork](https://attack.mitre.org/groups/G0040) attempted to use RDP to move laterally.[^10]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Patchwork](https://attack.mitre.org/groups/G0040) has added the path of its second-stage malware to the startup folder to achieve persistence. One of its file stealers has also persisted by adding a Registry Run key.[^10] [^13]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Patchwork](https://attack.mitre.org/groups/G0040) copied all targeted files to a directory called index that was eventually uploaded to the C&C server.[^13]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Patchwork](https://attack.mitre.org/groups/G0040) installed its payload in the startup programs folder as "Baidu Software Update." The group also adds its second stage payload to the startup programs as “Net Monitor."[^10]  They have also dropped [QuasarRAT](https://attack.mitre.org/software/S0262) binaries as files named microsoft_network.exe and crome.exe.[^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Patchwork](https://attack.mitre.org/groups/G0040) has used spearphishing with an attachment to deliver files with exploits to initial victims.[^10] [^15] [^13] [^2]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Patchwork](https://attack.mitre.org/groups/G0040) has obfuscated a script with Crypto Obfuscator.[^13]  |
| [[Tool\|T1588.002]] | Tool | [Patchwork](https://attack.mitre.org/groups/G0040) has obtained and used open-source tools such as [QuasarRAT](https://attack.mitre.org/software/S0262).[^2]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Patchwork](https://attack.mitre.org/groups/G0040) has used watering holes to deliver files with exploits to initial victims.[^11] [^2]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Patchwork](https://attack.mitre.org/groups/G0040) has used spearphishing with links to try to get users to click, download and open malicious files.[^11] [^13] [^2] [^14]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Patchwork](https://attack.mitre.org/groups/G0040) scanned the “Program Files” directories for a directory with the string “Total Security” (the installation path of the “360 Total Security” antivirus tool).[^10]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Patchwork](https://attack.mitre.org/groups/G0040) uses malicious documents to deliver remote execution exploits as part of. The group has previously exploited CVE-2017-8570, CVE-2012-1856, CVE-2014-4114, CVE-2017-0199, CVE-2017-11882, and CVE-2015-1641.[^10] [^15] [^11] [^8] [^13] [^2] [^14]  |
| [[Software Packing\|T1027.002]] | Software Packing | A [Patchwork](https://attack.mitre.org/groups/G0040) payload was packed with UPX.[^15]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Patchwork](https://attack.mitre.org/groups/G0040) collected the victim username and whether it was running as admin, then sent the information to its C2 server.[^10] [^13]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Patchwork](https://attack.mitre.org/groups/G0040) collected and exfiltrated files from the infected system.[^10]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Patchwork](https://attack.mitre.org/groups/G0040) embedded a malicious macro in a Word document and lured the victim to click on an icon to execute the malware.[^13] [^2]  |
| [[Code Signing Certificates\|T1587.002]] | Code Signing Certificates | [Patchwork](https://attack.mitre.org/groups/G0040) has created self-signed certificates from fictitious and spoofed legitimate software companies that were later used to sign malware.[^14]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Patchwork](https://attack.mitre.org/groups/G0040) removed certain files and replaced them so they could not be retrieved.[^13]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Patchwork](https://attack.mitre.org/groups/G0040) developed a file stealer to search C:\ and collect files with certain extensions. [Patchwork](https://attack.mitre.org/groups/G0040) also executed a script to enumerate all drives, store them as a list, and upload generated files to the C2 server.[^13]  |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | [Patchwork](https://attack.mitre.org/groups/G0040) hides base64-encoded and encrypted C2 server locations in comments on legitimate websites.[^15]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Patchwork](https://attack.mitre.org/groups/G0040) enumerated all available drives on the victim's machine.[^10] [^13]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Patchwork](https://attack.mitre.org/groups/G0040) ran a reverse shell with Meterpreter.[^10]  [Patchwork](https://attack.mitre.org/groups/G0040) used JavaScript code and .SCT files on victim machines.[^13] [^2]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [Patchwork](https://attack.mitre.org/groups/G0040) apparently altered [NDiskMonitor](https://attack.mitre.org/software/S0272) samples by adding four bytes of random letters in a likely attempt to change the file hashes.[^13]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Patchwork](https://attack.mitre.org/groups/G0040) bypassed User Access Control (UAC).[^10]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Patchwork](https://attack.mitre.org/groups/G0040) used [PowerSploit](https://attack.mitre.org/software/S0194) to download payloads, run a reverse shell, and execute malware on the victim's machine.[^10] [^13]  |
| [[Spearphishing Link\|T1598.003]] | Spearphishing Link | [Patchwork](https://attack.mitre.org/groups/G0040) has used embedded image tags (known as web bugs) with unique, per-recipient tracking links in their emails for the purpose of identifying which recipients opened messages.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Patchwork](https://attack.mitre.org/groups/G0040) payloads download additional files from the C2 server.[^15] [^13]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Patchwork](https://attack.mitre.org/groups/G0040) has used spearphishing with links to deliver files with exploits to initial victims.[^11] [^13] [^14]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Patchwork](https://attack.mitre.org/groups/G0040) collected the victim computer name, OS version, and architecture type and sent the information to its C2 server.[^10] [^13]  |
| [[Dynamic Data Exchange\|T1559.002]] | Dynamic Data Exchange | [Patchwork](https://attack.mitre.org/groups/G0040) leveraged the DDE protocol to deliver their malware.[^13]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[PowerSploit\|S0194]] | PowerSploit | [^10]  |
| [[QuasarRAT\|S0262]] | QuasarRAT | [^13] [^2]  |
| [[TINYTYPHON\|S0131]] | TINYTYPHON | [^9]  |
| [[Unknown Logger\|S0130]] | Unknown Logger | [^9]  |
| [[BackConfig\|S0475]] | BackConfig | [^14]  |
| [[NDiskMonitor\|S0272]] | NDiskMonitor | [^13]  |
| [[BADNEWS\|S0128]] | BADNEWS | [^9] [^13]  |
| [[AutoIt backdoor\|S0129]] | AutoIt backdoor | [^9]  |



## References

[^1]: Operation Hangover


[^2]: [Volexity Patchwork June 2018](https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/)


[^3]: Hangover Group


[^4]: Chinastrats


[^5]: MONSOON


[^6]: Dropping Elephant


[^7]: Patchwork


[^8]: [PaloAlto Patchwork Mar 2018](https://researchcenter.paloaltonetworks.com/2018/03/unit42-patchwork-continues-deliver-badnews-indian-subcontinent/)


[^9]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)


[^10]: [Cymmetria Patchwork](https://web.archive.org/web/20180825085952/https:/s3-us-west-2.amazonaws.com/cymmetria-blog/public/Unveiling_Patchwork.pdf)


[^11]: [Symantec Patchwork](http://www.symantec.com/connect/blogs/patchwork-cyberespionage-group-expands-targets-governments-wide-range-industries)


[^12]: [Operation Hangover May 2013](https://web.archive.org/web/20140424084220/http://enterprise-manage.norman.c.bitbit.net/resources/files/Unveiling_an_Indian_Cyberattack_Infrastructure.pdf)


[^13]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)


[^14]: [Unit 42 BackConfig May 2020](https://unit42.paloaltonetworks.com/updated-backconfig-malware-targeting-government-and-military-organizations/)


[^15]: [Securelist Dropping Elephant](https://securelist.com/the-dropping-elephant-actor/75328/)


