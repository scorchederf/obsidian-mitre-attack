---
aliases: 
    - S0648
    
mitre-attack: https://attack.mitre.org/software/S0648
---

## S0648

[JSS Loader](https://attack.mitre.org/software/S0648) is Remote Access Trojan (RAT) with .NET and C++ variants that has been used by [FIN7](https://attack.mitre.org/groups/G0046) since at least 2020.[^3] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [JSS Loader](https://attack.mitre.org/software/S0648) has the ability to launch scheduled tasks to establish persistence.[^2]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [JSS Loader](https://attack.mitre.org/software/S0648) can download and execute VBScript files.[^2]  |
| [[JavaScript\|T1059.007]] | JavaScript | [JSS Loader](https://attack.mitre.org/software/S0648) can download and execute JavaScript files.[^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [JSS Loader](https://attack.mitre.org/software/S0648) has been delivered by phishing emails containing malicious Microsoft Excel attachments.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [JSS Loader](https://attack.mitre.org/software/S0648) has the ability to download malicious executables to a compromised host.[^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [JSS Loader](https://attack.mitre.org/software/S0648) has been executed through malicious attachments contained in spearphishing emails.[^3]  |
| [[PowerShell\|T1059.001]] | PowerShell | [JSS Loader](https://attack.mitre.org/software/S0648) has the ability to download and execute PowerShell scripts.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN7\|G0046]] | FIN7 |



## References

[^1]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^2]: [CrowdStrike Carbon Spider August 2021](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)


[^3]: [eSentire FIN7 July 2021](https://www.esentire.com/security-advisories/notorious-cybercrime-gang-fin7-lands-malware-in-law-firm-using-fake-legal-complaint-against-jack-daniels-owner-brown-forman-inc)


