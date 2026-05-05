---
aliases: 
    - T1213
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/collection
    - attack/type/technique
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1213-Data_from_Information_Repositories
tactic: 
     - Collection
platforms:
     - Linux - Windows - macOS - SaaS - IaaS - Office Suite
permissions required:
     - none
---

## Description

Adversaries may leverage information repositories to mine valuable information. Information repositories are tools that allow for storage of information, typically to facilitate collaboration or information sharing between users, and can store a wide variety of data that may aid adversaries in further objectives, such as Credential Access, Lateral Movement, or Defense Evasion, or direct access to the target information. Adversaries may also abuse external sharing features to share sensitive documents with recipients outside of the organization (i.e., [[kb/mitre/attack/techniques/T1537-Transfer_Data_to_Cloud_Account\|Transfer Data to Cloud Account]]). <br><br>The following is a brief list of example information that may hold potential value to an adversary and may also be found on an information repository:<br><br>* Policies, procedures, and standards<br>* Physical / logical network diagrams<br>* System architecture diagrams<br>* Technical system documentation<br>* Testing / development credentials (i.e., [[kb/mitre/attack/techniques/T1552-Unsecured_Credentials\|Unsecured Credentials]]) <br>* Work / project schedules<br>* Source code snippets<br>* Links to network shares and other internal resources<br>* Contact or other sensitive information about business partners and customers, including personally identifiable information (PII) <br><br>Information stored in a repository may vary based on the specific instance or environment. Specific common information repositories include the following:<br><br>* Storage services such as IaaS databases, enterprise databases, and more specialized platforms such as customer relationship management (CRM) databases <br>* Collaboration platforms such as SharePoint, Confluence, and code repositories<br>* Messaging platforms such as Slack and Microsoft Teams <br><br>In some cases, information repositories have been improperly secured, typically by unintentionally allowing for overly-broad access by all users or even public access to unauthenticated users. This is particularly common with cloud-native or cloud-hosted services, such as AWS Relational Database Service (RDS), Redis, or ElasticSearch.[^3] [^2] [^7] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-User_Training\|M1017]] | User Training | Develop and publish policies that define acceptable information to be stored in repositories. |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Enforce the principle of least-privilege. Consider implementing access control mechanisms that include both authentication and authorization. |
| [[kb/mitre/attack/mitigations/M1032-Multi-factor_Authentication\|M1032]] | Multi-factor Authentication | Use two or more pieces of evidence to authenticate to a system; such as username and password in addition to a token from a physical smart card or token generator. |
| [[kb/mitre/attack/mitigations/M1041-Encrypt_Sensitive_Information\|M1041]] | Encrypt Sensitive Information | Encrypt data stored at rest in databases.  |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Consider periodic review of accounts and privileges for critical and sensitive repositories. Ensure that repositories such as cloud-hosted databases are not unintentionally exposed to the public, and that security groups assigned to them permit only necessary and authorized hosts.[^8]  |
| [[kb/mitre/attack/mitigations/M1054-Software_Configuration\|M1054]] | Software Configuration | Consider implementing data retention policies to automate periodically archiving and/or deleting data that is no longer needed.   |
| [[kb/mitre/attack/mitigations/M1060-Out-of-Band_Communications_Channel\|M1060]] | Out-of-Band Communications Channel | Create plans for leveraging a secure out-of-band communications channel, rather than existing in-network chat applications, in case of a security incident.[^6]  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1213.001-Confluence\|T1213.001]] | Confluence |
| [[kb/mitre/attack/techniques/T1213.002-Sharepoint\|T1213.002]] | Sharepoint |
| [[kb/mitre/attack/techniques/T1213.003-Code_Repositories\|T1213.003]] | Code Repositories |
| [[kb/mitre/attack/techniques/T1213.004-Customer_Relationship_Management_Software\|T1213.004]] | Customer Relationship Management Software |
| [[kb/mitre/attack/techniques/T1213.005-Messaging_Applications\|T1213.005]] | Messaging Applications |
| [[kb/mitre/attack/techniques/T1213.006-Databases\|T1213.006]] | Databases |




> [!info]- References
> [^1]: [Atlassian Confluence Logging](https://confluence.atlassian.com/confkb/how-to-enable-user-access-logging-182943.html)

> [^2]: [TrendMicro Exposed Redis 2020](https://www.trendmicro.com/en_us/research/20/d/exposed-redis-instances-abused-for-remote-code-execution-cryptocurrency-mining.html)

> [^3]: [Mitiga](https://www.mitiga.io/blog/how-mitiga-found-pii-in-exposed-amazon-rds-snapshots)

> [^4]: [Sharepoint Sharing Events](https://docs.microsoft.com/en-us/microsoft-365/compliance/use-sharing-auditing?view=o365-worldwide#sharepoint-sharing-events)

> [^5]: [Microsoft SharePoint Logging](https://support.office.com/en-us/article/configure-audit-settings-for-a-site-collection-a9920c97-38c0-44f2-8bcb-4cf1e2ae22d2)

> [^6]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)

> [^7]: [Cybernews Reuters Leak 2022](https://cybernews.com/security/thomson-reuters-leaked-terabytes-sensitive-data/)

> [^8]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


