---
aliases: 
    - S0124
    
mitre-attack: https://attack.mitre.org/software/S0124
---

## S0124

[Pisloader](https://attack.mitre.org/software/S0124) is a malware family that is notable due to its use of DNS as a C2 protocol as well as its use of anti-analysis tactics. It has been used by [APT18](https://attack.mitre.org/groups/G0026) and is similar to another malware family, [HTTPBrowser](https://attack.mitre.org/software/S0070), that has been used by the group. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Pisloader](https://attack.mitre.org/software/S0124) establishes persistence via a Registry Run key.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Pisloader](https://attack.mitre.org/software/S0124) uses cmd.exe to set the Registry Run key value. It also has a command to spawn a command shell.[^2]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | Responses from the [Pisloader](https://attack.mitre.org/software/S0124) C2 server are base32-encoded.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Pisloader](https://attack.mitre.org/software/S0124) has a command to collect the victim's IP address.[^2]  |
| [[DNS\|T1071.004]] | DNS | [Pisloader](https://attack.mitre.org/software/S0124) uses DNS as its C2 protocol.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Pisloader](https://attack.mitre.org/software/S0124) obfuscates files by splitting strings into smaller sub-strings and including "garbage" strings that are never used. The malware also uses return-oriented programming (ROP) technique and single-byte XOR to obfuscate data.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Pisloader](https://attack.mitre.org/software/S0124) has a command to upload a file to the victim machine.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Pisloader](https://attack.mitre.org/software/S0124) has a command to collect victim system information, including the system name and OS version.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Pisloader](https://attack.mitre.org/software/S0124) has commands to list drives on the victim machine and to list file information for a given directory.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT18\|G0026]] | APT18 |



## References

[^1]: Pisloader


[^2]: [Palo Alto DNS Requests](http://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)


