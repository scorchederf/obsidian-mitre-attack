---
aliases: 
    - S0258
    
mitre-attack: https://attack.mitre.org/software/S0258
---

## S0258

[RGDoor](https://attack.mitre.org/software/S0258) is a malicious Internet Information Services (IIS) backdoor developed in the C++ language. [RGDoor](https://attack.mitre.org/software/S0258) has been seen deployed on webservers belonging to the Middle East government organizations. [RGDoor](https://attack.mitre.org/software/S0258) provides backdoor access to compromised IIS servers. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[IIS Components\|T1505.004]] | IIS Components | [RGDoor](https://attack.mitre.org/software/S0258) establishes persistence on webservers as an IIS module.[^2] [^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [RGDoor](https://attack.mitre.org/software/S0258) uses cmd.exe to execute commands on the victim’s machine.[^2]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [RGDoor](https://attack.mitre.org/software/S0258) encrypts files with XOR before sending them back to the C2 server.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [RGDoor](https://attack.mitre.org/software/S0258) uses HTTP for C2 communications.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [RGDoor](https://attack.mitre.org/software/S0258) executes the `whoami` on the victim’s machine.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [RGDoor](https://attack.mitre.org/software/S0258) decodes Base64 strings and decrypts strings using a custom XOR algorithm.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [RGDoor](https://attack.mitre.org/software/S0258) uploads and downloads files to and from the victim’s machine.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[OilRig\|G0049]] | OilRig |



## References

[^1]: [ESET IIS Malware 2021](https://i.blackhat.com/USA21/Wednesday-Handouts/us-21-Anatomy-Of-Native-Iis-Malware-wp.pdf)


[^2]: [Unit 42 RGDoor Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-oilrig-uses-rgdoor-iis-backdoor-targets-middle-east/)


[^3]: RGDoor


