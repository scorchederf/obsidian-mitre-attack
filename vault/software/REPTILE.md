---
aliases: 
    - S1219
    
mitre-attack: https://attack.mitre.org/software/S1219
---

## S1219

[REPTILE](https://attack.mitre.org/software/S1219) is an open-source Linux rootkit with multiple components that provides backdoor access and functionality.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Launch Daemon\|T1543.004]] | Launch Daemon | The [REPTILE](https://attack.mitre.org/software/S1219) launcher can daemonize a process.[^2]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [REPTILE](https://attack.mitre.org/software/S1219) can use TLS over raw TCP for secure C2.[^2] [^1]  |
| [[Port Knocking\|T1205.001]] | Port Knocking | [REPTILE](https://attack.mitre.org/software/S1219) has the ability to control compromised endpoints via port knocking.[^2]  |
| [[Udev Rules\|T1546.017]] | Udev Rules | <br>[REPTILE](https://attack.mitre.org/software/S1219) has used udev for persistence.[^2] <br> |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [REPTILE](https://attack.mitre.org/software/S1219) has the ability to communicate with the kernel-mode component to hide files.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | The [REPTILE](https://attack.mitre.org/software/S1219) launcher component can decrypt kernel module code from a file and load it into memory.[^2]  |
| [[Traffic Signaling\|T1205]] | Traffic Signaling | The [REPTILE](https://attack.mitre.org/software/S1219) reverse shell component can listen for a specialized packet in TCP, UDP, or ICMP for activation.[^2] [^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [REPTILE](https://attack.mitre.org/software/S1219) can deploy components automatically with shell scripts.[^2]  |
| [[Rootkit\|T1014]] | Rootkit | [REPTILE](https://attack.mitre.org/software/S1219) has the ability to hook kernel functions and modify functions data to achieve rootkit functionality such as hiding processes and network connections.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [REPTILE](https://attack.mitre.org/software/S1219) can communicate using TLS over raw TCP.[^2] [^1] <br> |
| [[Kernel Modules and Extensions\|T1547.006]] | Kernel Modules and Extensions | The [REPTILE](https://attack.mitre.org/software/S1219) rootkit is implemented as a loadable kernel module (LKM).[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[UNC3886\|G1048]] | UNC3886 |



## References

[^1]: [Mandiant Fortinet Zero Day](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)


[^2]: [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)


