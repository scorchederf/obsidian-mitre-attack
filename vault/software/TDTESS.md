---
aliases: 
    - S0164
    
mitre-attack: https://attack.mitre.org/software/S0164
---

## S0164

[TDTESS](https://attack.mitre.org/software/S0164) is a 64-bit .NET binary backdoor used by [CopyKittens](https://attack.mitre.org/groups/G0052). [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File Deletion\|T1070.004]] | File Deletion | [TDTESS](https://attack.mitre.org/software/S0164) creates then deletes log files during installation of itself as a service.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [TDTESS](https://attack.mitre.org/software/S0164) has a command to download and execute an additional file.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [TDTESS](https://attack.mitre.org/software/S0164) provides a reverse shell on the victim.[^2]  |
| [[Timestomp\|T1070.006]] | Timestomp | After creating a new service for persistence, [TDTESS](https://attack.mitre.org/software/S0164) sets the file creation time for the service to the creation time of the victim's legitimate svchost.exe file.[^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | If running as administrator, [TDTESS](https://attack.mitre.org/software/S0164) installs itself as a new service named bmwappushservice to establish persistence.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[CopyKittens\|G0052]] | CopyKittens |



## References

[^1]: TDTESS


[^2]: [ClearSky Wilted Tulip July 2017](http://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf)


