---
aliases: 
    - S0008
    
mitre-attack: https://attack.mitre.org/software/S0008
---

## S0008

[gsecdump](https://attack.mitre.org/software/S0008) is a publicly-available credential dumper used to obtain password hashes and LSA secrets from Windows operating systems. [^7] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [gsecdump](https://attack.mitre.org/software/S0008) can dump Windows password hashes from the SAM.[^4]  |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | [gsecdump](https://attack.mitre.org/software/S0008) can dump LSA secrets.[^7]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 |
| [[APT1\|G0006]] | APT1 |
| [[PittyTiger\|G0011]] | PittyTiger |
| [[Tonto Team\|G0131]] | Tonto Team |
| [[BRONZE BUTLER\|G0060]] | BRONZE BUTLER |



## References

[^1]: [Secureworks BRONZE BUTLER Oct 2017](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)


[^2]: [Dell TG-3390](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)


[^3]: [Bizeul 2014](https://airbus-cyber-security.com/the-eye-of-the-tiger/)


[^4]: [Microsoft Gsecdump](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=HackTool:Win32/Gsecdump)


[^5]: [Symantec Tick Apr 2016](https://www.symantec.com/connect/blogs/tick-cyberespionage-group-zeros-japan)


[^6]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)


[^7]: [TrueSec Gsecdump](https://web.archive.org/web/20140328102838/https://www.truesec.se/sakerhet/verktyg/saakerhet/gsecdump_v2.0b5)


[^8]: [TrendMicro Tonto Team October 2020](https://vb2020.vblocalhost.com/uploads/VB2020-06.pdf)


