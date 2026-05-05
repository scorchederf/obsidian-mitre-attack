---
aliases: 
    - S0167
    
mitre-attack: https://attack.mitre.org/software/S0167
---

## S0167

[Matryoshka](https://attack.mitre.org/software/S0167) is a malware framework used by [CopyKittens](https://attack.mitre.org/groups/G0052) that consists of a dropper, loader, and RAT. It has multiple versions; v1 was seen in the wild from July 2016 until January 2017. v2 has fewer commands and other minor differences. [^3]  [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Keylogging\|T1056.001]] | Keylogging | [Matryoshka](https://attack.mitre.org/software/S0167) is capable of keylogging.[^3] [^1]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [Matryoshka](https://attack.mitre.org/software/S0167) is capable of providing Meterpreter shell access.[^3]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Matryoshka](https://attack.mitre.org/software/S0167) can establish persistence by adding Registry Run keys.[^3] [^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Matryoshka](https://attack.mitre.org/software/S0167) uses reflective DLL injection to inject the malicious library and execute the RAT.[^1]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [Matryoshka](https://attack.mitre.org/software/S0167) is capable of stealing Outlook passwords.[^3] [^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Matryoshka](https://attack.mitre.org/software/S0167) obfuscates API function names using a substitute cipher combined with Base64 encoding.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Matryoshka](https://attack.mitre.org/software/S0167) is capable of performing screen captures.[^3] [^1]  |
| [[DNS\|T1071.004]] | DNS | [Matryoshka](https://attack.mitre.org/software/S0167) uses DNS for C2.[^3] [^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Matryoshka](https://attack.mitre.org/software/S0167) uses rundll32.exe in a Registry Run key value for execution as part of its persistence mechanism.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Matryoshka](https://attack.mitre.org/software/S0167) can establish persistence by adding a Scheduled Task named "Microsoft Boost Kernel Optimization".[^3] [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[CopyKittens\|G0052]] | CopyKittens |



## References

[^1]: [CopyKittens Nov 2015](https://cdn2.hubspot.net/hubfs/1903456/Whitepapers/CopyKittens.pdf)


[^2]: Matryoshka


[^3]: [ClearSky Wilted Tulip July 2017](http://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf)


