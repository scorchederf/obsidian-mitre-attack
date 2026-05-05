---
aliases: 
    - S0579
    
mitre-attack: https://attack.mitre.org/software/S0579
---

## S0579

[Waterbear](https://attack.mitre.org/software/S0579) is modular malware attributed to [BlackTech](https://attack.mitre.org/groups/G0098) that has been used primarily for lateral movement, decrypting, and triggering payloads and is capable of hiding network behaviors.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[DLL\|T1574.001]] | DLL | [Waterbear](https://attack.mitre.org/software/S0579) has used DLL side loading to import and load a malicious DLL loader.[^1]   |
| [[Thread Execution Hijacking\|T1055.003]] | Thread Execution Hijacking | [Waterbear](https://attack.mitre.org/software/S0579) can use thread injection to inject shellcode into the process of security software.[^1]  |
| [[Process Injection\|T1055]] | Process Injection | [Waterbear](https://attack.mitre.org/software/S0579) can inject decrypted shellcode into the LanmanServer service.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Waterbear](https://attack.mitre.org/software/S0579) can receive and load executables from remote C2 servers.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Waterbear](https://attack.mitre.org/software/S0579) has deleted certain values from the Registry to load a malicious DLL.[^1]   |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Waterbear](https://attack.mitre.org/software/S0579) has the ability to decrypt its RC4 encrypted payload for execution.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Waterbear](https://attack.mitre.org/software/S0579) has used RC4 encrypted shellcode and encrypted functions.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Waterbear](https://attack.mitre.org/software/S0579) can use API hooks on `GetExtendedTcpTable` to retrieve a table containing a list of TCP endpoints available to the application.[^1]   |
| [[Query Registry\|T1012]] | Query Registry | [Waterbear](https://attack.mitre.org/software/S0579) can query the Registry key `"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\MSDTC\MTxOCI"` to see if the value `OracleOcilib` exists.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Waterbear](https://attack.mitre.org/software/S0579) can find the presence of a specific security software.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Waterbear](https://attack.mitre.org/software/S0579) can identify the process for a specific security product.[^1]  |
| [[Native API\|T1106]] | Native API | [Waterbear](https://attack.mitre.org/software/S0579) can leverage API functions for execution.[^1]  |
| [[Indicator Removal from Tools\|T1027.005]] | Indicator Removal from Tools | [Waterbear](https://attack.mitre.org/software/S0579) can scramble functions not to be executed again with random values.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Waterbear](https://attack.mitre.org/software/S0579) can hook the `ZwOpenProcess` and `GetExtendedTcpTable` APIs called by the process of a security product to hide PIDs and TCP records from detection.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[BlackTech\|G0098]] | BlackTech |



## References

[^1]: [Trend Micro Waterbear December 2019](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)


[^2]: Waterbear


