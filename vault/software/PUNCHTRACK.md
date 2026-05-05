---
aliases: 
    - S0197
    
mitre-attack: https://attack.mitre.org/software/S0197
---

## S0197

[PUNCHTRACK](https://attack.mitre.org/software/S0197) is non-persistent point of sale (POS) system malware utilized by [FIN8](https://attack.mitre.org/groups/G0061) to scrape payment card data. [^1]  [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data from Local System\|T1005]] | Data from Local System | [PUNCHTRACK](https://attack.mitre.org/software/S0197) scrapes memory for properly formatted payment card data.[^1] [^4]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [PUNCHTRACK](https://attack.mitre.org/software/S0197) is loaded and executed by a highly obfuscated launcher.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [PUNCHTRACK](https://attack.mitre.org/software/S0197) aggregates collected data in a tmp file.[^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN8\|G0061]] | FIN8 |



## References

[^1]: [FireEye Fin8 May 2016](https://www.fireeye.com/blog/threat-research/2016/05/windows-zero-day-payment-cards.html)


[^2]: PUNCHTRACK


[^3]: PSVC


[^4]: [FireEye Know Your Enemy FIN8 Aug 2016](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)


