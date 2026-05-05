---
aliases: 
    - S0370
    
mitre-attack: https://attack.mitre.org/software/S0370
---

## S0370

[SamSam](https://attack.mitre.org/software/S0370) is ransomware that appeared in early 2016. Unlike some ransomware, its variants have required operators to manually interact with the malware to execute some of its core components.[^2] [^4] [^1] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File Deletion\|T1070.004]] | File Deletion | [SamSam](https://attack.mitre.org/software/S0370) has been seen deleting its own files and payloads to make analysis of the attack more difficult.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [SamSam](https://attack.mitre.org/software/S0370) has been seen using AES or DES to encrypt payloads and payload components.[^1] [^4]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [SamSam](https://attack.mitre.org/software/S0370) uses custom batch scripts to execute some of its components.[^1]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [SamSam](https://attack.mitre.org/software/S0370) has used garbage code to pad some of its malware components.[^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [SamSam](https://attack.mitre.org/software/S0370) encrypts victim files using RSA-2048 encryption and demands a ransom be paid in Bitcoin to decrypt those files.[^1]  |




## References

[^1]: [Sophos SamSam Apr 2018](https://www.sophos.com/en-us/medialibrary/PDFs/technical-papers/SamSam-ransomware-chooses-Its-targets-carefully-wpna.pdf)


[^2]: [US-CERT SamSam 2018](https://www.us-cert.gov/ncas/alerts/AA18-337A)


[^3]: [Symantec SamSam Oct 2018](https://www.symantec.com/blogs/threat-intelligence/samsam-targeted-ransomware-attacks)


[^4]: [Talos SamSam Jan 2018](https://blog.talosintelligence.com/2018/01/samsam-evolution-continues-netting-over.html)


[^5]: Samas


