---
aliases: 
    - S0593
    
mitre-attack: https://attack.mitre.org/software/S0593
---

## S0593

[ECCENTRICBANDWAGON](https://attack.mitre.org/software/S0593) is a remote access Trojan (RAT) used by North Korean cyber actors that was first identified in August 2020. It is a reconnaissance tool--with keylogging and screen capture functionality--used for information gathering on compromised systems.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File Deletion\|T1070.004]] | File Deletion | [ECCENTRICBANDWAGON](https://attack.mitre.org/software/S0593) can delete log files generated from the malware stored at `C:\windows\temp\tmp0207`.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [ECCENTRICBANDWAGON](https://attack.mitre.org/software/S0593) has encrypted strings with RC4.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [ECCENTRICBANDWAGON](https://attack.mitre.org/software/S0593) can use [cmd](https://attack.mitre.org/software/S0106) to execute commands on a victim’s machine.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [ECCENTRICBANDWAGON](https://attack.mitre.org/software/S0593) can capture screenshots and store them locally.[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [ECCENTRICBANDWAGON](https://attack.mitre.org/software/S0593) can capture and store keystrokes.[^2]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [ECCENTRICBANDWAGON](https://attack.mitre.org/software/S0593) has stored keystrokes and screenshots within the `%temp%\GoogleChrome`, `%temp%\Downloads`, and `%temp%\TrendMicroUpdate` directories.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT38\|G0082]] | APT38 |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: ECCENTRICBANDWAGON


[^2]: [CISA EB Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-239a)


[^3]: [CISA AA20-239A BeagleBoyz August 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-239a)


