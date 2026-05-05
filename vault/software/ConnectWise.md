---
aliases: 
    - S0591
    
mitre-attack: https://attack.mitre.org/software/S0591
---

## S0591

[ConnectWise](https://attack.mitre.org/software/S0591) is a legitimate remote administration tool that has been used since at least 2016 by threat actors including [MuddyWater](https://attack.mitre.org/groups/G0069) and [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) to connect to and conduct lateral movement in target environments.[^2] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Video Capture\|T1125]] | Video Capture | [ConnectWise](https://attack.mitre.org/software/S0591) can record video on remote hosts.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [ConnectWise](https://attack.mitre.org/software/S0591) can be used to execute PowerShell commands on target machines.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [ConnectWise](https://attack.mitre.org/software/S0591) can take screenshots on remote hosts.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[GOLD SOUTHFIELD\|G0115]] | GOLD SOUTHFIELD |
| [[MuddyWater\|G0069]] | MuddyWater |
| [[Scattered Spider\|G1015]] | Scattered Spider |



## References

[^1]: [Mandiant UNC3944 May 2025](https://cloud.google.com/blog/topics/threat-intelligence/unc3944-proactive-hardening-recommendations)


[^2]: [Anomali Static Kitten February 2021](https://www.anomali.com/blog/probable-iranian-cyber-actors-static-kitten-conducting-cyberespionage-campaign-targeting-uae-and-kuwait-government-agencies)


[^3]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)


[^4]: ScreenConnect


[^5]: [Check Point Scattered Spider JUL 2025](https://blog.checkpoint.com/research/exposing-scattered-spider-new-indicators-highlight-growing-threat-to-enterprises-and-aviation/)


[^6]: [Tetra Defense Sodinokibi March 2020](https://web.archive.org/web/20210414101816/https://tetradefense.com/incident-response-services/cause-and-effect-sodinokibi-ransomware-analysis/)


