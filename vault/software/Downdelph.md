---
aliases: 
    - S0134
    
mitre-attack: https://attack.mitre.org/software/S0134
---

## S0134

[Downdelph](https://attack.mitre.org/software/S0134) is a first-stage downloader written in Delphi that has been used by [APT28](https://attack.mitre.org/groups/G0007) in rare instances between 2013 and 2015. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Junk Data\|T1001.001]] | Junk Data | [Downdelph](https://attack.mitre.org/software/S0134) inserts pseudo-random characters between each original character during encoding of C2 network requests, making it difficult to write signatures on them.[^1]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Downdelph](https://attack.mitre.org/software/S0134) bypasses UAC to escalate privileges by using a custom “RedirectEXE” shim database.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Downdelph](https://attack.mitre.org/software/S0134) uses RC4 to encrypt C2 responses.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | After downloading its main config file, [Downdelph](https://attack.mitre.org/software/S0134) downloads multiple payloads from C2 servers.[^1]  |
| [[DLL\|T1574.001]] | DLL | [Downdelph](https://attack.mitre.org/software/S0134) uses search order hijacking of the Windows executable sysprep.exe to escalate privileges.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT28\|G0007]] | APT28 |



## References

[^1]: [ESET Sednit Part 3](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part3.pdf)


[^2]: [Secureworks IRON TWILIGHT Active Measures March 2017](https://www.secureworks.com/research/iron-twilight-supports-active-measures)


