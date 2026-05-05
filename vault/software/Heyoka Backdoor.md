---
aliases: 
    - S1027
    
mitre-attack: https://attack.mitre.org/software/S1027
---

## S1027

[Heyoka Backdoor](https://attack.mitre.org/software/S1027) is a custom backdoor--based on the Heyoka open source exfiltration tool--that  has been used by [Aoqin Dragon](https://attack.mitre.org/groups/G1007) since at least 2013.[^1] [^2]  

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Heyoka Backdoor](https://attack.mitre.org/software/S1027) can inject a DLL into rundll32.exe for execution.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Heyoka Backdoor](https://attack.mitre.org/software/S1027) has the ability to delete folders and files from a targeted system.[^1]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Heyoka Backdoor](https://attack.mitre.org/software/S1027) can use spoofed DNS requests to create a bidirectional tunnel between a compromised host and its C2 servers.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Heyoka Backdoor](https://attack.mitre.org/software/S1027) can decrypt its payload prior to execution.[^1]  |
| [[DNS\|T1071.004]] | DNS | [Heyoka Backdoor](https://attack.mitre.org/software/S1027) can use DNS tunneling for C2 communications.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Heyoka Backdoor](https://attack.mitre.org/software/S1027) can enumerate drives on a compromised host.[^1]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Heyoka Backdoor](https://attack.mitre.org/software/S1027) can check if it is running as a service on a compromised host.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Heyoka Backdoor](https://attack.mitre.org/software/S1027) can gather process information.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Heyoka Backdoor](https://attack.mitre.org/software/S1027) can use rundll32.exe to gain execution.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Heyoka Backdoor](https://attack.mitre.org/software/S1027) has the ability to search the compromised host for files.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Heyoka Backdoor](https://attack.mitre.org/software/S1027) can establish persistence with the auto start function including using the value `EverNoteTrayUService`.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Heyoka Backdoor](https://attack.mitre.org/software/S1027) can encrypt its payload.[^1]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [Heyoka Backdoor](https://attack.mitre.org/software/S1027) can identify removable media attached to victim's machines.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Heyoka Backdoor](https://attack.mitre.org/software/S1027) has been named `srvdll.dll` to appear as a legitimate service.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Heyoka Backdoor](https://attack.mitre.org/software/S1027) has been spread through malicious document lures.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Aoqin Dragon\|G1007]] | Aoqin Dragon |



## References

[^1]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)


[^2]: [Sourceforge Heyoka 2022](https://heyoka.sourceforge.net/)


