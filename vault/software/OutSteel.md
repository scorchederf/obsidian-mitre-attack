---
aliases: 
    - S1017
    
mitre-attack: https://attack.mitre.org/software/S1017
---

## S1017

[OutSteel](https://attack.mitre.org/software/S1017) is a file uploader and document stealer developed with the scripting language AutoIT that has been used by [Saint Bear](https://attack.mitre.org/groups/G1031) since at least March 2021.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [OutSteel](https://attack.mitre.org/software/S1017) has used `cmd.exe` to scan a compromised host for specific file extensions.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [OutSteel](https://attack.mitre.org/software/S1017) can upload files from a compromised host over its C2 channel.[^1]   |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [OutSteel](https://attack.mitre.org/software/S1017) has been distributed through malicious links contained within spearphishing emails.[^1]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [OutSteel](https://attack.mitre.org/software/S1017) has relied on a user to click a malicious link within a spearphishing email.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [OutSteel](https://attack.mitre.org/software/S1017) can collect information from a compromised host.[^1]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [OutSteel](https://attack.mitre.org/software/S1017) can automatically upload collected files to its C2 server.[^1]  |
| [[AutoHotKey & AutoIT\|T1059.010]] | AutoHotKey & AutoIT | [OutSteel](https://attack.mitre.org/software/S1017) was developed using the AutoIT scripting language.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [OutSteel](https://attack.mitre.org/software/S1017) can search for specific file extensions, including zipped files.[^1]  |
| [[Automated Collection\|T1119]] | Automated Collection | [OutSteel](https://attack.mitre.org/software/S1017) can automatically scan for and collect files with specific extensions.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [OutSteel](https://attack.mitre.org/software/S1017) has relied on a user to execute a malicious attachment delivered via spearphishing.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [OutSteel](https://attack.mitre.org/software/S1017) has been distributed as a malicious attachment within a spearphishing email.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [OutSteel](https://attack.mitre.org/software/S1017) can delete itself following the successful execution of a follow-on payload.[^1]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [OutSteel](https://attack.mitre.org/software/S1017) can download the [Saint Bot](https://attack.mitre.org/software/S1018) malware for follow-on execution.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [OutSteel](https://attack.mitre.org/software/S1017) has used HTTP for C2 communications.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [OutSteel](https://attack.mitre.org/software/S1017) can download files from its C2 server.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [OutSteel](https://attack.mitre.org/software/S1017) can identify running processes on a compromised host.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [OutSteel](https://attack.mitre.org/software/S1017) attempts to download and execute [Saint Bot](https://attack.mitre.org/software/S1018) to a statically-defined location attempting to mimic svchost: `%TEMP%\\svjhost.exe`.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Saint Bear\|G1031]] | Saint Bear |



## References

[^1]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)


