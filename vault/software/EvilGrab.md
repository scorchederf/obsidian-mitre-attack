---
aliases: 
    - S0152
    
mitre-attack: https://attack.mitre.org/software/S0152
---

## S0152

[EvilGrab](https://attack.mitre.org/software/S0152) is a malware family with common reconnaissance capabilities. It has been deployed by [menuPass](https://attack.mitre.org/groups/G0045) via malicious Microsoft Office documents as part of spearphishing campaigns. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Keylogging\|T1056.001]] | Keylogging | [EvilGrab](https://attack.mitre.org/software/S0152) has the capability to capture keystrokes.[^1]  |
| [[Audio Capture\|T1123]] | Audio Capture | [EvilGrab](https://attack.mitre.org/software/S0152) has the capability to capture audio from a victim machine.[^1]  |
| [[Video Capture\|T1125]] | Video Capture | [EvilGrab](https://attack.mitre.org/software/S0152) has the capability to capture video from a victim machine.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [EvilGrab](https://attack.mitre.org/software/S0152) has the capability to capture screenshots.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [EvilGrab](https://attack.mitre.org/software/S0152) adds a Registry Run key for ctfmon.exe to establish persistence.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[menuPass\|G0045]] | menuPass |



## References

[^1]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


