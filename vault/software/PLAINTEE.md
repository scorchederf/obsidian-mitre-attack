---
aliases: 
    - S0254
    
mitre-attack: https://attack.mitre.org/software/S0254
---

## S0254

[PLAINTEE](https://attack.mitre.org/software/S0254) is a malware sample that has been used by [Rancor](https://attack.mitre.org/groups/G0075) in targeted attacks in Singapore and Cambodia. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [PLAINTEE](https://attack.mitre.org/software/S0254) collects general system enumeration data about the infected machine and checks the OS version.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [PLAINTEE](https://attack.mitre.org/software/S0254) uses `reg add` to add a Registry Run key for persistence.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [PLAINTEE](https://attack.mitre.org/software/S0254) uses the `ipconfig /all` command to gather the victim’s IP address.[^1]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | An older variant of [PLAINTEE](https://attack.mitre.org/software/S0254) performs UAC bypass.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [PLAINTEE](https://attack.mitre.org/software/S0254) performs the `tasklist` command to list running processes.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [PLAINTEE](https://attack.mitre.org/software/S0254) gains persistence by adding the Registry key `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce`.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [PLAINTEE](https://attack.mitre.org/software/S0254) encodes C2 beacons using XOR.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [PLAINTEE](https://attack.mitre.org/software/S0254) uses cmd.exe to execute commands on the victim’s machine.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [PLAINTEE](https://attack.mitre.org/software/S0254) has downloaded and executed additional plugins.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Rancor\|G0075]] | Rancor |



## References

[^1]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)


[^2]: PLAINTEE


