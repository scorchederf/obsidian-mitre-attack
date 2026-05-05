---
aliases: 
    - S1108
    
mitre-attack: https://attack.mitre.org/software/S1108
---

## S1108

[PULSECHECK](https://attack.mitre.org/software/S1108) is a web shell written in Perl that was used by [APT5](https://attack.mitre.org/groups/G1023) as early as 2020 including against Pulse Secure VPNs at US Defense Industrial Base (DIB) companies.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [PULSECHECK](https://attack.mitre.org/software/S1108) can check HTTP request headers for a specific backdoor key and if found will output the result of the command in the variable `HTTP_X_CMD.`[^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [PULSECHECK](https://attack.mitre.org/software/S1108) can use Unix shell script for command execution.[^1]  |
| [[Web Shell\|T1505.003]] | Web Shell | [PULSECHECK](https://attack.mitre.org/software/S1108) is a web shell that can enable command execution on compromised servers.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [PULSECHECK](https://attack.mitre.org/software/S1108) can base-64 encode encrypted data sent through C2.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT5\|G1023]] | APT5 |



## References

[^1]: [Mandiant Pulse Secure Zero-Day April 2021](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)


