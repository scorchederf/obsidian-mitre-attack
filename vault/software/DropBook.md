---
aliases: 
    - S0547
    
mitre-attack: https://attack.mitre.org/software/S0547
---

## S0547

[DropBook](https://attack.mitre.org/software/S0547) is a Python-based backdoor compiled with PyInstaller.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Python\|T1059.006]] | Python | [DropBook](https://attack.mitre.org/software/S0547) is a Python-based backdoor compiled with PyInstaller.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [DropBook](https://attack.mitre.org/software/S0547) can execute arbitrary shell commands on the victims' machines.[^2] [^1]   |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [DropBook](https://attack.mitre.org/software/S0547) can collect the names of all files and folders in the Program Files directories.[^2] [^1]   |
| [[Web Service\|T1102]] | Web Service | [DropBook](https://attack.mitre.org/software/S0547) can communicate with its operators by exploiting the Simplenote, DropBox, and the social media platform, Facebook, where it can create fake accounts to control the backdoor and receive instructions.[^2] [^1]  |
| [[Exfiltration Over Web Service\|T1567]] | Exfiltration Over Web Service | [DropBook](https://attack.mitre.org/software/S0547) has used legitimate web services to exfiltrate data.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [DropBook](https://attack.mitre.org/software/S0547) can download and execute additional files.[^2] [^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [DropBook](https://attack.mitre.org/software/S0547) can unarchive data downloaded from the C2 to obtain the payload and persistence modules.[^2]   |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [DropBook](https://attack.mitre.org/software/S0547) has checked for the presence of Arabic language in the infected machine's settings.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [DropBook](https://attack.mitre.org/software/S0547) has checked for the presence of Arabic language in the infected machine's settings.[^2]   |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Molerats\|G0021]] | Molerats |



## References

[^1]: [BleepingComputer Molerats Dec 2020](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)


[^2]: [Cybereason Molerats Dec 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)


[^3]: DropBook


