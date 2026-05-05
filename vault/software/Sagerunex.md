---
aliases: 
    - S1210
    
mitre-attack: https://attack.mitre.org/software/S1210
---

## S1210

[Sagerunex](https://attack.mitre.org/software/S1210) is a malware family exclusively associated with [Lotus Blossom](https://attack.mitre.org/groups/G0030) operations, with variants existing since at least 2016. Variations of [Sagerunex](https://attack.mitre.org/software/S1210) leverage non-traditional command and control mechanisms such as various web services.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Proxy\|T1090]] | Proxy | [Sagerunex](https://attack.mitre.org/software/S1210) uses several proxy configuration settings to ensure connectivity.[^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Sagerunex](https://attack.mitre.org/software/S1210) encrypts collected system data then exfiltrates via existing command and control channels.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Sagerunex](https://attack.mitre.org/software/S1210) will gather system information such as MAC and IP addresses.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Sagerunex](https://attack.mitre.org/software/S1210) communicates via HTTPS, at times using a hard-coded User Agent of `Mozilla/5.0 (compatible; MSIE 7.0; Win32)`.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Sagerunex](https://attack.mitre.org/software/S1210) can be passed a reference to an XOR-encrypted configuration file at runtime.[^1]  |
| [[Native API\|T1106]] | Native API | [Sagerunex](https://attack.mitre.org/software/S1210) calls the `WaitForSingleObject` API function as part of time-check logic.[^2]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Sagerunex](https://attack.mitre.org/software/S1210) is designed to be dynamic link library (DLL) injected into an infected endpoint and executed directly in memory.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Sagerunex](https://attack.mitre.org/software/S1210) identifies the `explorer.exe` process on the executing system.[^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Sagerunex](https://attack.mitre.org/software/S1210) has used VMProtect to pack and obscure itself.[^2]  |
| [[One-Way Communication\|T1102.003]] | One-Way Communication | [Sagerunex](https://attack.mitre.org/software/S1210) has used web services such as Twitter for command and control purposes.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Sagerunex](https://attack.mitre.org/software/S1210) uses a custom decryption routine to unpack itself during installation.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Sagerunex](https://attack.mitre.org/software/S1210) gathers information from the infected system such as hostname.[^2]  |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [Sagerunex](https://attack.mitre.org/software/S1210) finds the `explorer.exe` process after execution and uses it to change the token of its executing thread.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Sagerunex](https://attack.mitre.org/software/S1210) uses HTTPS for command and control communication.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Sagerunex](https://attack.mitre.org/software/S1210) gathers host information and stages it locally as a RAR file prior to exfiltration.[^2]  [Sagerunex](https://attack.mitre.org/software/S1210) stores logged data in an encrypted file located at `%TEMP%/TS_FB56.tmp` during execution.[^1]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [Sagerunex](https://attack.mitre.org/software/S1210) uses a "servicemain" function to verify its environment to ensure it can only be executed as a service, as well as the existence of a configuration file in a specified directory.[^2]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Sagerunex](https://attack.mitre.org/software/S1210) has archived collected materials in RAR format.[^2]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [Sagerunex](https://attack.mitre.org/software/S1210) has used virtual private servers (VPS) for command and control traffic as well as third-party cloud services in more recent variants.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lotus Blossom\|G0030]] | Lotus Blossom |



## References

[^1]: [Symantec Bilbug 2022](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)


[^2]: [Cisco LotusBlossom 2025](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)


