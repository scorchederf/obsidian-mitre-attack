---
aliases: 
    - S0486
    
mitre-attack: https://attack.mitre.org/software/S0486
---

## S0486

[Bonadan](https://attack.mitre.org/software/S0486) is a malicious version of OpenSSH which acts as a custom backdoor. [Bonadan](https://attack.mitre.org/software/S0486) has been active since at least 2018 and combines a new cryptocurrency-mining module with the same credential-stealing module used by the Onderon family of backdoors.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Bonadan](https://attack.mitre.org/software/S0486) can XOR-encrypt C2 communications.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Bonadan](https://attack.mitre.org/software/S0486) has discovered the OS version, CPU model, and RAM size of the system it has been installed on.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Bonadan](https://attack.mitre.org/software/S0486) can find the external IP address of the infected host.[^1]  |
| [[Compute Hijacking\|T1496.001]] | Compute Hijacking | [Bonadan](https://attack.mitre.org/software/S0486) can download an additional module which has a cryptocurrency mining extension.[^1]  |
| [[Compromise Host Software Binary\|T1554]] | Compromise Host Software Binary | [Bonadan](https://attack.mitre.org/software/S0486) has maliciously altered the OpenSSH binary on targeted systems to create a backdoor.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Bonadan](https://attack.mitre.org/software/S0486) can download additional modules from the C2 server.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Bonadan](https://attack.mitre.org/software/S0486) has discovered the username of the user running the backdoor.[^1]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [Bonadan](https://attack.mitre.org/software/S0486) can create bind and reverse shells on the infected system.[^1] 	 |
| [[Process Discovery\|T1057]] | Process Discovery | [Bonadan](https://attack.mitre.org/software/S0486) can use the `ps` command to discover other cryptocurrency miners active on the system.[^1]  |




## References

[^1]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)


