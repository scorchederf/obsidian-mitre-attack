---
aliases: 
    - Confucius
    - Confucius APT
mitre-attack: https://attack.mitre.org/groups/G0142
---

## G0142

[Confucius](https://attack.mitre.org/groups/G0142) is a cyber espionage group that has primarily targeted military personnel, high-profile personalities, business persons, and government organizations in South Asia since at least 2013. Security researchers have noted similarities between [Confucius](https://attack.mitre.org/groups/G0142) and [Patchwork](https://attack.mitre.org/groups/G0040), particularly in their respective custom malware code and targets.[^1] [^3] [^4] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Confucius](https://attack.mitre.org/groups/G0142) has sent malicious links to victims through email campaigns.[^3]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Confucius](https://attack.mitre.org/groups/G0142) has lured victims into clicking on a malicious link sent through spearphishing.[^3]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Confucius](https://attack.mitre.org/groups/G0142) has exfiltrated victim data to cloud storage service accounts.[^1]  |
| [[Template Injection\|T1221]] | Template Injection | [Confucius](https://attack.mitre.org/groups/G0142) has used a weaponized Microsoft Word document with an embedded RTF exploit.[^4]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Confucius](https://attack.mitre.org/groups/G0142) has used VBScript to execute malicious code.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Confucius](https://attack.mitre.org/groups/G0142) has crafted and sent victims malicious attachments to gain initial access.[^4]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Confucius](https://attack.mitre.org/groups/G0142) has exploited Microsoft Office vulnerabilities, including CVE-2015-1641, CVE-2017-11882, and CVE-2018-0802.[^4] [^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Confucius](https://attack.mitre.org/groups/G0142) has used a file stealer that can examine system drives, including those other than the C drive.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Confucius](https://attack.mitre.org/groups/G0142) has downloaded additional files and payloads onto a compromised host following initial access.[^4] [^3]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Confucius](https://attack.mitre.org/groups/G0142) has used a file stealer to steal documents and images with the following extensions: txt, pdf, png, jpg, doc, xls, xlm, odp, ods, odt, rtf, ppt, xlsx, xlsm, docx, pptx, and jpeg.[^3]  |
| [[Web Services\|T1583.006]] | Web Services | [Confucius](https://attack.mitre.org/groups/G0142) has obtained cloud storage service accounts to host stolen data.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Confucius](https://attack.mitre.org/groups/G0142) has used HTTP for C2 communications.[^4]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Confucius](https://attack.mitre.org/groups/G0142) has exfiltrated stolen files to its C2 server.[^3]  |
| [[Mshta\|T1218.005]] | Mshta | [Confucius](https://attack.mitre.org/groups/G0142) has used mshta.exe to execute malicious VBScript.[^1]   |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Confucius](https://attack.mitre.org/groups/G0142) has used a file stealer that checks the Document, Downloads, Desktop, and Picture folders for documents and images with specific extensions.[^3]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Confucius](https://attack.mitre.org/groups/G0142) has dropped malicious files into the startup folder `%AppData%\Microsoft\Windows\Start Menu\Programs\Startup` on a compromised host in order to maintain persistence.[^4]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Confucius](https://attack.mitre.org/groups/G0142) has created scheduled tasks to maintain persistence on a compromised host.[^3]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Confucius](https://attack.mitre.org/groups/G0142) has lured victims to execute malicious attachments included in crafted spearphishing emails related to current topics.[^4]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Confucius](https://attack.mitre.org/groups/G0142) has used PowerShell to execute malicious files and payloads.[^3]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[WarzoneRAT\|S0670]] | WarzoneRAT | [^2] [^4]  |



## References

[^1]: [TrendMicro Confucius APT Feb 2018](https://www.trendmicro.com/en_us/research/18/b/deciphering-confucius-cyberespionage-operations.html)


[^2]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)


[^3]: [TrendMicro Confucius APT Aug 2021](https://www.trendmicro.com/en_us/research/21/h/confucius-uses-pegasus-spyware-related-lures-to-target-pakistani.html)


[^4]: [Uptycs Confucius APT Jan 2021](https://www.uptycs.com/blog/confucius-apt-deploys-warzone-rat)


