---
aliases: 
    - T1619
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/discovery
    - attack/type/technique
    - platform/iaas
mitre-attack: kb/mitre/attack/techniques/T1619-Cloud_Storage_Object_Discovery
tactic: 
     - Discovery
platforms:
     - IaaS
permissions required:
     - none
---

## Description

Adversaries may enumerate objects in cloud storage infrastructure. Adversaries may use this information during automated discovery to shape follow-on behaviors, including requesting all or specific objects from cloud storage.  Similar to [[kb/mitre/attack/techniques/T1083-File_and_Directory_Discovery\|File and Directory Discovery]] on a local host, after identifying available storage services (i.e. [[kb/mitre/attack/techniques/T1580-Cloud_Infrastructure_Discovery\|Cloud Infrastructure Discovery]]) adversaries may access the contents/objects stored in cloud infrastructure.<br><br>Cloud service providers offer APIs allowing users to enumerate objects stored within cloud storage. Examples include ListObjectsV2 in AWS [^3]  and List Blobs in Azure[^1]  .


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0683-Peirates\|S0683]] | Peirates | [[kb/mitre/attack/software/S0683-Peirates\|Peirates]] can list AWS S3 buckets.[^5]  |
| [[kb/mitre/attack/software/S1091-Pacu\|S1091]] | Pacu | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can enumerate AWS storage services, such as S3 buckets and Elastic Block Store volumes.[^4]  |
| [[kb/mitre/attack/software/S9009-TruffleHog\|S9009]] | TruffleHog | [[kb/mitre/attack/software/S9009-TruffleHog\|TruffleHog]] can enumerate cloud storage environments including Amazon Web Service (AWS) S3 buckets and Google Cloud Storage buckets.[^6] [^2]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Restrict granting of permissions related to listing objects in cloud storage to necessary accounts. |






> [!info]- References
> [^1]: [List Blobs](https://docs.microsoft.com/en-us/rest/api/storageservices/list-blobs)

> [^2]: [Github TruffleSecurity Trufflehog April 2025](https://github.com/trufflesecurity/trufflehog)

> [^3]: [ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html)

> [^4]: [GitHub Pacu](https://github.com/RhinoSecurityLabs/pacu)

> [^5]: [Peirates GitHub](https://github.com/inguardians/peirates)

> [^6]: [Black Hills Information Security TruffleHog January 2024](https://www.blackhillsinfosec.com/rooting-for-secrets-with-trufflehog/)


