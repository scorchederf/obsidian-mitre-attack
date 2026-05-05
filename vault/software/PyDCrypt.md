---
aliases: 
    - S1032
    
mitre-attack: https://attack.mitre.org/software/S1032
---

## S1032

[PyDCrypt](https://attack.mitre.org/software/S1032) is malware written in Python designed to deliver [DCSrv](https://attack.mitre.org/software/S1033). It has been used by [Moses Staff](https://attack.mitre.org/groups/G1009) since at least September 2021, with each sample tailored for its intended victim organization.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Python\|T1059.006]] | Python | [PyDCrypt](https://attack.mitre.org/software/S1032), along with its functions, is written in Python.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [PyDCrypt](https://attack.mitre.org/software/S1032) has used `cmd.exe` for execution.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [PyDCrypt](https://attack.mitre.org/software/S1032) has dropped [DCSrv](https://attack.mitre.org/software/S1033) under the `svchost.exe` name to disk.[^1] <br> |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [PyDCrypt](https://attack.mitre.org/software/S1032) has decrypted and dropped the [DCSrv](https://attack.mitre.org/software/S1033) payload to disk.[^1]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [PyDCrypt](https://attack.mitre.org/software/S1032) has modified firewall rules to allow incoming SMB, NetBIOS, and RPC connections using `netsh.exe` on remote machines.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [PyDCrypt](https://attack.mitre.org/software/S1032) has used [netsh](https://attack.mitre.org/software/S0108) to find RPC connections on remote machines.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [PyDCrypt](https://attack.mitre.org/software/S1032) has been compiled and encrypted with PyInstaller, specifically using the --key flag during the build phase.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [PyDCrypt](https://attack.mitre.org/software/S1032) has attempted to execute with PowerShell.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [PyDCrypt](https://attack.mitre.org/software/S1032) has attempted to execute with WMIC.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [PyDCrypt](https://attack.mitre.org/software/S1032) has probed victim machines with `whoami` and has collected the username from the machine.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [PyDCrypt](https://attack.mitre.org/software/S1032) will remove all created artifacts such as dropped executables.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Moses Staff\|G1009]] | Moses Staff |



## References

[^1]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)


