---
aliases: 
    - DarkHydrus
mitre-attack: https://attack.mitre.org/groups/G0079
---

## G0079

[DarkHydrus](https://attack.mitre.org/groups/G0079) is a threat group that has targeted government agencies and educational institutions in the Middle East since at least 2016. The group heavily leverages open-source tools and custom payloads for carrying out attacks. [^4]  [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Malicious File\|T1204.002]] | Malicious File | [DarkHydrus](https://attack.mitre.org/groups/G0079) has sent malware that required users to hit the enable button in Microsoft Excel to allow an .iqy file to be downloaded.[^4] [^2]  |
| [[Forced Authentication\|T1187]] | Forced Authentication | [DarkHydrus](https://attack.mitre.org/groups/G0079) used [Template Injection](https://attack.mitre.org/techniques/T1221) to launch an authentication window for users to enter their credentials.[^1]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [DarkHydrus](https://attack.mitre.org/groups/G0079) has used `-WindowStyle Hidden` to conceal [PowerShell](https://attack.mitre.org/techniques/T1059/001) windows. [^4]  |
| [[PowerShell\|T1059.001]] | PowerShell | [DarkHydrus](https://attack.mitre.org/groups/G0079) leveraged PowerShell to download and execute additional scripts for execution.[^4] [^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [DarkHydrus](https://attack.mitre.org/groups/G0079) has sent spearphishing emails with password-protected RAR archives containing malicious Excel Web Query files (.iqy). The group has also sent spearphishing emails that contained malicious Microsoft Office documents that use the “attachedTemplate” technique to load a template from a remote server.[^4] [^1] [^2]  |
| [[Template Injection\|T1221]] | Template Injection | [DarkHydrus](https://attack.mitre.org/groups/G0079) used an open-source tool, Phishery, to inject malicious remote template URLs into Microsoft Word documents and then sent them to victims to enable [Forced Authentication](https://attack.mitre.org/techniques/T1187).[^1]  |
| [[Tool\|T1588.002]] | Tool | [DarkHydrus](https://attack.mitre.org/groups/G0079) has obtained and used tools such as [Mimikatz](https://attack.mitre.org/software/S0002), [Empire](https://attack.mitre.org/software/S0363), and [Cobalt Strike](https://attack.mitre.org/software/S0154).[^4]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Mimikatz\|S0002]] | Mimikatz | [^4] [^2]  |
| [[RogueRobin\|S0270]] | RogueRobin | [^4] [^5]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^4] [^2]  |



## References

[^1]: [Unit 42 Phishery Aug 2018](https://researchcenter.paloaltonetworks.com/2018/08/unit42-darkhydrus-uses-phishery-harvest-credentials-middle-east/)


[^2]: [Unit 42 Playbook Dec 2017](https://pan-unit42.github.io/playbook_viewer/)


[^3]: DarkHydrus


[^4]: [Unit 42 DarkHydrus July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)


[^5]: [Unit42 DarkHydrus Jan 2019](https://unit42.paloaltonetworks.com/darkhydrus-delivers-new-trojan-that-can-use-google-drive-for-c2-communications/)


