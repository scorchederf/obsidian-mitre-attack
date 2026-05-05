---
aliases: 
    - S1091
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S1091-Pacu
---

## Description

Pacu is an open-source AWS exploitation framework. The tool is written in Python and publicly available on GitHub.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1049-System_Network_Connections_Discovery\|T1049]] | System Network Connections Discovery | Once inside a Virtual Private Cloud, [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can attempt to identify DirectConnect, VPN, or VPC Peering.[^1]  |
| [[kb/mitre/attack/techniques/T1059.009-Cloud_API\|T1059.009]] | Cloud API | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] leverages the AWS CLI for its operations.[^1]  |
| [[kb/mitre/attack/techniques/T1069.003-Cloud_Groups\|T1069.003]] | Cloud Groups | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can enumerate IAM permissions.[^1]  |
| [[kb/mitre/attack/techniques/T1078.004-Cloud_Accounts\|T1078.004]] | Cloud Accounts | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] leverages valid cloud accounts to perform most of its operations.[^1]  |
| [[kb/mitre/attack/techniques/T1087.004-Cloud_Account\|T1087.004]] | Cloud Account | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can enumerate IAM users, roles, and groups. [^1]  |
| [[kb/mitre/attack/techniques/T1098.001-Additional_Cloud_Credentials\|T1098.001]] | Additional Cloud Credentials | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can generate SSH and API keys for AWS infrastructure and additional API keys for other IAM users.[^1]  |
| [[kb/mitre/attack/techniques/T1119-Automated_Collection\|T1119]] | Automated Collection | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can automatically collect data, such as CloudFormation templates, EC2 user data, AWS Inspector reports, and IAM credential reports.[^1]  |
| [[kb/mitre/attack/techniques/T1518.001-Security_Software_Discovery\|T1518.001]] | Security Software Discovery | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can enumerate AWS security services, including WAF rules and GuardDuty detectors.[^1]  |
| [[kb/mitre/attack/techniques/T1526-Cloud_Service_Discovery\|T1526]] | Cloud Service Discovery | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can enumerate AWS services, such as CloudTrail and CloudWatch.[^1]  |
| [[kb/mitre/attack/techniques/T1530-Data_from_Cloud_Storage\|T1530]] | Data from Cloud Storage | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can enumerate and download files stored in AWS storage services, such as S3 buckets.[^1]  |
| [[kb/mitre/attack/techniques/T1546-Event_Triggered_Execution\|T1546]] | Event Triggered Execution | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can set up S3 bucket notifications to trigger a malicious Lambda function when a CloudFormation template is uploaded to the bucket. It can also create Lambda functions that trigger upon the creation of users, roles, and groups.[^1]  |
| [[kb/mitre/attack/techniques/T1552-Unsecured_Credentials\|T1552]] | Unsecured Credentials | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can search for sensitive data: for example, in Code Build environment variables, EC2 user data, and Cloud Formation templates.[^1]  |
| [[kb/mitre/attack/techniques/T1555.006-Cloud_Secrets_Management_Stores\|T1555.006]] | Cloud Secrets Management Stores | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can retrieve secrets from the AWS Secrets Manager via the enum_secrets module.[^1]  |
| [[kb/mitre/attack/techniques/T1578.001-Create_Snapshot\|T1578.001]] | Create Snapshot | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can create snapshots of EBS volumes and RDS instances.[^1]  |
| [[kb/mitre/attack/techniques/T1580-Cloud_Infrastructure_Discovery\|T1580]] | Cloud Infrastructure Discovery | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can enumerate AWS infrastructure, such as EC2 instances.[^1]  |
| [[kb/mitre/attack/techniques/T1619-Cloud_Storage_Object_Discovery\|T1619]] | Cloud Storage Object Discovery | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can enumerate AWS storage services, such as S3 buckets and Elastic Block Store volumes.[^1]  |
| [[kb/mitre/attack/techniques/T1648-Serverless_Execution\|T1648]] | Serverless Execution | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can create malicious Lambda functions.[^1]  |
| [[kb/mitre/attack/techniques/T1651-Cloud_Administration_Command\|T1651]] | Cloud Administration Command | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can run commands on EC2 instances using AWS Systems Manager Run Command.[^1]  |
| [[kb/mitre/attack/techniques/T1654-Log_Enumeration\|T1654]] | Log Enumeration | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can collect CloudTrail event histories and CloudWatch logs.[^1]  |
| [[kb/mitre/attack/techniques/T1685.002-Disable_or_Modify_Cloud_Log\|T1685.002]] | Disable or Modify Cloud Log | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can disable or otherwise restrict various AWS logging services, such as AWS CloudTrail and VPC flow logs.[^1]  |
| [[kb/mitre/attack/techniques/T1686.001-Cloud_Firewall\|T1686.001]] | Cloud Firewall | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can allowlist IP addresses in AWS GuardDuty.[^1]  |





> [!info]- References
> [^1]: [GitHub Pacu](https://github.com/RhinoSecurityLabs/pacu)


