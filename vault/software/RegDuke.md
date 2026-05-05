---
aliases: 
    - S0511
    
mitre-attack: https://attack.mitre.org/software/S0511
---

## S0511

[RegDuke](https://attack.mitre.org/software/S0511) is a first stage implant written in .NET and used by [APT29](https://attack.mitre.org/groups/G0016) since at least 2017. [RegDuke](https://attack.mitre.org/software/S0511) has been used to control a compromised machine when control of other implants on the machine was lost.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [RegDuke](https://attack.mitre.org/software/S0511) can download files from C2.[^1]  |
| [[Steganography\|T1027.003]] | Steganography | [RegDuke](https://attack.mitre.org/software/S0511) can hide data in images, including use of the Least Significant Bit (LSB).[^1]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [RegDuke](https://attack.mitre.org/software/S0511) can persist using a WMI consumer that is launched every time a process named WINWORD.EXE is started.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [RegDuke](https://attack.mitre.org/software/S0511) can extract and execute PowerShell scripts from C2 communications.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [RegDuke](https://attack.mitre.org/software/S0511) can create seemingly legitimate Registry key to store its encryption key.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [RegDuke](https://attack.mitre.org/software/S0511) can decrypt strings with a key either stored in the Registry or hardcoded in the code.[^1]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [RegDuke](https://attack.mitre.org/software/S0511) can store its encryption key in the Registry.[^1]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [RegDuke](https://attack.mitre.org/software/S0511) can use Dropbox as its C2 server.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [RegDuke](https://attack.mitre.org/software/S0511) can use control-flow flattening or the commercially available .NET Reactor for obfuscation.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)


[^2]: [Secureworks IRON HEMLOCK Profile](http://www.secureworks.com/research/threat-profiles/iron-hemlock)


