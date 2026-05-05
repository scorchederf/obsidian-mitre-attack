---
aliases: 
    - Rancor
mitre-attack: https://attack.mitre.org/groups/G0075
---

## G0075

[Rancor](https://attack.mitre.org/groups/G0075) is a threat group that has led targeted campaigns against the South East Asia region. [Rancor](https://attack.mitre.org/groups/G0075) uses politically-motivated lures to entice victims to open malicious documents. [^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Rancor](https://attack.mitre.org/groups/G0075) has used HTTP for C2.[^1]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Rancor](https://attack.mitre.org/groups/G0075) has used VBS scripts as well as embedded macros for execution.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Rancor](https://attack.mitre.org/groups/G0075) attempted to get users to click on an embedded macro within a Microsoft Office Excel document to launch their malware.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Rancor](https://attack.mitre.org/groups/G0075) launched a scheduled task to gain persistence using the `schtasks /create /sc` command.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Rancor](https://attack.mitre.org/groups/G0075) has downloaded additional malware, including by using [certutil](https://attack.mitre.org/software/S0160).[^1]  |
| [[Msiexec\|T1218.007]] | Msiexec | [Rancor](https://attack.mitre.org/groups/G0075) has used `msiexec` to download and execute malicious installer files over HTTP.[^1]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [Rancor](https://attack.mitre.org/groups/G0075) has complied VBScript-generated MOF files into WMI event subscriptions for persistence.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Rancor](https://attack.mitre.org/groups/G0075) has used cmd.exe to execute commmands.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Rancor](https://attack.mitre.org/groups/G0075) has attached a malicious document to an email to gain initial access.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[certutil\|S0160]] | certutil | [^1]  |
| [[Reg\|S0075]] | Reg | [^1]  |
| [[PLAINTEE\|S0254]] | PLAINTEE | [^1]  |
| [[DDKONG\|S0255]] | DDKONG | [^1]  |



## References

[^1]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)


[^2]: [Rancor WMI](https://unit42.paloaltonetworks.com/rancor-cyber-espionage-group-uses-new-custom-malware-to-attack-southeast-asia/)


[^3]: Rancor


