---
aliases: 
    - S0244
    
mitre-attack: https://attack.mitre.org/software/S0244
---

## S0244

[Comnie](https://attack.mitre.org/software/S0244) is a remote backdoor which has been used in attacks in East Asia. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Comnie](https://attack.mitre.org/software/S0244) runs the command: `net start >> %TEMP%\info.dat` on a victim.[^2]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Comnie](https://attack.mitre.org/software/S0244) executes a batch script to store discovery information in %TEMP%\info.dat and then uploads the temporarily file to the remote C2 server.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Comnie](https://attack.mitre.org/software/S0244) attempts to detect several anti-virus products.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Comnie](https://attack.mitre.org/software/S0244) executes BAT scripts.[^2]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [Comnie](https://attack.mitre.org/software/S0244) uses blogs and third-party sites (GitHub, tumbler, and BlogSpot) to avoid DNS-based blocking of their communication to the command and control server.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Comnie](https://attack.mitre.org/software/S0244) uses the `tasklist` to view running processes on the victim’s machine.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Comnie](https://attack.mitre.org/software/S0244) uses `ipconfig /all` and `route PRINT` to identify network adapter and interface information.[^2]  |
| [[Local Account\|T1087.001]] | Local Account | [Comnie](https://attack.mitre.org/software/S0244) uses the `net user` command.[^2]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Comnie](https://attack.mitre.org/software/S0244) executes the `netstat -ano` command.[^2]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Comnie](https://attack.mitre.org/software/S0244) runs the `net view` command |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [Comnie](https://attack.mitre.org/software/S0244) establishes persistence via a .lnk file in the victim’s startup path.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Comnie](https://attack.mitre.org/software/S0244) uses HTTP for C2 communication.[^2]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Comnie](https://attack.mitre.org/software/S0244) executes VBS scripts.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Comnie](https://attack.mitre.org/software/S0244) encrypts command and control communications with RC4.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Comnie](https://attack.mitre.org/software/S0244) collects the hostname of the victim machine.[^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Comnie](https://attack.mitre.org/software/S0244) uses Rundll32 to load a malicious DLL.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Comnie](https://attack.mitre.org/software/S0244) achieves persistence by adding a shortcut of itself to the startup path in the Registry.[^2]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [Comnie](https://attack.mitre.org/software/S0244) appends a total of 64MB of garbage data to a file to deter any security products in place that may be scanning files on disk.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Comnie](https://attack.mitre.org/software/S0244) uses RC4 and Base64 to obfuscate strings.[^2]  |




## References

[^1]: Comnie


[^2]: [Palo Alto Comnie](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)


