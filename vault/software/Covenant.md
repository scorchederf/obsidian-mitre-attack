---
aliases: 
    - S1155
    
mitre-attack: https://attack.mitre.org/software/S1155
---

## S1155

[Covenant](https://attack.mitre.org/software/S1155) is a multi-platform command and control framework written in .NET. While designed for penetration testing and security research, the tool has also been used by threat actors such as [HAFNIUM](https://attack.mitre.org/groups/G0125) during operations. [Covenant](https://attack.mitre.org/software/S1155) functions through a central listener managing multiple deployed "Grunts" that communicate back to the controller.[^2] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[PowerShell\|T1059.001]] | PowerShell | [Covenant](https://attack.mitre.org/software/S1155) can create PowerShell-based launchers for Grunt installation.[^2]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [Covenant](https://attack.mitre.org/software/S1155) listeners and controllers can be configured to use non-standard ports.[^2]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Covenant](https://attack.mitre.org/software/S1155) can utilize WMI to install new Grunt listeners through XSL files or command one-liners.[^2]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Covenant](https://attack.mitre.org/software/S1155) can create SCT files for installation via `Regsvr32` to deploy new Grunt listeners.[^2]  |
| [[InstallUtil\|T1218.004]] | InstallUtil | [Covenant](https://attack.mitre.org/software/S1155) can create launchers via an InstallUtil XML file to install new Grunt listeners.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Covenant](https://attack.mitre.org/software/S1155) implants can gather basic information on infected systems.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Covenant](https://attack.mitre.org/software/S1155) provides access to a Command Shell in Windows environments for follow-on command execution and tasking.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Covenant](https://attack.mitre.org/software/S1155) can establish command and control via HTTP.[^2]  |
| [[Mshta\|T1218.005]] | Mshta | [Covenant](https://attack.mitre.org/software/S1155) can create HTA files to install Grunt listeners.[^2]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Covenant](https://attack.mitre.org/software/S1155) can utilize SSL to encrypt command and control traffic.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[HAFNIUM\|G0125]] | HAFNIUM |



## References

[^1]: [Microsoft Silk Typhoon MAR 2025](https://www.microsoft.com/en-us/security/blog/2025/03/05/silk-typhoon-targeting-it-supply-chain/)


[^2]: [Github Covenant](https://github.com/cobbr/Covenant)


[^3]: [Microsoft HAFNIUM March 2020](https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/)


