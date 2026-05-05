---
aliases: 
    - S0497
    
mitre-attack: https://attack.mitre.org/software/S0497
---

## S0497

[Dacls](https://attack.mitre.org/software/S0497) is a multi-platform remote access tool used by [Lazarus Group](https://attack.mitre.org/groups/G0032) since at least December 2019.[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Dacls](https://attack.mitre.org/software/S0497) can download its payload from a C2 server.[^1] [^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Dacls](https://attack.mitre.org/software/S0497) can use HTTPS in C2 communications.[^1] [^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Dacls](https://attack.mitre.org/software/S0497) can collect data on running and parent processes.[^2]  |
| [[Launch Agent\|T1543.001]] | Launch Agent | [Dacls](https://attack.mitre.org/software/S0497) can establish persistence via a LaunchAgent.[^1] [^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Dacls](https://attack.mitre.org/software/S0497) can encrypt its configuration file with AES CBC.[^2]  |
| [[Launch Daemon\|T1543.004]] | Launch Daemon | [Dacls](https://attack.mitre.org/software/S0497) can establish persistence via a Launch Daemon.[^1] [^2]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [Dacls](https://attack.mitre.org/software/S0497) has had its payload named with a dot prefix to make it hidden from view in the Finder application.[^1] [^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Dacls](https://attack.mitre.org/software/S0497) can scan directories on a compromised host.[^2]  |
| [[Masquerading\|T1036]] | Masquerading | The [Dacls](https://attack.mitre.org/software/S0497) Mach-O binary has been disguised as a .nib file.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: [SentinelOne Lazarus macOS July 2020](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/)


[^2]: [TrendMicro macOS Dacls May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-dacls-rat-backdoor-show-lazarus-multi-platform-attack-capability/)


