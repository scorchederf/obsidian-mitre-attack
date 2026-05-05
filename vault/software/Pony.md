---
aliases: 
    - S0453
    
mitre-attack: https://attack.mitre.org/software/S0453
---

## S0453

[Pony](https://attack.mitre.org/software/S0453) is a credential stealing malware, though has also been used among adversaries for its downloader capabilities. The source code for Pony Loader 1.0 and 2.0 were leaked online, leading to their use by various threat actors.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Native API\|T1106]] | Native API | [Pony](https://attack.mitre.org/software/S0453) has used several Windows functions for various purposes.[^1] 	 |
| [[Malicious File\|T1204.002]] | Malicious File | [Pony](https://attack.mitre.org/software/S0453) has attempted to lure targets into downloading an attached executable (ZIP, RAR, or CAB archives) or document (PDF or other MS Office format).[^1]  |
| [[Compression\|T1027.015]] | Compression | [Pony](https://attack.mitre.org/software/S0453) attachments have been delivered via compressed archive files.[^1]  |
| [[Masquerading\|T1036]] | Masquerading | [Pony](https://attack.mitre.org/software/S0453) has used the Adobe Reader icon for the downloaded file to look more trustworthy.[^1] 	 |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Pony](https://attack.mitre.org/software/S0453) can download additional files onto the infected system.[^1] 	 |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Pony](https://attack.mitre.org/software/S0453) has used batch scripts to delete itself after execution.[^1] 	 |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [Pony](https://attack.mitre.org/software/S0453) obfuscates memory flow by adding junk instructions when executing to make analysis more difficult.[^1] 	 |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Pony](https://attack.mitre.org/software/S0453) has been delivered via spearphishing emails which contained malicious links.[^1] 	 |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Pony](https://attack.mitre.org/software/S0453) has collected the Service Pack, language, and region information to send to the C2.[^1] 	 |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [Pony](https://attack.mitre.org/software/S0453) has delayed execution using a built-in function to avoid detection and analysis.[^1] 	 |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Pony](https://attack.mitre.org/software/S0453) has attempted to lure targets into clicking links in spoofed emails from legitimate banks.[^1] 	 |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Pony](https://attack.mitre.org/software/S0453) has sent collected information to the C2 via HTTP POST request.[^1] 	 |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Pony](https://attack.mitre.org/software/S0453) has been delivered via spearphishing attachments.[^1]  |
| [[Local Account\|T1087.001]] | Local Account | [Pony](https://attack.mitre.org/software/S0453) has used the `NetUserEnum` function to enumerate local accounts.[^1] 	 |
| [[Password Guessing\|T1110.001]] | Password Guessing | [Pony](https://attack.mitre.org/software/S0453) has used a small dictionary of common passwords against a collected list of local accounts.[^1] 	 |
| [[File Deletion\|T1070.004]] | File Deletion | [Pony](https://attack.mitre.org/software/S0453) has used scripts to delete itself after execution.[^1] 	 |




## References

[^1]: [Malwarebytes Pony April 2016](https://blog.malwarebytes.com/threat-analysis/2015/11/no-money-but-pony-from-a-mail-to-a-trojan-horse/)


