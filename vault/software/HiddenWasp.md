---
aliases: 
    - S0394
    
mitre-attack: https://attack.mitre.org/software/S0394
---

## S0394

[HiddenWasp](https://attack.mitre.org/software/S0394) is a Linux-based Trojan used to target systems for remote control. It comes in the form of a statically linked ELF binary with stdlibc++.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Local Account\|T1136.001]] | Local Account | [HiddenWasp](https://attack.mitre.org/software/S0394) creates a user account as a means to provide initial persistence to the compromised machine.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [HiddenWasp](https://attack.mitre.org/software/S0394) communicates with a simple network protocol over TCP.[^2]  |
| [[Dynamic Linker Hijacking\|T1574.006]] | Dynamic Linker Hijacking | [HiddenWasp](https://attack.mitre.org/software/S0394) adds itself as a shared object to the LD_PRELOAD environment variable.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [HiddenWasp](https://attack.mitre.org/software/S0394) uses an RC4-like algorithm with an already computed PRGA generated key-stream for network communication.[^2]  |
| [[RC Scripts\|T1037.004]] | RC Scripts | [HiddenWasp](https://attack.mitre.org/software/S0394) installs reboot persistence by adding itself to `/etc/rc.local`.[^2]  |
| [[Rootkit\|T1014]] | Rootkit | [HiddenWasp](https://attack.mitre.org/software/S0394) uses a rootkit to hook and implement functions on the system.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [HiddenWasp](https://attack.mitre.org/software/S0394) uses a script to automate tasks on the victim's machine and to assist in execution.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [HiddenWasp](https://attack.mitre.org/software/S0394) uses a cipher to implement a decoding function.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [HiddenWasp](https://attack.mitre.org/software/S0394) downloads a tar compressed archive from a download server to the system.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [HiddenWasp](https://attack.mitre.org/software/S0394) encrypts its configuration and payload.[^2]  |




## References

[^1]: HiddenWasp


[^2]: [Intezer HiddenWasp Map 2019](https://www.intezer.com/blog-hiddenwasp-malware-targeting-linux-systems/)


