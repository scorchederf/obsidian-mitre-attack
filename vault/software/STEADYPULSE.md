---
aliases: 
    - S1112
    
mitre-attack: https://attack.mitre.org/software/S1112
---

## S1112

[STEADYPULSE](https://attack.mitre.org/software/S1112) is a web shell that infects targeted Pulse Secure VPN servers through modification of a legitimate Perl script that was used as early as 2020 including in activity against US Defense Industrial Base (DIB) entities.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [STEADYPULSE](https://attack.mitre.org/software/S1112) can transmit URL encoded data over C2.[^1]  |
| [[Web Shell\|T1505.003]] | Web Shell | [STEADYPULSE](https://attack.mitre.org/software/S1112) is a web shell that can enable the execution of arbitrary commands on compromised web servers.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [STEADYPULSE](https://attack.mitre.org/software/S1112) can URL decode key/value pairs sent over C2.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [STEADYPULSE](https://attack.mitre.org/software/S1112) can parse web requests made to a targeted server to determine the next stage of execution.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [STEADYPULSE](https://attack.mitre.org/software/S1112) can add lines to a Perl script on a targeted server to import additional Perl modules.[^1]  |




## References

[^1]: [Mandiant Pulse Secure Zero-Day April 2021](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)


