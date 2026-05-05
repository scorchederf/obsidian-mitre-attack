---
aliases: 
    - Windshift
    - Bahamut
mitre-attack: https://attack.mitre.org/groups/G0112
---

## G0112

[Windshift](https://attack.mitre.org/groups/G0112) is a threat group that has been active since at least 2017, targeting specific individuals for surveillance in government departments and critical infrastructure across the Middle East.[^5] [^1] [^4] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [Windshift](https://attack.mitre.org/groups/G0112) has used malware to enumerate active processes.[^2]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Windshift](https://attack.mitre.org/groups/G0112) has used compromised websites to register custom URL schemes on a remote system.[^1]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Windshift](https://attack.mitre.org/groups/G0112) has used Visual Basic 6 (VB6) payloads.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Windshift](https://attack.mitre.org/groups/G0112) has used malware to identify installed AV and commonly used forensic and malware analysis tools.[^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Windshift](https://attack.mitre.org/groups/G0112) has sent spearphishing emails with attachment to harvest credentials and deliver malware.[^5]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Windshift](https://attack.mitre.org/groups/G0112) has used links embedded in e-mails to lure victims into executing malicious code.[^5]  |
| [[Spearphishing via Service\|T1566.003]] | Spearphishing via Service | [Windshift](https://attack.mitre.org/groups/G0112) has used fake personas on social media to engage and target victims.[^5] 	 |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Windshift](https://attack.mitre.org/groups/G0112) has created LNK files in the Startup folder to establish persistence.[^2]  |
| [[Software Discovery\|T1518]] | Software Discovery | [Windshift](https://attack.mitre.org/groups/G0112) has used malware to identify installed software.[^2]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Windshift](https://attack.mitre.org/groups/G0112) has sent spearphishing emails with links to harvest credentials and deliver malware.[^5]  |
| [[Invalid Code Signature\|T1036.001]] | Invalid Code Signature | [Windshift](https://attack.mitre.org/groups/G0112) has used revoked certificates to sign malware.[^1] [^5]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Windshift](https://attack.mitre.org/groups/G0112) has used string encoding with floating point calculations.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Windshift](https://attack.mitre.org/groups/G0112) has used tools that communicate with C2 over HTTP.[^2]  |
| [[Masquerading\|T1036]] | Masquerading | [Windshift](https://attack.mitre.org/groups/G0112) has used icons mimicking MS Office files to mask malicious executables.[^1]  [Windshift](https://attack.mitre.org/groups/G0112) has also attempted to hide executables by changing the file extension to ".scr" to mimic Windows screensavers.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Windshift](https://attack.mitre.org/groups/G0112) has used tools to deploy additional payloads to compromised hosts.[^2]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Windshift](https://attack.mitre.org/groups/G0112) has used WMI to collect information about target machines.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Windshift](https://attack.mitre.org/groups/G0112) has used malware to identify the username on a compromised host.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Windshift](https://attack.mitre.org/groups/G0112) has used malware to identify the computer name of a compromised host.[^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Windshift](https://attack.mitre.org/groups/G0112) has used e-mail attachments to lure victims into executing malicious code.[^5]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[WindTail\|S0466]] | WindTail | [^5] [^1] [^4]  |



## References

[^1]: [objective-see windtail1 dec 2018](https://objective-see.com/blog/blog_0x3B.html)


[^2]: [BlackBerry Bahamut](https://www.blackberry.com/us/en/pdfviewer?file=/content/dam/blackberry-com/asset/enterprise/pdf/direct/report-spark-bahamut.pdf)


[^3]: Bahamut


[^4]: [objective-see windtail2 jan 2019](https://objective-see.com/blog/blog_0x3D.html)


[^5]: [SANS Windshift August 2018](https://www.scribd.com/document/661837258/WINDSHIFT-summit-archive-1554718868)


