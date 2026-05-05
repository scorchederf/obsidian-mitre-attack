---
aliases: 
    - S0562
    
mitre-attack: https://attack.mitre.org/software/S0562
---

## S0562

[SUNSPOT](https://attack.mitre.org/software/S0562) is an implant that injected the [SUNBURST](https://attack.mitre.org/software/S0559) backdoor into the SolarWinds Orion software update framework. It was used by [APT29](https://attack.mitre.org/groups/G0016) since at least February 2020.[^3]  

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [SUNSPOT](https://attack.mitre.org/software/S0562) monitored running processes for instances of `MsBuild.exe` by hashing the name of each running process and comparing it to the corresponding value `0x53D525`. It also extracted command-line arguments and individual arguments from the running `MsBuild.exe` process to identify the directory path of the Orion software Visual Studio solution.[^3]  |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [SUNSPOT](https://attack.mitre.org/software/S0562) modified its security token to grants itself debugging privileges by adding `SeDebugPrivilege`.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | Following the successful injection of [SUNBURST](https://attack.mitre.org/software/S0559), [SUNSPOT](https://attack.mitre.org/software/S0562) deleted a temporary file it created named `InventoryManager.bk` after restoring the original SolarWinds Orion source code to the software library.[^3]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [SUNSPOT](https://attack.mitre.org/software/S0562) encrypted log entries it collected with the stream cipher RC4 using a hard-coded key. It also uses AES128-CBC encrypted blobs for [SUNBURST](https://attack.mitre.org/software/S0559) source code and data extracted from the SolarWinds Orion <MsBuild.exe` process.[^3]  |
| [[Stored Data Manipulation\|T1565.001]] | Stored Data Manipulation | [SUNSPOT](https://attack.mitre.org/software/S0562) created a copy of the SolarWinds Orion software source file with a `.bk` extension to backup the original content, wrote [SUNBURST](https://attack.mitre.org/software/S0559) using the same filename but with a `.tmp` extension, and then moved [SUNBURST](https://attack.mitre.org/software/S0559) using `MoveFileEx` to the original filename with a `.cs` extension so it could be compiled within Orion software.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [SUNSPOT](https://attack.mitre.org/software/S0562) enumerated the Orion software Visual Studio solution directory path.[^3]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [SUNSPOT](https://attack.mitre.org/software/S0562) only replaces SolarWinds Orion source code if the MD5 checksums of both the original source code file and backdoored replacement source code match hardcoded values.[^3]   |
| [[Compromise Software Supply Chain\|T1195.002]] | Compromise Software Supply Chain | [SUNSPOT](https://attack.mitre.org/software/S0562) malware was designed and used to insert [SUNBURST](https://attack.mitre.org/software/S0559) into software builds of the SolarWinds Orion IT management product.[^3]  |
| [[Native API\|T1106]] | Native API | [SUNSPOT](https://attack.mitre.org/software/S0562) used Windows API functions such as `MoveFileEx` and `NtQueryInformationProcess` as part of the [SUNBURST](https://attack.mitre.org/software/S0559) injection process.[^3]   |
| [[Mutual Exclusion\|T1480.002]] | Mutual Exclusion | [SUNSPOT](https://attack.mitre.org/software/S0562) creates a mutex using the hard-coded value ` {12d61a41-4b74-7610-a4d8-3028d2f56395}` to ensure that only one instance of itself is running.[^3]   |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [SUNSPOT](https://attack.mitre.org/software/S0562) decrypts [SUNBURST](https://attack.mitre.org/software/S0559), which was stored in AES128-CBC encrypted blobs.[^3]    |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [SUNSPOT](https://attack.mitre.org/software/S0562) was identified on disk with a filename of `taskhostsvc.exe` and it created an encrypted log file at `C:\Windows\Temp\vmware-vmdmp.log`.[^3]   |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: SUNSPOT


[^2]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)


[^3]: [CrowdStrike SUNSPOT Implant January 2021](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)


