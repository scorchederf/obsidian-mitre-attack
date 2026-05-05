---
aliases: 
    - S0569
    
mitre-attack: https://attack.mitre.org/software/S0569
---

## S0569

[Explosive](https://attack.mitre.org/software/S0569) is a custom-made remote access tool used by the group [Volatile Cedar](https://attack.mitre.org/groups/G0123). It was first identified in the wild in 2015.[^1] [^3]   

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery |  [Explosive](https://attack.mitre.org/software/S0569) has collected the MAC address from the victim's machine.[^1]   |
| [[Modify Registry\|T1112]] | Modify Registry | [Explosive](https://attack.mitre.org/software/S0569) has a function to write itself to Registry values.[^1]   |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | [Explosive](https://attack.mitre.org/software/S0569) can scan all .exe files located in the USB drive.[^1]   |
| [[Keylogging\|T1056.001]] | Keylogging | [Explosive](https://attack.mitre.org/software/S0569) has leveraged its keylogging capabilities to gain access to administrator accounts on target servers.[^1] [^3]   |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Explosive](https://attack.mitre.org/software/S0569) has collected the username from the infected host.[^1]   |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Explosive](https://attack.mitre.org/software/S0569) has encrypted communications with the RC4 method.[^3]   |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Explosive](https://attack.mitre.org/software/S0569) has a function to download a file to the infected system.[^1]   |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Explosive](https://attack.mitre.org/software/S0569) has used HTTP for communication.[^1]  |
| [[Native API\|T1106]] | Native API | [Explosive](https://attack.mitre.org/software/S0569) has a function to call the OpenClipboard wrapper.[^1]    |
| [[Clipboard Data\|T1115]] | Clipboard Data | [Explosive](https://attack.mitre.org/software/S0569) has a function to use the OpenClipboard wrapper.[^1]   |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Explosive](https://attack.mitre.org/software/S0569) has collected the computer name from the infected host.[^1]   |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [Explosive](https://attack.mitre.org/software/S0569) has commonly set file and path attributes to hidden.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Volatile Cedar\|G0123]] | Volatile Cedar |



## References

[^1]: [CheckPoint Volatile Cedar March 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)


[^2]: Explosive


[^3]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)


