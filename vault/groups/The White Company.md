---
aliases: 
    - The White Company
mitre-attack: https://attack.mitre.org/groups/G0089
---

## G0089

[The White Company](https://attack.mitre.org/groups/G0089) is a likely state-sponsored threat actor with advanced capabilities. From 2017 through 2018, the group led an espionage campaign called Operation Shaheen targeting government and military organizations in Pakistan.[^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Software Packing\|T1027.002]] | Software Packing | [The White Company](https://attack.mitre.org/groups/G0089) has obfuscated their payloads through packing.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [The White Company](https://attack.mitre.org/groups/G0089) has checked for specific antivirus products on the target’s computer, including Kaspersky, Quick Heal, AVG, BitDefender, Avira, Sophos, Avast!, and ESET.[^1]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution |  [The White Company](https://attack.mitre.org/groups/G0089) has taken advantage of a known vulnerability in Microsoft Word (CVE 2012-0158) to execute code.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [The White Company](https://attack.mitre.org/groups/G0089) has the ability to delete its malware entirely from the target system.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [The White Company](https://attack.mitre.org/groups/G0089) has sent phishing emails with malicious Microsoft Word attachments to victims.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [The White Company](https://attack.mitre.org/groups/G0089) has used phishing lure documents that trick users into opening them and infecting their computers.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [The White Company](https://attack.mitre.org/groups/G0089) has checked the current date on the victim system.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[NETWIRE\|S0198]] | NETWIRE | [^1]  |
| [[Revenge RAT\|S0379]] | Revenge RAT | [^1]  |



## References

[^1]: [Cylance Shaheen Nov 2018](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)


