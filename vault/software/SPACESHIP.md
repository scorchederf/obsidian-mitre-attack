---
aliases: 
    - S0035
    
mitre-attack: https://attack.mitre.org/software/S0035
---

## S0035

[SPACESHIP](https://attack.mitre.org/software/S0035) is malware developed by [APT30](https://attack.mitre.org/groups/G0013) that allows propagation and exfiltration of data over removable devices. [APT30](https://attack.mitre.org/groups/G0013) may use this capability to exfiltrate data across air-gaps. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Exfiltration over USB\|T1052.001]] | Exfiltration over USB | [SPACESHIP](https://attack.mitre.org/software/S0035) copies staged data to removable drives when they are inserted into the system.[^1]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | Data [SPACESHIP](https://attack.mitre.org/software/S0035) copies to the staging area is compressed with zlib. Bytes are rotated by four positions and XOR'ed with 0x23.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [SPACESHIP](https://attack.mitre.org/software/S0035) achieves persistence by creating a shortcut in the current user's Startup folder.[^1]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [SPACESHIP](https://attack.mitre.org/software/S0035) achieves persistence by creating a shortcut in the current user's Startup folder.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [SPACESHIP](https://attack.mitre.org/software/S0035) identifies files with certain extensions and copies them to a directory in the user's profile.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [SPACESHIP](https://attack.mitre.org/software/S0035) identifies files and directories for collection by searching for specific file extensions or file modification time.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT30\|G0013]] | APT30 |



## References

[^1]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)


