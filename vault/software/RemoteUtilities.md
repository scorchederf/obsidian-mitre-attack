---
aliases: 
    - S0592
    
mitre-attack: https://attack.mitre.org/software/S0592
---

## S0592

[RemoteUtilities](https://attack.mitre.org/software/S0592) is a legitimate remote administration tool that has been used by [MuddyWater](https://attack.mitre.org/groups/G0069) since at least 2021 for execution on target machines.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [RemoteUtilities](https://attack.mitre.org/software/S0592) can enumerate files and directories on a target machine.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [RemoteUtilities](https://attack.mitre.org/software/S0592) can upload and download files to and from a target machine.[^1]  |
| [[Msiexec\|T1218.007]] | Msiexec | [RemoteUtilities](https://attack.mitre.org/software/S0592) can use Msiexec to install a service.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [RemoteUtilities](https://attack.mitre.org/software/S0592) can take screenshots on a compromised host.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MuddyWater\|G0069]] | MuddyWater |



## References

[^1]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)


