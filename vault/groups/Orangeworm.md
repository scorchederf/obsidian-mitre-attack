---
aliases: 
    - Orangeworm
mitre-attack: https://attack.mitre.org/groups/G0071
---

## G0071

[Orangeworm](https://attack.mitre.org/groups/G0071) is a group that has targeted organizations in the healthcare sector in the United States, Europe, and Asia since at least 2015, likely for the purpose of corporate espionage.[^4]  Reverse engineering of [Kwampirs](https://attack.mitre.org/software/S0236), directly associated with [Orangeworm](https://attack.mitre.org/groups/G0071) activity, indicates significant functional and development overlaps with [Shamoon](https://attack.mitre.org/software/S0140).[^3] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Orangeworm](https://attack.mitre.org/groups/G0071) has used HTTP for C2.[^1]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Orangeworm](https://attack.mitre.org/groups/G0071) has copied its backdoor across open network shares, including ADMIN$, C$WINDOWS, D$WINDOWS, and E$WINDOWS.[^4]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^4]  |
| [[ipconfig\|S0100]] | ipconfig | [^4]  |
| [[Arp\|S0099]] | Arp | [^4]  |
| [[netstat\|S0104]] | netstat | [^4]  |
| [[Systeminfo\|S0096]] | Systeminfo | [^4]  |
| [[cmd\|S0106]] | cmd | [^4]  |
| [[route\|S0103]] | route | [^4]  |
| [[Kwampirs\|S0236]] | Kwampirs | [^4]  |



## References

[^1]: [Symantec Orangeworm IOCs April 2018](https://symantec-enterprise-blogs.security.com/sites/default/files/2018-04/Orangeworm%20IOCs.pdf)


[^2]: Orangeworm


[^3]: [Cylera Kwampirs 2022](https://resources.cylera.com/hubfs/Cylera%20Labs/Cylera%20Labs%20Kwampirs%20Shamoon%20Technical%20Report.pdf)


[^4]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)


