---
aliases: 
    - S0532
    
mitre-attack: https://attack.mitre.org/software/S0532
---

## S0532

[Lucifer](https://attack.mitre.org/software/S0532) is a crypto miner and DDoS hybrid malware that leverages well-known exploits to spread laterally on Windows platforms.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Compute Hijacking\|T1496.001]] | Compute Hijacking | [Lucifer](https://attack.mitre.org/software/S0532) can use system resources to mine cryptocurrency, dropping XMRig to mine Monero.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Lucifer](https://attack.mitre.org/software/S0532) can collect the IP address of a compromised host.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Lucifer](https://attack.mitre.org/software/S0532) can identify the IP and port numbers for all remote connections from the compromised host.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Lucifer](https://attack.mitre.org/software/S0532) can decrypt its C2 address upon execution.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Lucifer](https://attack.mitre.org/software/S0532) can identify the process that owns remote connections.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Lucifer](https://attack.mitre.org/software/S0532) can persist by setting Registry key values `HKLM\Software\Microsoft\Windows\CurrentVersion\Run\QQMusic` and `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\QQMusic`.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Lucifer](https://attack.mitre.org/software/S0532) can download and execute a replica of itself using [certutil](https://attack.mitre.org/software/S0160).[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Lucifer](https://attack.mitre.org/software/S0532) can perform a decremental-xor encryption on the initial C2 request before sending it over the wire.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Lucifer](https://attack.mitre.org/software/S0532) has the ability to identify the username on a compromised host.[^1]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Lucifer](https://attack.mitre.org/software/S0532) can use [certutil](https://attack.mitre.org/software/S0160) for propagation on Windows hosts within intranets.[^1]  |
| [[System Checks\|T1497.001]] | System Checks | [Lucifer](https://attack.mitre.org/software/S0532) can check for specific usernames, computer names, device drivers, DLL's, and virtual devices associated with sandboxed environments and can enter an infinite loop and stop itself if any are detected.[^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Lucifer](https://attack.mitre.org/software/S0532) has used UPX packed binaries.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Lucifer](https://attack.mitre.org/software/S0532) has established persistence by creating the following scheduled task `schtasks /create /sc minute /mo 1 /tn QQMusic ^ /tr C:Users\%USERPROFILE%\Downloads\spread.exe /F`.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Lucifer](https://attack.mitre.org/software/S0532) can collect the computer name, system architecture, default language, and processor frequency of a compromised host.[^1]  |
| [[Password Guessing\|T1110.001]] | Password Guessing | [Lucifer](https://attack.mitre.org/software/S0532) has attempted to brute force TCP ports 135 (RPC) and 1433 (MSSQL) with the default username or list of usernames and    passwords.[^1]  |
| [[Network Denial of Service\|T1498]] | Network Denial of Service | [Lucifer](https://attack.mitre.org/software/S0532) can execute TCP, UDP,  and HTTP denial of service (DoS) attacks.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Lucifer](https://attack.mitre.org/software/S0532) can issue shell commands to download and execute additional payloads.[^1]  |
| [[Application Layer Protocol\|T1071]] | Application Layer Protocol | [Lucifer](https://attack.mitre.org/software/S0532) can use the Stratum protocol on port 10001 for communication between the cryptojacking bot and the mining server.[^1]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [Lucifer](https://attack.mitre.org/software/S0532) can exploit multiple vulnerabilities including EternalBlue (CVE-2017-0144) and EternalRomance (CVE-2017-0144).[^1]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [Lucifer](https://attack.mitre.org/software/S0532) can clear and remove event logs.[^1]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Lucifer](https://attack.mitre.org/software/S0532) can scan for open ports including TCP ports 135 and 1433.[^1]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Lucifer](https://attack.mitre.org/software/S0532) can infect victims by brute forcing SMB.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [Lucifer](https://attack.mitre.org/software/S0532) can check for existing stratum cryptomining information in `HKLM\Software\Microsoft\Windows\CurrentVersion\spreadCpuXmr – %stratum info%`.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Lucifer](https://attack.mitre.org/software/S0532) can use WMI to log into remote machines for propagation.[^1]  |




## References

[^1]: [Unit 42 Lucifer June 2020](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)


