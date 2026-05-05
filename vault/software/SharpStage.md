---
aliases: 
    - S0546
    
mitre-attack: https://attack.mitre.org/software/S0546
---

## S0546

[SharpStage](https://attack.mitre.org/software/S0546) is a .NET malware with backdoor capabilities.[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [SharpStage](https://attack.mitre.org/software/S0546) can execute arbitrary commands with the command line.[^2] [^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [SharpStage](https://attack.mitre.org/software/S0546) has a persistence component to write a scheduled task for the payload.[^2]   |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [SharpStage](https://attack.mitre.org/software/S0546) has the ability to create persistence for the malware using the Registry autorun key and startup folder.[^2]   |
| [[Web Service\|T1102]] | Web Service | [SharpStage](https://attack.mitre.org/software/S0546) has used a legitimate web service for evading detection.[^2]   |
| [[Screen Capture\|T1113]] | Screen Capture | [SharpStage](https://attack.mitre.org/software/S0546) has the ability to capture the victim's screen.[^2] [^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [SharpStage](https://attack.mitre.org/software/S0546) can execute arbitrary commands with PowerShell.[^2] [^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SharpStage](https://attack.mitre.org/software/S0546) has the ability to download and execute additional payloads via a DropBox API.[^2] [^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SharpStage](https://attack.mitre.org/software/S0546) has checked the system settings to see if Arabic is the configured language.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [SharpStage](https://attack.mitre.org/software/S0546) has decompressed data received from the C2 server.[^1]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [SharpStage](https://attack.mitre.org/software/S0546)  has been used to target Arabic-speaking users and used code that checks if the compromised machine has the Arabic language installed.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [SharpStage](https://attack.mitre.org/software/S0546) can use WMI for execution.[^2] [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Molerats\|G0021]] | Molerats |



## References

[^1]: [BleepingComputer Molerats Dec 2020](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)


[^2]: [Cybereason Molerats Dec 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)


[^3]: SharpStage


