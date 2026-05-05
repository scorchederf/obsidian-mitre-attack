---
aliases: 
    - S0634
    
mitre-attack: https://attack.mitre.org/software/S0634
---

## S0634

[EnvyScout](https://attack.mitre.org/software/S0634) is a dropper that has been used by [APT29](https://attack.mitre.org/groups/G0016) since at least 2021.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [EnvyScout](https://attack.mitre.org/software/S0634) can determine whether the ISO payload was received by a Windows or iOS device.[^1]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [EnvyScout](https://attack.mitre.org/software/S0634) can call `window.location.pathname` to ensure that embedded files are being executed from the C: drive, and will terminate if they are not.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [EnvyScout](https://attack.mitre.org/software/S0634) has been executed through malicious files attached to e-mails.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [EnvyScout](https://attack.mitre.org/software/S0634) has the ability to proxy execution of malicious files with Rundll32.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [EnvyScout](https://attack.mitre.org/software/S0634) can collect sensitive NTLM material from a compromised host.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [EnvyScout](https://attack.mitre.org/software/S0634) has been distributed via spearphishing as an email attachment.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [EnvyScout](https://attack.mitre.org/software/S0634) can deobfuscate and write malicious ISO files to disk.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [EnvyScout](https://attack.mitre.org/software/S0634) can Base64 encode payloads.[^1]  |
| [[JavaScript\|T1059.007]] | JavaScript | [EnvyScout](https://attack.mitre.org/software/S0634) can write files to disk with JavaScript using a modified version of the open-source tool FileSaver.[^1]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [EnvyScout](https://attack.mitre.org/software/S0634) can use hidden directories and files to hide malicious executables.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [EnvyScout](https://attack.mitre.org/software/S0634) can use cmd.exe to execute malicious files on compromised hosts.[^1]  |
| [[HTML Smuggling\|T1027.006]] | HTML Smuggling | [EnvyScout](https://attack.mitre.org/software/S0634) contains JavaScript code that can extract an encoded blob from its HTML body and write it to disk.[^1]  |
| [[Forced Authentication\|T1187]] | Forced Authentication | [EnvyScout](https://attack.mitre.org/software/S0634) can use protocol handlers to coax the operating system to send NTLMv2 authentication responses to attacker-controlled infrastructure.[^1]  |
| [[Masquerading\|T1036]] | Masquerading | [EnvyScout](https://attack.mitre.org/software/S0634) has used folder icons for malicious files to lure victims into opening them.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)


