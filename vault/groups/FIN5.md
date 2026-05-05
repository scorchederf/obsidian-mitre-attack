---
aliases: 
    - FIN5
mitre-attack: https://attack.mitre.org/groups/G0053
---

## G0053

[FIN5](https://attack.mitre.org/groups/G0053) is a financially motivated threat group that has targeted personally identifiable information and payment card information. The group has been active since at least 2008 and has targeted the restaurant, gaming, and hotel industries. The group is made up of actors who likely speak Russian. [^2]  [^4]  [^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[External Proxy\|T1090.002]] | External Proxy | [FIN5](https://attack.mitre.org/groups/G0053) maintains access to victim environments by using [FLIPSIDE](https://attack.mitre.org/software/S0173) to create a proxy for a backup RDP tunnel.[^4]  |
| [[File Deletion\|T1070.004]] | File Deletion | [FIN5](https://attack.mitre.org/groups/G0053) uses [SDelete](https://attack.mitre.org/software/S0195) to clean up the environment and attempt to prevent detection.[^4]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [FIN5](https://attack.mitre.org/groups/G0053) scripts save memory dump data into a specific directory on hosts in the victim environment.[^4]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [FIN5](https://attack.mitre.org/groups/G0053) scans processes on all victim systems in the environment and uses automated scripts to pull back the results.[^4]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [FIN5](https://attack.mitre.org/groups/G0053) has used the open source tool Essential NetTools to map the network and build a list of targets.[^4]  |
| [[Automated Collection\|T1119]] | Automated Collection | [FIN5](https://attack.mitre.org/groups/G0053) scans processes on all victim systems in the environment and uses automated scripts to pull back the results.[^4]  |
| [[Brute Force\|T1110]] | Brute Force | [FIN5](https://attack.mitre.org/groups/G0053) has has used the tool GET2 Penetrator to look for remote login and hard-coded credentials.[^1] [^4]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [FIN5](https://attack.mitre.org/groups/G0053) has cleared event logs from victims.[^4]  |
| [[Tool\|T1588.002]] | Tool | [FIN5](https://attack.mitre.org/groups/G0053) has obtained and used a customized version of [PsExec](https://attack.mitre.org/software/S0029), as well as use other tools such as [pwdump](https://attack.mitre.org/software/S0006), [SDelete](https://attack.mitre.org/software/S0195), and [Windows Credential Editor](https://attack.mitre.org/software/S0005).[^4]  |
| [[External Remote Services\|T1133]] | External Remote Services | [FIN5](https://attack.mitre.org/groups/G0053) has used legitimate VPN, Citrix, or VNC credentials to maintain access to a victim environment.[^2] [^1] [^4]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [FIN5](https://attack.mitre.org/groups/G0053) has used legitimate VPN, RDP, Citrix, or VNC credentials to maintain access to a victim environment.[^2] [^1] [^4]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Windows Credential Editor\|S0005]] | Windows Credential Editor | [^1] [^4]  |
| [[pwdump\|S0006]] | pwdump | [^4]  |
| [[SDelete\|S0195]] | SDelete | [^4]  |
| [[PsExec\|S0029]] | PsExec | [FIN5](https://attack.mitre.org/groups/G0053) uses a customized version of PsExec.[^4]  |
| [[FLIPSIDE\|S0173]] | FLIPSIDE | [^4]  |
| [[RawPOS\|S0169]] | RawPOS | [^1] [^4]  |



## References

[^1]: [DarkReading FireEye FIN5 Oct 2015](https://www.darkreading.com/analytics/prolific-cybercrime-gang-favors-legit-login-credentials/d/d-id/1322645?)


[^2]: [FireEye Respond Webinar July 2017](https://www2.fireeye.com/WBNR-Are-you-ready-to-respond.html)


[^3]: FIN5


[^4]: [Mandiant FIN5 GrrCON Oct 2016](https://www.youtube.com/watch?v=fevGZs0EQu8)


