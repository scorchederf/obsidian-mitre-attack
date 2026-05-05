---
aliases: 
    - S0346
    
mitre-attack: https://attack.mitre.org/software/S0346
---

## S0346

[OceanSalt](https://attack.mitre.org/software/S0346) is a Trojan that was used in a campaign targeting victims in South Korea, United States, and Canada. [OceanSalt](https://attack.mitre.org/software/S0346) shares code similarity with [SpyNote RAT](https://attack.mitre.org/software/S0305), which has been linked to [APT1](https://attack.mitre.org/groups/G0006).[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [OceanSalt](https://attack.mitre.org/software/S0346) can create a reverse shell on the infected endpoint using cmd.exe.[^2]  [OceanSalt](https://attack.mitre.org/software/S0346) has been executed via malicious macros.[^2]  |
| [[Non-Standard Encoding\|T1132.002]] | Non-Standard Encoding | [OceanSalt](https://attack.mitre.org/software/S0346) can encode data with a NOT operation before sending the data to the control server.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [OceanSalt](https://attack.mitre.org/software/S0346) can collect the victim’s IP address.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [OceanSalt](https://attack.mitre.org/software/S0346) can extract drive information from the endpoint and search files on the system.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [OceanSalt](https://attack.mitre.org/software/S0346) can delete files from the system.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [OceanSalt](https://attack.mitre.org/software/S0346) can collect the computer name from the system.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [OceanSalt](https://attack.mitre.org/software/S0346) can collect the name and ID for every process running on the system.[^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [OceanSalt](https://attack.mitre.org/software/S0346) has been delivered via spearphishing emails with Microsoft Office attachments.[^2]  |




## References

[^1]: OceanSalt


[^2]: [McAfee Oceansalt Oct 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-oceansalt.pdf)


