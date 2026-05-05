---
aliases: 
    - Sowbug
mitre-attack: https://attack.mitre.org/groups/G0054
---

## G0054

[Sowbug](https://attack.mitre.org/groups/G0054) is a threat group that has conducted targeted attacks against organizations in South America and Southeast Asia, particularly government entities, since at least 2015. [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Sowbug](https://attack.mitre.org/groups/G0054) identified and extracted all Word documents on a server by using a command containing * .doc and *.docx. The actors also searched for documents based on a specific date range and attempted to identify all installed software on a victim.[^2]  |
| [[Data from Network Shared Drive\|T1039]] | Data from Network Shared Drive | [Sowbug](https://attack.mitre.org/groups/G0054) extracted Word documents from a file server on a victim network.[^2]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Sowbug](https://attack.mitre.org/groups/G0054) extracted documents and bundled them into a RAR archive.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Sowbug](https://attack.mitre.org/groups/G0054) has used command line during its intrusions.[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Sowbug](https://attack.mitre.org/groups/G0054) has used keylogging tools.[^2]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Sowbug](https://attack.mitre.org/groups/G0054) listed remote shared drives that were accessible from a victim.[^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Sowbug](https://attack.mitre.org/groups/G0054) named its tools to masquerade as Windows or Adobe Reader software, such as by using the file name adobecms.exe and the directory `CSIDL_APPDATA\microsoft\security`.[^2]  |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | [Sowbug](https://attack.mitre.org/groups/G0054) has used credential dumping tools.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Sowbug](https://attack.mitre.org/groups/G0054) obtained OS version and hardware configuration from a victim.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Felismus\|S0171]] | Felismus | [^2]  |
| [[Starloader\|S0188]] | Starloader | [^2]  |



## References

[^1]: Sowbug


[^2]: [Symantec Sowbug Nov 2017](https://www.symantec.com/connect/blogs/sowbug-cyber-espionage-group-targets-south-american-and-southeast-asian-governments)


