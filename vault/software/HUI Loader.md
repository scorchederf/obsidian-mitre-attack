---
aliases: 
    - S1097
    
mitre-attack: https://attack.mitre.org/software/S1097
---

## S1097

[HUI Loader](https://attack.mitre.org/software/S1097) is a custom DLL loader that has been used since at least 2015 by China-based threat groups including [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) and [menuPass](https://attack.mitre.org/groups/G0045) to deploy malware on compromised hosts. [HUI Loader](https://attack.mitre.org/software/S1097) has been observed in campaigns loading [SodaMaster](https://attack.mitre.org/software/S0627), [PlugX](https://attack.mitre.org/software/S0013), [Cobalt Strike](https://attack.mitre.org/software/S0154), [Komplex](https://attack.mitre.org/software/S0162), and several strains of ransomware.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [HUI Loader](https://attack.mitre.org/software/S1097) can decrypt and load files containing malicious payloads.[^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [HUI Loader](https://attack.mitre.org/software/S1097) has the ability to disable Windows Event Tracing for Windows (ETW) and Antimalware Scan Interface (AMSI) functions.[^2]  |
| [[DLL\|T1574.001]] | DLL | [HUI Loader](https://attack.mitre.org/software/S1097) can be deployed to targeted systems via legitimate programs that are vulnerable to DLL search order hijacking.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Cinnamon Tempest\|G1021]] | Cinnamon Tempest |
| [[menuPass\|G0045]] | menuPass |



## References

[^1]: [Dell SecureWorks BRONZE STARLIGHT Profile](https://www.secureworks.com/research/threat-profiles/bronze-starlight)


[^2]: [SecureWorks BRONZE STARLIGHT Ransomware Operations June 2022](https://www.secureworks.com/research/bronze-starlight-ransomware-operations-use-hui-loader)


