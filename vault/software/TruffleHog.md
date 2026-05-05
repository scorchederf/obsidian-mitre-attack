---
aliases: 
    - S9009
    
mitre-attack: https://attack.mitre.org/software/S9009
---

## S9009

[TruffleHog](https://attack.mitre.org/software/S9009) is an open-source secrets-discovery tool that is used to search for credentials, API keys, and encryption keys across a variety of data sources and environments.[^1] [^3]  [TruffleHog](https://attack.mitre.org/software/S9009) has the ability to discover credentials and secrets stored in code repositories, git history, CI/CD pipelines, among other common storage locations to include filesystems and cloud storage buckets.[^1] [^2] [^3]  [TruffleHog](https://attack.mitre.org/software/S9009) was first released by its author in 2016.[^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Sharepoint\|T1213.002]] | Sharepoint | [TruffleHog](https://attack.mitre.org/software/S9009) has searched SharePoint for data and credentials.[^3]  |
| [[Messaging Applications\|T1213.005]] | Messaging Applications | [TruffleHog](https://attack.mitre.org/software/S9009) has obtained data and credentials associated with messaging applications to include Slack.[^3]  |
| [[Cloud Storage Object Discovery\|T1619]] | Cloud Storage Object Discovery | [TruffleHog](https://attack.mitre.org/software/S9009) can enumerate cloud storage environments including Amazon Web Service (AWS) S3 buckets and Google Cloud Storage buckets.[^1] [^3]  |
| [[Cloud API\|T1059.009]] | Cloud API | [TruffleHog](https://attack.mitre.org/software/S9009) has leveraged Cloud CLI in order to enumerate and gather credentials.[^3]  |
| [[Cloud Service Discovery\|T1526]] | Cloud Service Discovery | [TruffleHog](https://attack.mitre.org/software/S9009) has the ability to scan code repositories and CI/CD platforms.[^1] [^3]  |
| [[Cloud Secrets Management Stores\|T1555.006]] | Cloud Secrets Management Stores | [TruffleHog](https://attack.mitre.org/software/S9009) can obtain secrets from AWS Secrets and GCP Secret Manager.[^1] [^3]  [TruffleHog](https://attack.mitre.org/software/S9009) has also gathered passwords, secrets and API keys from source repositories, .env files, and git history.[^2]  |
| [[Cloud Infrastructure Discovery\|T1580]] | Cloud Infrastructure Discovery | [TruffleHog](https://attack.mitre.org/software/S9009) can enumerate AWS Infrastructure to include EC2 instances.[^3]  |
| [[Cloud Instance Metadata API\|T1552.005]] | Cloud Instance Metadata API | [TruffleHog](https://attack.mitre.org/software/S9009) can query the AWS and GCP metadata endpoints for instances and service credentials.[^1] [^3]  |
| [[Steal Application Access Token\|T1528]] | Steal Application Access Token | [TruffleHog](https://attack.mitre.org/software/S9009) has gathered access tokens and API tokens from CI/CD pipeline solutions and repositories.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [TruffleHog](https://attack.mitre.org/software/S9009) has can browse and scan individual files and directories.[^1] [^2] [^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [TruffleHog](https://attack.mitre.org/software/S9009) has gathered data from home directories of the victim environment.[^2]  |
| [[Cloud Accounts\|T1078.004]] | Cloud Accounts | [TruffleHog](https://attack.mitre.org/software/S9009) has used stolen credentials to log into cloud services to access cloud hosted repositories and other cloud storage solutions to discover sensitive data to include API Keys, tokens and credentials.[^3]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [TruffleHog](https://attack.mitre.org/software/S9009) has obtained credentials stored in config files and credential files in victim environments.[^1] [^2]  |
| [[Data from Cloud Storage\|T1530]] | Data from Cloud Storage | [TruffleHog](https://attack.mitre.org/software/S9009) has the ability to scan cloud storage services for credentials to include Amazon (AWS) S3 and Google Cloud Storage.[^1] [^3]  |
| [[Confluence\|T1213.001]] | Confluence | [TruffleHog](https://attack.mitre.org/software/S9009) has collected credentials and data associated with Confluence.[^3]  |
| [[Code Repositories\|T1213.003]] | Code Repositories | [TruffleHog](https://attack.mitre.org/software/S9009) has gathered data and credentials from code repositories.[^3]  |




## References

[^1]: [Black Hills Information Security TruffleHog January 2024](https://www.blackhillsinfosec.com/rooting-for-secrets-with-trufflehog/)


[^2]: [Netskope Shai-Hulud November 2025](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)


[^3]: [Github TruffleSecurity Trufflehog April 2025](https://github.com/trufflesecurity/trufflehog)


