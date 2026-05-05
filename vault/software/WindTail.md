---
aliases: 
    - S0466
    
mitre-attack: https://attack.mitre.org/software/S0466
---

## S0466

[WindTail](https://attack.mitre.org/software/S0466) is a macOS surveillance implant used by [Windshift](https://attack.mitre.org/groups/G0112). [WindTail](https://attack.mitre.org/software/S0466) shares code similarities with Hack Back aka KitM OSX.[^2] [^3] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Invalid Code Signature\|T1036.001]] | Invalid Code Signature | [WindTail](https://attack.mitre.org/software/S0466) has been incompletely signed with revoked certificates.[^3]  |
| [[Native API\|T1106]] | Native API | [WindTail](https://attack.mitre.org/software/S0466) can invoke Apple APIs `contentsOfDirectoryAtPath`, `pathExtension`, and (string) `compare`.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [WindTail](https://attack.mitre.org/software/S0466) has the ability to enumerate the users home directory and the path to its own application bundle.[^3] [^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [WindTail](https://attack.mitre.org/software/S0466) can be delivered as a compressed, encrypted, and encoded payload.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [WindTail](https://attack.mitre.org/software/S0466) has the ability to use HTTP for C2 communications.[^1]  |
| [[Compression\|T1027.015]] | Compression | [WindTail](https://attack.mitre.org/software/S0466) can be delivered as a compressed, encrypted, and encoded payload.[^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [WindTail](https://attack.mitre.org/software/S0466) can use the `open` command to execute an application.[^3]  |
| [[Automated Collection\|T1119]] | Automated Collection | [WindTail](https://attack.mitre.org/software/S0466) can identify and add files that possess specific file extensions to an array for archiving.[^1]  |
| [[Masquerading\|T1036]] | Masquerading | [WindTail](https://attack.mitre.org/software/S0466) has used icons mimicking MS Office files to mask payloads.[^3]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [WindTail](https://attack.mitre.org/software/S0466) has the ability to use the macOS built-in zip utility to archive files.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [WindTail](https://attack.mitre.org/software/S0466) has the ability to decrypt strings using hard-coded AES keys.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [WindTail](https://attack.mitre.org/software/S0466) has the ability to receive and execute a self-delete command.[^1]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [WindTail](https://attack.mitre.org/software/S0466) has the ability to automatically exfiltrate files using the macOS built-in utility /usr/bin/curl.[^1]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [WindTail](https://attack.mitre.org/software/S0466) can instruct the OS to execute an application without a dock icon or menu.[^3]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [WindTail](https://attack.mitre.org/software/S0466) has the ability to generate the current date and time.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Windshift\|G0112]] | Windshift |



## References

[^1]: [objective-see windtail2 jan 2019](https://objective-see.com/blog/blog_0x3D.html)


[^2]: [SANS Windshift August 2018](https://www.scribd.com/document/661837258/WINDSHIFT-summit-archive-1554718868)


[^3]: [objective-see windtail1 dec 2018](https://objective-see.com/blog/blog_0x3B.html)


