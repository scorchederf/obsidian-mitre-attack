---
aliases: 
    - S0586
    
mitre-attack: https://attack.mitre.org/software/S0586
---

## S0586

[TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) is a fully-featured beaconing implant integrated with command modules used by [Lazarus Group](https://attack.mitre.org/groups/G0032). It was first reported in May 2020.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | The [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) command and execution module can perform target system enumeration.[^1]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) can execute `FileRecvWriteRand` to append random bytes to the end of a file received from C2.[^1]  |
| [[Timestomp\|T1070.006]] | Timestomp | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) can change the timestamp of specified filenames.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) can use `DirectoryList` to enumerate files in a specified directory.[^1]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) has used `FileReadZipSend` to compress a file and send to C2.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) can execute `ProcessList` for process discovery.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | The [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) main executable has disguised itself as Microsoft’s Narrator.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) can copy itself into the current user’s Startup folder as “Narrator.exe” for persistence.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) can enable Windows CLI access and execute files.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) uses a Linear Feedback Shift Register (LFSR) algorithm for network encryption.[^1]  |
| [[Protocol or Service Impersonation\|T1001.003]] | Protocol or Service Impersonation | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) has used FakeTLS for session authentication.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) can download additional modules from its C2 server.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) can execute `GetLocalTime` for time discovery.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) can randomly pick one of five hard-coded IP addresses for C2 communication; if one of the IP fails, it will wait 60 seconds and then try another IP address.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) can delete files from a compromised host.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) can use `DriveList` to retrieve drive information.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: [CISA MAR-10288834-2.v1  TAINTEDSCRIBE MAY 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)


