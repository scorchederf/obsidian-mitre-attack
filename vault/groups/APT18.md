---
aliases: 
    - APT18
    - TG-0416
    - Dynamite Panda
    - Threat Group-0416
mitre-attack: https://attack.mitre.org/groups/G0026
---

## G0026

[APT18](https://attack.mitre.org/groups/G0026) is a threat group that has operated since at least 2009 and has targeted a range of industries, including technology, manufacturing, human rights groups, government, and medical. [^5] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Valid Accounts\|T1078]] | Valid Accounts | [APT18](https://attack.mitre.org/groups/G0026) actors leverage legitimate credentials to log into external remote services.[^10]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [APT18](https://attack.mitre.org/groups/G0026) obfuscates strings in the payload.[^8]  |
| [[External Remote Services\|T1133]] | External Remote Services | [APT18](https://attack.mitre.org/groups/G0026) actors leverage legitimate credentials to log into external remote services.[^10]  |
| [[File Deletion\|T1070.004]] | File Deletion | [APT18](https://attack.mitre.org/groups/G0026) actors deleted tools and batch files from victim systems.[^5]  |
| [[At\|T1053.002]] | At | [APT18](https://attack.mitre.org/groups/G0026) actors used the native [at](https://attack.mitre.org/software/S0110) Windows task scheduler tool to use scheduled tasks for execution on a victim network.[^5]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [APT18](https://attack.mitre.org/groups/G0026) can upload a file to the victim’s machine.[^8]  |
| [[DNS\|T1071.004]] | DNS | [APT18](https://attack.mitre.org/groups/G0026) uses DNS for C2 communications.[^8]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [APT18](https://attack.mitre.org/groups/G0026) can collect system information from the victim’s machine.[^8]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [APT18](https://attack.mitre.org/groups/G0026) uses HTTP for C2 communications.[^8]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [APT18](https://attack.mitre.org/groups/G0026) can list files information for specific directories.[^8]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [APT18](https://attack.mitre.org/groups/G0026) uses cmd.exe to execute commands on the victim’s machine.[^8] [^6]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [APT18](https://attack.mitre.org/groups/G0026) establishes persistence via the `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` key.[^6] [^8]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[cmd\|S0106]] | cmd | [^5]  |
| [[gh0st RAT\|S0032]] | gh0st RAT | [^10]  |
| [[hcdLoader\|S0071]] | hcdLoader | [^5] [^3]  |
| [[Pisloader\|S0124]] | Pisloader | [^7]  |
| [[HTTPBrowser\|S0070]] | HTTPBrowser | [^10]  |



## References

[^1]: Threat Group-0416


[^2]: Dynamite Panda


[^3]: [ThreatStream Evasion Analysis](https://www.threatstream.com/blog/evasive-maneuvers-the-wekby-group-attempts-to-evade-analysis-via-custom-rop)


[^4]: APT18


[^5]: [Dell Lateral Movement](http://www.secureworks.com/resources/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems/)


[^6]: [Anomali Evasive Maneuvers July 2015](https://www.anomali.com/blog/evasive-maneuvers-the-wekby-group-attempts-to-evade-analysis-via-custom-rop)


[^7]: [Palo Alto DNS Requests](http://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)


[^8]: [PaloAlto DNS Requests May 2016](https://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)


[^9]: TG-0416


[^10]: [RSA2017 Detect and Respond Adair](https://web.archive.org/web/20210803040540/https://published-prd.lanyonevents.com/published/rsaus17/sessionsFiles/5009/HTA-F02-Detecting-and-Responding-to-Advanced-Threats-within-Exchange-Environments.pdf)


