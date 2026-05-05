---
aliases: 
    - S0382
    
mitre-attack: https://attack.mitre.org/software/S0382
---

## S0382

[ServHelper](https://attack.mitre.org/software/S0382) is a backdoor first observed in late 2018. The backdoor is written in Delphi and is typically delivered as a DLL file.[^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [ServHelper](https://attack.mitre.org/software/S0382) can execute shell commands against [cmd](https://attack.mitre.org/software/S0106).[^3] [^4]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [ServHelper](https://attack.mitre.org/software/S0382) may set up a reverse SSH tunnel to give the attacker access to services running on the victim, such as RDP.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [ServHelper](https://attack.mitre.org/software/S0382) uses HTTP for C2.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [ServHelper](https://attack.mitre.org/software/S0382) may download additional files to execute.[^3] [^4]  |
| [[Local Account\|T1136.001]] | Local Account | [ServHelper](https://attack.mitre.org/software/S0382) has created a new user named "supportaccount".[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [ServHelper](https://attack.mitre.org/software/S0382) will attempt to enumerate Windows version and system architecture.[^3]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [ServHelper](https://attack.mitre.org/software/S0382) has commands for adding a remote desktop user and sending RDP traffic to the attacker through a reverse SSH tunnel.[^3]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [ServHelper](https://attack.mitre.org/software/S0382) may attempt to establish persistence via the `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\` run key.[^4]  |
| [[PowerShell\|T1059.001]] | PowerShell | [ServHelper](https://attack.mitre.org/software/S0382) has the ability to execute a PowerShell script to get information from the infected host.[^2]  |
| [[Masquerade Account Name\|T1036.010]] | Masquerade Account Name | [ServHelper](https://attack.mitre.org/software/S0382) has created a new user named `supportaccount`.[^3]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [ServHelper](https://attack.mitre.org/software/S0382) will attempt to enumerate the username of the victim.[^3]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [ServHelper](https://attack.mitre.org/software/S0382) contains a module for downloading and executing DLLs that leverages `rundll32.exe`.[^4]  |
| [[File Deletion\|T1070.004]] | File Deletion | [ServHelper](https://attack.mitre.org/software/S0382) has a module to delete itself from the infected machine.[^3] [^4]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [ServHelper](https://attack.mitre.org/software/S0382) contains modules that will use [schtasks](https://attack.mitre.org/software/S0111) to carry out malicious operations.[^3]  |
| [[Additional Local or Domain Groups\|T1098.007]] | Additional Local or Domain Groups | [ServHelper](https://attack.mitre.org/software/S0382) has added a user named "supportaccount" to the Remote Desktop Users and Administrators groups.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA505\|G0092]] | TA505 |



## References

[^1]: [Cybereason TA505 April 2019](https://www.cybereason.com/blog/threat-actor-ta505-targets-financial-enterprises-using-lolbins-and-a-new-backdoor-malware)


[^2]: [Trend Micro TA505 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/shifting-tactics-breaking-down-ta505-groups-use-of-html-rats-and-other-techniques-in-latest-campaigns/)


[^3]: [Proofpoint TA505 Jan 2019](https://www.proofpoint.com/us/threat-insight/post/servhelper-and-flawedgrace-new-malware-introduced-ta505)


[^4]: [Deep Instinct TA505 Apr 2019](https://www.deepinstinct.com/blog/new-servhelper-variant-employs-excel-4-0-macro-to-drop-signed-payload)


