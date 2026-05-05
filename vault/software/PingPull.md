---
aliases: 
    - S1031
    
mitre-attack: https://attack.mitre.org/software/S1031
---

## S1031

[PingPull](https://attack.mitre.org/software/S1031) is a remote access Trojan (RAT) written in Visual C++ that has been used by [GALLIUM](https://attack.mitre.org/groups/G0093) since at least June 2022. [PingPull](https://attack.mitre.org/software/S1031) has been used to target telecommunications companies, financial institutions, and government entities in Afghanistan, Australia, Belgium, Cambodia, Malaysia, Mozambique, the Philippines, Russia, and Vietnam.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [PingPull](https://attack.mitre.org/software/S1031) can use HTTPS over port 8080 for C2.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [PingPull](https://attack.mitre.org/software/S1031) can enumerate storage volumes and folder contents of a compromised host.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [PingPull](https://attack.mitre.org/software/S1031) can collect data from a compromised host.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | A [PingPull](https://attack.mitre.org/software/S1031) variant can communicate with its C2 servers by using HTTPS.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [PingPull](https://attack.mitre.org/software/S1031) can retrieve the hostname of a compromised host.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [PingPull](https://attack.mitre.org/software/S1031) can mimic the names and descriptions of legitimate services such as `iphlpsvc`, `IP Helper`,  and `Onedrive` to evade detection.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [PingPull](https://attack.mitre.org/software/S1031) can retrieve the IP address of a compromised host.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [PingPull](https://attack.mitre.org/software/S1031) can encode C2 traffic with Base64.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [PingPull](https://attack.mitre.org/software/S1031) has the ability to install itself as a service.[^1]  |
| [[Timestomp\|T1070.006]] | Timestomp | [PingPull](https://attack.mitre.org/software/S1031) has the ability to timestomp a file.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol |  [PingPull](https://attack.mitre.org/software/S1031) variants have the ability to communicate with C2 servers using ICMP or TCP.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [PingPull](https://attack.mitre.org/software/S1031) can use `cmd.exe` to run various commands as a reverse shell.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [PingPull](https://attack.mitre.org/software/S1031) can decrypt received data from its C2 server by using AES.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [PingPull](https://attack.mitre.org/software/S1031) has the ability to exfiltrate stolen victim data through its C2 channel.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [PingPull](https://attack.mitre.org/software/S1031) can use AES, in cipher block chaining (CBC) mode padded with PKCS5, to encrypt C2 server communications.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[GALLIUM\|G0093]] | GALLIUM |



## References

[^1]: [Unit 42 PingPull Jun 2022](https://unit42.paloaltonetworks.com/pingpull-gallium/)


