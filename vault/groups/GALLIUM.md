---
aliases: 
    - GALLIUM
    - Granite Typhoon
mitre-attack: https://attack.mitre.org/groups/G0093
---

## G0093

[GALLIUM](https://attack.mitre.org/groups/G0093) is a cyberespionage group that has been active since at least 2012, primarily targeting telecommunications companies, financial institutions, and government entities in Afghanistan, Australia, Belgium, Cambodia, Malaysia, Mozambique, the Philippines, Russia, and Vietnam. This group is particularly known for launching Operation Soft Cell, a long-term campaign targeting telecommunications providers.[^1]  Security researchers have identified [GALLIUM](https://attack.mitre.org/groups/G0093) as a likely Chinese state-sponsored group, based in part on tools used and TTPs commonly associated with Chinese threat actors.[^1] [^6] [^5] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [GALLIUM](https://attack.mitre.org/groups/G0093) used the Windows command shell to execute commands.[^1]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [GALLIUM](https://attack.mitre.org/groups/G0093) used `reg` commands to dump specific hives from the Windows Registry, such as the SAM hive, and obtain password hashes.[^1]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [GALLIUM](https://attack.mitre.org/groups/G0093) leveraged valid accounts to maintain access to a victim network.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [GALLIUM](https://attack.mitre.org/groups/G0093) established persistence for [PoisonIvy](https://attack.mitre.org/software/S0012) by created a scheduled task.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [GALLIUM](https://attack.mitre.org/groups/G0093) used a modified version of [HTRAN](https://attack.mitre.org/software/S0040) in which they obfuscated strings such as debug messages in an apparent attempt to evade detection.[^1]  |
| [[Code Signing\|T1553.002]] | Code Signing | [GALLIUM](https://attack.mitre.org/groups/G0093) has used stolen certificates to sign its tools including those from Whizzimo LLC.[^6]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [GALLIUM](https://attack.mitre.org/groups/G0093) used Web shells and [HTRAN](https://attack.mitre.org/software/S0040) for C2 and to exfiltrate data.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [GALLIUM](https://attack.mitre.org/groups/G0093) collected data from the victim's local system, including password hashes from the SAM hive in the Registry.[^1]  |
| [[DLL\|T1574.001]] | DLL | [GALLIUM](https://attack.mitre.org/groups/G0093) used DLL side-loading to covertly load [PoisonIvy](https://attack.mitre.org/software/S0012) into memory on the victim machine.[^1]  |
| [[Tool\|T1588.002]] | Tool | [GALLIUM](https://attack.mitre.org/groups/G0093) has used a variety of widely-available tools, which in some cases they modified to add functionality and/or subvert antimalware solutions.[^6]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [GALLIUM](https://attack.mitre.org/groups/G0093) used WMI for execution to assist in lateral movement as well as for installing tools across multiple assets.[^1]  |
| [[Domain Account\|T1136.002]] | Domain Account | [GALLIUM](https://attack.mitre.org/groups/G0093) created high-privileged domain user accounts to maintain access to victim networks.[^1] [^6]  |
| [[Server\|T1583.004]] | Server | [GALLIUM](https://attack.mitre.org/groups/G0093) has used Taiwan-based servers that appear to be exclusive to [GALLIUM](https://attack.mitre.org/groups/G0093).[^6]  |
| [[External Remote Services\|T1133]] | External Remote Services | [GALLIUM](https://attack.mitre.org/groups/G0093) has used VPN services, including SoftEther VPN, to access and maintain persistence in victim environments.[^1] [^6]  |
| [[Software Packing\|T1027.002]] | Software Packing | [GALLIUM](https://attack.mitre.org/groups/G0093) packed some payloads using different types of packers, both known and custom.[^1]  |
| [[Web Shell\|T1505.003]] | Web Shell | [GALLIUM](https://attack.mitre.org/groups/G0093) used Web shells to persist in victim environments and assist in execution and exfiltration.[^1] [^6]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [GALLIUM](https://attack.mitre.org/groups/G0093) used a modified version of [Mimikatz](https://attack.mitre.org/software/S0002) along with a PowerShell-based [Mimikatz](https://attack.mitre.org/software/S0002) to dump credentials on the victim machines.[^1] [^6]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [GALLIUM](https://attack.mitre.org/groups/G0093) used WinRAR to compress and encrypt stolen data prior to exfiltration.[^1] [^6]  |
| [[PowerShell\|T1059.001]] | PowerShell | [GALLIUM](https://attack.mitre.org/groups/G0093) used PowerShell for execution to assist in lateral movement as well as for dumping credentials stored on compromised machines.[^1]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [GALLIUM](https://attack.mitre.org/groups/G0093) has used [PsExec](https://attack.mitre.org/software/S0029) to move laterally between hosts in the target network.[^6]  |
| [[Indicator Removal from Tools\|T1027.005]] | Indicator Removal from Tools | [GALLIUM](https://attack.mitre.org/groups/G0093) ensured each payload had a unique hash, including by using different types of packers.[^1]  |
| [[External Proxy\|T1090.002]] | External Proxy | [GALLIUM](https://attack.mitre.org/groups/G0093) used a modified version of [HTRAN](https://attack.mitre.org/software/S0040) to redirect connections between networks.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [GALLIUM](https://attack.mitre.org/groups/G0093) used `netstat -oan` to obtain information about the victim network connections.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [GALLIUM](https://attack.mitre.org/groups/G0093) compressed and staged files in multi-part archives in the Recycle Bin prior to exfiltration.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [GALLIUM](https://attack.mitre.org/groups/G0093) used `whoami` and `query user` to obtain information about the victim user.[^1]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [GALLIUM](https://attack.mitre.org/groups/G0093) exploited a publicly-facing servers including Wildfly/JBoss servers to gain access to the network.[^1] [^6]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [GALLIUM](https://attack.mitre.org/groups/G0093) used `ipconfig /all` to obtain information about the victim network configuration. The group also ran a modified version of [NBTscan](https://attack.mitre.org/software/S0590) to identify available NetBIOS name servers.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [GALLIUM](https://attack.mitre.org/groups/G0093) dropped additional tools to victims during their operation, including portqry.exe, a renamed cmd.exe file, winrar, and [HTRAN](https://attack.mitre.org/software/S0040).[^1] [^6]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [GALLIUM](https://attack.mitre.org/groups/G0093) used a modified version of [NBTscan](https://attack.mitre.org/software/S0590) to identify available NetBIOS name servers over the network as well as `ping` to identify remote systems.[^1]  |
| [[Pass the Hash\|T1550.002]] | Pass the Hash | [GALLIUM](https://attack.mitre.org/groups/G0093) used dumped hashes to authenticate to other machines via pass the hash.[^1]  |
| [[Rename Legitimate Utilities\|T1036.003]] | Rename Legitimate Utilities | [GALLIUM](https://attack.mitre.org/groups/G0093) used a renamed cmd.exe file to evade detection.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^1]  |
| [[at\|S0110]] | at | [^1]  |
| [[Windows Credential Editor\|S0005]] | Windows Credential Editor | [^6]  |
| [[ipconfig\|S0100]] | ipconfig | [^1]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^1] [^6]  |
| [[NBTscan\|S0590]] | NBTscan | [^1]  |
| [[Ping\|S0097]] | Ping | [^1]  |
| [[cmd\|S0106]] | cmd | [^1] [^6]  |
| [[Reg\|S0075]] | Reg | [^1]  |
| [[HTRAN\|S0040]] | HTRAN | [^1] [^6]  |
| [[PsExec\|S0029]] | PsExec | [^1] [^6]  |
| [[PingPull\|S1031]] | PingPull | [^5]  |
| [[China Chopper\|S0020]] | China Chopper | [^1] [^6]  |
| [[BlackMould\|S0564]] | BlackMould | [^6]  |
| [[PlugX\|S0013]] | PlugX | [^1]  |
| [[PoisonIvy\|S0012]] | PoisonIvy | [^1] [^6]  |



## References

[^1]: [Cybereason Soft Cell June 2019](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)


[^2]: GALLIUM


[^3]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^4]: Granite Typhoon


[^5]: [Unit 42 PingPull Jun 2022](https://unit42.paloaltonetworks.com/pingpull-gallium/)


[^6]: [Microsoft GALLIUM December 2019](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)


