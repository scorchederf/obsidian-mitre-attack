---
aliases: 
    - S0684
    
mitre-attack: https://attack.mitre.org/software/S0684
---

## S0684

[ROADTools](https://attack.mitre.org/software/S0684) is a framework for enumerating Azure Active Directory environments. The tool is written in Python and publicly available on GitHub.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [ROADTools](https://attack.mitre.org/software/S0684) can enumerate Azure AD systems and devices.[^3]  |
| [[Automated Collection\|T1119]] | Automated Collection | [ROADTools](https://attack.mitre.org/software/S0684) automatically gathers data from Azure AD environments using the Azure Graph API.[^3]  |
| [[Cloud Service Discovery\|T1526]] | Cloud Service Discovery | [ROADTools](https://attack.mitre.org/software/S0684) can enumerate Azure AD applications and service principals.[^3] 	 |
| [[Cloud Account\|T1087.004]] | Cloud Account | [ROADTools](https://attack.mitre.org/software/S0684) can enumerate Azure AD users.[^3]  |
| [[Cloud Groups\|T1069.003]] | Cloud Groups | [ROADTools](https://attack.mitre.org/software/S0684) can enumerate Azure AD groups.[^3] 	 |
| [[Cloud Accounts\|T1078.004]] | Cloud Accounts | [ROADTools](https://attack.mitre.org/software/S0684) leverages valid cloud credentials to perform enumeration operations using the internal Azure AD Graph API.[^3] 	 |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [MSTIC Nobelium Oct 2021](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks/)


[^2]: [ROADtools Github](https://github.com/dirkjanm/ROADtools)


[^3]: [Roadtools](https://dirkjanm.io/introducing-roadtools-and-roadrecon-azure-ad-exploration-framework/)


