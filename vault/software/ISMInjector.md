---
aliases: 
    - S0189
    
mitre-attack: https://attack.mitre.org/software/S0189
---

## S0189

[ISMInjector](https://attack.mitre.org/software/S0189) is a Trojan used to install another [OilRig](https://attack.mitre.org/groups/G0049) backdoor, ISMAgent. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [ISMInjector](https://attack.mitre.org/software/S0189) uses the `certutil` command to decode a payload file.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [ISMInjector](https://attack.mitre.org/software/S0189) is obfuscated with the off-the-shelf SmartAssembly .NET obfuscator created by red-gate.com.[^2]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [ISMInjector](https://attack.mitre.org/software/S0189) hollows out a newly created process RegASM.exe and injects its payload into the hollowed process.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [ISMInjector](https://attack.mitre.org/software/S0189) creates scheduled tasks to establish persistence.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[OilRig\|G0049]] | OilRig |



## References

[^1]: ISMInjector


[^2]: [OilRig New Delivery Oct 2017](https://researchcenter.paloaltonetworks.com/2017/10/unit42-oilrig-group-steps-attacks-new-delivery-documents-new-injector-trojan/)


