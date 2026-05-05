---
aliases: 
    - S0664
    
mitre-attack: https://attack.mitre.org/software/S0664
---

## S0664

[Pandora](https://attack.mitre.org/software/S0664) is a multistage kernel rootkit with backdoor functionality that has been in use by [Threat Group-3390](https://attack.mitre.org/groups/G0027) since at least 2020.[^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Pandora](https://attack.mitre.org/software/S0664) can load additional drivers and files onto a victim machine.[^3]  |
| [[DLL\|T1574.001]] | DLL | [Pandora](https://attack.mitre.org/software/S0664) can use DLL side-loading to execute malicious payloads.[^3]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Pandora](https://attack.mitre.org/software/S0664) has the ability to encrypt communications with D3DES.[^3]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [Pandora](https://attack.mitre.org/software/S0664) can use CVE-2017-15303 to bypass Windows Driver Signature Enforcement (DSE) protection and load its driver.[^3]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Pandora](https://attack.mitre.org/software/S0664) has the ability to gain system privileges through Windows services.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Pandora](https://attack.mitre.org/software/S0664) can communicate over HTTP.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Pandora](https://attack.mitre.org/software/S0664) can monitor processes on a compromised host.[^3]  |
| [[Traffic Signaling\|T1205]] | Traffic Signaling | [Pandora](https://attack.mitre.org/software/S0664) can identify if incoming HTTP traffic contains a token and if so it will intercept the traffic and process the received command.[^3]  |
| [[Compression\|T1027.015]] | Compression | [Pandora](https://attack.mitre.org/software/S0664) has the ability to compress stings with QuickLZ.[^3]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Pandora](https://attack.mitre.org/software/S0664) has the ability to install itself as a Windows service.[^3]  |
| [[Code Signing Policy Modification\|T1553.006]] | Code Signing Policy Modification | [Pandora](https://attack.mitre.org/software/S0664) can use CVE-2017-15303 to disable Windows Driver Signature Enforcement (DSE) protection and load its driver.[^3]  |
| [[Process Injection\|T1055]] | Process Injection | [Pandora](https://attack.mitre.org/software/S0664) can start and inject code into a new `svchost` process.[^3]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Pandora](https://attack.mitre.org/software/S0664) can write an encrypted token to the Registry to enable processing of remote commands.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Cinnamon Tempest\|G1021]] | Cinnamon Tempest |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 |



## References

[^1]: [Dell SecureWorks BRONZE STARLIGHT Profile](https://www.secureworks.com/research/threat-profiles/bronze-starlight)


[^2]: [Sygnia Emperor Dragonfly October 2022](https://blog.sygnia.co/revealing-emperor-dragonfly-a-chinese-ransomware-group)


[^3]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)


[^4]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^5]: [SecureWorks BRONZE STARLIGHT Ransomware Operations June 2022](https://www.secureworks.com/research/bronze-starlight-ransomware-operations-use-hui-loader)


