---
aliases: 
    - Group5
mitre-attack: https://attack.mitre.org/groups/G0043
---

## G0043

[Group5](https://attack.mitre.org/groups/G0043) is a threat group with a suspected Iranian nexus, though this attribution is not definite. The group has targeted individuals connected to the Syrian opposition via spearphishing and watering holes, normally using Syrian and Iranian themes. [Group5](https://attack.mitre.org/groups/G0043) has used two commonly available remote access tools (RATs), [njRAT](https://attack.mitre.org/software/S0385) and [NanoCore](https://attack.mitre.org/software/S0336), as well as an Android RAT, DroidJack. [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Keylogging\|T1056.001]] | Keylogging | Malware used by [Group5](https://attack.mitre.org/groups/G0043) is capable of capturing keystrokes.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | Malware used by [Group5](https://attack.mitre.org/groups/G0043) is capable of watching the victim's screen.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | Malware used by [Group5](https://attack.mitre.org/groups/G0043) is capable of remotely deleting files from victims.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Group5](https://attack.mitre.org/groups/G0043) disguised its malicious binaries with several layers of obfuscation, including encrypting the files.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[NanoCore\|S0336]] | NanoCore | [^2]  |
| [[njRAT\|S0385]] | njRAT | [^2]  |



## References

[^1]: Group5


[^2]: [Citizen Lab Group5](https://citizenlab.ca/2016/08/group5-syria/)


