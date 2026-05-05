---
aliases: 
    - T1087
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/identity_provider
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1087-Account_Discovery
tactic: 
     - Discovery
platforms:
     - ESXi - IaaS - Identity Provider - Linux - macOS - Office Suite - SaaS - Windows
permissions required:
     - none
---

## Description

Adversaries may attempt to get a listing of valid accounts, usernames, or email addresses on a system or within a compromised environment. This information can help adversaries determine which accounts exist, which can aid in follow-on behavior such as brute-forcing, spear-phishing attacks, or account takeovers (e.g., [[kb/mitre/attack/techniques/T1078-Valid_Accounts\|Valid Accounts]]).<br><br>Adversaries may use several methods to enumerate accounts, including abuse of existing tools, built-in commands, and potential misconfigurations that leak account names and roles or permissions in the targeted environment.<br><br>For examples, cloud environments typically provide easily accessible interfaces to obtain user lists.[^5] [^4]  On hosts, adversaries can use default [[kb/mitre/attack/techniques/T1059.001-PowerShell\|PowerShell]] and other command line functionality to identify accounts. Information about email addresses and accounts may also be extracted by searching an infected system’s files.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0445-ShimRatReporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] listed all non-privileged and privileged accounts available on the machine.[^3]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Manage the creation, modification, use, and permissions associated to user accounts. |
| [[kb/mitre/attack/mitigations/M1028-Operating_System_Configuration\|M1028]] | Operating System Configuration | Prevent administrator accounts from being enumerated when an application is elevating through UAC since it can lead to the disclosure of account names. The Registry key is located `HKLM\ SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\CredUI\EnumerateAdministrators`. It can be disabled through GPO: Computer Configuration > [Policies] > Administrative Templates > Windows Components > Credential User Interface: E numerate administrator accounts on elevation. [^1]  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1087.001-Local_Account\|T1087.001]] | Local Account |
| [[kb/mitre/attack/techniques/T1087.002-Domain_Account\|T1087.002]] | Domain Account |
| [[kb/mitre/attack/techniques/T1087.003-Email_Account\|T1087.003]] | Email Account |
| [[kb/mitre/attack/techniques/T1087.004-Cloud_Account\|T1087.004]] | Cloud Account |




> [!info]- References
> [^1]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)

> [^2]: [Elastic - Koadiac Detection with EQL](https://www.elastic.co/security-labs/embracing-offensive-tooling-building-detections-against-koadic-using-eql)

> [^3]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)

> [^4]: [Google Cloud - IAM Servie Accounts List API](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/list)

> [^5]: [AWS List Users](https://docs.aws.amazon.com/cli/latest/reference/iam/list-users.html)


