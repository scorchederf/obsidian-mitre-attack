---
aliases: 
    - S0034
    
mitre-attack: https://attack.mitre.org/software/S0034
---

## S0034

[NETEAGLE](https://attack.mitre.org/software/S0034) is a backdoor developed by [APT30](https://attack.mitre.org/groups/G0013) with compile dates as early as 2008. It has two main variants known as “Scout” and “Norton.” [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [NETEAGLE](https://attack.mitre.org/software/S0034) will decrypt resources it downloads with HTTP requests by using RC4 with the key "ScoutEagle."[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [NETEAGLE](https://attack.mitre.org/software/S0034) can send process listings over the C2 channel.[^1]  |
| [[Application Layer Protocol\|T1071]] | Application Layer Protocol | Adversaries can also use [NETEAGLE](https://attack.mitre.org/software/S0034) to establish an RDP connection with a controller over TCP/7519. |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [NETEAGLE](https://attack.mitre.org/software/S0034) is capable of reading files over the C2 channel.[^1]  |
| [[Dynamic Resolution\|T1568]] | Dynamic Resolution | [NETEAGLE](https://attack.mitre.org/software/S0034) can use HTTP to download resources that contain an IP address and port number pair to connect to for C2.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [NETEAGLE](https://attack.mitre.org/software/S0034) allows adversaries to enumerate and modify the infected host's file system. It supports searching for directories, creating directories, listing directory contents, reading and writing to files, retrieving file attributes, and retrieving volume information.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | The "SCOUT" variant of [NETEAGLE](https://attack.mitre.org/software/S0034) achieves persistence by adding itself to the `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` Registry key.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [NETEAGLE](https://attack.mitre.org/software/S0034) will attempt to detect if the infected host is configured to a proxy. If so, [NETEAGLE](https://attack.mitre.org/software/S0034) will send beacons via an HTTP POST request. [NETEAGLE](https://attack.mitre.org/software/S0034) will also use HTTP to download resources that contain an IP address and Port Number pair to connect to for further C2.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [NETEAGLE](https://attack.mitre.org/software/S0034) allows adversaries to execute shell commands on the infected host.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [NETEAGLE](https://attack.mitre.org/software/S0034) will attempt to detect if the infected host is configured to a proxy. If so, [NETEAGLE](https://attack.mitre.org/software/S0034) will send beacons via an HTTP POST request; otherwise it will send beacons via UDP/6000.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | If [NETEAGLE](https://attack.mitre.org/software/S0034) does not detect a proxy configured on the infected machine, it will send beacons via UDP/6000. Also, after retrieving a C2 IP address and Port Number, [NETEAGLE](https://attack.mitre.org/software/S0034) will initiate a TCP connection to this socket. The ensuing connection is a plaintext C2 channel in which commands are specified by DWORDs.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT30\|G0013]] | APT30 |



## References

[^1]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)


