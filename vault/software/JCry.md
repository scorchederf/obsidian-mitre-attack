---
aliases: 
    - S0389
    
mitre-attack: https://attack.mitre.org/software/S0389
---

## S0389

[JCry](https://attack.mitre.org/software/S0389) is ransomware written in Go. It was identified as apart of the #OpJerusalem 2019 campaign.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [JCry](https://attack.mitre.org/software/S0389) has encrypted files and demanded Bitcoin to decrypt those files. [^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [JCry](https://attack.mitre.org/software/S0389) has created payloads in the Startup directory to maintain persistence. [^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [JCry](https://attack.mitre.org/software/S0389) has used PowerShell to execute payloads.[^2]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [JCry](https://attack.mitre.org/software/S0389) has used VBS scripts. [^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [JCry](https://attack.mitre.org/software/S0389) has achieved execution by luring users to click on a file that appeared to be an Adobe Flash Player update installer. [^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [JCry](https://attack.mitre.org/software/S0389) has used `cmd.exe` to launch PowerShell.[^2] 	 |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [JCry](https://attack.mitre.org/software/S0389) has been observed deleting shadow copies to ensure that data cannot be restored easily.[^2] 	 |




## References

[^1]: JCry


[^2]: [Carbon Black JCry May 2019](https://www.carbonblack.com/2019/05/14/cb-tau-threat-intelligence-notification-jcry-ransomware-pretends-to-be-adobe-flash-player-update-installer/)


