---
aliases: 
    - S0567
    
mitre-attack: https://attack.mitre.org/software/S0567
---

## S0567

[Dtrack](https://attack.mitre.org/software/S0567) is spyware that was discovered in 2019 and has been used against Indian financial institutions, research facilities, and the Kudankulam Nuclear Power Plant. [Dtrack](https://attack.mitre.org/software/S0567) shares similarities with the DarkSeoul campaign, which was attributed to [Lazarus Group](https://attack.mitre.org/groups/G0032). [^4] [^1] [^3] [^2] [^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data from Local System\|T1005]] | Data from Local System | [Dtrack](https://attack.mitre.org/software/S0567) can collect a variety of information from victim machines.[^2]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Dtrack](https://attack.mitre.org/software/S0567) can save collected data to disk, different file formats, and network shares.[^1] [^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Dtrack](https://attack.mitre.org/software/S0567) can collect the victim's computer name, hostname and adapter information to create a unique identifier.[^1] [^2]  |
| [[Hijack Execution Flow\|T1574]] | Hijack Execution Flow | One of [Dtrack](https://attack.mitre.org/software/S0567) can replace the normal flow of a program execution with malicious code.[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Dtrack](https://attack.mitre.org/software/S0567)’s dropper contains a keylogging executable.[^1]  |
| [[Boot or Logon Autostart Execution\|T1547]] | Boot or Logon Autostart Execution | [Dtrack](https://attack.mitre.org/software/S0567)’s RAT makes a persistent target file with auto execution on the host start.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Dtrack](https://attack.mitre.org/software/S0567) can add a service called WBService to establish persistence.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Dtrack](https://attack.mitre.org/software/S0567) has used `cmd.exe` to add a persistent service.[^2]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Dtrack](https://attack.mitre.org/software/S0567) used hard-coded credentials to gain access to a network share.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Dtrack](https://attack.mitre.org/software/S0567) can remove its persistence and delete itself.[^1]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [Dtrack](https://attack.mitre.org/software/S0567) can retrieve browser history.[^1] [^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | One of [Dtrack](https://attack.mitre.org/software/S0567) can hide in replicas of legitimate programs like OllyDbg, 7-Zip, and FileZilla.[^2]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Dtrack](https://attack.mitre.org/software/S0567) can collect network and active connection information.[^1]  |
| [[Embedded Payloads\|T1027.009]] | Embedded Payloads | [Dtrack](https://attack.mitre.org/software/S0567) has used a dropper that embeds an encrypted payload as extra data.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [Dtrack](https://attack.mitre.org/software/S0567) can collect the RegisteredOwner, RegisteredOrganization, and InstallDate registry values.[^2]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Dtrack](https://attack.mitre.org/software/S0567) has used process hollowing shellcode to target a predefined list of processes from `%SYSTEM32%`.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Dtrack](https://attack.mitre.org/software/S0567) can list files on available disk volumes.[^1] [^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Dtrack](https://attack.mitre.org/software/S0567) can collect the host's IP addresses using the `ipconfig` command.[^1] [^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Dtrack](https://attack.mitre.org/software/S0567)’s dropper can list all running processes.[^1] [^2]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Dtrack](https://attack.mitre.org/software/S0567) packs collected data into a password protected archive.[^1]  |
| [[Shared Modules\|T1129]] | Shared Modules | [Dtrack](https://attack.mitre.org/software/S0567) contains a function that calls `LoadLibrary` and `GetProcAddress`.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Dtrack](https://attack.mitre.org/software/S0567)’s can download and upload a file to the victim’s computer.[^1] [^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Dtrack](https://attack.mitre.org/software/S0567) has used a decryption routine that is part of an executable physical patch.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: [Securelist Dtrack](https://securelist.com/my-name-is-dtrack/93338/)


[^2]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)


[^3]: [Dragos WASSONITE](https://www.dragos.com/threat/wassonite/)


[^4]: [Kaspersky Dtrack](https://usa.kaspersky.com/about/press-releases/2019_dtrack-previously-unknown-spy-tool-hits-financial-institutions-and-research-centers)


[^5]: [ZDNet Dtrack](https://www.zdnet.com/article/confirmed-north-korean-malware-found-on-indian-nuclear-plants-network/)


