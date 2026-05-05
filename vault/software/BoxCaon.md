---
aliases: 
    - S0651
    
mitre-attack: https://attack.mitre.org/software/S0651
---

## S0651

[BoxCaon](https://attack.mitre.org/software/S0651) is a Windows backdoor that was used by [IndigoZebra](https://attack.mitre.org/groups/G0136) in a 2021 spearphishing campaign against Afghan government officials. [BoxCaon](https://attack.mitre.org/software/S0651)'s name stems from similarities shared with the malware family [xCaon](https://attack.mitre.org/software/S0653).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [BoxCaon](https://attack.mitre.org/software/S0651) has used DropBox for C2 communications.[^1]   |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [BoxCaon](https://attack.mitre.org/software/S0651) can execute arbitrary commands and utilize the "ComSpec" environment variable.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [BoxCaon](https://attack.mitre.org/software/S0651) has searched for files on the system, such as documents located in the desktop folder.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BoxCaon](https://attack.mitre.org/software/S0651) can download files.[^1]  |
| [[Native API\|T1106]] | Native API | [BoxCaon](https://attack.mitre.org/software/S0651) has used Windows API calls to obtain information about the compromised host.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [BoxCaon](https://attack.mitre.org/software/S0651) can upload files from a compromised host.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [BoxCaon](https://attack.mitre.org/software/S0651) uploads files and data from a compromised host over the existing C2 channel.[^1]  |
| [[Boot or Logon Autostart Execution\|T1547]] | Boot or Logon Autostart Execution | [BoxCaon](https://attack.mitre.org/software/S0651) established persistence by setting the `HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Windows\load` registry key to point to its executable.[^1]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [BoxCaon](https://attack.mitre.org/software/S0651) has the capability to download folders' contents on the system and upload the results back to its Dropbox drive.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [BoxCaon](https://attack.mitre.org/software/S0651) used the "StackStrings" obfuscation technique to hide malicious functionalities.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [BoxCaon](https://attack.mitre.org/software/S0651) can collect the victim's MAC address by using the `GetAdaptersInfo` API.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [BoxCaon](https://attack.mitre.org/software/S0651) has created a working folder for collected files that it sends to the C2 server.[^1]   |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[IndigoZebra\|G0136]] | IndigoZebra |



## References

[^1]: [Checkpoint IndigoZebra July 2021](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)


[^2]: [HackerNews IndigoZebra July 2021](https://thehackernews.com/2021/07/indigozebra-apt-hacking-campaign.html)


[^3]: BoxCaon


