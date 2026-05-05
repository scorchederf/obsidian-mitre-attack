---
aliases: 
    - S9030
    
mitre-attack: https://attack.mitre.org/software/S9030
---

## S9030

[SameCoin](https://attack.mitre.org/software/S9030) is a multi-platform wiper with Windows and Android versions that has been used by [WIRTE](https://attack.mitre.org/groups/G0090) to target entities in the Middle East including in Israel.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Internal Spearphishing\|T1534]] | Internal Spearphishing | [SameCoin](https://attack.mitre.org/software/S9030) can send its Setup.exe file as an attachment to other addresses in the same compromised organization.[^1]  |
| [[Data Destruction\|T1485]] | Data Destruction | [SameCoin](https://attack.mitre.org/software/S9030) can overwrite designated files on targeted systems with random bytes.[^1]  |
| [[Internal Defacement\|T1491.001]] | Internal Defacement | [SameCoin](https://attack.mitre.org/software/S9030) can alter the victim’s background to display an image showing the name of Hamas’s military wing.[^1]  |
| [[System Location Discovery\|T1614]] | System Location Discovery | [SameCoin](https://attack.mitre.org/software/S9030) can attempt to connect to the Israel Home Front Command site, oref.org[.]il, which is only reachable from within Israel to verify the target's location.[^1]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [SameCoin](https://attack.mitre.org/software/S9030) can copy its wiper executable to remote machines within the same Active Directory.[^1]  |
| [[Selective Exclusion\|T1679]] | Selective Exclusion | [SameCoin](https://attack.mitre.org/software/S9030) can avoid overwriting file names that contain “desktop.ini” and “conf.conf." [^1] <br> |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [SameCoin](https://attack.mitre.org/software/S9030) can list all system files and can avoid wiping specific directories such as Program Files, Windows, and Users.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [SameCoin](https://attack.mitre.org/software/S9030) has named files to appear legitimate such as "MicrosoftEdge.exe."[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [SameCoin](https://attack.mitre.org/software/S9030) has the ability to set a scheduled task for execution.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[WIRTE\|G0090]] | WIRTE |



## References

[^1]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)


