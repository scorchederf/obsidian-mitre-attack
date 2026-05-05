---
aliases: 
    - S0166
    
mitre-attack: https://attack.mitre.org/software/S0166
---

## S0166

[RemoteCMD](https://attack.mitre.org/software/S0166) is a custom tool used by [APT3](https://attack.mitre.org/groups/G0022) to execute commands on a remote system similar to SysInternal's PSEXEC functionality. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Service Execution\|T1569.002]] | Service Execution | [RemoteCMD](https://attack.mitre.org/software/S0166) can execute commands remotely by creating a new service on the remote system.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [RemoteCMD](https://attack.mitre.org/software/S0166) can execute commands remotely by creating a new schedule task on the remote system[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [RemoteCMD](https://attack.mitre.org/software/S0166) copies a file over to the remote system before execution.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT3\|G0022]] | APT3 |



## References

[^1]: [Symantec Buckeye](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)


