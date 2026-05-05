---
aliases: 
    - S0353
    
mitre-attack: https://attack.mitre.org/software/S0353
---

## S0353

[NOKKI](https://attack.mitre.org/software/S0353) is a modular remote access tool. The earliest observed attack using [NOKKI](https://attack.mitre.org/software/S0353) was in January 2018. [NOKKI](https://attack.mitre.org/software/S0353) has significant code overlap with the [KONNI](https://attack.mitre.org/software/S0356) malware family. There is some evidence potentially linking [NOKKI](https://attack.mitre.org/software/S0353) to [APT37](https://attack.mitre.org/groups/G0067).[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Time Discovery\|T1124]] | System Time Discovery | [NOKKI](https://attack.mitre.org/software/S0353) can collect the current timestamp of the victim's machine.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [NOKKI](https://attack.mitre.org/software/S0353) has established persistence by writing the payload to the Registry key `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [NOKKI](https://attack.mitre.org/software/S0353) has downloaded a remote module for execution.[^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [NOKKI](https://attack.mitre.org/software/S0353) is written to %LOCALAPPDATA%\MicroSoft Updatea\svServiceUpdate.exe prior being executed in a new process in an apparent attempt to masquerade as a legitimate folder and file.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [NOKKI](https://attack.mitre.org/software/S0353) uses Base64 encoding for strings.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [NOKKI](https://attack.mitre.org/software/S0353) can delete files to cover tracks.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [NOKKI](https://attack.mitre.org/software/S0353) can collect the username from the victim’s machine.[^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [NOKKI](https://attack.mitre.org/software/S0353) has used rundll32 for execution.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [NOKKI](https://attack.mitre.org/software/S0353) uses a unique, custom de-obfuscation technique.[^2]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [NOKKI](https://attack.mitre.org/software/S0353) can gather information on drives on the victim’s machine.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [NOKKI](https://attack.mitre.org/software/S0353) has used HTTP for C2 communications.[^2]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [NOKKI](https://attack.mitre.org/software/S0353) can collect data from the victim and stage it in `LOCALAPPDATA%\MicroSoft Updatea\uplog.tmp`.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [NOKKI](https://attack.mitre.org/software/S0353) can gather information on the victim IP address.[^2]  |
| [[Credential API Hooking\|T1056.004]] | Credential API Hooking | [NOKKI](https://attack.mitre.org/software/S0353) uses the Windows call SetWindowsHookEx and begins injecting it into every GUI process running on the victim's machine.[^2]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [NOKKI](https://attack.mitre.org/software/S0353) has used FTP for C2 communications.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [NOKKI](https://attack.mitre.org/software/S0353) can gather information on the operating system on the victim’s machine.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Kimsuky\|G0094]] | Kimsuky |



## References

[^1]: [Unit 42 Nokki Oct 2018](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)


[^2]: [Unit 42 NOKKI Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)


[^3]: NOKKI


[^4]: [Crowdstrike GTR2020 Mar 2020](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)


