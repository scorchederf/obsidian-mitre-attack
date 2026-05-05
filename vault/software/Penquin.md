---
aliases: 
    - S0587
    
mitre-attack: https://attack.mitre.org/software/S0587
---

## S0587

[Penquin](https://attack.mitre.org/software/S0587) is a remote access trojan (RAT) with multiple versions used by [Turla](https://attack.mitre.org/groups/G0010) to target Linux systems since at least 2014.[^4] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Penquin](https://attack.mitre.org/software/S0587) can execute remote commands using bash scripts.[^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Penquin](https://attack.mitre.org/software/S0587) can report the IP of the compromised host to attacker controlled infrastructure.[^3]  |
| [[Traffic Signaling\|T1205]] | Traffic Signaling | [Penquin](https://attack.mitre.org/software/S0587) will connect to C2 only after sniffing a "magic packet" value in TCP or UDP packets matching specific conditions.[^3] [^4]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Penquin](https://attack.mitre.org/software/S0587) has mimicked the Cron binary to hide itself on compromised systems.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Penquin](https://attack.mitre.org/software/S0587) can execute the command code `do_download` to retrieve remote files from C2.[^3]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Penquin](https://attack.mitre.org/software/S0587) can report the disk space of a compromised host to C2.[^3]  |
| [[Cron\|T1053.003]] | Cron | [Penquin](https://attack.mitre.org/software/S0587) can use Cron to create periodic and pre-scheduled background jobs.[^3]  |
| [[Network Sniffing\|T1040]] | Network Sniffing | [Penquin](https://attack.mitre.org/software/S0587) can sniff network traffic to look for packets matching specific conditions.[^3] [^4]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Penquin](https://attack.mitre.org/software/S0587) can encrypt communications using the BlowFish algorithm and a symmetric key exchanged with Diffie Hellman.[^3]  |
| [[Indicator Removal from Tools\|T1027.005]] | Indicator Removal from Tools | [Penquin](https://attack.mitre.org/software/S0587) can remove strings from binaries.[^3]  |
| [[Linux and Mac Permissions\|T1222.002]] | Linux and Mac Permissions | [Penquin](https://attack.mitre.org/software/S0587) can add the executable flag to a downloaded file.[^3]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Penquin](https://attack.mitre.org/software/S0587) can execute the command code `do_upload` to send files to C2.[^3]  |
| [[Socket Filters\|T1205.002]] | Socket Filters | [Penquin](https://attack.mitre.org/software/S0587) installs a `TCP` and `UDP` filter on the `eth0` interface.[^3]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | The [Penquin](https://attack.mitre.org/software/S0587) C2 mechanism is based on TCP and UDP packets.[^4] [^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Penquin](https://attack.mitre.org/software/S0587) can use the command code `do_vslist` to send file names, size, and status to C2.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Penquin](https://attack.mitre.org/software/S0587) can report the file system type of a compromised host to C2.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Penquin](https://attack.mitre.org/software/S0587) can delete downloaded executables after running them.[^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Penquin](https://attack.mitre.org/software/S0587) has encrypted strings in the binary for obfuscation.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Turla\|G0010]] | Turla |



## References

[^1]: Penquin_x64


[^2]: Penquin 2.0


[^3]: [Leonardo Turla Penquin May 2020](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)


[^4]: [Kaspersky Turla Penquin December 2014](https://securelist.com/the-penquin-turla-2/67962/)


