---
aliases: 
    - S0165
    
mitre-attack: https://attack.mitre.org/software/S0165
---

## S0165

[OSInfo](https://attack.mitre.org/software/S0165) is a custom tool used by [APT3](https://attack.mitre.org/groups/G0022) to do internal discovery on a victim's computer and network. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Local Account\|T1087.001]] | Local Account | [OSInfo](https://attack.mitre.org/software/S0165) enumerates local and domain users[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [OSInfo](https://attack.mitre.org/software/S0165) queries the registry to look for information about Terminal Services.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [OSInfo](https://attack.mitre.org/software/S0165) discovers information about the infected machine.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [OSInfo](https://attack.mitre.org/software/S0165) enumerates the current network connections similar to ` net use `.[^1]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [OSInfo](https://attack.mitre.org/software/S0165) performs a connection test to discover remote systems in the network[^1]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [OSInfo](https://attack.mitre.org/software/S0165) specifically looks for Domain Admins and power users within the domain.[^1]   |
| [[Domain Account\|T1087.002]] | Domain Account | [OSInfo](https://attack.mitre.org/software/S0165) enumerates local and domain users[^1]  |
| [[Local Groups\|T1069.001]] | Local Groups | [OSInfo](https://attack.mitre.org/software/S0165) has enumerated the local administrators group.[^1]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [OSInfo](https://attack.mitre.org/software/S0165) discovers shares on the network[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [OSInfo](https://attack.mitre.org/software/S0165) discovers the current domain information.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT3\|G0022]] | APT3 |



## References

[^1]: [Symantec Buckeye](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)


