---
aliases: 
    - S1030
    
mitre-attack: https://attack.mitre.org/software/S1030
---

## S1030

[Squirrelwaffle](https://attack.mitre.org/software/S1030) is a loader that was first seen in September 2021. It has been used in spam email campaigns to deliver additional malware such as [Cobalt Strike](https://attack.mitre.org/software/S0154) and the [QakBot](https://attack.mitre.org/software/S0650) banking trojan.[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Squirrelwaffle](https://attack.mitre.org/software/S1030) can collect the user name from a compromised host.[^2]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has used malicious VBA macros in Microsoft Word documents and Excel spreadsheets that execute an `AutoOpen` subroutine.[^2] [^1]   |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has gathered victim computer information and configurations.[^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has exfiltrated victim data using HTTP POST requests to its C2 servers.[^2]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has been distributed through phishing emails containing a malicious URL.[^2]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has been executed using `regsvr32.exe`.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has decrypted files and payloads using a XOR-based algorithm.[^2] [^1]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has relied on victims to click on a malicious link send via phishing campaigns.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has downloaded and executed additional encoded payloads.[^2] [^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has been distributed via malicious Microsoft Office documents within spam emails.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has encoded its communications to C2 servers using Base64.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has used HTTP POST requests for C2 communications.[^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has relied on users enabling malicious macros within Microsoft Excel and Word attachments.[^2] [^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has been obfuscated with a XOR-based algorithm.[^2] [^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has been packed with a custom packer to hide payloads.[^2] [^1]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has encrypted collected data using a XOR-based algorithm.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has used PowerShell to execute its payload.[^2] [^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has used `cmd.exe` for execution.[^1]  |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has contained a hardcoded list of IP addresses to block that belong to sandboxes and analysis platforms.[^2] [^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has been executed using `rundll32.exe`.[^2] [^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has collected the victim’s external IP address.[^2]  |




## References

[^1]: [Netskope Squirrelwaffle Oct 2021](https://www.netskope.com/blog/squirrelwaffle-new-malware-loader-delivering-cobalt-strike-and-qakbot)


[^2]: [ZScaler Squirrelwaffle Sep 2021](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)


