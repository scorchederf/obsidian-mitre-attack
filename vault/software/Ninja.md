---
aliases: 
    - S1100
    
mitre-attack: https://attack.mitre.org/software/S1100
---

## S1100

[Ninja](https://attack.mitre.org/software/S1100) is a malware developed in C++ that has been used by [ToddyCat](https://attack.mitre.org/groups/G1022) to penetrate networks and control remote systems since at least 2020.  [Ninja](https://attack.mitre.org/software/S1100) is possibly part of a post exploitation toolkit exclusively used by [ToddyCat](https://attack.mitre.org/groups/G1022) and allows multiple operators to work simultaneously on the same machine. [Ninja](https://attack.mitre.org/software/S1100) has been used against government and military entities in Europe and Asia and observed in specific infection chains being deployed by [Samurai](https://attack.mitre.org/software/S1099).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | The [Ninja](https://attack.mitre.org/software/S1100) payload is XOR encrypted and compressed.[^2]  [Ninja](https://attack.mitre.org/software/S1100) has also XORed its configuration data with a constant value of `0xAA`.[^1] [^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Ninja](https://attack.mitre.org/software/S1100) can forward TCP packets between the C2 and a remote host.[^1] [^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Ninja](https://attack.mitre.org/software/S1100) has used legitimate looking filenames for its loader including update.dll and x64.dll.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Ninja](https://attack.mitre.org/software/S1100) can enumerate the IP address on compromised systems.[^1]  |
| [[Spearphishing via Service\|T1566.003]] | Spearphishing via Service | [Ninja](https://attack.mitre.org/software/S1100) has been distributed to victims via the messaging app Telegram.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Ninja](https://attack.mitre.org/software/S1100) has gained execution through victims opening malicious executable files embedded in zip archives.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Ninja](https://attack.mitre.org/software/S1100) has the ability to enumerate directory content.[^1] [^2]  |
| [[Native API\|T1106]] | Native API | The [Ninja](https://attack.mitre.org/software/S1100) loader can call Windows APIs for discovery, process injection, and payload decryption.[^1] [^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Ninja](https://attack.mitre.org/software/S1100) can XOR and AES encrypt C2 messages.[^1]  |
| [[Scheduled Transfer\|T1029]] | Scheduled Transfer | [Ninja](https://attack.mitre.org/software/S1100) can configure its agent to work only in specific time frames.[^1]  |
| [[DLL\|T1574.001]] | DLL | [Ninja](https://attack.mitre.org/software/S1100) loaders can be side-loaded with legitimate and signed executables including the  VLC.exe media player.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Ninja](https://attack.mitre.org/software/S1100) can obtain the computer name and information on the OS from targeted hosts.[^1] [^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | The [Ninja](https://attack.mitre.org/software/S1100) loader component can decrypt and decompress the payload.[^1] [^2]  |
| [[Data Obfuscation\|T1001]] | Data Obfuscation | [Ninja](https://attack.mitre.org/software/S1100) has the ability to modify headers and URL paths to hide malicious traffic in HTTP requests.[^1]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [Ninja](https://attack.mitre.org/software/S1100) has the ability to use a proxy chain with up to 255 hops when using TCP.[^1]  |
| [[Environmental Keying\|T1480.001]] | Environmental Keying | [Ninja](https://attack.mitre.org/software/S1100) can store its final payload in the Registry under `$HKLM\SOFTWARE\Classes\Interface\` encrypted with a dynamically generated key based on the drive’s serial number.[^1]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [Ninja](https://attack.mitre.org/software/S1100) can proxy C2 communications including to and from internal agents without internet connectivity.[^1] [^2]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Ninja](https://attack.mitre.org/software/S1100) can obtain information on physical drives from targeted hosts.[^1] [^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Ninja](https://attack.mitre.org/software/S1100) loader components can be executed through rundll32.exe.[^2]  |
| [[Process Injection\|T1055]] | Process Injection | [Ninja](https://attack.mitre.org/software/S1100) has the ability to inject an agent module into a new process and arbitrary shellcode into running processes.[^1] [^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Ninja](https://attack.mitre.org/software/S1100) can create the services `httpsvc` and `w3esvc` for persistence .[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Ninja](https://attack.mitre.org/software/S1100) can enumerate processes on a targeted host.[^1] [^2]  |
| [[Protocol or Service Impersonation\|T1001.003]] | Protocol or Service Impersonation | [Ninja](https://attack.mitre.org/software/S1100) has the ability to mimic legitimate services with customized HTTP URL paths and headers to hide malicious traffic.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Ninja](https://attack.mitre.org/software/S1100) can use HTTP for C2 communications.[^1]  |
| [[Compression\|T1027.015]] | Compression | [Ninja](https://attack.mitre.org/software/S1100) has compressed its data with the LZSS algorithm.[^1] [^2]  |
| [[Timestomp\|T1070.006]] | Timestomp | [Ninja](https://attack.mitre.org/software/S1100) can change or create the last access or write times.[^1]  |
| [[Inter-Process Communication\|T1559]] | Inter-Process Communication | [Ninja](https://attack.mitre.org/software/S1100) can use pipes to redirect the standard input and the standard output.[^1]  |
| [[Non-Standard Encoding\|T1132.002]] | Non-Standard Encoding | [Ninja](https://attack.mitre.org/software/S1100) can encode C2 communications with a base64 algorithm using a custom alphabet.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[ToddyCat\|G1022]] | ToddyCat |



## References

[^1]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)


[^2]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)


