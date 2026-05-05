---
aliases: 
    - S0221
    
mitre-attack: https://attack.mitre.org/software/S0221
---

## S0221

A Linux rootkit that provides backdoor access and hides from defenders.

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Umbreon](https://attack.mitre.org/software/S0221) provides access using both standard facilities like SSH and additional access using its backdoor Espeon, providing a reverse shell upon receipt of a special packet[^1]  |
| [[Rootkit\|T1014]] | Rootkit | [Umbreon](https://attack.mitre.org/software/S0221) hides from defenders by hooking libc function calls, hiding artifacts that would reveal its presence, such as the user account it creates to provide access and undermining strace, a tool often used to identify malware.[^1]  |
| [[Traffic Signaling\|T1205]] | Traffic Signaling | [Umbreon](https://attack.mitre.org/software/S0221) provides additional access using its backdoor Espeon, providing a reverse shell upon receipt of a special packet.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Umbreon](https://attack.mitre.org/software/S0221) provides access to the system via SSH or any other protocol that uses PAM to authenticate.[^1]  |
| [[Local Accounts\|T1078.003]] | Local Accounts | [Umbreon](https://attack.mitre.org/software/S0221) creates valid local users to provide access to the system.[^1]  |




## References

[^1]: [Umbreon Trend Micro](https://blog.trendmicro.com/trendlabs-security-intelligence/pokemon-themed-umbreon-linux-rootkit-hits-x86-arm-systems/?_ga=2.180041126.367598458.1505420282-1759340220.1502477046)


[^2]: Umbreon


