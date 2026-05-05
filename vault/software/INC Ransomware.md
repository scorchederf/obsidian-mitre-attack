---
aliases: 
    - S1139
    
mitre-attack: https://attack.mitre.org/software/S1139
---

## S1139

[INC Ransomware](https://attack.mitre.org/software/S1139) is a ransomware strain that has been used by the [INC Ransom](https://attack.mitre.org/groups/G1032) group since at least 2023 against multiple industry sectors worldwide. [INC Ransomware](https://attack.mitre.org/software/S1139) can employ partial encryption combined with multi-threading to speed encryption.[^2] [^5] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [INC Ransomware](https://attack.mitre.org/software/S1139) can identify external USB and hard drives for encryption and printers to print ransom notes.[^4]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | <br>[INC Ransomware](https://attack.mitre.org/software/S1139) can push its encryption executable to multiple endpoints within compromised infrastructure.[^5]  |
| [[Phishing\|T1566]] | Phishing | [INC Ransomware](https://attack.mitre.org/software/S1139) campaigns have used spearphishing emails for initial access.[^2]  |
| [[Native API\|T1106]] | Native API | [INC Ransomware](https://attack.mitre.org/software/S1139) can use the API `DeviceIoControl` to resize the allocated space for and cause the deletion of volume shadow copy snapshots.[^4]  |
| [[Device Driver Discovery\|T1652]] | Device Driver Discovery | [INC Ransomware](https://attack.mitre.org/software/S1139) can verify the presence of specific drivers on compromised hosts including Microsoft Print to PDF and Microsoft XPS Document Writer.[^4]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [INC Ransomware](https://attack.mitre.org/software/S1139) can delete volume shadow copy backups from victim machines.[^4]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [INC Ransomware](https://attack.mitre.org/software/S1139) has the ability to use wmic.exe to spread to multiple endpoints within a compromised environment.[^5] [^3] <br> |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [INC Ransomware](https://attack.mitre.org/software/S1139) can discover and mount hidden drives to encrypt them.[^4]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [INC Ransomware](https://attack.mitre.org/software/S1139) has the ability to check for shared network drives to encrypt.[^4]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [INC Ransomware](https://attack.mitre.org/software/S1139) can encrypt data on victim systems, including through the use of partial encryption and multi-threading to speed encryption.[^2] [^5] [^4] [^1] [^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [INC Ransomware](https://attack.mitre.org/software/S1139) can run `CryptStringToBinaryA` to decrypt base64 content containing its ransom note.[^4]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [INC Ransomware](https://attack.mitre.org/software/S1139) can receive command line arguments to encrypt specific files and directories.[^4] [^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [INC Ransomware](https://attack.mitre.org/software/S1139) can use the Microsoft Win32 Restart Manager to kill processes with a specific handle or that are accessing resources it wants to encrypt.[^4]  |
| [[Service Stop\|T1489]] | Service Stop | [INC Ransomware](https://attack.mitre.org/software/S1139) can issue a command to kill a process on compromised hosts.[^4]  |
| [[Internal Defacement\|T1491.001]] | Internal Defacement | [INC Ransomware](https://attack.mitre.org/software/S1139) has the ability to change the background wallpaper image to display the ransom note.[^4] [^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[INC Ransom\|G1032]] | INC Ransom |



## References

[^1]: [SOCRadar INC Ransom January 2024](https://socradar.io/dark-web-profile-inc-ransom/)


[^2]: [SentinelOne INC Ransomware](https://www.sentinelone.com/anthology/inc-ransom/)


[^3]: [Secureworks GOLD IONIC April 2024](https://www.secureworks.com/blog/gold-ionic-deploys-inc-ransomware)


[^4]: [Cybereason INC Ransomware November 2023](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)


[^5]: [Huntress INC Ransom Group August 2023](https://www.huntress.com/blog/investigating-new-inc-ransom-group-activity)


