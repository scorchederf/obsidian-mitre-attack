---
aliases: 
    - RTM
mitre-attack: https://attack.mitre.org/groups/G0048
---

## G0048

[RTM](https://attack.mitre.org/groups/G0048) is a cybercriminal group that has been active since at least 2015 and is primarily interested in users of remote banking systems in Russia and neighboring countries. The group uses a Trojan by the same name ([RTM](https://attack.mitre.org/software/S0148)). [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [RTM](https://attack.mitre.org/groups/G0048) has distributed its malware via the RIG and SUNDOWN exploit kits, as well as online advertising network `Yandex.Direct`.[^2] [^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [RTM](https://attack.mitre.org/groups/G0048) has used Registry run keys to establish persistence for the [RTM](https://attack.mitre.org/software/S0148) Trojan and other tools, such as a modified version of TeamViewer remote desktop software.[^2] [^3]  |
| [[DLL\|T1574.001]] | DLL | [RTM](https://attack.mitre.org/groups/G0048) has used search order hijacking to force TeamViewer to load a malicious DLL.[^3]  |
| [[Malicious File\|T1204.002]] | Malicious File | [RTM](https://attack.mitre.org/groups/G0048) has attempted to lure victims into opening e-mail attachments to execute malicious code.[^3]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [RTM](https://attack.mitre.org/groups/G0048) has used spearphishing attachments to distribute its malware.[^3]  |
| [[Remote Desktop Software\|T1219.002]] | Remote Desktop Software | [RTM](https://attack.mitre.org/groups/G0048) has used a modified version of TeamViewer and Remote Utilities for remote access.[^3]  |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | [RTM](https://attack.mitre.org/groups/G0048) has used an RSS feed on Livejournal to update a list of encrypted C2 server names.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[RTM\|S0148]] | RTM | [^2]  |



## References

[^1]: [ESET Buhtrap and Buran April 2019](https://www.welivesecurity.com/2019/04/30/buhtrap-backdoor-ransomware-advertising-platform/)


[^2]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)


[^3]: [Group IB RTM August 2019](https://www.group-ib.com/blog/rtm)


[^4]: RTM


