---
aliases: 
    - S1134
    
mitre-attack: https://attack.mitre.org/software/S1134
---

## S1134

[DEADWOOD](https://attack.mitre.org/software/S1134) is wiper malware written in C++ using Boost libraries. [DEADWOOD](https://attack.mitre.org/software/S1134) was first observed in an unattributed wiping event in Saudi Arabia in 2019, and has since been incorporated into [Agrius](https://attack.mitre.org/groups/G1030) operations.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Disk Content Wipe\|T1561.001]] | Disk Content Wipe | [DEADWOOD](https://attack.mitre.org/software/S1134) deletes files following overwriting them with random data.[^2]  |
| [[Embedded Payloads\|T1027.009]] | Embedded Payloads | [DEADWOOD](https://attack.mitre.org/software/S1134) contains an embedded, AES-encrypted payload labeled `METADATA` that provides configuration information for follow-on execution.[^2]  |
| [[Data Destruction\|T1485]] | Data Destruction | [DEADWOOD](https://attack.mitre.org/software/S1134) overwrites files on victim systems with random data to effectively destroy them.[^2]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [DEADWOOD](https://attack.mitre.org/software/S1134) will attempt to masquerade its service execution using benign-looking names such as `ScDeviceEnums`.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [DEADWOOD](https://attack.mitre.org/software/S1134) contains an embedded, AES-encrypted resource named `METADATA` that contains configuration information for follow-on execution.[^2]  |
| [[Service Execution\|T1569.002]] | Service Execution | [DEADWOOD](https://attack.mitre.org/software/S1134) can be executed as a service using various names, such as `ScDeviceEnums`.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [DEADWOOD](https://attack.mitre.org/software/S1134) XORs some strings within the binary using the value `0xD5`, and deobfuscates these items at runtime.[^2]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [DEADWOOD](https://attack.mitre.org/software/S1134) will set a timestamp value to determine when wiping functionality starts. When the timestamp is met on the system, a trigger file is created on the operating system allowing for execution to proceed. If the timestamp is in the past, the wiper will execute immediately.[^2]  |
| [[Account Access Removal\|T1531]] | Account Access Removal | [DEADWOOD](https://attack.mitre.org/software/S1134) changes the password for local and domain users via `net.exe` to a random 32 character string to prevent these accounts from logging on. Additionally, [DEADWOOD](https://attack.mitre.org/software/S1134) will terminate the `winlogon.exe` process to prevent attempts to log on to the infected system.[^2]  |
| [[Disk Structure Wipe\|T1561.002]] | Disk Structure Wipe | [DEADWOOD](https://attack.mitre.org/software/S1134) opens and writes zeroes to the first 512 bytes of each drive, deleting the MBR. [DEADWOOD](https://attack.mitre.org/software/S1134) then sends the control code `IOCTL_DISK_DELETE_DRIVE_LAYOUT` to ensure the MBR is removed from the drive.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT33\|G0064]] | APT33 |
| [[Agrius\|G1030]] | Agrius |



## References

[^1]: [RecordedFuture IranianResponse 2020](https://www.recordedfuture.com/blog/iranian-cyber-response)


[^2]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)


