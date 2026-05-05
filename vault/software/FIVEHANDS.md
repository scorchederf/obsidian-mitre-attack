---
aliases: 
    - S0618
    
mitre-attack: https://attack.mitre.org/software/S0618
---

## S0618

[FIVEHANDS](https://attack.mitre.org/software/S0618) is a customized version of [DEATHRANSOM](https://attack.mitre.org/software/S0616) ransomware written in C++. [FIVEHANDS](https://attack.mitre.org/software/S0618) has been used since at least 2021, including in Ransomware-as-a-Service (RaaS) campaigns, sometimes along with [SombRAT](https://attack.mitre.org/software/S0615).[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [FIVEHANDS](https://attack.mitre.org/software/S0618) can use WMI to delete files on a  target machine.[^2] [^3]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [FIVEHANDS](https://attack.mitre.org/software/S0618) can receive a command line argument to limit file encryption to specified directories.[^2] [^1]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [FIVEHANDS](https://attack.mitre.org/software/S0618) can enumerate network shares and mounted drives on a network.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [FIVEHANDS](https://attack.mitre.org/software/S0618) has the ability to enumerate files on a compromised host in order to encrypt files with specific extensions.[^3] [^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [FIVEHANDS](https://attack.mitre.org/software/S0618) can use an embedded NTRU public key to encrypt data for ransom.[^2] [^3] [^1]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [FIVEHANDS](https://attack.mitre.org/software/S0618) has the ability to delete volume shadow copies on compromised hosts.[^2] [^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [FIVEHANDS](https://attack.mitre.org/software/S0618) has the ability to decrypt its payload prior to execution.[^2] [^3] [^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | The [FIVEHANDS](https://attack.mitre.org/software/S0618) payload is encrypted with AES-128.[^2] [^3] [^1]  |




## References

[^1]: [NCC Group Fivehands June 2021](https://research.nccgroup.com/2021/06/15/handy-guide-to-a-new-fivehands-ransomware-variant/)


[^2]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)


[^3]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)


