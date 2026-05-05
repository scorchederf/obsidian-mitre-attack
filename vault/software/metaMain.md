---
aliases: 
    - S1059
    
mitre-attack: https://attack.mitre.org/software/S1059
---

## S1059

[metaMain](https://attack.mitre.org/software/S1059) is a backdoor used by [Metador](https://attack.mitre.org/groups/G1013) to maintain long-term access to compromised machines; it has also been used to decrypt [Mafalda](https://attack.mitre.org/software/S1060) into memory.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [metaMain](https://attack.mitre.org/software/S1059) can collect the username from a compromised host.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [metaMain](https://attack.mitre.org/software/S1059)'s module file has been encrypted via XOR.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [metaMain](https://attack.mitre.org/software/S1059) can enumerate the processes that run on the platform.[^1] [^2]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [metaMain](https://attack.mitre.org/software/S1059) has stored the collected system files in a working directory.[^1] [^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [metaMain](https://attack.mitre.org/software/S1059) can establish an indirect and raw TCP socket-based connection to the C2 server.[^1] [^2]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [metaMain](https://attack.mitre.org/software/S1059) registered a WMI event subscription consumer called "hard_disk_stat" to establish persistence.[^1]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [metaMain](https://attack.mitre.org/software/S1059) has reflectively loaded a DLL to read, decrypt, and load an orchestrator file.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [metaMain](https://attack.mitre.org/software/S1059) can write the process ID of a target process into the `HKEY_LOCAL_MACHINE\SOFTWARE\DDE\tpid` Registry value as part of its reflective loading activity.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [metaMain](https://attack.mitre.org/software/S1059) can decrypt and load other modules.[^1]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [metaMain](https://attack.mitre.org/software/S1059) has used XOR-based encryption for collected files before exfiltration.[^1]  |
| [[Input Capture\|T1056]] | Input Capture | [metaMain](https://attack.mitre.org/software/S1059) can log mouse events.[^2]  |
| [[Native API\|T1106]] | Native API | [metaMain](https://attack.mitre.org/software/S1059) can execute an operator-provided Windows command by leveraging functions such as `WinExec`, `WriteFile`, and `ReadFile`.[^1] [^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [metaMain](https://attack.mitre.org/software/S1059) can take and save screenshots.[^1] [^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [metaMain](https://attack.mitre.org/software/S1059) can use HTTP for C2 communications.[^1] [^2]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [metaMain](https://attack.mitre.org/software/S1059) has delayed execution for five to six minutes during its persistence establishment process.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [metaMain](https://attack.mitre.org/software/S1059) can collect files and system information from a compromised host.[^1] [^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [metaMain](https://attack.mitre.org/software/S1059) can recursively enumerate files in an operator-provided directory.[^1] [^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [metaMain](https://attack.mitre.org/software/S1059) can upload collected files and data to its C2 server.[^2]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [metaMain](https://attack.mitre.org/software/S1059) can create a named pipe to listen for and send data to a named pipe-based C2 server.[^2]  |
| [[DLL\|T1574.001]] | DLL | [metaMain](https://attack.mitre.org/software/S1059) can support an HKCMD sideloading start method.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [metaMain](https://attack.mitre.org/software/S1059) can download files onto compromised systems.[^1] [^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [metaMain](https://attack.mitre.org/software/S1059) has deleted collected items after uploading the content to its C2 server.[^1] [^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [metaMain](https://attack.mitre.org/software/S1059) has the ability to log keyboard events.[^1] [^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [metaMain](https://attack.mitre.org/software/S1059) can encrypt the data that it sends and receives from the C2 server using an RC4 encryption algorithm.[^1] [^2]  |
| [[Timestomp\|T1070.006]] | Timestomp | [metaMain](https://attack.mitre.org/software/S1059) can change the `CreationTime`, `LastAccessTime`, and `LastWriteTime` file time attributes when executed with `SYSTEM` privileges.[^2]  |
| [[Process Injection\|T1055]] | Process Injection | [metaMain](https://attack.mitre.org/software/S1059) can inject the loader file, Speech02.db, into a process.[^1]  |
| [[Port Knocking\|T1205.001]] | Port Knocking | [metaMain](https://attack.mitre.org/software/S1059) has authenticated itself to a different implant, Cryshell, through a port knocking and handshake procedure.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [metaMain](https://attack.mitre.org/software/S1059) can collect the computer name from a compromised host.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Metador\|G1013]] | Metador |



## References

[^1]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)


[^2]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)


