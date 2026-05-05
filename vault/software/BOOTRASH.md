---
aliases: 
    - S0114
    
mitre-attack: https://attack.mitre.org/software/S0114
---

## S0114

[BOOTRASH](https://attack.mitre.org/software/S0114) is a [Bootkit](https://attack.mitre.org/techniques/T1542/003) that targets Windows operating systems. It has been used by threat actors that target the financial sector.[^2] [^3] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Hidden File System\|T1564.005]] | Hidden File System | [BOOTRASH](https://attack.mitre.org/software/S0114) has used unallocated disk space between partitions for a hidden file system that stores components of the Nemesis bootkit.[^3]  |
| [[Bootkit\|T1542.003]] | Bootkit | [BOOTRASH](https://attack.mitre.org/software/S0114) is a Volume Boot Record (VBR) bootkit that uses the VBR to maintain persistence.[^2] [^3] [^1]  |




## References

[^1]: [FireEye BOOTRASH SANS](https://web.archive.org/web/20190926040727/https://www.sans.org/cyber-security-summit/archives/file/summit-archive-1498163766.pdf)


[^2]: [Mandiant M Trends 2016](https://web.archive.org/web/20211024160454/https://www.fireeye.com/content/dam/fireeye-www/current-threats/pdfs/rpt-mtrends-2016.pdf)


[^3]: [FireEye Bootkits](https://www.fireeye.com/blog/threat-research/2015/12/fin1-targets-boot-record.html)


