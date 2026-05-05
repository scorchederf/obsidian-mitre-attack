---
aliases: 
    - S0026
    
mitre-attack: https://attack.mitre.org/software/S0026
---

## S0026

[GLOOXMAIL](https://attack.mitre.org/software/S0026) is malware used by [APT1](https://attack.mitre.org/groups/G0006) that mimics legitimate Jabber/XMPP traffic. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Publish／Subscribe Protocols\|T1071.005]] | Publish／Subscribe Protocols | [GLOOXMAIL](https://attack.mitre.org/software/S0026) communicates to servers operated by Google using the Jabber/XMPP protocol for C2.[^2]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [GLOOXMAIL](https://attack.mitre.org/software/S0026) communicates to servers operated by Google using the Jabber/XMPP protocol.[^1] [^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT1\|G0006]] | APT1 |



## References

[^1]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)


[^2]: [Mandiant APT1 Appendix](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)


[^3]: [CyberESI GTALK](https://web.archive.org/web/20141226203328/http://www.cyberengineeringservices.com/2011/12/15/trojan-gtalk/)


