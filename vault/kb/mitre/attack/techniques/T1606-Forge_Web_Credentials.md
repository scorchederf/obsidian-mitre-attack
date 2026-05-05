---
aliases: 
    - T1606
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/credential_access
    - attack/type/technique
    - platform/iaas
    - platform/identity_provider
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1606-Forge_Web_Credentials
tactic: 
     - Credential Access
platforms:
     - SaaS - Windows - macOS - Linux - IaaS - Office Suite - Identity Provider
permissions required:
     - none
---

## Description

Adversaries may forge credential materials that can be used to gain access to web applications or Internet services. Web applications and services (hosted in cloud SaaS environments or on-premise servers) often use session cookies, tokens, or other materials to authenticate and authorize user access.<br><br>Adversaries may generate these credential materials in order to gain access to web resources. This differs from [[kb/mitre/attack/techniques/T1539-Steal_Web_Session_Cookie\|Steal Web Session Cookie]], [[kb/mitre/attack/techniques/T1528-Steal_Application_Access_Token\|Steal Application Access Token]], and other similar behaviors in that the credentials are new and forged by the adversary, rather than stolen or intercepted from legitimate users.<br><br>The generation of web credentials often requires secret values, such as passwords, [[kb/mitre/attack/techniques/T1552.004-Private_Keys\|Private Keys]], or other cryptographic seed values.[^1]  Adversaries may also forge tokens by taking advantage of features such as the `AssumeRole` and `GetFederationToken` APIs in AWS, which allow users to request temporary security credentials (i.e., [[kb/mitre/attack/techniques/T1548.005-Temporary_Elevated_Cloud_Access\|Temporary Elevated Cloud Access]]), or the `zmprov gdpak` command in Zimbra, which generates a pre-authentication key that can be used to generate tokens for any user in the domain.[^7] [^8] <br><br>Once forged, adversaries may use these web credentials to access resources (ex: [[kb/mitre/attack/techniques/T1550-Use_Alternate_Authentication_Material\|Use Alternate Authentication Material]]), which may bypass multi-factor and other authentication protection mechanisms.[^3] [^4] [^2]   




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Ensure that user accounts with administrative rights follow best practices, including use of privileged access workstations, Just in Time/Just Enough Administration (JIT/JEA), and strong authentication. Reduce the number of users that are members of highly privileged Directory Roles.[^2]  In AWS environments, prohibit users from calling the `sts:GetFederationToken` API unless explicitly required.[^6]  |
| [[kb/mitre/attack/mitigations/M1026-Privileged_Account_Management\|M1026]] | Privileged Account Management | Restrict permissions and access to the AD FS server to only originate from privileged access workstations.[^5]  |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Administrators should perform an audit of all access lists and the permissions they have been granted to access web applications and services. This should be done extensively on all resources in order to establish a baseline, followed up on with periodic audits of new or updated resources. Suspicious accounts/credentials should be investigated and removed.<br> <br>Enable advanced auditing on ADFS. Check the success and failure audit options in the ADFS Management snap-in. Enable Audit Application Generated events on the AD FS farm via Group Policy Object.[^5]  |
| [[kb/mitre/attack/mitigations/M1054-Software_Configuration\|M1054]] | Software Configuration | Configure browsers/applications to regularly delete persistent web credentials (such as cookies). |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1606.001-Web_Cookies\|T1606.001]] | Web Cookies |
| [[kb/mitre/attack/techniques/T1606.002-SAML_Tokens\|T1606.002]] | SAML Tokens |




> [!info]- References
> [^1]: [GitHub AWS-ADFS-Credential-Generator](https://github.com/pvanbuijtene/aws-adfs-credential-generator)

> [^2]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)

> [^3]: [Pass The Cookie](https://wunderwuzzi23.github.io/blog/passthecookie.html)

> [^4]: [Unit 42 Mac Crypto Cookies January 2019](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)

> [^5]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)

> [^6]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)

> [^7]: [AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html)

> [^8]: [Zimbra Preauth](https://wiki.zimbra.com/wiki/Preauth)


