---
aliases: 
    - S0672
    
mitre-attack: https://attack.mitre.org/software/S0672
---

## S0672

[Zox](https://attack.mitre.org/software/S0672) is a remote access tool that has been used by [Axiom](https://attack.mitre.org/groups/G0001) since at least 2008.[^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Zox](https://attack.mitre.org/software/S0672) has been encoded with Base64.[^3]  |
| [[Steganography\|T1001.002]] | Steganography | [Zox](https://attack.mitre.org/software/S0672) has used the .PNG file format for C2 communications.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Zox](https://attack.mitre.org/software/S0672) can download files to a compromised machine.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Zox](https://attack.mitre.org/software/S0672) can enumerate files on a compromised host.[^3]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Zox](https://attack.mitre.org/software/S0672) has the ability to use SMB for communication.[^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Zox](https://attack.mitre.org/software/S0672) has the ability to upload files from a targeted system.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Zox](https://attack.mitre.org/software/S0672) has the ability to list processes.[^3]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [Zox](https://attack.mitre.org/software/S0672) has the ability to leverage local and remote exploits to escalate privileges.[^3]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Zox](https://attack.mitre.org/software/S0672) can enumerate attached drives.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Axiom\|G0001]] | Axiom |



## References

[^1]: ZoxRPC


[^2]: ZoxPNG


[^3]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)


[^4]: Gresim


