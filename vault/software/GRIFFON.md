---
aliases: 
    - S0417
    
mitre-attack: https://attack.mitre.org/software/S0417
---

## S0417

[GRIFFON](https://attack.mitre.org/software/S0417) is a JavaScript backdoor used by [FIN7](https://attack.mitre.org/groups/G0046). [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Screen Capture\|T1113]] | Screen Capture | [GRIFFON](https://attack.mitre.org/software/S0417) has used a screenshot module that can be used to take a screenshot of the remote system.[^4]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [GRIFFON](https://attack.mitre.org/software/S0417) has used a reconnaissance module that can be used to retrieve Windows domain membership information.[^4]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [GRIFFON](https://attack.mitre.org/software/S0417) has used a reconnaissance module that can be used to retrieve the date and time of the system.[^4] 	 |
| [[JavaScript\|T1059.007]] | JavaScript | [GRIFFON](https://attack.mitre.org/software/S0417) is written in and executed as [JavaScript](https://attack.mitre.org/techniques/T1059/007).[^4] 	 |
| [[System Information Discovery\|T1082]] | System Information Discovery | [GRIFFON](https://attack.mitre.org/software/S0417) has used a reconnaissance module that can be used to retrieve information about a victim's computer, including the resolution of the workstation .[^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [GRIFFON](https://attack.mitre.org/software/S0417) has used a persistence module that stores the implant inside the Registry, which executes at logon.[^4]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [GRIFFON](https://attack.mitre.org/software/S0417) has used `sctasks` for persistence. [^4]  |
| [[PowerShell\|T1059.001]] | PowerShell | [GRIFFON](https://attack.mitre.org/software/S0417) has used PowerShell to execute the Meterpreter downloader TinyMet.[^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN7\|G0046]] | FIN7 |



## References

[^1]: [FBI Flash FIN7 USB](https://therecord.media/fbi-fin7-hackers-target-us-companies-with-badusb-devices-to-install-ransomware/)


[^2]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^3]: [CrowdStrike Carbon Spider August 2021](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)


[^4]: [SecureList Griffon May 2019](https://securelist.com/fin7-5-the-infamous-cybercrime-rig-fin7-continues-its-activities/90703/)


