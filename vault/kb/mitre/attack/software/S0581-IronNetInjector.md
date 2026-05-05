---
aliases: 
    - S0581
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0581-IronNetInjector
---

## Description

[[kb/mitre/attack/software/S0581-IronNetInjector\|IronNetInjector]] is a Turla toolchain that utilizes scripts from the open-source IronPython implementation of Python with a .NET injector to drop one or more payloads including ComRAT.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1027.013-Encrypted_Encoded_File\|T1027.013]] | Encrypted／Encoded File | [[kb/mitre/attack/software/S0581-IronNetInjector\|IronNetInjector]] can obfuscate variable names, encrypt strings, as well as base64 encode and Rijndael encrypt payloads.[^1]  |
| [[kb/mitre/attack/techniques/T1036.004-Masquerade_Task_or_Service\|T1036.004]] | Masquerade Task or Service | [[kb/mitre/attack/software/S0581-IronNetInjector\|IronNetInjector]] has been disguised as a legitimate service using the name PythonUpdateSrvc.[^1]  |
| [[kb/mitre/attack/techniques/T1053.005-Scheduled_Task\|T1053.005]] | Scheduled Task | [[kb/mitre/attack/software/S0581-IronNetInjector\|IronNetInjector]] has used a task XML file named `mssch.xml` to run an IronPython script when a user logs in or when specific system events are created.[^1]  |
| [[kb/mitre/attack/techniques/T1055-Process_Injection\|T1055]] | Process Injection | [[kb/mitre/attack/software/S0581-IronNetInjector\|IronNetInjector]] can use an IronPython scripts to load a .NET injector to inject a payload into its own or a remote process.[^1]  |
| [[kb/mitre/attack/techniques/T1055.001-Dynamic-link_Library_Injection\|T1055.001]] | Dynamic-link Library Injection | [[kb/mitre/attack/software/S0581-IronNetInjector\|IronNetInjector]] has the ability to inject a DLL into running processes, including the [[kb/mitre/attack/software/S0581-IronNetInjector\|IronNetInjector]] DLL into explorer.exe.[^1]  |
| [[kb/mitre/attack/techniques/T1057-Process_Discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S0581-IronNetInjector\|IronNetInjector]] can identify processes via C# methods such as `GetProcessesByName` and running [[kb/mitre/attack/software/S0057-Tasklist\|Tasklist]] with the Python `os.popen` function.[^1]  |
| [[kb/mitre/attack/techniques/T1059.006-Python\|T1059.006]] | Python | [[kb/mitre/attack/software/S0581-IronNetInjector\|IronNetInjector]] can use IronPython scripts to load payloads with the help of a .NET injector.[^1]  |
| [[kb/mitre/attack/techniques/T1140-Deobfuscate_Decode_Files_or_Information\|T1140]] | Deobfuscate／Decode Files or Information | [[kb/mitre/attack/software/S0581-IronNetInjector\|IronNetInjector]] has the ability to decrypt embedded .NET and PE payloads.[^1]  |





> [!info]- References
> [^1]: [Unit 42 IronNetInjector February 2021 ](https://unit42.paloaltonetworks.com/ironnetinjector/)


