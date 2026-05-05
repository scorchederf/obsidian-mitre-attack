---
aliases: 
    - S0644
    
mitre-attack: https://attack.mitre.org/software/S0644
---

## S0644

[ObliqueRAT](https://attack.mitre.org/software/S0644) is a remote access trojan, similar to [Crimson](https://attack.mitre.org/software/S0115), that has been in use by [Transparent Tribe](https://attack.mitre.org/groups/G0134) since at least 2020.[^1] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Screen Capture\|T1113]] | Screen Capture | [ObliqueRAT](https://attack.mitre.org/software/S0644) can capture a screenshot of the current screen.[^1] <br> |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [ObliqueRAT](https://attack.mitre.org/software/S0644) can discover pluggable/removable drives to extract files from.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [ObliqueRAT](https://attack.mitre.org/software/S0644) can gain persistence by a creating a shortcut in the infected user's Startup directory.[^1]  |
| [[Data Transfer Size Limits\|T1030]] | Data Transfer Size Limits | [ObliqueRAT](https://attack.mitre.org/software/S0644) can break large files of interest into smaller chunks to prepare them for exfiltration.[^1]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [ObliqueRAT](https://attack.mitre.org/software/S0644) has gained execution on targeted systems through luring users to click on links to malicious URLs.[^1] [^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [ObliqueRAT](https://attack.mitre.org/software/S0644) has the ability to check for blocklisted computer names on infected endpoints.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [ObliqueRAT](https://attack.mitre.org/software/S0644) has the ability to recursively enumerate files on an infected endpoint.[^1]  |
| [[Steganography\|T1027.003]] | Steganography | [ObliqueRAT](https://attack.mitre.org/software/S0644) can hide its payload in BMP images hosted on compromised websites.[^1]  |
| [[System Checks\|T1497.001]] | System Checks | [ObliqueRAT](https://attack.mitre.org/software/S0644) can halt execution if it identifies processes belonging to virtual machine software or analysis tools.[^1]  |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | [ObliqueRAT](https://attack.mitre.org/software/S0644) has the ability to extract data from removable devices connected to the endpoint.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [ObliqueRAT](https://attack.mitre.org/software/S0644) can copy specific files, webcam captures, and screenshots to local directories.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [ObliqueRAT](https://attack.mitre.org/software/S0644) can check for blocklisted process names on a compromised host.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [ObliqueRAT](https://attack.mitre.org/software/S0644) can check for blocklisted usernames on infected endpoints.[^1]  |
| [[Video Capture\|T1125]] | Video Capture | [ObliqueRAT](https://attack.mitre.org/software/S0644) can capture images from webcams on compromised hosts.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Transparent Tribe\|G0134]] | Transparent Tribe |



## References

[^1]: [Talos Oblique RAT March 2021](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)


[^2]: [Cisco Talos Transparent Tribe Education Campaign July 2022](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)


[^3]: [Talos Transparent Tribe May 2021](https://blog.talosintelligence.com/2021/05/transparent-tribe-infra-and-targeting.html)


