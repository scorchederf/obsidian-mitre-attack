---
aliases: 
    - PLATINUM
mitre-attack: https://attack.mitre.org/groups/G0068
---

## G0068

[PLATINUM](https://attack.mitre.org/groups/G0068) is an activity group that has targeted victims since at least 2009. The group has focused on targets associated with governments and related organizations in South and Southeast Asia. [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [PLATINUM](https://attack.mitre.org/groups/G0068) has sometimes used drive-by attacks against vulnerable browser plugins.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [PLATINUM](https://attack.mitre.org/groups/G0068) has transferred files using the Intel® Active Management Technology (AMT) Serial-over-LAN (SOL) channel.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [PLATINUM](https://attack.mitre.org/groups/G0068) has attempted to get users to open malicious files by sending spearphishing emails with attachments to victims.[^2]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [PLATINUM](https://attack.mitre.org/groups/G0068) has leveraged a zero-day vulnerability to escalate privileges.[^2]  |
| [[Credential API Hooking\|T1056.004]] | Credential API Hooking | [PLATINUM](https://attack.mitre.org/groups/G0068) is capable of using Windows hook interfaces for information gathering such as credential access.[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [PLATINUM](https://attack.mitre.org/groups/G0068) has used several different keyloggers.[^2]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [PLATINUM](https://attack.mitre.org/groups/G0068) has used keyloggers that are also capable of dumping credentials.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [PLATINUM](https://attack.mitre.org/groups/G0068) has used the Intel® Active Management Technology (AMT) Serial-over-LAN (SOL) channel for command and control.[^1]  |
| [[Process Injection\|T1055]] | Process Injection | [PLATINUM](https://attack.mitre.org/groups/G0068) has used various methods of process injection including hot patching.[^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [PLATINUM](https://attack.mitre.org/groups/G0068) has sent spearphishing emails with attachments to victims as its primary initial access vector.[^2]  |
| [[Masquerading\|T1036]] | Masquerading | [PLATINUM](https://attack.mitre.org/groups/G0068) has renamed rar.exe to avoid detection.[^4]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[adbupd\|S0202]] | adbupd | [^2]  |
| [[JPIN\|S0201]] | JPIN | [^2]  |
| [[Dipsind\|S0200]] | Dipsind | [^2]  |



## References

[^1]: [Microsoft PLATINUM June 2017](https://cloudblogs.microsoft.com/microsoftsecure/2017/06/07/platinum-continues-to-evolve-find-ways-to-maintain-invisibility/?source=mmpc)


[^2]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)


[^3]: PLATINUM


[^4]: [Twitter ItsReallyNick Platinum Masquerade](https://x.com/ItsReallyNick/status/1055321868641689600)


