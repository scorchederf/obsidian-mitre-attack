---
aliases: 
    - S0677
    
mitre-attack: https://attack.mitre.org/software/S0677
---

## S0677

[AADInternals](https://attack.mitre.org/software/S0677) is a PowerShell-based framework for administering, enumerating, and exploiting Azure Active Directory. The tool is publicly available on GitHub.[^5] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Cloud Service Discovery\|T1526]] | Cloud Service Discovery | [AADInternals](https://attack.mitre.org/software/S0677) can enumerate information about a variety of cloud services, such as Office 365 and Sharepoint instances or OpenID Configurations.[^3]  |
| [[Steal or Forge Authentication Certificates\|T1649]] | Steal or Forge Authentication Certificates | [AADInternals](https://attack.mitre.org/software/S0677) can create and export various authentication certificates, including those associated with Azure AD joined/registered devices.[^3]  |
| [[Hybrid Identity\|T1556.007]] | Hybrid Identity | [AADInternals](https://attack.mitre.org/software/S0677) can inject a malicious DLL (`PTASpy`) into the `AzureADConnectAuthenticationAgentService` to backdoor Azure AD Pass-Through Authentication.[^9]  |
| [[Device Registration\|T1098.005]] | Device Registration | [AADInternals](https://attack.mitre.org/software/S0677) can register a device to Azure AD.[^3]  |
| [[Spearphishing Link\|T1598.003]] | Spearphishing Link | [AADInternals](https://attack.mitre.org/software/S0677) can send phishing emails containing malicious links designed to collect users’ credentials.[^3]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [AADInternals](https://attack.mitre.org/software/S0677) can gather unsecured credentials for Azure AD services, such as Azure AD Connect, from a local machine.[^3]  |
| [[Trust Modification\|T1484.002]] | Trust Modification | [AADInternals](https://attack.mitre.org/software/S0677) can create a backdoor by converting a domain to a federated domain which will be able to authenticate any user across the tenant. [AADInternals](https://attack.mitre.org/software/S0677) can also modify DesktopSSO information.[^3] [^7]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [AADInternals](https://attack.mitre.org/software/S0677) can send "consent phishing" emails containing malicious links designed to steal users’ access tokens.[^3]  |
| [[Cloud Groups\|T1069.003]] | Cloud Groups | [AADInternals](https://attack.mitre.org/software/S0677) can enumerate Azure AD groups.[^3]  |
| [[Cloud Account\|T1136.003]] | Cloud Account | [AADInternals](https://attack.mitre.org/software/S0677) can create new Azure AD users.[^3]  |
| [[SAML Tokens\|T1606.002]] | SAML Tokens | [AADInternals](https://attack.mitre.org/software/S0677) can be used to create SAML tokens using the AD Federated Services token signing certificate.[^3]  |
| [[Domain Properties\|T1590.001]] | Domain Properties | [AADInternals](https://attack.mitre.org/software/S0677) can gather information about a tenant’s domains using public Microsoft APIs.[^3] [^4]  |
| [[Email Addresses\|T1589.002]] | Email Addresses | [AADInternals](https://attack.mitre.org/software/S0677) can check for the existence of user email addresses using public Microsoft APIs.[^3] [^4]  |
| [[Silver Ticket\|T1558.002]] | Silver Ticket | [AADInternals](https://attack.mitre.org/software/S0677) can be used to forge Kerberos tickets using the password hash of the AZUREADSSOACC account.[^3]  |
| [[Private Keys\|T1552.004]] | Private Keys | [AADInternals](https://attack.mitre.org/software/S0677) can gather encryption keys from Azure AD services such as ADSync and Active Directory Federated Services servers.[^3]  |
| [[Steal Application Access Token\|T1528]] | Steal Application Access Token | [AADInternals](https://attack.mitre.org/software/S0677) can steal users’ access tokens via phishing emails containing malicious links.[^3]  |
| [[Cloud Account\|T1087.004]] | Cloud Account | [AADInternals](https://attack.mitre.org/software/S0677) can enumerate Azure AD users.[^3]  |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | [AADInternals](https://attack.mitre.org/software/S0677) can dump secrets from the Local Security Authority.[^3]  |
| [[Multi-Factor Authentication\|T1556.006]] | Multi-Factor Authentication | The [AADInternals](https://attack.mitre.org/software/S0677) `Set-AADIntUserMFA` command can be used to disable MFA for a specified user. |
| [[Cloud Administration Command\|T1651]] | Cloud Administration Command | [AADInternals](https://attack.mitre.org/software/S0677) can execute commands on Azure virtual machines using the VM agent.[^6]  |
| [[Data from Cloud Storage\|T1530]] | Data from Cloud Storage | AADInternals can collect files from a user’s OneDrive.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [AADInternals](https://attack.mitre.org/software/S0677) is written and executed via PowerShell.[^3]  |
| [[Modify Registry\|T1112]] | Modify Registry | [AADInternals](https://attack.mitre.org/software/S0677) can modify registry keys as part of setting a new pass-through authentication agent.[^3]  |
| [[Exfiltration Over Alternative Protocol\|T1048]] | Exfiltration Over Alternative Protocol | [AADInternals](https://attack.mitre.org/software/S0677) can directly download cloud user data such as OneDrive files.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |
| [[Storm-0501\|G1053]] | Storm-0501 |



## References

[^1]: [Microsoft Storm-501 Sabbath Ransomware Embargo September 2024](https://www.microsoft.com/en-us/security/blog/2024/09/26/storm-0501-ransomware-attacks-expanding-to-hybrid-cloud-environments/)


[^2]: [AADInternals](https://o365blog.com/aadinternals/)


[^3]: [AADInternals Documentation](https://o365blog.com/aadinternals)


[^4]: [Azure AD Recon](https://o365blog.com/post/just-looking)


[^5]: [AADInternals Github](https://github.com/Gerenios/AADInternals)


[^6]: [AADInternals Root Access to Azure VMs](https://aadinternals.com/post/azurevms/)


[^7]: [Azure AD Federation Vulnerability](https://o365blog.com/post/federation-vulnerability/)


[^8]: [MSTIC Nobelium Oct 2021](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks/)


[^9]: [AADInternals Azure AD On-Prem to Cloud](https://o365blog.com/post/on-prem_admin/)


