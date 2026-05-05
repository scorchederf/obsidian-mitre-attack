---
aliases: 
    - S0087
    
mitre-attack: https://attack.mitre.org/software/S0087
---

## S0087

[Hi-Zor](https://attack.mitre.org/software/S0087) is a remote access tool (RAT) that has characteristics similar to [Sakula](https://attack.mitre.org/software/S0074). It was used in a campaign named INOCNATION. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Hi-Zor](https://attack.mitre.org/software/S0087) has the ability to upload and download files from its C2 server.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Hi-Zor](https://attack.mitre.org/software/S0087) communicates with its C2 server over HTTPS.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Hi-Zor](https://attack.mitre.org/software/S0087) encrypts C2 traffic with a double XOR using two distinct single-byte keys.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Hi-Zor](https://attack.mitre.org/software/S0087) creates a Registry Run key to establish persistence.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Hi-Zor](https://attack.mitre.org/software/S0087) deletes its RAT installer file as it executes its DLL payload file.[^2]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Hi-Zor](https://attack.mitre.org/software/S0087) encrypts C2 traffic with TLS.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Hi-Zor](https://attack.mitre.org/software/S0087) has the ability to create a reverse shell.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Hi-Zor](https://attack.mitre.org/software/S0087) uses various XOR techniques to obfuscate its components.[^2]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Hi-Zor](https://attack.mitre.org/software/S0087) executes using regsvr32.exe called from the [Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001) persistence mechanism.[^2]  |




## References

[^1]: [Fidelis Hi-Zor](https://www.fidelissecurity.com/threatgeek/archive/introducing-hi-zor-rat/)


[^2]: [Fidelis INOCNATION](https://fidelissecurity.com/resource/report/fidelis-threat-advisory-1020-dissecting-the-malware-involved-in-the-inocnation-campaign/)


