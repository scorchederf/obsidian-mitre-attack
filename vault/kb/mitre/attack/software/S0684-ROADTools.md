---
aliases: 
    - S0684
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0684-ROADTools
---

## Description

[[kb/mitre/attack/software/S0684-ROADTools\|ROADTools]] is a framework for enumerating Azure Active Directory environments. The tool is written in Python and publicly available on GitHub.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1018-Remote_System_Discovery\|T1018]] | Remote System Discovery | [[kb/mitre/attack/software/S0684-ROADTools\|ROADTools]] can enumerate Azure AD systems and devices.[^2]  |
| [[kb/mitre/attack/techniques/T1069.003-Cloud_Groups\|T1069.003]] | Cloud Groups | [[kb/mitre/attack/software/S0684-ROADTools\|ROADTools]] can enumerate Azure AD groups.[^2] 	 |
| [[kb/mitre/attack/techniques/T1078.004-Cloud_Accounts\|T1078.004]] | Cloud Accounts | [[kb/mitre/attack/software/S0684-ROADTools\|ROADTools]] leverages valid cloud credentials to perform enumeration operations using the internal Azure AD Graph API.[^2] 	 |
| [[kb/mitre/attack/techniques/T1087.004-Cloud_Account\|T1087.004]] | Cloud Account | [[kb/mitre/attack/software/S0684-ROADTools\|ROADTools]] can enumerate Azure AD users.[^2]  |
| [[kb/mitre/attack/techniques/T1119-Automated_Collection\|T1119]] | Automated Collection | [[kb/mitre/attack/software/S0684-ROADTools\|ROADTools]] automatically gathers data from Azure AD environments using the Azure Graph API.[^2]  |
| [[kb/mitre/attack/techniques/T1526-Cloud_Service_Discovery\|T1526]] | Cloud Service Discovery | [[kb/mitre/attack/software/S0684-ROADTools\|ROADTools]] can enumerate Azure AD applications and service principals.[^2] 	 |





> [!info]- References
> [^1]: [ROADtools Github](https://github.com/dirkjanm/ROADtools)

> [^2]: [Roadtools](https://dirkjanm.io/introducing-roadtools-and-roadrecon-azure-ad-exploration-framework/)


