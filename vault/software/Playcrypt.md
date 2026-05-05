---
aliases: 
    - S1162
    
mitre-attack: https://attack.mitre.org/software/S1162
---

## S1162

[Playcrypt](https://attack.mitre.org/software/S1162) is a ransomware that has been used by [Play](https://attack.mitre.org/groups/G1040) since at least 2022 in attacks against against the business, government, critical infrastructure, healthcare, and media sectors in North America, South America, and Europe. [Playcrypt](https://attack.mitre.org/software/S1162) derives its name from adding the .play extension to encrypted files and has overlap with tactics and tools associated with Hive and Nokoyawa ransomware and infrastructure associated with Quantum ransomware.[^3] [^4] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Playcrypt](https://attack.mitre.org/software/S1162) encrypts files on targeted hosts with an AES-RSA hybrid encryption, encrypting every other file portion of 0x100000 bytes.[^4] [^1]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Playcrypt](https://attack.mitre.org/software/S1162) can use AlphaVSS to delete shadow copies.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Playcrypt](https://attack.mitre.org/software/S1162) can avoid encrypting files with a .PLAY, .exe, .msi, .dll, .lnk, or .sys file extension.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Play\|G1040]] | Play |



## References

[^1]: [Trend Micro Ransomware Spotlight Play July 2023](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)


[^2]: Play


[^3]: [Microsoft PlayCrypt August 2022](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Ransom:Win32/PlayCrypt.PA&ThreatID=2147830341)


[^4]: [CISA Play Ransomware Advisory December 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a)


