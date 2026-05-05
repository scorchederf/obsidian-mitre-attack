---
aliases: 
    - S0177
    
mitre-attack: https://attack.mitre.org/software/S0177
---

## S0177

[Power Loader](https://attack.mitre.org/software/S0177) is modular code sold in the cybercrime market used as a downloader in malware families such as Carberp, Redyms and Gapz. [^2]  [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Extra Window Memory Injection\|T1055.011]] | Extra Window Memory Injection | [Power Loader](https://attack.mitre.org/software/S0177) overwrites Explorer’s Shell_TrayWnd extra window memory to redirect execution to a NTDLL function that is abused to assemble and execute a return-oriented programming (ROP) chain and create a malicious thread within Explorer.exe.[^2] [^1]  |




## References

[^1]: [WeLiveSecurity Gapz and Redyms Mar 2013](https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/)


[^2]: [MalwareTech Power Loader Aug 2013](https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html)


