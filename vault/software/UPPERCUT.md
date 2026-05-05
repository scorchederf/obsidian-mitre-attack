---
aliases: 
    - S0275
    
mitre-attack: https://attack.mitre.org/software/S0275
---

## S0275

[UPPERCUT](https://attack.mitre.org/software/S0275) is a 32-bit HTTP-based backdoor that has been used by [menuPass](https://attack.mitre.org/groups/G0045) since at least 2017.[^6]  Once thought to be exclusive to [menuPass](https://attack.mitre.org/groups/G0045), [UPPERCUT](https://attack.mitre.org/software/S0275) was also observed being used by [menuPass](https://attack.mitre.org/groups/G0045)-associated [MirrorFace](https://attack.mitre.org/groups/G1054) during [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060).[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [UPPERCUT](https://attack.mitre.org/software/S0275) has used HTTP for C2, including sending error codes in cookie headers.[^6] [^2] [^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [UPPERCUT](https://attack.mitre.org/software/S0275) has the capability to obtain the time zone information and the current timestamp of the victim’s machine.[^6]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [UPPERCUT](https://attack.mitre.org/software/S0275) has the capability to collect the current logged on user’s username from a machine.[^6]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [UPPERCUT](https://attack.mitre.org/software/S0275) uses cmd.exe to execute commands on the victim’s machine.[^6]  |
| [[DLL\|T1574.001]] | DLL | [UPPERCUT](https://attack.mitre.org/software/S0275) has been sideloaded through a legitimately signed application from the JustSystems Corporation.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [UPPERCUT](https://attack.mitre.org/software/S0275) can capture desktop screenshots in the PNG format and send them to the C2 server.[^6] [^3] [^2] [^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | Some versions of [UPPERCUT](https://attack.mitre.org/software/S0275) have used the hard-coded string “this is the encrypt key” for Blowfish encryption when communicating with a C2. Later versions have hard-coded keys uniquely for each C2 address.[^6]  [UPPERCUT](https://attack.mitre.org/software/S0275) has also used custom ChaCha20, XOR, and LZO algorithms for C2 communication.[^3] [^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [UPPERCUT](https://attack.mitre.org/software/S0275) has the capability to gather the victim's proxy information.[^6]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [UPPERCUT](https://attack.mitre.org/software/S0275) can base64 encode C2 communications.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [UPPERCUT](https://attack.mitre.org/software/S0275) has the capability to gather the system’s hostname and OS version.[^6] [^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [UPPERCUT](https://attack.mitre.org/software/S0275) can download and upload files to and from the victim’s machine.[^6] [^3] [^2] <br> |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [UPPERCUT](https://attack.mitre.org/software/S0275) contains functionality to bypass UAC.[^3] [^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [UPPERCUT](https://attack.mitre.org/software/S0275) can upload files to the C2 from infected machines.[^3] [^2]  |
| [[Delay Execution\|T1678]] | Delay Execution | [UPPERCUT](https://attack.mitre.org/software/S0275) can use a sleep function to delay execution.[^3] [^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [UPPERCUT](https://attack.mitre.org/software/S0275) has the capability to gather the victim's current directory.[^6]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[menuPass\|G0045]] | menuPass |
| [[MirrorFace\|G1054]] | MirrorFace |



## References

[^1]: [ESET MirrorFace 2025](https://www.welivesecurity.com/en/eset-research/operation-akairyu-mirrorface-invites-europe-expo-2025-revives-anel-backdoor/)


[^2]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)


[^3]: [Trend Micro Earth Kasha Updates APR 2025](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)


[^4]: UPPERCUT


[^5]: ANEL


[^6]: [FireEye APT10 Sept 2018](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)


