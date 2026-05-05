---
aliases: 
    - S1169
    
mitre-attack: https://attack.mitre.org/software/S1169
---

## S1169

[Mango](https://attack.mitre.org/software/S1169) is a first-stage backdoor written in C#/.NET that was used by [OilRig](https://attack.mitre.org/groups/G0049) during the [Juicy Mix](https://attack.mitre.org/campaigns/C0044) campaign. [Mango](https://attack.mitre.org/software/S1169) is the successor to [Solar](https://attack.mitre.org/software/S1166) and includes additional exfiltration capabilities, the use of native APIs, and added detection evasion code.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Mango](https://attack.mitre.org/software/S1169) can receive XOR-encrypted commands from C2.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Mango](https://attack.mitre.org/software/S1169) can collect the machine name of a compromised system which is later used as part of a unique victim identifier.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Mango](https://attack.mitre.org/software/S1169) can use TLS to encrypt C2 communications.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Mango](https://attack.mitre.org/software/S1169) contains a series of base64 encoded substrings.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Mango](https://attack.mitre.org/software/S1169) can enumerate the contents of current working or other specified directories.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Mango](https://attack.mitre.org/software/S1169) contains an unused capability to block endpoint security solutions from loading user-mode code hooks via a DLL in a specified process by using the `UpdateProcThreadAttribute API` to set the `PROC_THREAD_ATTRIBUTE_MITIGATION_POLICY` to `PROCESS_CREATION_MITIGATION_POLICY_BLOCK_NON_MICROSOFT_BINARIES_ALWAYS_ON` for an identified process. [^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Mango](https://attack.mitre.org/software/S1169) has been executed through a Microsoft Word document with a malicious macro.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Mango](https://attack.mitre.org/software/S1169) can use its HTTP C2 channel for exfiltration.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Mango](https://attack.mitre.org/software/S1169) can retrieve C2 commands sent in HTTP responses.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Mango](https://attack.mitre.org/software/S1169) can collect the user name from a compromised system which is used to create a unique victim identifier.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Mango](https://attack.mitre.org/software/S1169) can receive Base64-encoded commands from C2.[^1]  |
| [[Native API\|T1106]] | Native API | [Mango](https://attack.mitre.org/software/S1169) has the ability to use Native APIs.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Mango](https://attack.mitre.org/software/S1169) can create a scheduled task to run every 32 seconds to communicate with C2 and execute received commands.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[OilRig\|G0049]] | OilRig |



## References

[^1]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)


