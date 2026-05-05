---
aliases: 
    - S1234
    
mitre-attack: https://attack.mitre.org/software/S1234
---

## S1234

[SplatCloak](https://attack.mitre.org/software/S1234) is a malware that disables EDR-related routines used by Windows Defender and Kaspersky to aid in evading detection.  [SplatCloak](https://attack.mitre.org/software/S1234) has been deployed by [SplatDropper](https://attack.mitre.org/software/S1232) and is known to be leveraged by [Mustang Panda](https://attack.mitre.org/groups/G0129) since 2025.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [SplatCloak](https://attack.mitre.org/software/S1234) has identified and disabled API callback features of Windows Defender and Kaspersky.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SplatCloak](https://attack.mitre.org/software/S1234) has collected the Windows build number using the windows kernel API `RtlGetVersion` to determine if the response is 19000 or higher (Windows 10 version 2004 or later).[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [SplatCloak](https://attack.mitre.org/software/S1234) has identified drivers of AV solutions by searching for related filenames, keywords and signed certificates.[^1]  |
| [[Invalid Code Signature\|T1036.001]] | Invalid Code Signature | [SplatCloak](https://attack.mitre.org/software/S1234) has used a revoked certificate to exploit Windows driver execution policy where certificates issued before a specific date could still load.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [SplatCloak](https://attack.mitre.org/software/S1234) has used Windows API to identify files associated with Windows Defender and Kaspersky.[^1]  |
| [[Native API\|T1106]] | Native API | [SplatCloak](https://attack.mitre.org/software/S1234) has utilized Native Windows API calls dynamically through `ZwQuerySystemInformation`.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Mustang Panda\|G0129]] | Mustang Panda |



## References

[^1]: [Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)


