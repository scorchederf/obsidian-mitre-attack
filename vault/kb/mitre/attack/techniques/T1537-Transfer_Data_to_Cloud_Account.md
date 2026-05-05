---
aliases: 
    - T1537
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/exfiltration
    - attack/type/technique
    - platform/iaas
    - platform/office_suite
    - platform/saas
mitre-attack: kb/mitre/attack/techniques/T1537-Transfer_Data_to_Cloud_Account
tactic: 
     - Exfiltration
platforms:
     - IaaS - Office Suite - SaaS
permissions required:
     - none
---

## Description

Adversaries may exfiltrate data by transferring the data, including through sharing/syncing and creating backups of cloud environments, to another cloud account they control on the same service.<br><br>A defender who is monitoring for large transfers to outside the cloud environment through normal file transfers or over command and control channels may not be watching for data transfers to another account within the same cloud provider. Such transfers may utilize existing cloud provider APIs and the internal address space of the cloud provider to blend into normal traffic or avoid data transfers over external network interfaces.[^4] <br><br>Adversaries may also use cloud-native mechanisms to share victim data with adversary-controlled cloud accounts, such as creating anonymous file sharing links or, in Azure, a shared access signature (SAS) URI.[^1] <br><br>Incidents have been observed where adversaries have created backups of cloud instances and transferred them to separate accounts.[^3]  




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Limit user account and IAM policies to the least privileges required. |
| [[kb/mitre/attack/mitigations/M1037-Filter_Network_Traffic\|M1037]] | Filter Network Traffic | Implement network-based filtering restrictions to prohibit data transfers to untrusted VPCs. |
| [[kb/mitre/attack/mitigations/M1054-Software_Configuration\|M1054]] | Software Configuration | Configure appropriate data sharing restrictions in cloud services. For example, external sharing in Microsoft SharePoint and Google Drive can be turned off altogether, blocked for certain domains, or restricted to certain users.[^5]  [^8]  |
| [[kb/mitre/attack/mitigations/M1057-Data_Loss_Prevention\|M1057]] | Data Loss Prevention | Data loss prevention can prevent and block sensitive data from being shared with individuals outside an organization.[^9]  [^7]  |






> [!info]- References
> [^1]: [Microsoft Azure Storage Shared Access Signature](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)

> [^2]: [Azure Shared Access Signature](https://docs.microsoft.com/en-us/rest/api/storageservices/delegate-access-with-shared-access-signature)

> [^3]: [DOJ GRU Indictment Jul 2018](https://cdn.cnn.com/cnn/2018/images/07/13/gru.indictment.pdf)

> [^4]: [TLDRSec AWS Attacks](https://tldrsec.com/p/blog-lesser-known-aws-attacks)

> [^5]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)

> [^6]: [Azure Blob Snapshots](https://docs.microsoft.com/en-us/azure/storage/blobs/snapshots-overview)

> [^7]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)

> [^8]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)

> [^9]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)

> [^10]: [AWS EBS Snapshot Sharing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html)


