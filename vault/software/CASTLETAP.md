---
aliases: 
    - S1224
    
mitre-attack: https://attack.mitre.org/software/S1224
---

## S1224

[CASTLETAP](https://attack.mitre.org/software/S1224) is an ICMP port knocking backdoor that has been installed on compromised FortiGate firewalls by [UNC3886](https://attack.mitre.org/groups/G1048).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Unix Shell\|T1059.004]] | Unix Shell | [CASTLETAP](https://attack.mitre.org/software/S1224) has the ability to spawn BusyBox command shell in victim environments.[^1] <br> |
| [[Socket Filters\|T1205.002]] | Socket Filters | [CASTLETAP](https://attack.mitre.org/software/S1224) can listen for a specialized ICMP packet for activation on compromised network devices.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [CASTLETAP](https://attack.mitre.org/software/S1224) can transfer files to compromised network devices.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [CASTLETAP](https://attack.mitre.org/software/S1224) can filter and deobfuscate an XOR encrypted activation string in the payload of an ICMP echo request.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [CASTLETAP](https://attack.mitre.org/software/S1224) can initiate a C2 connection over an SSL socket.[^1]  |
| [[Network Sniffing\|T1040]] | Network Sniffing | [CASTLETAP](https://attack.mitre.org/software/S1224) has the ability to create a raw promiscuous socket to sniff network traffic.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [CASTLETAP](https://attack.mitre.org/software/S1224) can receive a 9-byte XOR encrypted activation string in the payload of an ICMP echo request packet.[^1] <br> |
| [[Data from Local System\|T1005]] | Data from Local System | [CASTLETAP](https://attack.mitre.org/software/S1224) can execute a C2 command to transfer files from victim machines.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[UNC3886\|G1048]] | UNC3886 |



## References

[^1]: [Mandiant Fortinet Zero Day](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)


