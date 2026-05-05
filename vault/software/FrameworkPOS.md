---
aliases: 
    - S0503
    
mitre-attack: https://attack.mitre.org/software/S0503
---

## S0503

[FrameworkPOS](https://attack.mitre.org/software/S0503) is a point of sale (POS) malware used by [FIN6](https://attack.mitre.org/groups/G0037) to steal payment card data from sytems that run physical POS devices.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data from Local System\|T1005]] | Data from Local System | [FrameworkPOS](https://attack.mitre.org/software/S0503) can collect elements related to credit card data from process memory.[^2]  |
| [[Exfiltration Over Alternative Protocol\|T1048]] | Exfiltration Over Alternative Protocol | [FrameworkPOS](https://attack.mitre.org/software/S0503) can use DNS tunneling for exfiltration of credit card data.[^2]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [FrameworkPOS](https://attack.mitre.org/software/S0503) can identifiy payment card track data on the victim and copy it to a local file in a subdirectory of C:\Windows\.[^4]  |
| [[Process Discovery\|T1057]] | Process Discovery | [FrameworkPOS](https://attack.mitre.org/software/S0503) can enumerate and exclude selected processes on a compromised host to speed execution of memory scraping.[^2]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [FrameworkPOS](https://attack.mitre.org/software/S0503) can XOR credit card information before exfiltration.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN6\|G0037]] | FIN6 |



## References

[^1]: [Crowdstrike Global Threat Report Feb 2018](https://crowdstrike.lookbookhq.com/global-threat-report-2018-web/cs-2018-global-threat-report)


[^2]: [SentinelOne FrameworkPOS September 2019](https://labs.sentinelone.com/fin6-frameworkpos-point-of-sale-malware-analysis-internals-2/)


[^3]: [Visa FIN6 Feb 2019](https://usa.visa.com/dam/VCOM/global/support-legal/documents/fin6-cybercrime-group-expands-threat-To-ecommerce-merchants.pdf)


[^4]: [FireEye FIN6 April 2016](https://web.archive.org/web/20190807112824/https://www2.fireeye.com/rs/848-DID-242/images/rpt-fin6.pdf)


[^5]: Trinity


