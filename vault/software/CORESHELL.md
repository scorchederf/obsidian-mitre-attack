---
aliases: 
    - S0137
    
mitre-attack: https://attack.mitre.org/software/S0137
---

## S0137

[CORESHELL](https://attack.mitre.org/software/S0137) is a downloader used by [APT28](https://attack.mitre.org/groups/G0007). The older versions of this malware are known as SOURFACE and newer versions as CORESHELL.[^5]  [^8] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [CORESHELL](https://attack.mitre.org/software/S0137) can communicate over HTTP for C2.[^5] [^7]  |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [CORESHELL](https://attack.mitre.org/software/S0137) can communicate over SMTP and POP3 for C2.[^5] [^7]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [CORESHELL](https://attack.mitre.org/software/S0137) C2 messages are Base64-encoded.[^5]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [CORESHELL](https://attack.mitre.org/software/S0137) collects the volume serial number from the victim and sends the information to its C2 server.[^5]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [CORESHELL](https://attack.mitre.org/software/S0137) collects hostname and OS version data from the victim and sends the information to its C2 server.[^5]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [CORESHELL](https://attack.mitre.org/software/S0137) contains unused machine instructions in a likely attempt to hinder analysis.[^5]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [CORESHELL](https://attack.mitre.org/software/S0137) is installed via execution of rundll32 with an export named "init" or "InitW."[^7]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [CORESHELL](https://attack.mitre.org/software/S0137) has established persistence by creating autostart extensibility point (ASEP) Registry entries in the Run key and other Registry keys, as well as by creating shortcuts in the Internet Explorer Quick Start folder.[^7]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [CORESHELL](https://attack.mitre.org/software/S0137) downloads another dropper from its C2 server.[^5]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [CORESHELL](https://attack.mitre.org/software/S0137) obfuscates strings using a custom stream cipher.[^5]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [CORESHELL](https://attack.mitre.org/software/S0137) C2 messages are encrypted with custom stream ciphers using six-byte or eight-byte keys.[^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT28\|G0007]] | APT28 |



## References

[^1]: Sofacy


[^2]: CORESHELL


[^3]: [Secureworks IRON TWILIGHT Active Measures March 2017](https://www.secureworks.com/research/iron-twilight-supports-active-measures)


[^4]: SOURFACE


[^5]: [FireEye APT28](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)


[^6]: [Securelist Sofacy Feb 2018](https://securelist.com/a-slice-of-2017-sofacy-activity/83930/)


[^7]: [Microsoft SIR Vol 19](http://download.microsoft.com/download/4/4/C/44CDEF0E-7924-4787-A56A-16261691ACE3/Microsoft_Security_Intelligence_Report_Volume_19_English.pdf)


[^8]: [FireEye APT28 January 2017](https://www.mandiant.com/sites/default/files/2021-09/APT28-Center-of-Storm-2017.pdf)


