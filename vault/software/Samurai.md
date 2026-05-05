---
aliases: 
    - S1099
    
mitre-attack: https://attack.mitre.org/software/S1099
---

## S1099

[Samurai](https://attack.mitre.org/software/S1099) is a passive backdoor that has been used by [ToddyCat](https://attack.mitre.org/groups/G1022) since at least 2020. [Samurai](https://attack.mitre.org/software/S1099) allows arbitrary C# code execution and is used with multiple modules for remote administration and lateral movement.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Samurai](https://attack.mitre.org/software/S1099) has been used to deploy other malware including [Ninja](https://attack.mitre.org/software/S1100).[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Samurai](https://attack.mitre.org/software/S1099) can use a proxy module to forward TCP packets to external hosts.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Samurai](https://attack.mitre.org/software/S1099) can create a service at `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SvcHost` to trigger execution and maintain persistence.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Samurai](https://attack.mitre.org/software/S1099) can encrypt C2 communications with AES.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Samurai](https://attack.mitre.org/software/S1099) can use a specific module for file enumeration.[^1]  |
| [[Compression\|T1027.015]] | Compression | [Samurai](https://attack.mitre.org/software/S1099) can deliver its final payload as a compressed, encrypted and base64-encoded blob.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | The [Samurai](https://attack.mitre.org/software/S1099) loader component can create multiple Registry keys to force the svchost.exe process to load the final backdoor.[^1]  |
| [[Compile After Delivery\|T1027.004]] | Compile After Delivery | [Samurai](https://attack.mitre.org/software/S1099) can compile and execute downloaded modules at runtime.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Samurai](https://attack.mitre.org/software/S1099) can base64 encode data sent in C2 communications prior to its encryption.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [Samurai](https://attack.mitre.org/software/S1099) can query `SOFTWARE\Microsoft\.NETFramework\policy\v2.0` for discovery.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Samurai](https://attack.mitre.org/software/S1099) has created the directory `%COMMONPROGRAMFILES%\Microsoft Shared\wmi\` to contain DLLs for loading successive stages.[^1]  |
| [[Proxy\|T1090]] | Proxy | [Samurai](https://attack.mitre.org/software/S1099) has the ability to proxy connections to specified remote IPs and ports through a a proxy module.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Samurai](https://attack.mitre.org/software/S1099) can use a remote command module for execution via the Windows command line.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Samurai](https://attack.mitre.org/software/S1099) can use a .NET HTTPListener class to receive and handle HTTP POST requests.[^1]  |
| [[Dynamic API Resolution\|T1027.007]] | Dynamic API Resolution | [Samurai](https://attack.mitre.org/software/S1099) can encrypt API name strings with an XOR-based algorithm.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Samurai](https://attack.mitre.org/software/S1099) can encrypt the names of requested APIs.[^1]  |
| [[Native API\|T1106]] | Native API | [Samurai](https://attack.mitre.org/software/S1099) has the ability to call Windows APIs.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Samurai](https://attack.mitre.org/software/S1099) can leverage an exfiltration module to download arbitrary files from compromised machines.[^1]  |
| [[Software Discovery\|T1518]] | Software Discovery | [Samurai](https://attack.mitre.org/software/S1099) can check for the presence and version of the .NET framework.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[ToddyCat\|G1022]] | ToddyCat |



## References

[^1]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)


