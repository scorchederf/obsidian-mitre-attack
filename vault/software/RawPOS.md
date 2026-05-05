---
aliases: 
    - S0169
    
mitre-attack: https://attack.mitre.org/software/S0169
---

## S0169

[RawPOS](https://attack.mitre.org/software/S0169) is a point-of-sale (POS) malware family that searches for cardholder data on victims. It has been in use since at least 2008. [^1]  [^5]  [^4]  FireEye divides RawPOS into three components: FIENDCRY, DUEBREW, and DRIFTWOOD. [^9]  [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | New services created by [RawPOS](https://attack.mitre.org/software/S0169) are made to appear like legitimate Windows services, with names such as "Windows Management Help Service", "Microsoft Support", and "Windows Advanced Task Manager".[^1] [^5] [^9]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [RawPOS](https://attack.mitre.org/software/S0169) encodes credit card data it collected from the victim with XOR.[^5] [^9] [^4]  |
| [[Data from Local System\|T1005]] | Data from Local System | [RawPOS](https://attack.mitre.org/software/S0169) dumps memory from specific processes on a victim system, parses the dumped files, and scrapes them for credit card data.[^1] [^5] [^9]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | Data captured by [RawPOS](https://attack.mitre.org/software/S0169) is placed in a temporary file under a directory named "memdump".[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [RawPOS](https://attack.mitre.org/software/S0169) installs itself as a service to maintain persistence.[^1] [^5] [^9]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN5\|G0053]] | FIN5 |



## References

[^1]: [Kroll RawPOS Jan 2017](https://www.kroll.com/en/insights/publications/malware-analysis-report-rawpos-malware)


[^2]: [DarkReading FireEye FIN5 Oct 2015](https://www.darkreading.com/analytics/prolific-cybercrime-gang-favors-legit-login-credentials/d/d-id/1322645?)


[^3]: DRIFTWOOD


[^4]: [Visa RawPOS March 2015](https://usa.visa.com/dam/VCOM/download/merchants/alert-rawpos.pdf)


[^5]: [TrendMicro RawPOS April 2015](http://sjc1-te-ftp.trendmicro.com/images/tex/pdf/RawPOS%20Technical%20Brief.pdf)


[^6]: FIENDCRY


[^7]: RawPOS


[^8]: [Github Mempdump](https://github.com/DiabloHorn/mempdump)


[^9]: [Mandiant FIN5 GrrCON Oct 2016](https://www.youtube.com/watch?v=fevGZs0EQu8)


[^10]: DUEBREW


