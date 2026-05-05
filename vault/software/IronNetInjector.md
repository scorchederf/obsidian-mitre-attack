---
aliases: 
    - S0581
    
mitre-attack: https://attack.mitre.org/software/S0581
---

## S0581

[IronNetInjector](https://attack.mitre.org/software/S0581) is a [Turla](https://attack.mitre.org/groups/G0010) toolchain that utilizes scripts from the open-source IronPython implementation of Python with a .NET injector to drop one or more payloads including [ComRAT](https://attack.mitre.org/software/S0126).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Python\|T1059.006]] | Python | [IronNetInjector](https://attack.mitre.org/software/S0581) can use IronPython scripts to load payloads with the help of a .NET injector.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [IronNetInjector](https://attack.mitre.org/software/S0581) can identify processes via C# methods such as `GetProcessesByName` and running [Tasklist](https://attack.mitre.org/software/S0057) with the Python `os.popen` function.[^1]  |
| [[Process Injection\|T1055]] | Process Injection | [IronNetInjector](https://attack.mitre.org/software/S0581) can use an IronPython scripts to load a .NET injector to inject a payload into its own or a remote process.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [IronNetInjector](https://attack.mitre.org/software/S0581) has been disguised as a legitimate service using the name PythonUpdateSrvc.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [IronNetInjector](https://attack.mitre.org/software/S0581) has used a task XML file named `mssch.xml` to run an IronPython script when a user logs in or when specific system events are created.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [IronNetInjector](https://attack.mitre.org/software/S0581) has the ability to decrypt embedded .NET and PE payloads.[^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [IronNetInjector](https://attack.mitre.org/software/S0581) has the ability to inject a DLL into running processes, including the [IronNetInjector](https://attack.mitre.org/software/S0581) DLL into explorer.exe.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [IronNetInjector](https://attack.mitre.org/software/S0581) can obfuscate variable names, encrypt strings, as well as base64 encode and Rijndael encrypt payloads.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Turla\|G0010]] | Turla |



## References

[^1]: [Unit 42 IronNetInjector February 2021 ](https://unit42.paloaltonetworks.com/ironnetinjector/)


