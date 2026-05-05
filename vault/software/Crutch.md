---
aliases: 
    - S0538
    
mitre-attack: https://attack.mitre.org/software/S0538
---

## S0538

[Crutch](https://attack.mitre.org/software/S0538) is a backdoor designed for document theft that has been used by [Turla](https://attack.mitre.org/groups/G0010) since at least 2015.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Crutch](https://attack.mitre.org/software/S0538) has used the WinRAR utility to compress and encrypt stolen files.[^1]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [Crutch](https://attack.mitre.org/software/S0538) can monitor for removable drives being plugged into the compromised machine.[^1]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [Crutch](https://attack.mitre.org/software/S0538) can use Dropbox to receive commands and upload stolen data.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Crutch](https://attack.mitre.org/software/S0538) has conducted C2 communications with a Dropbox account using the HTTP API.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Crutch](https://attack.mitre.org/software/S0538) has the ability to persist using scheduled tasks.[^1]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Crutch](https://attack.mitre.org/software/S0538) has exfiltrated stolen data to Dropbox.[^1]  |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | [Crutch](https://attack.mitre.org/software/S0538) can monitor removable drives and exfiltrate files matching a given extension list.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Crutch](https://attack.mitre.org/software/S0538) has established persistence with a scheduled task impersonating the Outlook item finder.[^1]  |
| [[DLL\|T1574.001]] | DLL | [Crutch](https://attack.mitre.org/software/S0538) can persist via DLL search order hijacking on Google Chrome, Mozilla Firefox, or Microsoft OneDrive.[^1]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [Crutch](https://attack.mitre.org/software/S0538) has automatically exfiltrated stolen files to Dropbox.[^1]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Crutch](https://attack.mitre.org/software/S0538) can automatically monitor removable drives in a loop and copy interesting files.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Crutch](https://attack.mitre.org/software/S0538) can exfiltrate files from compromised systems.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Crutch](https://attack.mitre.org/software/S0538) has used a hardcoded GitHub repository as a fallback channel.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Crutch](https://attack.mitre.org/software/S0538) has staged stolen files in the `C:\AMD\Temp` directory.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Crutch](https://attack.mitre.org/software/S0538) can exfiltrate data over the primary C2 channel (Dropbox HTTP API).[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Turla\|G0010]] | Turla |



## References

[^1]: [ESET Crutch December 2020](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)


[^2]: [Talos TinyTurla September 2021](https://blog.talosintelligence.com/2021/09/tinyturla.html)


