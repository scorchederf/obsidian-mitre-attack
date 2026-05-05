---
aliases: 
    - S0400
    
mitre-attack: https://attack.mitre.org/software/S0400
---

## S0400

[RobbinHood](https://attack.mitre.org/software/S0400) is ransomware that was first observed being used in an attack against the Baltimore city government's computer network.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [RobbinHood](https://attack.mitre.org/software/S0400) deletes shadow copies to ensure that all the data cannot be restored easily.[^1]   |
| [[Service Stop\|T1489]] | Service Stop | [RobbinHood](https://attack.mitre.org/software/S0400) stops 181 Windows services on the system before beginning the encryption process.[^1]   |
| [[Network Share Connection Removal\|T1070.005]] | Network Share Connection Removal | [RobbinHood](https://attack.mitre.org/software/S0400) disconnects all network shares from the computer with the command `net use * /DELETE /Y`.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [RobbinHood](https://attack.mitre.org/software/S0400) will search for Windows services that are associated with antivirus software on the system and kill the process.[^1]   |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [RobbinHood](https://attack.mitre.org/software/S0400) will search for an RSA encryption key and then perform its encryption process on the system files.[^1]   |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [RobbinHood](https://attack.mitre.org/software/S0400) uses cmd.exe on the victim's computer.[^1]  |




## References

[^1]: [CarbonBlack RobbinHood May 2019](https://www.carbonblack.com/2019/05/17/cb-tau-threat-intelligence-notification-robbinhood-ransomware-stops-181-windows-services-before-encryption/)


[^2]: [BaltimoreSun RobbinHood May 2019](https://www.baltimoresun.com/politics/bs-md-ci-it-outage-20190507-story.html)


