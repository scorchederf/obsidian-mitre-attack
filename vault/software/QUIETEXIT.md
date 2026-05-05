---
aliases: 
    - S1084
    
mitre-attack: https://attack.mitre.org/software/S1084
---

## S1084

[QUIETEXIT](https://attack.mitre.org/software/S1084) is a novel backdoor, based on the open-source Dropbear SSH client-server software, that has been used by [APT29](https://attack.mitre.org/groups/G0016) since at least 2021. [APT29](https://attack.mitre.org/groups/G0016) has deployed [QUIETEXIT](https://attack.mitre.org/software/S1084) on opaque network appliances that typically don't support antivirus or endpoint detection and response tools within a victim environment.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[External Proxy\|T1090.002]] | External Proxy | [QUIETEXIT](https://attack.mitre.org/software/S1084) can proxy traffic via SOCKS.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [QUIETEXIT](https://attack.mitre.org/software/S1084) can attempt to connect to a second hard-coded C2 if the first hard-coded C2 address fails.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [QUIETEXIT](https://attack.mitre.org/software/S1084) can establish a TCP connection as part of its initial connection to the C2.[^1]  |
| [[Application Layer Protocol\|T1071]] | Application Layer Protocol | [QUIETEXIT](https://attack.mitre.org/software/S1084) can use an inverse negotiated SSH connection as part of its C2.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [QUIETEXIT](https://attack.mitre.org/software/S1084) has attempted to change its name to `cron` upon startup. During incident response, [QUIETEXIT](https://attack.mitre.org/software/S1084) samples have been identified that were renamed to blend in with other legitimate files.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [Mandiant APT29 Eye Spy Email Nov 22](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)


