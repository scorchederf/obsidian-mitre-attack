---
aliases: 
    - S0583
    
mitre-attack: https://attack.mitre.org/software/S0583
---

## S0583

[Pysa](https://attack.mitre.org/software/S0583) is a ransomware that was first used in October 2018 and has been seen to target particularly high-value finance, government and healthcare organizations.[^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Pysa](https://attack.mitre.org/software/S0583) can perform network reconnaissance using the Advanced IP Scanner tool.[^4]  |
| [[Python\|T1059.006]] | Python | [Pysa](https://attack.mitre.org/software/S0583) has used Python scripts to deploy ransomware.[^4]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [Pysa](https://attack.mitre.org/software/S0583) has extracted credentials from the password database before encrypting the files.[^4]   |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Pysa](https://attack.mitre.org/software/S0583) has the capability to stop antivirus services and disable Windows Defender.[^4]   |
| [[PowerShell\|T1059.001]] | PowerShell | [Pysa](https://attack.mitre.org/software/S0583) has used Powershell scripts to deploy its ransomware.[^4]   |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Pysa](https://attack.mitre.org/software/S0583) has used RSA and AES-CBC encryption algorithm to encrypt a list of targeted file extensions.[^4]   |
| [[Modify Registry\|T1112]] | Modify Registry | [Pysa](https://attack.mitre.org/software/S0583) has modified the registry key “SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System” and added the ransom note.[^4]   |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Pysa](https://attack.mitre.org/software/S0583) has laterally moved using RDP connections.[^4]   |
| [[Service Execution\|T1569.002]] | Service Execution | [Pysa](https://attack.mitre.org/software/S0583) has used [PsExec](https://attack.mitre.org/software/S0029) to copy and execute the ransomware.[^4]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Pysa](https://attack.mitre.org/software/S0583) can perform OS credential dumping using [Mimikatz](https://attack.mitre.org/software/S0002).[^4]  |
| [[Service Stop\|T1489]] | Service Stop | [Pysa](https://attack.mitre.org/software/S0583) can stop services and processes.[^4]   |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Pysa](https://attack.mitre.org/software/S0583) has the functionality to delete shadow copies.[^4]   |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Pysa](https://attack.mitre.org/software/S0583) has executed a malicious executable by naming it svchost.exe.[^4]  |
| [[Brute Force\|T1110]] | Brute Force | [Pysa](https://attack.mitre.org/software/S0583) has used brute force attempts against a central management console, as well as some Active Directory accounts.[^4]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Pysa](https://attack.mitre.org/software/S0583) has deleted batch files after execution. [^4]   |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Pysa](https://attack.mitre.org/software/S0583) can perform network reconnaissance using the Advanced Port Scanner tool.[^4]  |




## References

[^1]: Pysa


[^2]: [NHS Digital Pysa Oct 2020](https://digital.nhs.uk/cyber-alerts/2020/cc-3633)


[^3]: Mespinoza


[^4]: [CERT-FR PYSA April 2020](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2020-CTI-003.pdf)


[^5]: [DFIR Pysa Nov 2020](https://thedfirreport.com/2020/11/23/pysa-mespinoza-ransomware/)


