---
aliases: 
    - S9022
    
mitre-attack: https://attack.mitre.org/software/S9022
---

## S9022

[MirrorStealer](https://attack.mitre.org/software/S9022) is a credential stealer that has been used by [MirrorFace](https://attack.mitre.org/groups/G1054) since at least 2022 to steal credentials from various applications, including browsers and email clients. [MirrorStealer](https://attack.mitre.org/software/S9022) has been delivered directly into system memory via commands issued by [LODEINFO](https://attack.mitre.org/software/S9020).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [MirrorStealer](https://attack.mitre.org/software/S9022) has the ability to steal credentials from email clients.[^1] [^2]  |
| [[Group Policy Preferences\|T1552.006]] | Group Policy Preferences | [MirrorStealer](https://attack.mitre.org/software/S9022) can target Group Policy Preferences for credentials.[^2]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [MirrorStealer](https://attack.mitre.org/software/S9022) has stored stolen credentials on the local machine in `%TEMP%\31558.txt`.[^1]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [MirrorStealer](https://attack.mitre.org/software/S9022) can steal credentials stored in browsers.[^1] [^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MirrorFace\|G1054]] | MirrorFace |



## References

[^1]: [ESET MirrorFace DEC 2022](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)


[^2]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)


