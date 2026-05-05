---
aliases: 
    - S0018
    
mitre-attack: https://attack.mitre.org/software/S0018
---

## S0018

[Sykipot](https://attack.mitre.org/software/S0018) is malware that has been used in spearphishing campaigns since approximately 2007 against victims primarily in the US. One variant of [Sykipot](https://attack.mitre.org/software/S0018) hijacks smart cards on victims. [^3]  The group using this malware has also been referred to as Sykipot. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Sykipot](https://attack.mitre.org/software/S0018) may use `net start` to display running services.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Sykipot](https://attack.mitre.org/software/S0018) uses SSL for encrypting C2 communications.[^2]  |
| [[Multi-Factor Authentication Interception\|T1111]] | Multi-Factor Authentication Interception | [Sykipot](https://attack.mitre.org/software/S0018) is known to contain functionality that enables targeting of smart card technologies to proxy authentication for connections to restricted network resources using detected hardware tokens.[^3]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Sykipot](https://attack.mitre.org/software/S0018) may use `net group "domain admins" /domain` to display accounts in the "domain admins" permissions group and `net localgroup "administrators"` to list local system administrator group membership.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Sykipot](https://attack.mitre.org/software/S0018) may gather a list of running processes by running `tasklist /v`.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Sykipot](https://attack.mitre.org/software/S0018) contains keylogging functionality to steal passwords.[^3]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Sykipot](https://attack.mitre.org/software/S0018) may use `net view /domain` to display hostnames of available systems on a network.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Sykipot](https://attack.mitre.org/software/S0018) may use `netstat -ano` to display active network connections.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Sykipot](https://attack.mitre.org/software/S0018) may use `ipconfig /all` to gather system network configuration details.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Sykipot](https://attack.mitre.org/software/S0018) has been known to establish persistence by adding programs to the Run Registry key.[^2]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Sykipot](https://attack.mitre.org/software/S0018) injects itself into running instances of outlook.exe, iexplore.exe, or firefox.exe.[^1]  |




## References

[^1]: [AlienVault Sykipot 2011](https://www.alienvault.com/open-threat-exchange/blog/another-sykipot-sample-likely-targeting-us-federal-agencies)


[^2]: [Blasco 2013](http://www.alienvault.com/open-threat-exchange/blog/new-sykipot-developments)


[^3]: [Alienvault Sykipot DOD Smart Cards](https://www.alienvault.com/open-threat-exchange/blog/sykipot-variant-hijacks-dod-and-windows-smart-cards)


