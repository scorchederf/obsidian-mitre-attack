---
aliases: 
    - S0236
    
mitre-attack: https://attack.mitre.org/software/S0236
---

## S0236

[Kwampirs](https://attack.mitre.org/software/S0236) is a backdoor Trojan used by [Orangeworm](https://attack.mitre.org/groups/G0071). [Kwampirs](https://attack.mitre.org/software/S0236) has been found on machines which had software installed for the use and control of high-tech imaging devices such as X-Ray and MRI machines.[^4]  [Kwampirs](https://attack.mitre.org/software/S0236) has multiple technical overlaps with [Shamoon](https://attack.mitre.org/software/S0140) based on reverse engineering analysis.[^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Domain Groups\|T1069.002]] | Domain Groups | [Kwampirs](https://attack.mitre.org/software/S0236) collects a list of domain groups with the command `net localgroup /domain`.[^4]  |
| [[Local Account\|T1087.001]] | Local Account | [Kwampirs](https://attack.mitre.org/software/S0236) collects a list of accounts with the command `net users`.[^4]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Kwampirs](https://attack.mitre.org/software/S0236) collects a list of network shares with the command `net share`.[^4]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Kwampirs](https://attack.mitre.org/software/S0236) decrypts and extracts a copy of its main DLL payload when executing.[^4]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Kwampirs](https://attack.mitre.org/software/S0236) collects a list of running services with the command `tasklist /svc`.[^4]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Kwampirs](https://attack.mitre.org/software/S0236) collects a list of files and directories in C:\ with the command `dir /s /a c:\ >> "C:\windows\TEMP\[RANDOM].tmp"`.[^4]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Kwampirs](https://attack.mitre.org/software/S0236) downloads additional files that are base64-encoded and encrypted with another cipher.[^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Kwampirs](https://attack.mitre.org/software/S0236) creates a new service named WmiApSrvEx to establish persistence.[^4]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Kwampirs](https://attack.mitre.org/software/S0236) collects registered owner details by using the commands `systeminfo` and `net config workstation`.[^4]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Kwampirs](https://attack.mitre.org/software/S0236) collects a list of available servers with the command `net view`.[^4]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Kwampirs](https://attack.mitre.org/software/S0236) copies itself over network shares to move laterally on a victim network.[^4]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | Before writing to disk, [Kwampirs](https://attack.mitre.org/software/S0236) inserts a randomly generated string into the middle of the decrypted payload in an attempt to evade hash-based detections.[^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Kwampirs](https://attack.mitre.org/software/S0236) downloads additional files from C2 servers.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Kwampirs](https://attack.mitre.org/software/S0236) collects OS version information such as registered owner details, manufacturer details, processor type, available storage, installed patches, hostname, version info, system date, and other system information by using the commands `systeminfo`, `net config workstation`, `hostname`, `ver`, `set`, and `date /t`.[^4]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Kwampirs](https://attack.mitre.org/software/S0236) establishes persistence by adding a new service with the display name "WMI Performance Adapter Extension" in an attempt to masquerade as a legitimate WMI service.[^4]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Kwampirs](https://attack.mitre.org/software/S0236) uses rundll32.exe in a Registry value added to establish persistence.[^4]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Kwampirs](https://attack.mitre.org/software/S0236) collects a list of running services with the command `tasklist /v`.[^4]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Kwampirs](https://attack.mitre.org/software/S0236) collects a list of active and listening connections by using the command `netstat -nao` as well as a list of available network mappings with `net use`.[^4]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Kwampirs](https://attack.mitre.org/software/S0236) collects network adapter and interface information by using the commands `ipconfig /all`, `arp -a` and `route print`. It also collects the system's MAC address with `getmac` and domain configuration with `net config workstation`.[^4]  |
| [[Password Policy Discovery\|T1201]] | Password Policy Discovery | [Kwampirs](https://attack.mitre.org/software/S0236) collects password policy information with the command `net accounts`.[^4]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Kwampirs](https://attack.mitre.org/software/S0236) uses a large list of C2 servers that it cycles through until a successful connection is established.[^4]  |
| [[Local Groups\|T1069.001]] | Local Groups | [Kwampirs](https://attack.mitre.org/software/S0236) collects a list of users belonging to the local users and administrators groups with the commands `net localgroup administrators` and `net localgroup users`.[^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Orangeworm\|G0071]] | Orangeworm |



## References

[^1]: Kwampirs


[^2]: [Symantec Security Center Trojan.Kwampirs](https://www.symantec.com/security-center/writeup/2016-081923-2700-99)


[^3]: [Cylera Kwampirs 2022](https://resources.cylera.com/hubfs/Cylera%20Labs/Cylera%20Labs%20Kwampirs%20Shamoon%20Technical%20Report.pdf)


[^4]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)


