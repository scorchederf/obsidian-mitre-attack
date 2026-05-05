---
aliases: 
    - S0333
    
mitre-attack: https://attack.mitre.org/software/S0333
---

## S0333

[UBoatRAT](https://attack.mitre.org/software/S0333) is a remote access tool that was identified in May 2017.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [UBoatRAT](https://attack.mitre.org/software/S0333) can start a command shell.[^1]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [UBoatRAT](https://attack.mitre.org/software/S0333) has used GitHub and a public blog service in Hong Kong for C2 communications.[^1]  |
| [[BITS Jobs\|T1197]] | BITS Jobs | [UBoatRAT](https://attack.mitre.org/software/S0333) takes advantage of the /SetNotifyCmdLine option in [BITSAdmin](https://attack.mitre.org/software/S0190) to ensure it stays running on a system to maintain persistence.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [UBoatRAT](https://attack.mitre.org/software/S0333) has used HTTP for C2 communications.[^1]  |
| [[System Checks\|T1497.001]] | System Checks | [UBoatRAT](https://attack.mitre.org/software/S0333) checks for virtualization software such as VMWare, VirtualBox, or QEmu on the compromised machine.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [UBoatRAT](https://attack.mitre.org/software/S0333) can list running processes on the system.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [UBoatRAT](https://attack.mitre.org/software/S0333) encrypts instructions in its C2 network payloads using a simple XOR cipher.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [UBoatRAT](https://attack.mitre.org/software/S0333) can upload and download files to the victim’s machine.[^1]  |




## References

[^1]: [PaloAlto UBoatRAT Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-uboatrat-navigates-east-asia/)


[^2]: UBoatRAT


