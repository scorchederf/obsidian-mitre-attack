---
aliases: 
    - S0695
    
mitre-attack: https://attack.mitre.org/software/S0695
---

## S0695

[Donut](https://attack.mitre.org/software/S0695) is an open source framework used to generate position-independent shellcode.[^2] [^1]  [Donut](https://attack.mitre.org/software/S0695) generated code has been used by multiple threat actors to inject and load malicious payloads into memory.[^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Indicator Removal\|T1070]] | Indicator Removal | [Donut](https://attack.mitre.org/software/S0695) can erase file references to payloads in-memory after being reflectively loaded and executed.[^2]  |
| [[Python\|T1059.006]] | Python | [Donut](https://attack.mitre.org/software/S0695) can generate shellcode outputs that execute via Python.[^2] 	 |
| [[Process Injection\|T1055]] | Process Injection | [Donut](https://attack.mitre.org/software/S0695) includes a subproject `DonutTest` to inject shellcode into a target process.[^2] 	 |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [Donut](https://attack.mitre.org/software/S0695) can generate shellcode outputs that execute via Ruby.[^2] 	 |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Donut](https://attack.mitre.org/software/S0695) can generate shellcode outputs that execute via VBScript.[^2] 	 |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Donut](https://attack.mitre.org/software/S0695) can generate encrypted, compressed/encoded, or otherwise obfuscated code modules.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Donut](https://attack.mitre.org/software/S0695) includes subprojects that enumerate and identify information about [Process Injection](https://attack.mitre.org/techniques/T1055) candidates.[^2] 	 |
| [[Software Packing\|T1027.002]] | Software Packing | [Donut](https://attack.mitre.org/software/S0695) can generate packed code modules.[^2] 	 |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Donut](https://attack.mitre.org/software/S0695) can use HTTP to download previously staged shellcode payloads.[^2]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Donut](https://attack.mitre.org/software/S0695) can generate shellcode outputs that execute via JavaScript or JScript.[^2] 	 |
| [[Native API\|T1106]] | Native API | [Donut](https://attack.mitre.org/software/S0695) code modules use various API functions to load and inject code.[^2] 	 |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [Donut](https://attack.mitre.org/software/S0695) can generate code modules that enable in-memory execution of VBScript, JScript, EXE, DLL, and dotNET payloads.[^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Donut](https://attack.mitre.org/software/S0695) can patch Antimalware Scan Interface (AMSI), Windows Lockdown Policy (WLDP), as well as exit-related [Native API](https://attack.mitre.org/techniques/T1106) functions to avoid process termination.[^2] 	 |
| [[Compression\|T1027.015]] | Compression | [Donut](https://attack.mitre.org/software/S0695) can generate encrypted, compressed/encoded, or otherwise obfuscated code modules.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Donut](https://attack.mitre.org/software/S0695) can generate shellcode outputs that execute via PowerShell.[^2] 	 |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Donut](https://attack.mitre.org/software/S0695) can download and execute previously staged shellcode payloads.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Indrik Spider\|G0119]] | Indrik Spider |



## References

[^1]: [Introducing Donut](https://thewover.github.io/Introducing-Donut/)


[^2]: [Donut Github](https://github.com/TheWover/donut)


[^3]: [NCC Group WastedLocker June 2020](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)


