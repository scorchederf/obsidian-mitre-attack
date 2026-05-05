---
aliases: 
    - S0145
    
mitre-attack: https://attack.mitre.org/software/S0145
---

## S0145

[POWERSOURCE](https://attack.mitre.org/software/S0145) is a PowerShell backdoor that is a heavily obfuscated and modified version of the publicly available tool DNS_TXT_Pwnage. It was observed in February 2017 in spearphishing campaigns against personnel involved with United States Securities and Exchange Commission (SEC) filings at various organizations. The malware was delivered when macros were enabled by the victim and a VBS script was dropped. [^1]  [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[PowerShell\|T1059.001]] | PowerShell | [POWERSOURCE](https://attack.mitre.org/software/S0145) is a PowerShell backdoor.[^1] [^4]  |
| [[Query Registry\|T1012]] | Query Registry | [POWERSOURCE](https://attack.mitre.org/software/S0145) queries Registry keys in preparation for setting Run keys to achieve persistence.[^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [POWERSOURCE](https://attack.mitre.org/software/S0145) achieves persistence by setting a Registry Run key, with the path depending on whether the victim account has user or administrator access.[^4]  |
| [[NTFS File Attributes\|T1564.004]] | NTFS File Attributes | If the victim is using PowerShell 3.0 or later, [POWERSOURCE](https://attack.mitre.org/software/S0145) writes its decoded payload to an alternate data stream (ADS) named kernel32.dll that is saved in `%PROGRAMDATA%\Windows\`.[^4]  |
| [[DNS\|T1071.004]] | DNS | [POWERSOURCE](https://attack.mitre.org/software/S0145) uses DNS TXT records for C2.[^1] [^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [POWERSOURCE](https://attack.mitre.org/software/S0145) has been observed being used to download [TEXTMATE](https://attack.mitre.org/software/S0146) and the Cobalt Strike Beacon payload onto victims.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN7\|G0046]] | FIN7 |



## References

[^1]: [FireEye FIN7 March 2017](https://web.archive.org/web/20180808125108/https:/www.fireeye.com/blog/threat-research/2017/03/fin7_spear_phishing.html)


[^2]: DNSMessenger


[^3]: POWERSOURCE


[^4]: [Cisco DNSMessenger March 2017](http://blog.talosintelligence.com/2017/03/dnsmessenger.html)


