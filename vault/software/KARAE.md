---
aliases: 
    - S0215
    
mitre-attack: https://attack.mitre.org/software/S0215
---

## S0215

[KARAE](https://attack.mitre.org/software/S0215) is a backdoor typically used by [APT37](https://attack.mitre.org/groups/G0067) as first-stage malware. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [KARAE](https://attack.mitre.org/software/S0215) was distributed through torrent file-sharing websites to South Korean victims, using a YouTube video downloader application as a lure.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [KARAE](https://attack.mitre.org/software/S0215) can upload and download files, including second-stage malware.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [KARAE](https://attack.mitre.org/software/S0215) can collect system information.[^2]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [KARAE](https://attack.mitre.org/software/S0215) can use public cloud-based storage providers for command and control.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT37\|G0067]] | APT37 |



## References

[^1]: KARAE


[^2]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)


