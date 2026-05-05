---
aliases: 
    - S0695
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0695-Donut
---

## Description

[[kb/mitre/attack/software/S0695-Donut\|Donut]] is an open source framework used to generate position-independent shellcode.[^2] [^3]  [[kb/mitre/attack/software/S0695-Donut\|Donut]] generated code has been used by multiple threat actors to inject and load malicious payloads into memory.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1027.002-Software_Packing\|T1027.002]] | Software Packing | [[kb/mitre/attack/software/S0695-Donut\|Donut]] can generate packed code modules.[^2] 	 |
| [[kb/mitre/attack/techniques/T1027.013-Encrypted_Encoded_File\|T1027.013]] | Encrypted／Encoded File | [[kb/mitre/attack/software/S0695-Donut\|Donut]] can generate encrypted, compressed/encoded, or otherwise obfuscated code modules.[^2]  |
| [[kb/mitre/attack/techniques/T1027.015-Compression\|T1027.015]] | Compression | [[kb/mitre/attack/software/S0695-Donut\|Donut]] can generate encrypted, compressed/encoded, or otherwise obfuscated code modules.[^2]  |
| [[kb/mitre/attack/techniques/T1055-Process_Injection\|T1055]] | Process Injection | [[kb/mitre/attack/software/S0695-Donut\|Donut]] includes a subproject `DonutTest` to inject shellcode into a target process.[^2] 	 |
| [[kb/mitre/attack/techniques/T1057-Process_Discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S0695-Donut\|Donut]] includes subprojects that enumerate and identify information about [[kb/mitre/attack/techniques/T1055-Process_Injection\|Process Injection]] candidates.[^2] 	 |
| [[kb/mitre/attack/techniques/T1059-Command_and_Scripting_Interpreter\|T1059]] | Command and Scripting Interpreter | [[kb/mitre/attack/software/S0695-Donut\|Donut]] can generate shellcode outputs that execute via Ruby.[^2] 	 |
| [[kb/mitre/attack/techniques/T1059.001-PowerShell\|T1059.001]] | PowerShell | [[kb/mitre/attack/software/S0695-Donut\|Donut]] can generate shellcode outputs that execute via PowerShell.[^2] 	 |
| [[kb/mitre/attack/techniques/T1059.005-Visual_Basic\|T1059.005]] | Visual Basic | [[kb/mitre/attack/software/S0695-Donut\|Donut]] can generate shellcode outputs that execute via VBScript.[^2] 	 |
| [[kb/mitre/attack/techniques/T1059.006-Python\|T1059.006]] | Python | [[kb/mitre/attack/software/S0695-Donut\|Donut]] can generate shellcode outputs that execute via Python.[^2] 	 |
| [[kb/mitre/attack/techniques/T1059.007-JavaScript\|T1059.007]] | JavaScript | [[kb/mitre/attack/software/S0695-Donut\|Donut]] can generate shellcode outputs that execute via JavaScript or JScript.[^2] 	 |
| [[kb/mitre/attack/techniques/T1070-Indicator_Removal\|T1070]] | Indicator Removal | [[kb/mitre/attack/software/S0695-Donut\|Donut]] can erase file references to payloads in-memory after being reflectively loaded and executed.[^2]  |
| [[kb/mitre/attack/techniques/T1071.001-Web_Protocols\|T1071.001]] | Web Protocols | [[kb/mitre/attack/software/S0695-Donut\|Donut]] can use HTTP to download previously staged shellcode payloads.[^2]  |
| [[kb/mitre/attack/techniques/T1105-Ingress_Tool_Transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0695-Donut\|Donut]] can download and execute previously staged shellcode payloads.[^2]  |
| [[kb/mitre/attack/techniques/T1106-Native_API\|T1106]] | Native API | [[kb/mitre/attack/software/S0695-Donut\|Donut]] code modules use various API functions to load and inject code.[^2] 	 |
| [[kb/mitre/attack/techniques/T1620-Reflective_Code_Loading\|T1620]] | Reflective Code Loading | [[kb/mitre/attack/software/S0695-Donut\|Donut]] can generate code modules that enable in-memory execution of VBScript, JScript, EXE, DLL, and dotNET payloads.[^2]  |
| [[kb/mitre/attack/techniques/T1685-Disable_or_Modify_Tools\|T1685]] | Disable or Modify Tools | [[kb/mitre/attack/software/S0695-Donut\|Donut]] can patch Antimalware Scan Interface (AMSI), Windows Lockdown Policy (WLDP), as well as exit-related [[kb/mitre/attack/techniques/T1106-Native_API\|Native API]] functions to avoid process termination.[^2] 	 |





> [!info]- References
> [^1]: [NCC Group WastedLocker June 2020](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)

> [^2]: [Donut Github](https://github.com/TheWover/donut)

> [^3]: [Introducing Donut](https://thewover.github.io/Introducing-Donut/)


