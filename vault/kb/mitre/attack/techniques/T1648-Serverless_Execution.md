---
aliases: 
    - T1648
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/execution
    - attack/type/technique
    - platform/iaas
    - platform/office_suite
    - platform/saas
mitre-attack: kb/mitre/attack/techniques/T1648-Serverless_Execution
tactic: 
     - Execution
platforms:
     - SaaS - IaaS - Office Suite
permissions required:
     - none
---

## Description

Adversaries may abuse serverless computing, integration, and automation services to execute arbitrary code in cloud environments. Many cloud providers offer a variety of serverless resources, including compute engines, application integration services, and web servers. <br><br>Adversaries may abuse these resources in various ways as a means of executing arbitrary commands. For example, adversaries may use serverless functions to execute malicious code, such as crypto-mining malware (i.e. [[kb/mitre/attack/techniques/T1496-Resource_Hijacking\|Resource Hijacking]]).[^1]  Adversaries may also create functions that enable further compromise of the cloud environment. For example, an adversary may use the `IAM:PassRole` permission in AWS or the `iam.serviceAccounts.actAs` permission in Google Cloud to add [[kb/mitre/attack/techniques/T1098.003-Additional_Cloud_Roles\|Additional Cloud Roles]] to a serverless cloud function, which may then be able to perform actions the original user cannot.[^10] [^3] <br><br>Serverless functions can also be invoked in response to cloud events (i.e. [[kb/mitre/attack/techniques/T1546-Event_Triggered_Execution\|Event Triggered Execution]]), potentially enabling persistent execution over time. For example, in AWS environments, an adversary may create a Lambda function that automatically adds [[kb/mitre/attack/techniques/T1098.001-Additional_Cloud_Credentials\|Additional Cloud Credentials]] to a user and a corresponding CloudWatch events rule that invokes that function whenever a new user is created.[^6]  This is also possible in many cloud-based office application suites. For example, in Microsoft 365 environments, an adversary may create a Power Automate workflow that forwards all emails a user receives or creates anonymous sharing links whenever a user is granted access to a document in SharePoint.[^8] [^4]  In Google Workspace environments, they may instead create an Apps Script that exfiltrates a user's data when they open a file.[^7] [^9] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S1091-Pacu\|S1091]] | Pacu | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can create malicious Lambda functions.[^11]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Remove permissions to create, modify, or run serverless resources from users that do not explicitly require them. |
| [[kb/mitre/attack/mitigations/M1036-Account_Use_Policies\|M1036]] | Account Use Policies | Where possible, consider restricting access to and use of serverless functions. For examples, conditional access policies can be applied to users attempting to create workflows in Microsoft Power Automate. Google Apps Scripts that use OAuth can be limited by restricting access to high-risk OAuth scopes.[^2] [^5]  |






> [!info]- References
> [^1]: [Cado Security Denonia](https://www.cadosecurity.com/cado-discovers-denonia-the-first-malware-specifically-targeting-lambda/)

> [^2]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)

> [^3]: [Rhingo Security Labs GCP Privilege Escalation](https://rhinosecuritylabs.com/gcp/privilege-escalation-google-cloud-platform-part-1/)

> [^4]: [Microsoft DART Case Report 001](https://www.microsoft.com/security/blog/2020/03/09/real-life-cybercrime-stories-dart-microsoft-detection-and-response-team)

> [^5]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)

> [^6]: [Backdooring an AWS account](https://medium.com/daniel-grzelak/backdooring-an-aws-account-da007d36f8f9)

> [^7]: [Cloud Hack Tricks GWS Apps Script](https://cloud.hacktricks.xyz/pentesting-cloud/workspace-security/gws-google-platforms-phishing/gws-app-scripts)

> [^8]: [Varonis Power Automate Data Exfiltration](https://www.varonis.com/blog/power-automate-data-exfiltration)

> [^9]: [OWN-CERT Google App Script 2024](https://www.own.security/ressources/blog/google-workspace-malicious-app-script-analysis)

> [^10]: [Rhino Security Labs AWS Privilege Escalation](https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/)

> [^11]: [GitHub Pacu](https://github.com/RhinoSecurityLabs/pacu)


