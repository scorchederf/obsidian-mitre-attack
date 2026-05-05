---
aliases: 
    - S1116
    
mitre-attack: https://attack.mitre.org/software/S1116
---

## S1116

[WARPWIRE](https://attack.mitre.org/software/S1116) is a Javascript credential stealer that targets plaintext passwords and usernames for exfiltration that was used during [Cutting Edge](https://attack.mitre.org/campaigns/C0029) to target Ivanti Connect Secure VPNs.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Compromise Host Software Binary\|T1554]] | Compromise Host Software Binary | [WARPWIRE](https://attack.mitre.org/software/S1116) can embed itself into a legitimate file on compromised Ivanti Connect Secure VPNs.[^1]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [WARPWIRE](https://attack.mitre.org/software/S1116) can send captured credentials to C2 via HTTP `GET` or `POST` requests.[^1] [^2]  |
| [[JavaScript\|T1059.007]] | JavaScript | [WARPWIRE](https://attack.mitre.org/software/S1116) is a credential harvester written in JavaScript.[^1]  |
| [[Web Portal Capture\|T1056.003]] | Web Portal Capture | [WARPWIRE](https://attack.mitre.org/software/S1116) can capture credentials submitted during the web logon process in order to access layer seven applications such as RDP.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [WARPWIRE](https://attack.mitre.org/software/S1116) can Base64 encode captured credentials with `btoa()` prior to sending to C2.[^1]  |




## References

[^1]: [Mandiant Cutting Edge January 2024](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)


[^2]: [Mandiant Cutting Edge Part 2 January 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)


