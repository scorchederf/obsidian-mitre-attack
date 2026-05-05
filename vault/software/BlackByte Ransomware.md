---
aliases: 
    - S1180
    
mitre-attack: https://attack.mitre.org/software/S1180
---

## S1180

[BlackByte Ransomware](https://attack.mitre.org/software/S1180) is uniquely associated with [BlackByte](https://attack.mitre.org/groups/G1043) operations. [BlackByte Ransomware](https://attack.mitre.org/software/S1180) used a common key for infections, allowing for the creation of a universal decryptor.[^1] [^3]  [BlackByte Ransomware](https://attack.mitre.org/software/S1180) was replaced in [BlackByte](https://attack.mitre.org/groups/G1043) operations by [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) by 2023.[^4] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) can identify network shares connected to the victim machine.[^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) is ransomware using a shared key across victims for encryption.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) enumerates the Registry, specifically the `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options` key.[^1]  |
| [[JavaScript\|T1059.007]] | JavaScript | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) is distributed as a JavaScript launcher file.[^1]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) spreads itself laterally by writing the JavaScript launcher file to mapped shared folders.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) gathers victim system information to generate a unique victim identifier.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) creates a schedule task to execute remotely deployed ransomware payloads.[^1]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) deletes all volume shadow copies and restore points among other actions to inhibit system recovery following ransomware deployment.[^1]  |
| [[Downgrade Attack\|T1689]] | Downgrade Attack | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) enables SMBv1 during execution.[^1]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) identifies remote systems via active directory queries for hostnames prior to launching remote ransomware payloads.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) is distributed as an encrypted payload.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) adds .JS and .EXE extensions to the Microsoft Defender exclusion list. [BlackByte Ransomware](https://attack.mitre.org/software/S1180) terminates and removes the Raccine anti-ransomware utility.[^1]  |
| [[Native API\|T1106]] | Native API | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) uses the `SetThreadExecutionState` API to prevent the victim system from entering sleep.[^1]  |
| [[Windows Permissions\|T1222.001]] | Windows Permissions | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) uses the `mountvol.exe` command to mount volume names and leverages the Microsoft Discretionary Access Control List tool, `icacls.exe`, to grant the group to “Everyone” full access to the root of the drive.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) modifies the victim Registry to prevent system recovery.[^1]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) creates a mutex value with a hard-coded name, and terminates if that mutex already exists on the victim system. [BlackByte Ransomware](https://attack.mitre.org/software/S1180) checks the system language to see if it matches one of a list of hard-coded values; if a match is found, the malware will terminate.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) is distributed as an obfuscated JavaScript launcher file.[^1]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) uses mapped shared folders to transfer ransomware payloads via SMB.[^1]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) identifies the language on the victim system.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) looks for security software products prior to full execution.[^1]  |
| [[System Checks\|T1497.001]] | System Checks | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) checks for files related to known sandboxes.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[BlackByte\|G1043]] | BlackByte |



## References

[^1]: [Trustwave BlackByte 2021](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)


[^2]: [Cisco BlackByte 2024](https://blog.talosintelligence.com/blackbyte-blends-tried-and-true-tradecraft-with-newly-disclosed-vulnerabilities-to-support-ongoing-attacks/)


[^3]: [FBI BlackByte 2022](https://www.ic3.gov/CSA/2022/220211.pdf)


[^4]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)


