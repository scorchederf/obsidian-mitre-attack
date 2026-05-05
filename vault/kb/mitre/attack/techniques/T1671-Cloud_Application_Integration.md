---
aliases: 
    - T1671
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/persistence
    - attack/type/technique
    - platform/office_suite
    - platform/saas
mitre-attack: kb/mitre/attack/techniques/T1671-Cloud_Application_Integration
tactic: 
     - Persistence
platforms:
     - Office Suite - SaaS
permissions required:
     - none
---

## Description

Adversaries may achieve persistence by leveraging OAuth application integrations in a software-as-a-service environment. Adversaries may create a custom application, add a legitimate application into the environment, or even co-opt an existing integration to achieve malicious ends.[^9] [^7] <br><br>OAuth is an open standard that allows users to authorize applications to access their information on their behalf. In a SaaS environment such as Microsoft 365 or Google Workspace, users may integrate applications to improve their workflow and achieve tasks.  <br><br>Leveraging application integrations may allow adversaries to persist in an environment – for example, by granting consent to an application from a high-privileged adversary-controlled account in order to maintain access to its data, even in the event of losing access to the account.[^3] [^6] [^8]  In some cases, integrations may remain valid even after the original consenting user account is disabled.[^4]  Application integrations may also allow adversaries to bypass multi-factor authentication requirements through the use of [[kb/mitre/attack/techniques/T1550.001-Application_Access_Token\|Application Access Token]]s. Finally, they may enable persistent [[kb/mitre/attack/techniques/T1020-Automated_Exfiltration\|Automated Exfiltration]] over time.[^1] <br><br>Creating or adding a new application may require the adversary to create a dedicated [[kb/mitre/attack/techniques/T1136.003-Cloud_Account\|Cloud Account]] for the application and assign it [[kb/mitre/attack/techniques/T1098.003-Additional_Cloud_Roles\|Additional Cloud Roles]] – for example, in Microsoft 365 environments, an application can only access resources via an associated service principal.[^2]   




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1042-Disable_or_Remove_Feature_or_Program\|M1042]] | Disable or Remove Feature or Program | Do not allow users to add new application integrations into a SaaS environment. In Entra ID environments, consider enforcing the “Do not allow user consent” option.[^5]  |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Periodically review SaaS integrations for unapproved or potentially malicious applications.   |






> [!info]- References
> [^1]: [Synes Cyber Corner Malicious Azure Application 2023](https://cybercorner.tech/malicious-azure-application-perfectdata-software-and-office365-business-email-compromise/)

> [^2]: [Microsoft Entra ID Service Principals](https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals?tabs=browser)

> [^3]: [Wiz Midnight Blizzard 2024](https://www.wiz.io/blog/midnight-blizzard-microsoft-breach-analysis-and-best-practices)

> [^4]: [Push Security Slack Persistence 2023](https://pushsecurity.com/blog/phishing-slack-persistence/)

> [^5]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)

> [^6]: [Microsoft Malicious OAuth Applications 2022](https://www.microsoft.com/en-us/security/blog/2022/09/22/malicious-OAuth-applications-used-to-compromise-email-servers-and-spread-spam/)

> [^7]: [SaaS Attacks GitHub Evil Twin Integrations](https://github.com/pushsecurity/saas-attacks/blob/main/techniques/evil_twin_integrations/description.md)

> [^8]: [Huntress Persistence Microsoft 365 Compromise 2024](https://www.huntress.com/blog/legitimate-apps-as-traitorware-for-persistent-microsoft-365-compromise)

> [^9]: [Push Security SaaS Persistence 2022](https://pushsecurity.com/blog/maintaining-persistent-access-in-a-saas-first-world/)


