---
aliases: 
    - Daggerfly
    - Evasive Panda
    - BRONZE HIGHLAND
mitre-attack: https://attack.mitre.org/groups/G1034
---

## G1034

[Daggerfly](https://attack.mitre.org/groups/G1034) is a People's Republic of China-linked APT entity active since at least 2012. [Daggerfly](https://attack.mitre.org/groups/G1034) has targeted individuals, government and NGO entities, and telecommunication companies in Asia and Africa. [Daggerfly](https://attack.mitre.org/groups/G1034) is associated with exclusive use of [MgBot](https://attack.mitre.org/software/S1146) malware and is noted for several potential supply chain infection campaigns.[^4] [^6] [^2] [^3] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [Daggerfly](https://attack.mitre.org/groups/G1034) used [Reg](https://attack.mitre.org/software/S0075) to dump the Security Account Manager (SAM) hive from victim machines for follow-on credential extraction.[^4]  |
| [[Code Signing Certificates\|T1587.002]] | Code Signing Certificates | [Daggerfly](https://attack.mitre.org/groups/G1034) created code signing certificates to sign malicious macOS files.[^3]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Daggerfly](https://attack.mitre.org/groups/G1034) has attempted to use scheduled tasks for persistence in victim environments.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Daggerfly](https://attack.mitre.org/groups/G1034) uses HTTP for command and control communication.[^3]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Daggerfly](https://attack.mitre.org/groups/G1034) used PowerShell to download and execute remote-hosted files on victim systems.[^4]  |
| [[Rename Legitimate Utilities\|T1036.003]] | Rename Legitimate Utilities | [Daggerfly](https://attack.mitre.org/groups/G1034) used a renamed version of rundll32.exe, such as "dbengin.exe" located in the `ProgramData\Microsoft\PlayReady` directory, to proxy malicious DLL execution.[^4]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Daggerfly](https://attack.mitre.org/groups/G1034) has used strategic website compromise to deliver a malicious link requiring user interaction.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Daggerfly](https://attack.mitre.org/groups/G1034) has used PowerShell and [BITSAdmin](https://attack.mitre.org/software/S0190) to retrieve follow-on payloads from external locations for execution on victim machines.[^4]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Daggerfly](https://attack.mitre.org/groups/G1034) utilizes victim machine operating system information to create custom User Agent strings for subsequent command and control communication.[^3]  |
| [[Compromise Software Supply Chain\|T1195.002]] | Compromise Software Supply Chain | [Daggerfly](https://attack.mitre.org/groups/G1034) is associated with several supply chain compromises using malicious updates to compromise victims.[^6] [^3]  |
| [[DLL\|T1574.001]] | DLL | [Daggerfly](https://attack.mitre.org/groups/G1034) has used legitimate software to side-load [PlugX](https://attack.mitre.org/software/S0013) loaders onto victim systems.[^4]  [Daggerfly](https://attack.mitre.org/groups/G1034) is also linked to multiple other instances of side-loading for initial loading activity.[^3]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Daggerfly](https://attack.mitre.org/groups/G1034) proxied execution of malicious DLLs through a renamed rundll32.exe binary.[^4]  |
| [[Server\|T1584.004]] | Server | [Daggerfly](https://attack.mitre.org/groups/G1034) compromised web servers hosting updates for software as part of a supply chain intrusion.[^3]  |
| [[Local Account\|T1136.001]] | Local Account | [Daggerfly](https://attack.mitre.org/groups/G1034) created a local account on victim machines to maintain access.[^4]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Daggerfly](https://attack.mitre.org/groups/G1034) has used signed, but not notarized, malicious files for execution in macOS environments.[^3]  |
| [[Query Registry\|T1012]] | Query Registry | [Daggerfly](https://attack.mitre.org/groups/G1034) used [Reg](https://attack.mitre.org/software/S0075) to dump the Security Account Manager (SAM), System, and Security Windows registry hives from victim machines.[^4]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Daggerfly](https://attack.mitre.org/groups/G1034) has used strategic website compromise for initial access against victims.[^3]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[BITSAdmin\|S0190]] | BITSAdmin | [Daggerfly](https://attack.mitre.org/groups/G1034) has used [BITSAdmin](https://attack.mitre.org/software/S0190) to retrieve files from remote locations to run on victim systems.[^4]  |
| [[Reg\|S0075]] | Reg | [Daggerfly](https://attack.mitre.org/groups/G1034) has used [Reg](https://attack.mitre.org/software/S0075) to dump various Windows registry hives from victim machines.[^4]  |
| [[Nightdoor\|S1147]] | Nightdoor | [Daggerfly](https://attack.mitre.org/groups/G1034) uses [Nightdoor](https://attack.mitre.org/software/S1147) as a backdoor mechanism for Windows hosts.[^3] [^2]  |
| [[PlugX\|S0013]] | PlugX | [Daggerfly](https://attack.mitre.org/groups/G1034) has used [PlugX](https://attack.mitre.org/software/S0013) loaders as part of intrusions.[^4]  |
| [[MgBot\|S1146]] | MgBot | [Daggerfly](https://attack.mitre.org/groups/G1034) is uniquely associated with the use of [MgBot](https://attack.mitre.org/software/S1146) since at least 2012.[^6]  |
| [[MacMa\|S1016]] | MacMa | [Daggerfly](https://attack.mitre.org/groups/G1034) is linked to the use and potentially development of [MacMa](https://attack.mitre.org/software/S1016) through overlapping command and control infrastructure and shared libraries with other unique tools.[^2]  |



## References

[^1]: BRONZE HIGHLAND


[^2]: [Symantec Daggerfly 2024](https://symantec-enterprise-blogs.security.com/threat-intelligence/daggerfly-espionage-updated-toolset)


[^3]: [ESET EvasivePanda 2024](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)


[^4]: [Symantec Daggerfly 2023](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)


[^5]: Evasive Panda


[^6]: [ESET EvasivePanda 2023](https://www.welivesecurity.com/2023/04/26/evasive-panda-apt-group-malware-updates-popular-chinese-software/)


