---
aliases: 
    - S1104
    
mitre-attack: https://attack.mitre.org/software/S1104
---

## S1104

[SLOWPULSE](https://attack.mitre.org/software/S1104) is a malware that was used by [APT5](https://attack.mitre.org/groups/G1023) as early as 2020 including against U.S. Defense Industrial Base (DIB) companies. [SLOWPULSE](https://attack.mitre.org/software/S1104) has several variants and can modify legitimate Pulse Secure VPN files in order to log credentials and bypass single and two-factor authentication flows.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Network Device Authentication\|T1556.004]] | Network Device Authentication | [SLOWPULSE](https://attack.mitre.org/software/S1104) can modify LDAP and two factor authentication flows by inspecting login credentials and forcing successful authentication if the provided password matches a chosen backdoor password.[^1]  |
| [[Multi-Factor Authentication Interception\|T1111]] | Multi-Factor Authentication Interception | [SLOWPULSE](https://attack.mitre.org/software/S1104) can log credentials on compromised Pulse Secure VPNs during the `DSAuth::AceAuthServer::checkUsernamePassword`ACE-2FA authentication procedure.[^1]  |
| [[Multi-Factor Authentication\|T1556.006]] | Multi-Factor Authentication | [SLOWPULSE](https://attack.mitre.org/software/S1104) can insert malicious logic to bypass RADIUS and ACE two factor authentication (2FA) flows if a designated attacker-supplied password is provided.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [SLOWPULSE](https://attack.mitre.org/software/S1104) can write logged ACE credentials to `/home/perl/PAUS.pm` in append mode, using the format string `%s:%s\n`.[^1]  |
| [[Compromise Host Software Binary\|T1554]] | Compromise Host Software Binary | [SLOWPULSE](https://attack.mitre.org/software/S1104) is applied in compromised environments through modifications to legitimate Pulse Secure files.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [SLOWPULSE](https://attack.mitre.org/software/S1104) can hide malicious code in the padding regions between legitimate functions in the Pulse Secure `libdsplibs.so` file.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT5\|G1023]] | APT5 |



## References

[^1]: [Mandiant Pulse Secure Zero-Day April 2021](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)


[^2]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)


