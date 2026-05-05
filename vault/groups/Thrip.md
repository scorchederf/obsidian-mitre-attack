---
aliases: 
    - Thrip
mitre-attack: https://attack.mitre.org/groups/G0076
---

## G0076

[Thrip](https://attack.mitre.org/groups/G0076) is an espionage group that has targeted satellite communications, telecoms, and defense contractor companies in the U.S. and Southeast Asia. The group uses custom malware as well as "living off the land" techniques. [^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[PowerShell\|T1059.001]] | PowerShell | [Thrip](https://attack.mitre.org/groups/G0076) leveraged PowerShell to run commands to download payloads, traverse the compromised networks, and carry out reconnaissance.[^1]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [Thrip](https://attack.mitre.org/groups/G0076) has used WinSCP to exfiltrate data from a targeted organization over FTP.[^1]  |
| [[Remote Desktop Software\|T1219.002]] | Remote Desktop Software | [Thrip](https://attack.mitre.org/groups/G0076) used a cloud-based remote access software called LogMeIn for their attacks.[^1]  |
| [[Tool\|T1588.002]] | Tool | [Thrip](https://attack.mitre.org/groups/G0076) has obtained and used tools such as [Mimikatz](https://attack.mitre.org/software/S0002) and [PsExec](https://attack.mitre.org/software/S0029).[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Mimikatz\|S0002]] | Mimikatz | [^1]  |
| [[PsExec\|S0029]] | PsExec | [Thrip](https://attack.mitre.org/groups/G0076) used PsExec to move laterally between computers on the victim’s network.[^1]  |
| [[Catchamas\|S0261]] | Catchamas | [^1]  |



## References

[^1]: [Symantec Thrip June 2018](https://www.symantec.com/blogs/threat-intelligence/thrip-hits-satellite-telecoms-defense-targets)


[^2]: Thrip


