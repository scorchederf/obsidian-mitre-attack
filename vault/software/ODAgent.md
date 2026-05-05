---
aliases: 
    - S1170
    
mitre-attack: https://attack.mitre.org/software/S1170
---

## S1170

[ODAgent](https://attack.mitre.org/software/S1170) is a C#/.NET downloader that has been used by [OilRig](https://attack.mitre.org/groups/G0049) since at least 2022 including against target organizations in Israel to download and execute payloads and to exfiltrate staged files.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [ODAgent](https://attack.mitre.org/software/S1170) can use an attacker-controlled OneDrive account for exfiltration.[^1]   |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [ODAgent](https://attack.mitre.org/software/S1170) can use the Microsoft Graph API to access an attacker-controlled OneDrive account and retrieve payloads and backdoor commands.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [ODAgent](https://attack.mitre.org/software/S1170) can execute a specified command line passed via API.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [ODAgent](https://attack.mitre.org/software/S1170) has the ability to download and execute files on compromised systems.[^1]  |
| [[Native API\|T1106]] | Native API | [ODAgent](https://attack.mitre.org/software/S1170) can pass commands using native APIs.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [ODAgent](https://attack.mitre.org/software/S1170) can identify the current working directory.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [ODAgent](https://attack.mitre.org/software/S1170) can use an attacker-controlled OneDrive account to receive C2 commands and to exfiltrate files.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [ODAgent](https://attack.mitre.org/software/S1170) can delete payloads and files used to pass C2 commands from remotely hosted cloud accounts.[^1]   |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [ODAgent](https://attack.mitre.org/software/S1170) can Base64-decode and XOR decrypt received C2 commands.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[OilRig\|G0049]] | OilRig |



## References

[^1]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)


