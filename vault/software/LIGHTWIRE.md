---
aliases: 
    - S1119
    
mitre-attack: https://attack.mitre.org/software/S1119
---

## S1119

[LIGHTWIRE](https://attack.mitre.org/software/S1119) is a web shell written in Perl that was used during [Cutting Edge](https://attack.mitre.org/campaigns/C0029) to maintain access and enable command execution by imbedding into the legitimate compcheckresult.cgi component of Ivanti Secure Connect VPNs.[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [LIGHTWIRE](https://attack.mitre.org/software/S1119) can use HTTP for C2 communications.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [LIGHTWIRE](https://attack.mitre.org/software/S1119) can RC4 decrypt and Base64 decode C2 commands.[^2]  |
| [[Web Shell\|T1505.003]] | Web Shell | [LIGHTWIRE](https://attack.mitre.org/software/S1119) is a web shell capable of command execution and establishing persistence on compromised Ivanti Secure Connect VPNs.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [LIGHTWIRE](https://attack.mitre.org/software/S1119) can RC4 encrypt C2 commands.[^2]  |
| [[Compromise Host Software Binary\|T1554]] | Compromise Host Software Binary | [LIGHTWIRE](https://attack.mitre.org/software/S1119) can imbed itself into the legitimate `compcheckresult.cgi` component of Ivanti Connect Secure VPNs to enable command execution.[^1] [^2]  |




## References

[^1]: [Mandiant Cutting Edge January 2024](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)


[^2]: [Mandiant Cutting Edge Part 2 January 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)


