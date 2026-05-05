---
aliases: 
    - BackdoorDiplomacy
mitre-attack: https://attack.mitre.org/groups/G0135
---

## G0135

[BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) is a cyber espionage threat group that has been active since at least 2017. [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has targeted Ministries of Foreign Affairs and telecommunication companies in Africa, Europe, the Middle East, and Asia.[^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has obfuscated tools and malware it uses with VMProtect.[^1]  |
| [[Web Shell\|T1505.003]] | Web Shell | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has used web shells to establish an initial foothold and for lateral movement within a victim's system.[^1]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has exploited CVE-2020-5902, an F5 BIP-IP vulnerability, to drop a Linux backdoor. [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has also exploited mis-configured Plesk servers.[^1]  |
| [[Tool\|T1588.002]] | Tool | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has obtained a variety of open-source reconnaissance and red team tools for discovery and lateral movement.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has dropped implants in folders named for legitimate software.[^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has dropped legitimate software onto a compromised host and used it to execute malicious DLLs.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has downloaded additional files and tools onto a compromised host.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has copied files of interest to the main drive's recycle bin.[^1]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has used SMBTouch, a vulnerability scanner, to determine whether a target is vulnerable to EternalBlue malware.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has used NetCat and PortQry  to enumerate network connections and display the status of related TCP and UDP ports.[^1]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has used an executable to detect removable media, such as USB flash drives.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has used EarthWorm for network tunneling with a SOCKS5 server and port transfer functionalities.[^1]  |
| [[DLL\|T1574.001]] | DLL | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has executed DLL search order hijacking.[^1]  |
| [[Malware\|T1588.001]] | Malware | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has obtained and used leaked malware, including DoublePulsar, EternalBlue, EternalRocks, and EternalSynergy, in its operations.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has disguised their backdoor droppers with naming conventions designed to blend into normal operations.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Mimikatz\|S0002]] | Mimikatz | [^1]  |
| [[NBTscan\|S0590]] | NBTscan | [^1]  |
| [[QuasarRAT\|S0262]] | QuasarRAT | [^1]  |
| [[Turian\|S0647]] | Turian | [^1]  |
| [[China Chopper\|S0020]] | China Chopper | [^1]  |



## References

[^1]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)


