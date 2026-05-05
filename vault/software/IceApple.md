---
aliases: 
    - S1022
    
mitre-attack: https://attack.mitre.org/software/S1022
---

## S1022

[IceApple](https://attack.mitre.org/software/S1022) is a modular Internet Information Services (IIS) post-exploitation framework, that has been used since at least 2021 against the technology, academic, and government sectors.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | The [IceApple](https://attack.mitre.org/software/S1022) [ifconfig](https://attack.mitre.org/software/S0101) module can iterate over all network interfaces on the host and retrieve the name, description, MAC address, DNS suffix, DNS servers, gateways, IPv4 addresses, and subnet masks.[^1]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [IceApple](https://attack.mitre.org/software/S1022) can use Base64 and "junk" JavaScript code to obfuscate information.[^1]  |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | [IceApple](https://attack.mitre.org/software/S1022)'s Credential Dumper module can dump LSA secrets from registry keys, including: `HKLM\SECURITY\Policy\PolEKList\default`, `HKLM\SECURITY\Policy\Secrets\*\CurrVal`, and `HKLM\SECURITY\Policy\Secrets\*\OldVal`.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [IceApple](https://attack.mitre.org/software/S1022) .NET assemblies have used `App_Web_` in their file names to appear legitimate.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [IceApple](https://attack.mitre.org/software/S1022) can delete files and directories from targeted systems.[^1]  |
| [[Credentials in Registry\|T1552.002]] | Credentials in Registry | [IceApple](https://attack.mitre.org/software/S1022) can harvest credentials from local and remote host registries.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [IceApple](https://attack.mitre.org/software/S1022)'s Multi File Exfiltrator module can exfiltrate multiple files from a compromised host as an HTTP response over C2.[^1]   |
| [[IIS Components\|T1505.004]] | IIS Components | [IceApple](https://attack.mitre.org/software/S1022) is an IIS post-exploitation framework, consisting of 18 modules that provide several functionalities.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [IceApple](https://attack.mitre.org/software/S1022) can collect files, passwords, and other data from a compromised host.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [IceApple](https://attack.mitre.org/software/S1022) can use a Base64-encoded AES key to decrypt tasking.[^1]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [IceApple](https://attack.mitre.org/software/S1022) can encrypt and compress files using Gzip prior to exfiltration.[^1]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [IceApple](https://attack.mitre.org/software/S1022) can use reflective code loading to load .NET assemblies into `MSExchangeOWAAppPool` on targeted Exchange servers.[^1]  |
| [[Web Portal Capture\|T1056.003]] | Web Portal Capture | The [IceApple](https://attack.mitre.org/software/S1022) OWA credential logger can monitor for OWA authentication requests and log the credentials.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [IceApple](https://attack.mitre.org/software/S1022) can use HTTP GET to request and pull information from C2.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | The [IceApple](https://attack.mitre.org/software/S1022) Server Variable Dumper module iterates over all server variables present for the current request and returns them to the adversary.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | The [IceApple](https://attack.mitre.org/software/S1022) Directory Lister module can list information about files and directories including creation time, last write time, name, and size.[^1]  |
| [[Domain Account\|T1087.002]] | Domain Account | The [IceApple](https://attack.mitre.org/software/S1022) Active Directory Querier module  can perform authenticated requests against an Active Directory server.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | The [IceApple](https://attack.mitre.org/software/S1022) Result Retriever module can AES encrypt C2 responses.[^1]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [IceApple](https://attack.mitre.org/software/S1022)'s Credential Dumper module can dump encrypted password hashes from SAM registry keys, including `HKLM\SAM\SAM\Domains\Account\F` and `HKLM\SAM\SAM\Domains\Account\Users\*\V`.[^1]  |




## References

[^1]: [CrowdStrike IceApple May 2022](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)


