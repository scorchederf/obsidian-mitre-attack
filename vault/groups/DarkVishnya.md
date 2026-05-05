---
aliases: 
    - DarkVishnya
mitre-attack: https://attack.mitre.org/groups/G0105
---

## G0105

[DarkVishnya](https://attack.mitre.org/groups/G0105) is a financially motivated threat actor targeting financial institutions in Eastern Europe. In 2017-2018 the group attacked at least 8 banks in this region.[^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Hardware Additions\|T1200]] | Hardware Additions | [DarkVishnya](https://attack.mitre.org/groups/G0105) physically connected Bash Bunny, Raspberry Pi, netbooks, and inexpensive laptops to the target organization's environment to access the company’s local network.[^1]  |
| [[Tool\|T1588.002]] | Tool | [DarkVishnya](https://attack.mitre.org/groups/G0105) has obtained and used tools such as [Impacket](https://attack.mitre.org/software/S0357), [Winexe](https://attack.mitre.org/software/S0191), and [PsExec](https://attack.mitre.org/software/S0029).[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [DarkVishnya](https://attack.mitre.org/groups/G0105) created new services for shellcode loaders distribution.[^1]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [DarkVishnya](https://attack.mitre.org/groups/G0105) performed port scanning to obtain the list of active services.[^1]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [DarkVishnya](https://attack.mitre.org/groups/G0105) scanned the network for public shared folders.[^1]  |
| [[Brute Force\|T1110]] | Brute Force | [DarkVishnya](https://attack.mitre.org/groups/G0105) used brute-force attack to obtain login data.[^1]  |
| [[Remote Access Tools\|T1219]] | Remote Access Tools | [DarkVishnya](https://attack.mitre.org/groups/G0105) used DameWare Mini Remote Control for lateral movement.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [DarkVishnya](https://attack.mitre.org/groups/G0105) used PowerShell to create shellcode loaders.[^1]  |
| [[Network Sniffing\|T1040]] | Network Sniffing | [DarkVishnya](https://attack.mitre.org/groups/G0105) used network sniffing to obtain login data. [^1]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [DarkVishnya](https://attack.mitre.org/groups/G0105) used ports 5190 and 7900 for shellcode listeners, and 4444, 4445, 31337 for shellcode C2.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Winexe\|S0191]] | Winexe | [^1]   |
| [[PsExec\|S0029]] | PsExec | [^1]   |



## References

[^1]: [Securelist DarkVishnya Dec 2018](https://securelist.com/darkvishnya/89169/)


[^2]: DarkVishnya


