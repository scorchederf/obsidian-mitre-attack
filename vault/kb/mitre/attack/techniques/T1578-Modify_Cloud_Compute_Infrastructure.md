---
aliases: 
    - T1578
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/defense_impairment
    - attack/type/technique
    - platform/iaas
mitre-attack: kb/mitre/attack/techniques/T1578-Modify_Cloud_Compute_Infrastructure
tactic: 
     - Defense Impairment
platforms:
     - IaaS
permissions required:
     - none
---

## Description

An adversary may attempt to modify a cloud account's compute service infrastructure to evade defenses. A modification to the compute service infrastructure can include the creation, deletion, or modification of one or more components such as compute instances, virtual machines, and snapshots.<br><br>Permissions gained from the modification of infrastructure components may bypass restrictions that prevent access to existing infrastructure. Modifying infrastructure components may also allow an adversary to evade detection and remove evidence of their presence.[^1] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Limit permissions for creating, deleting, and otherwise altering compute components in accordance with least privilege. Organizations should limit the number of users within the organization with an IAM role that has administrative privileges, strive to reduce all permanent privileged role assignments, and conduct periodic entitlement reviews on IAM users, roles and policies.[^1]  |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Routinely monitor user permissions to ensure only the expected users have the capability to modify cloud compute infrastructure components. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1578.001-Create_Snapshot\|T1578.001]] | Create Snapshot |
| [[kb/mitre/attack/techniques/T1578.002-Create_Cloud_Instance\|T1578.002]] | Create Cloud Instance |
| [[kb/mitre/attack/techniques/T1578.003-Delete_Cloud_Instance\|T1578.003]] | Delete Cloud Instance |
| [[kb/mitre/attack/techniques/T1578.004-Revert_Cloud_Instance\|T1578.004]] | Revert Cloud Instance |
| [[kb/mitre/attack/techniques/T1578.005-Modify_Cloud_Compute_Configurations\|T1578.005]] | Modify Cloud Compute Configurations |




> [!info]- References
> [^1]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


