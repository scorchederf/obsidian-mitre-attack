---
aliases: 
    - S1033
    
mitre-attack: https://attack.mitre.org/software/S1033
---

## S1033

[DCSrv](https://attack.mitre.org/software/S1033) is destructive malware that has been used by [Moses Staff](https://attack.mitre.org/groups/G1009) since at least  September 2021. Though [DCSrv](https://attack.mitre.org/software/S1033) has ransomware-like capabilities, [Moses Staff](https://attack.mitre.org/groups/G1009) does not demand ransom or offer a decryption key.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [DCSrv](https://attack.mitre.org/software/S1033) has masqueraded its service as a legitimate svchost.exe process.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [DCSrv](https://attack.mitre.org/software/S1033) has created new services for persistence by modifying the Registry.[^1]  |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [DCSrv](https://attack.mitre.org/software/S1033) has a function to sleep for two hours before rebooting the system.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [DCSrv](https://attack.mitre.org/software/S1033) has created Registry keys for persistence.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [DCSrv](https://attack.mitre.org/software/S1033)'s configuration is encrypted.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [DCSrv](https://attack.mitre.org/software/S1033) can compare the current time on an infected host with a configuration value to determine when to start the encryption process.[^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [DCSrv](https://attack.mitre.org/software/S1033) has encrypted drives using the core encryption mechanism from DiskCryptor.[^1]  |
| [[Native API\|T1106]] | Native API | [DCSrv](https://attack.mitre.org/software/S1033) has used various Windows API functions, including `DeviceIoControl`, as part of its encryption process.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Moses Staff\|G1009]] | Moses Staff |



## References

[^1]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)


