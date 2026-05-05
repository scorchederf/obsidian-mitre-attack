---
aliases: 
    - S0572
    
mitre-attack: https://attack.mitre.org/software/S0572
---

## S0572

[Caterpillar WebShell](https://attack.mitre.org/software/S0572) is a self-developed Web Shell tool created by the group [Volatile Cedar](https://attack.mitre.org/groups/G0123).[^3]  

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) can gather a list of processes running on the machine.[^3]   |
| [[Data from Local System\|T1005]] | Data from Local System | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) has a module to collect information from the local database.[^3]   |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) can gather the IP address from the victim's machine using the IP config command.[^3]   |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) can search for files in directories.[^3]   |
| [[Brute Force\|T1110]] | Brute Force | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) has a module to perform brute force attacks on a system.[^3]   |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) can run commands on the compromised asset with CMD functions.[^3]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) can obtain a list of the services from a system.[^3]   |
| [[Modify Registry\|T1112]] | Modify Registry | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) has a command to modify a Registry key.[^3]  |
| [[Local Groups\|T1069.001]] | Local Groups | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) can obtain a list of local groups of users from a system.[^3]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) can upload files over the C2 channel.[^3]   |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) has a module to gather information from the compromised asset, including the computer version, computer name, IIS version, and more.[^3]   |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) can obtain a list of user accounts from a victim's machine.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) has a module to download and upload files to the system.[^3]   |
| [[Rootkit\|T1014]] | Rootkit | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) has a module to use a rootkit on a system.[^3]   |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) has a module to use a port scanner on a system.[^3]   |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Volatile Cedar\|G0123]] | Volatile Cedar |



## References

[^1]: [CheckPoint Volatile Cedar March 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)


[^2]: Caterpillar WebShell


[^3]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)


