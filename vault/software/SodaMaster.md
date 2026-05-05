---
aliases: 
    - S0627
    
mitre-attack: https://attack.mitre.org/software/S0627
---

## S0627

[SodaMaster](https://attack.mitre.org/software/S0627) is a fileless malware used by [menuPass](https://attack.mitre.org/groups/G0045) to download and execute payloads since at least 2020.[^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SodaMaster](https://attack.mitre.org/software/S0627) has the ability to download additional payloads from C2 to the targeted system.[^4]  |
| [[Native API\|T1106]] | Native API | [SodaMaster](https://attack.mitre.org/software/S0627) can use `RegOpenKeyW` to access the Registry.[^4]  |
| [[System Checks\|T1497.001]] | System Checks | [SodaMaster](https://attack.mitre.org/software/S0627) can check for the presence of the Registry key `HKEY_CLASSES_ROOT\\Applications\\VMwareHostOpen.exe` before proceeding to its main functionality.[^4] 	  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [SodaMaster](https://attack.mitre.org/software/S0627) can use a hardcoded RSA key to encrypt some of its C2 traffic.[^4]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [SodaMaster](https://attack.mitre.org/software/S0627) has the ability to put itself to "sleep" for a specified time.[^4]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [SodaMaster](https://attack.mitre.org/software/S0627) can use "stackstrings" for obfuscation.[^4]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [SodaMaster](https://attack.mitre.org/software/S0627) can identify the username on a compromised host.[^4]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SodaMaster](https://attack.mitre.org/software/S0627) can enumerate the host name and OS version on a target system.[^4]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [SodaMaster](https://attack.mitre.org/software/S0627) can use RC4 to encrypt C2 communications.[^4]  |
| [[Process Discovery\|T1057]] | Process Discovery | [SodaMaster](https://attack.mitre.org/software/S0627) can search a list of running processes.[^4]  |
| [[Query Registry\|T1012]] | Query Registry | [SodaMaster](https://attack.mitre.org/software/S0627) has the ability to query the Registry to detect a key specific to VMware.[^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[menuPass\|G0045]] | menuPass |



## References

[^1]: DARKTOWN


[^2]: dfls


[^3]: DelfsCake


[^4]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)


