---
aliases: 
    - S0355
    
mitre-attack: https://attack.mitre.org/software/S0355
---

## S0355

[Final1stspy](https://attack.mitre.org/software/S0355) is a dropper family that has been used to deliver [DOGCALL](https://attack.mitre.org/software/S0213).[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Final1stspy](https://attack.mitre.org/software/S0355) creates a Registry Run key to establish persistence.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Final1stspy](https://attack.mitre.org/software/S0355) uses Python code to deobfuscate base64-encoded strings.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Final1stspy](https://attack.mitre.org/software/S0355) obfuscates strings with base64 encoding.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Final1stspy](https://attack.mitre.org/software/S0355) obtains a list of running processes.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Final1stspy](https://attack.mitre.org/software/S0355) obtains victim Microsoft Windows version information and CPU architecture.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Final1stspy](https://attack.mitre.org/software/S0355) uses HTTP for C2.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT37\|G0067]] | APT37 |



## References

[^1]: Final1stspy


[^2]: [Unit 42 Nokki Oct 2018](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)


