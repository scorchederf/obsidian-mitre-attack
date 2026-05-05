---
aliases: 
    - S0129
    
mitre-attack: https://attack.mitre.org/software/S0129
---

## S0129

[AutoIt backdoor](https://attack.mitre.org/software/S0129) is malware that has been used by the actors responsible for the MONSOON campaign. The actors frequently used it in weaponized .pps files exploiting CVE-2014-6352. [^1]  This malware makes use of the legitimate scripting language for Windows GUI automation with the same name.

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [AutoIt backdoor](https://attack.mitre.org/software/S0129) is capable of identifying documents on the victim with the following extensions: .doc; .pdf, .csv, .ppt, .docx, .pst, .xls, .xlsx, .pptx, and .jpeg.[^1]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [AutoIt backdoor](https://attack.mitre.org/software/S0129) attempts to escalate privileges by bypassing User Access Control.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [AutoIt backdoor](https://attack.mitre.org/software/S0129) has sent a C2 response that was base64-encoded.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [AutoIt backdoor](https://attack.mitre.org/software/S0129) downloads a PowerShell script that decodes to a typical shellcode loader.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT33\|G0064]] | APT33 |
| [[Patchwork\|G0040]] | Patchwork |



## References

[^1]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)


[^2]: [Symantec Elfin Mar 2019](https://www.symantec.com/blogs/threat-intelligence/elfin-apt33-espionage)


