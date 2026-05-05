---
aliases: 
    - S0691
    
mitre-attack: https://attack.mitre.org/software/S0691
---

## S0691

[Neoichor](https://attack.mitre.org/software/S0691) is C2 malware used by [Ke3chang](https://attack.mitre.org/groups/G0004) since at least 2019; similar malware families used by the group include Leeson and Numbldea.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [Neoichor](https://attack.mitre.org/software/S0691) can check for Internet connectivity by contacting bing[.]com with the request format `bing[.]com?id=<GetTickCount>`.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Neoichor](https://attack.mitre.org/software/S0691) can download additional files onto a compromised host.[^1]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [Neoichor](https://attack.mitre.org/software/S0691) can identify the system language on a compromised host.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Neoichor](https://attack.mitre.org/software/S0691) can collect the user name from a victim's machine.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Neoichor](https://attack.mitre.org/software/S0691) has the ability to configure browser settings by modifying Registry entries under `HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer`.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Neoichor](https://attack.mitre.org/software/S0691) can upload files from a victim's machine.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Neoichor](https://attack.mitre.org/software/S0691) can gather the IP address from an infected host.[^1]    |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Neoichor](https://attack.mitre.org/software/S0691) can collect the OS version and computer name from a compromised host.[^1]  |
| [[Component Object Model\|T1559.001]] | Component Object Model | [Neoichor](https://attack.mitre.org/software/S0691) can use the Internet Explorer (IE) COM interface to connect and receive commands from C2.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Neoichor](https://attack.mitre.org/software/S0691) can use HTTP for C2 communications.[^1]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [Neoichor](https://attack.mitre.org/software/S0691) can clear the browser history on a compromised host by changing the `ClearBrowsingHistoryOnExit` value to 1 in the `HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\Privacy` Registry key.[^1] <br><br> |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Ke3chang\|G0004]] | Ke3chang |



## References

[^1]: [Microsoft NICKEL December 2021](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)


