---
aliases: 
    - S9031
    
mitre-attack: https://attack.mitre.org/software/S9031
---

## S9031

[AshTag](https://attack.mitre.org/software/S9031) is a modular .NET backdoor with multiple features that has been used by [WIRTE](https://attack.mitre.org/groups/G0090) since at least 2025. [AshTag](https://attack.mitre.org/software/S9031) is designed for persistence and remote command execution and can masquerade as a legitimate VisualServer utility.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Screen Capture\|T1113]] | Screen Capture | The [AshTag](https://attack.mitre.org/software/S9031) AshenOrchestrator component has the ability to take screenshots.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | The [AshTag](https://attack.mitre.org/software/S9031) AshenOrchestrator component can enumerate files on victim hosts.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [AshTag](https://attack.mitre.org/software/S9031) can use a .NET program to execute WMI queries and send unique victim IDs to  C2.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [AshTag](https://attack.mitre.org/software/S9031) has been executed through victims downloading and opening malicious RAR archive files.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | The [AshTag](https://attack.mitre.org/software/S9031) loader and AshenOrchestrator components can collect reconnaissance data from victim machines.[^1]  |
| [[Web Service\|T1102]] | Web Service | [AshTag](https://attack.mitre.org/software/S9031) can download malicious payloads from file sharing services.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [AshTag](https://attack.mitre.org/software/S9031) can use HTTP to send and receive data from C2.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [AshTag](https://attack.mitre.org/software/S9031) has exfiltrated reconnaissance data on targeted systems to C2 servers.[^1]  |
| [[DLL\|T1574.001]] | DLL | [AshTag](https://attack.mitre.org/software/S9031) has enabled execution via DLL sideloading using a legitimate executable paired with a malicious DLL named wtsapi32.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | The [AshTag](https://attack.mitre.org/software/S9031) AshenOrchestrator component payload as been Base64 encoded and embedded with HTML content from the C2 server.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [AshTag](https://attack.mitre.org/software/S9031) can set persistence using scheduled tasks.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | The [AshTag](https://attack.mitre.org/software/S9031) stager compoment can decode and decrypt Base64 and XOR-encrypted payloads.[^1]  |
| [[JavaScript\|T1059.007]] | JavaScript | [AshTag](https://attack.mitre.org/software/S9031) can use JSON files to deliver payloads and configuration files.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | The [AshTag](https://attack.mitre.org/software/S9031) stager component can retrieve and execute the main payload.[^1]  |
| [[System Location Discovery\|T1614]] | System Location Discovery | [AshTag](https://attack.mitre.org/software/S9031) can check geolocation on targeted systems.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | The [AshTag](https://attack.mitre.org/software/S9031) AshenOrchestrator component has process management functionality.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [AshTag](https://attack.mitre.org/software/S9031) has masqueraded as a legitimate VisualServer utility.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [AshTag](https://attack.mitre.org/software/S9031) can use `volumeserialnumber` to enumerate volumes.[^1]   |
| [[Delay Execution\|T1678]] | Delay Execution | [AshTag](https://attack.mitre.org/software/S9031) can use a set sleep time to delay C2 beaconing.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[WIRTE\|G0090]] | WIRTE |



## References

[^1]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)


