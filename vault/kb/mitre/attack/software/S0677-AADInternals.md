---
aliases: 
    - S0677
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0677-AADInternals
---

## Description

[[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] is a PowerShell-based framework for administering, enumerating, and exploiting Azure Active Directory. The tool is publicly available on GitHub.[^4] [^6] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.004-LSA_Secrets\|T1003.004]] | LSA Secrets | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can dump secrets from the Local Security Authority.[^6]  |
| [[kb/mitre/attack/techniques/T1048-Exfiltration_Over_Alternative_Protocol\|T1048]] | Exfiltration Over Alternative Protocol | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can directly download cloud user data such as OneDrive files.[^6]  |
| [[kb/mitre/attack/techniques/T1059.001-PowerShell\|T1059.001]] | PowerShell | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] is written and executed via PowerShell.[^6]  |
| [[kb/mitre/attack/techniques/T1069.003-Cloud_Groups\|T1069.003]] | Cloud Groups | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can enumerate Azure AD groups.[^6]  |
| [[kb/mitre/attack/techniques/T1087.004-Cloud_Account\|T1087.004]] | Cloud Account | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can enumerate Azure AD users.[^6]  |
| [[kb/mitre/attack/techniques/T1098.005-Device_Registration\|T1098.005]] | Device Registration | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can register a device to Azure AD.[^6]  |
| [[kb/mitre/attack/techniques/T1112-Modify_Registry\|T1112]] | Modify Registry | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can modify registry keys as part of setting a new pass-through authentication agent.[^6]  |
| [[kb/mitre/attack/techniques/T1136.003-Cloud_Account\|T1136.003]] | Cloud Account | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can create new Azure AD users.[^6]  |
| [[kb/mitre/attack/techniques/T1484.002-Trust_Modification\|T1484.002]] | Trust Modification | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can create a backdoor by converting a domain to a federated domain which will be able to authenticate any user across the tenant. [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can also modify DesktopSSO information.[^6] [^5]  |
| [[kb/mitre/attack/techniques/T1526-Cloud_Service_Discovery\|T1526]] | Cloud Service Discovery | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can enumerate information about a variety of cloud services, such as Office 365 and Sharepoint instances or OpenID Configurations.[^6]  |
| [[kb/mitre/attack/techniques/T1528-Steal_Application_Access_Token\|T1528]] | Steal Application Access Token | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can steal users’ access tokens via phishing emails containing malicious links.[^6]  |
| [[kb/mitre/attack/techniques/T1530-Data_from_Cloud_Storage\|T1530]] | Data from Cloud Storage | AADInternals can collect files from a user’s OneDrive.[^3]  |
| [[kb/mitre/attack/techniques/T1552.001-Credentials_In_Files\|T1552.001]] | Credentials In Files | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can gather unsecured credentials for Azure AD services, such as Azure AD Connect, from a local machine.[^6]  |
| [[kb/mitre/attack/techniques/T1552.004-Private_Keys\|T1552.004]] | Private Keys | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can gather encryption keys from Azure AD services such as ADSync and Active Directory Federated Services servers.[^6]  |
| [[kb/mitre/attack/techniques/T1556.006-Multi-Factor_Authentication\|T1556.006]] | Multi-Factor Authentication | The [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] `Set-AADIntUserMFA` command can be used to disable MFA for a specified user. |
| [[kb/mitre/attack/techniques/T1556.007-Hybrid_Identity\|T1556.007]] | Hybrid Identity | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can inject a malicious DLL (`PTASpy`) into the `AzureADConnectAuthenticationAgentService` to backdoor Azure AD Pass-Through Authentication.[^2]  |
| [[kb/mitre/attack/techniques/T1558.002-Silver_Ticket\|T1558.002]] | Silver Ticket | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can be used to forge Kerberos tickets using the password hash of the AZUREADSSOACC account.[^6]  |
| [[kb/mitre/attack/techniques/T1566.002-Spearphishing_Link\|T1566.002]] | Spearphishing Link | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can send "consent phishing" emails containing malicious links designed to steal users’ access tokens.[^6]  |
| [[kb/mitre/attack/techniques/T1589.002-Email_Addresses\|T1589.002]] | Email Addresses | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can check for the existence of user email addresses using public Microsoft APIs.[^6] [^7]  |
| [[kb/mitre/attack/techniques/T1590.001-Domain_Properties\|T1590.001]] | Domain Properties | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can gather information about a tenant’s domains using public Microsoft APIs.[^6] [^7]  |
| [[kb/mitre/attack/techniques/T1598.003-Spearphishing_Link\|T1598.003]] | Spearphishing Link | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can send phishing emails containing malicious links designed to collect users’ credentials.[^6]  |
| [[kb/mitre/attack/techniques/T1606.002-SAML_Tokens\|T1606.002]] | SAML Tokens | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can be used to create SAML tokens using the AD Federated Services token signing certificate.[^6]  |
| [[kb/mitre/attack/techniques/T1649-Steal_or_Forge_Authentication_Certificates\|T1649]] | Steal or Forge Authentication Certificates | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can create and export various authentication certificates, including those associated with Azure AD joined/registered devices.[^6]  |
| [[kb/mitre/attack/techniques/T1651-Cloud_Administration_Command\|T1651]] | Cloud Administration Command | [[kb/mitre/attack/software/S0677-AADInternals\|AADInternals]] can execute commands on Azure virtual machines using the VM agent.[^1]  |





> [!info]- References
> [^1]: [AADInternals Root Access to Azure VMs](https://aadinternals.com/post/azurevms/)

> [^2]: [AADInternals Azure AD On-Prem to Cloud](https://o365blog.com/post/on-prem_admin/)

> [^3]: [AADInternals](https://o365blog.com/aadinternals/)

> [^4]: [AADInternals Github](https://github.com/Gerenios/AADInternals)

> [^5]: [Azure AD Federation Vulnerability](https://o365blog.com/post/federation-vulnerability/)

> [^6]: [AADInternals Documentation](https://o365blog.com/aadinternals)

> [^7]: [Azure AD Recon](https://o365blog.com/post/just-looking)


