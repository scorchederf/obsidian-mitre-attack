---
aliases: 
    - S0554
    
mitre-attack: https://attack.mitre.org/software/S0554
---

## S0554

[Egregor](https://attack.mitre.org/software/S0554) is a Ransomware-as-a-Service (RaaS) tool that was first observed in September 2020. Researchers have noted code similarities between [Egregor](https://attack.mitre.org/software/S0554) and Sekhmet ransomware, as well as [Maze](https://attack.mitre.org/software/S0449) ransomware.[^7] [^4] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [Egregor](https://attack.mitre.org/software/S0554) can perform a  long sleep (greater than or equal to 3 minutes) to evade detection.[^6]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Egregor](https://attack.mitre.org/software/S0554) has used rundll32 during execution.[^3]  |
| [[BITS Jobs\|T1197]] | BITS Jobs | [Egregor](https://attack.mitre.org/software/S0554) has used BITSadmin to download and execute malicious DLLs.[^2]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Egregor](https://attack.mitre.org/software/S0554) contains functionality to query the local/system time.[^6]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Egregor](https://attack.mitre.org/software/S0554)'s payloads are custom-packed, archived and encrypted to prevent analysis.[^7] [^4]  |
| [[Data from Network Shared Drive\|T1039]] | Data from Network Shared Drive | [Egregor](https://attack.mitre.org/software/S0554) can collect any files found in the enumerated drivers before sending it to its C2 channel.[^7]   |
| [[Native API\|T1106]] | Native API | [Egregor](https://attack.mitre.org/software/S0554) has used the Windows API to make detection more difficult.[^4]   |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Egregor](https://attack.mitre.org/software/S0554) has been decrypted before execution.[^7] [^3]   |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Egregor](https://attack.mitre.org/software/S0554) has masqueraded the svchost.exe process to exfiltrate data.[^2]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Egregor](https://attack.mitre.org/software/S0554) can enumerate all connected drives.[^7]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Egregor](https://attack.mitre.org/software/S0554) has used tools to gather information about users.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Egregor](https://attack.mitre.org/software/S0554) has the ability to download files from its C2 server.[^3] [^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Egregor](https://attack.mitre.org/software/S0554) has disabled Windows Defender to evade protections.[^2]  |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [Egregor](https://attack.mitre.org/software/S0554) has used multiple anti-analysis and anti-sandbox techniques to prevent automated analysis by sandboxes.[^4] [^7]   |
| [[DLL\|T1574.001]] | DLL | [Egregor](https://attack.mitre.org/software/S0554) has used DLL side-loading to execute its payload.[^4]   |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Egregor](https://attack.mitre.org/software/S0554) can encrypt all non-system files using a hybrid AES-RSA algorithm prior to displaying a ransom note.[^7] [^3]   |
| [[Domain Groups\|T1069.002]] | Domain Groups | [Egregor](https://attack.mitre.org/software/S0554) can conduct Active Directory reconnaissance using tools such as Sharphound or [AdFind](https://attack.mitre.org/software/S0552).[^2]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Egregor](https://attack.mitre.org/software/S0554) has used regsvr32.exe to execute malicious DLLs.[^6]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Egregor](https://attack.mitre.org/software/S0554) has communicated with its C2 servers via HTTPS protocol.[^2]  |
| [[Remote Access Tools\|T1219]] | Remote Access Tools | [Egregor](https://attack.mitre.org/software/S0554) has checked for the LogMein event log in an attempt to encrypt files in remote machines.[^4]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Egregor](https://attack.mitre.org/software/S0554) has used batch files for execution and can launch Internet Explorer from cmd.exe.[^6] [^3]   |
| [[Group Policy Modification\|T1484.001]] | Group Policy Modification | [Egregor](https://attack.mitre.org/software/S0554) can modify the GPO to evade detection.[^3]  [^2]  |
| [[Process Injection\|T1055]] | Process Injection | [Egregor](https://attack.mitre.org/software/S0554) can inject its payload into iexplore.exe process.[^4]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Egregor](https://attack.mitre.org/software/S0554) has used an encoded PowerShell command by a service created by [Cobalt Strike](https://attack.mitre.org/software/S0154) for lateral movement.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Egregor](https://attack.mitre.org/software/S0554) can perform a language check of the infected system and can query the CPU information (cupid).[^6] [^7]  |




## References

[^1]: [Security Boulevard Egregor Oct 2020](https://securityboulevard.com/2020/10/egregor-sekhmets-cousin/)


[^2]: [Intrinsec Egregor Nov 2020](https://www.intrinsec.com/egregor-prolock/?cn-reloaded=1)


[^3]: [Cybereason Egregor Nov 2020](https://www.cybereason.com/blog/cybereason-vs-egregor-ransomware)


[^4]: [Cyble Egregor Oct 2020](https://cybleinc.com/2020/10/31/egregor-ransomware-a-deep-dive-into-its-activities-and-techniques/)


[^5]: Egregor


[^6]: [JoeSecurity Egregor 2020](https://www.joesandbox.com/analysis/326673/0/pdf)


[^7]: [NHS Digital Egregor Nov 2020](https://digital.nhs.uk/cyber-alerts/2020/cc-3681#summary)


