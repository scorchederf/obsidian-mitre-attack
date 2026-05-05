---
aliases: 
    - S0649
    
mitre-attack: https://attack.mitre.org/software/S0649
---

## S0649

[SMOKEDHAM](https://attack.mitre.org/software/S0649) is a Powershell-based .NET backdoor that was first reported in May 2021; it has been used by at least one ransomware-as-a-service affiliate.[^1] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has encrypted its C2 traffic with RC4.[^3]  |
| [[Hidden Users\|T1564.002]] | Hidden Users | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has modified the Registry to hide created user accounts from the Windows logon screen. [^3]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has encoded its C2 traffic with Base64.[^3]  |
| [[Local Account\|T1136.001]] | Local Account | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has created user accounts.[^3]  |
| [[Modify Registry\|T1112]] | Modify Registry | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has modified registry keys for persistence, to enable credential caching for credential access, and to facilitate lateral movement via RDP.[^3]  |
| [[Additional Local or Domain Groups\|T1098.007]] | Additional Local or Domain Groups | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has added user accounts to local Admin groups.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has used Powershell to download UltraVNC and [ngrok](https://attack.mitre.org/software/S0508) from third-party file sharing sites.[^3]  |
| [[Web Service\|T1102]] | Web Service | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has used Google Drive and Dropbox to host files downloaded by victims via malicious links.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has used the `systeminfo` command on a compromised host.[^3]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has relied upon users clicking on a malicious link delivered through phishing.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has communicated with its C2 servers via HTTPS and HTTP POST requests.[^3]  |
| [[Keylogging\|T1056.001]] | Keylogging | [SMOKEDHAM](https://attack.mitre.org/software/S0649) can continuously capture keystrokes.[^1] [^3]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has used `reg.exe` to create a Registry Run key.[^3]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has used `whoami` commands to identify system owners.[^3]  |
| [[Spearphishing Link\|T1598.003]] | Spearphishing Link | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has been delivered via malicious links in phishing emails.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has exfiltrated data to its C2 server.[^3]  |
| [[Embedded Payloads\|T1027.009]] | Embedded Payloads | The [SMOKEDHAM](https://attack.mitre.org/software/S0649) source code is embedded in the dropper as an encrypted string.[^3]  |
| [[Screen Capture\|T1113]] | Screen Capture | [SMOKEDHAM](https://attack.mitre.org/software/S0649) can capture screenshots of the victim’s desktop.[^1] [^3]  |
| [[PowerShell\|T1059.001]] | PowerShell | [SMOKEDHAM](https://attack.mitre.org/software/S0649) can execute Powershell commands sent from its C2 server.[^3]  |
| [[Local Account\|T1087.001]] | Local Account | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has used `net.exe user` and `net.exe users` to enumerate local accounts on a compromised host.[^3]  |
| [[Domain Fronting\|T1090.004]] | Domain Fronting | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has used a fronted domain to obfuscate its hard-coded C2 server domain.[^3]  |




## References

[^1]: [FireEye Shining A Light on DARKSIDE May 2021](https://www.fireeye.com/blog/threat-research/2021/05/shining-a-light-on-darkside-ransomware-operations.html)


[^2]: SMOKEDHAM


[^3]: [FireEye SMOKEDHAM June 2021](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)


