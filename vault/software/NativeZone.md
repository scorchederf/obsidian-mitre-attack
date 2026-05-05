---
aliases: 
    - S0637
    
mitre-attack: https://attack.mitre.org/software/S0637
---

## S0637

[NativeZone](https://attack.mitre.org/software/S0637) is the name given collectively to disposable custom [Cobalt Strike](https://attack.mitre.org/software/S0154) loaders used by [APT29](https://attack.mitre.org/groups/G0016) since at least 2021.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Malicious File\|T1204.002]] | Malicious File | [NativeZone](https://attack.mitre.org/software/S0637) can display an RTF document to the user  to enable execution of  [Cobalt Strike](https://attack.mitre.org/software/S0154) stage shellcode.[^1]  |
| [[System Checks\|T1497.001]] | System Checks | [NativeZone](https://attack.mitre.org/software/S0637) has checked if Vmware or VirtualBox VM is running on a compromised host.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [NativeZone](https://attack.mitre.org/software/S0637) has used rundll32 to execute a malicious DLL.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [NativeZone](https://attack.mitre.org/software/S0637) can decrypt and decode embedded  [Cobalt Strike](https://attack.mitre.org/software/S0154) beacon stage shellcode.[^1]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [NativeZone](https://attack.mitre.org/software/S0637) can check for the presence of KM.EkeyAlmaz1C.dll and will halt execution unless it is in the same directory as the rest of the malware's components.[^1] [^2]  |
| [[Masquerading\|T1036]] | Masquerading | [NativeZone](https://attack.mitre.org/software/S0637) has, upon execution, displayed a message box that appears to be related to a Ukrainian electronic document management system.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)


[^2]: [SentinelOne NobleBaron June 2021](https://labs.sentinelone.com/noblebaron-new-poisoned-installers-could-be-used-in-supply-chain-attacks/)


