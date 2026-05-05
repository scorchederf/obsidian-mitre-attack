---
aliases: 
    - S0058
    
mitre-attack: https://attack.mitre.org/software/S0058
---

## S0058

[SslMM](https://attack.mitre.org/software/S0058) is a full-featured backdoor used by [Naikon](https://attack.mitre.org/groups/G0019) that has multiple variants. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [SslMM](https://attack.mitre.org/software/S0058) sends the logged-on username to its hard-coded C2.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [SslMM](https://attack.mitre.org/software/S0058) has a hard-coded primary and backup C2 string.[^1]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | To establish persistence, [SslMM](https://attack.mitre.org/software/S0058) identifies the Start Menu Startup directory and drops a link to its own executable disguised as an “Office Start,” “Yahoo Talk,” “MSN Gaming Z0ne,” or “MSN Talk” shortcut.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | To establish persistence, [SslMM](https://attack.mitre.org/software/S0058) identifies the Start Menu Startup directory and drops a link to its own executable disguised as an “Office Start,” “Yahoo Talk,” “MSN Gaming Z0ne,” or “MSN Talk” shortcut.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [SslMM](https://attack.mitre.org/software/S0058) creates a new thread implementing a keylogging facility using Windows Keyboard Accelerators.[^1]  |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [SslMM](https://attack.mitre.org/software/S0058) contains a feature to manipulate process privileges and tokens.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | To establish persistence, [SslMM](https://attack.mitre.org/software/S0058) identifies the Start Menu Startup directory and drops a link to its own executable disguised as an “Office Start,” “Yahoo Talk,” “MSN Gaming Z0ne,” or “MSN Talk” shortcut.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [SslMM](https://attack.mitre.org/software/S0058) identifies and kills anti-malware processes.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SslMM](https://attack.mitre.org/software/S0058) sends information to its hard-coded C2, including OS version, service pack information, processor speed, system name, and OS install date.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Naikon\|G0019]] | Naikon |



## References

[^1]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)


[^2]: [CameraShy](http://cdn2.hubspot.net/hubfs/454298/Project_CAMERASHY_ThreatConnect_Copyright_2015.pdf)


