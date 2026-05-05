---
aliases: 
    - S0028
    
mitre-attack: https://attack.mitre.org/software/S0028
---

## S0028

[SHIPSHAPE](https://attack.mitre.org/software/S0028) is malware developed by [APT30](https://attack.mitre.org/groups/G0013) that allows propagation and exfiltration of data over removable devices. [APT30](https://attack.mitre.org/groups/G0013) may use this capability to exfiltrate data across air-gaps. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [SHIPSHAPE](https://attack.mitre.org/software/S0028) achieves persistence by creating a shortcut in the Startup folder.[^1]  |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [APT30](https://attack.mitre.org/groups/G0013) may have used the [SHIPSHAPE](https://attack.mitre.org/software/S0028) malware to move onto air-gapped networks. [SHIPSHAPE](https://attack.mitre.org/software/S0028) targets removable drives to spread to other systems by modifying the drive to use Autorun to execute or by hiding legitimate document files and copying an executable to the folder with the same name as the legitimate document.[^1]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [SHIPSHAPE](https://attack.mitre.org/software/S0028) achieves persistence by creating a shortcut in the Startup folder.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT30\|G0013]] | APT30 |



## References

[^1]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)


