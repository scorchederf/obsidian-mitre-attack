---
aliases: 
    - Water Galura
    - GOLD FEATHER
mitre-attack: https://attack.mitre.org/groups/G1050
---

## G1050

[Water Galura](https://attack.mitre.org/groups/G1050) are the operators of the [Qilin](https://attack.mitre.org/software/S1242) Ransomware-as-a-Service (RaaS) who handle payload generation, ransom negotiations, and the publication of stolen data for [Qilin](https://attack.mitre.org/software/S1242) affilates recruited on Russian cybercrime forums. [Water Galura](https://attack.mitre.org/groups/G1050) have been active since at least 2022 and use a double extortion model where they demand payment for providing decryption keys and for refraining from publishing the stolen data to their leak site.[^1] [^3] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Social Media Accounts\|T1585.001]] | Social Media Accounts | [Water Galura](https://attack.mitre.org/groups/G1050) operates a news channel on Telegram to make announcements for the [Qilin](https://attack.mitre.org/software/S1242) RaaS.[^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Water Galura](https://attack.mitre.org/groups/G1050) has encrypted files on victim networks through the generation of [Qilin](https://attack.mitre.org/software/S1242) ransomware payloads.[^1] <br> |
| [[Financial Theft\|T1657]] | Financial Theft |  [Water Galura](https://attack.mitre.org/groups/G1050) has extorted victims for ransomware decryption keys and to prevent publication of data exfiltrated to their [Tor](https://attack.mitre.org/software/S0183) data leak site.[^1] [^2] <br><br> |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Tor\|S0183]] | Tor | [Water Galura](https://attack.mitre.org/groups/G1050) maintains a [Tor](https://attack.mitre.org/software/S0183)-hosted data leaks site for [Qilin](https://attack.mitre.org/software/S1242) ransomware and affiliates.[^1] [^3]  |
| [[Qilin\|S1242]] | Qilin | [Water Galura](https://attack.mitre.org/groups/G1050) are the operators of the [Qilin](https://attack.mitre.org/software/S1242) RaaS.[^1]  |



## References

[^1]: [BushidoToken Qilin RaaS JUN 2024](https://blog.bushidotoken.net/2024/06/tracking-adversaries-qilin-raas.html)


[^2]: [HC3 Qilin Threat Profile JUN 2024](https://www.aha.org/system/files/media/file/2024/06/tlp-clear-hc3-threat-profile-qilin-aka-agenda-ransomware-6-18-2024.pdf)


[^3]: [Sophos Qilin MSP APR 2025](https://news.sophos.com/en-us/2025/04/01/sophos-mdr-tracks-ongoing-campaign-by-qilin-affiliates-targeting-screenconnect/)


[^4]: GOLD FEATHER


