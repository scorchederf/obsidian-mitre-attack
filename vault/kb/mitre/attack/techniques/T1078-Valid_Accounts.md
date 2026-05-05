---
aliases: 
    - T1078
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/initial_access
    - attack/tactic/persistence
    - attack/tactic/privilege_escalation
    - attack/tactic/stealth
    - attack/type/technique
    - platform/containers
    - platform/esxi
    - platform/iaas
    - platform/identity_provider
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1078-Valid_Accounts
tactic: 
     - Stealth - Persistence - Privilege Escalation - Initial Access
platforms:
     - Containers - ESXi - IaaS - Identity Provider - Linux - macOS - Network Devices - Office Suite - SaaS - Windows
permissions required:
     - none
---

## Description

Adversaries may obtain and abuse credentials of existing accounts as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion. Compromised credentials may be used to bypass access controls placed on various resources on systems within the network and may even be used for persistent access to remote systems and externally available services, such as VPNs, Outlook Web Access, network devices, and remote desktop.[^5]  Compromised credentials may also grant an adversary increased privilege to specific systems or access to restricted areas of the network. Adversaries may choose not to use malware or tools in conjunction with the legitimate access those credentials provide to make it harder to detect their presence.<br><br>In some cases, adversaries may abuse inactive accounts: for example, those belonging to individuals who are no longer part of an organization. Using these accounts may allow the adversary to evade detection, as the original account user will not be present to identify any anomalous activity taking place on their account.[^1] <br><br>The overlap of permissions for local, domain, and cloud accounts across a network of systems is of concern because the adversary may be able to pivot across accounts and systems to reach a high level of access (i.e., domain or enterprise administrator) to bypass access controls set within the enterprise.[^7] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1013-Application_Developer_Guidance\|M1013]] | Application Developer Guidance | Ensure that applications do not store sensitive data or credentials insecurely. (e.g. plaintext credentials in code, published credentials in repositories, or credentials in public cloud storage). |
| [[kb/mitre/attack/mitigations/M1015-Active_Directory_Configuration\|M1015]] | Active Directory Configuration | Disable legacy authentication, which does not support MFA, and require the use of modern authentication protocols instead. |
| [[kb/mitre/attack/mitigations/M1017-User_Training\|M1017]] | User Training | Applications may send push notifications to verify a login as a form of multi-factor authentication (MFA). Train users to only accept valid push notifications and to report suspicious push notifications. |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Regularly audit user accounts for activity and deactivate or remove any that are no longer needed. |
| [[kb/mitre/attack/mitigations/M1026-Privileged_Account_Management\|M1026]] | Privileged Account Management | Audit domain and local accounts as well as their permission levels routinely to look for situations that could allow an adversary to gain wide access by obtaining credentials of a privileged account. [^7]  [^3]  These audits should also include if default accounts have been enabled, or if new local accounts are created that have not been authorized. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers. [^4]  |
| [[kb/mitre/attack/mitigations/M1027-Password_Policies\|M1027]] | Password Policies | Applications and appliances that utilize default username and password should be changed immediately after the installation, and before deployment to a production environment.[^2]  When possible, applications that use SSH keys should be updated periodically and properly secured.<br><br>Policies should minimize (if not eliminate) reuse of passwords between different user accounts, especially employees using the same credentials for personal accounts that may not be defended by enterprise security resources. |
| [[kb/mitre/attack/mitigations/M1032-Multi-factor_Authentication\|M1032]] | Multi-factor Authentication | Implement multi-factor authentication (MFA) across all account types, including default, local, domain, and cloud accounts, to prevent unauthorized access, even if credentials are compromised. MFA provides a critical layer of security by requiring multiple forms of verification beyond just a password. This measure significantly reduces the risk of adversaries abusing valid accounts to gain initial access, escalate privileges, maintain persistence, or evade defenses within your network. |
| [[kb/mitre/attack/mitigations/M1036-Account_Use_Policies\|M1036]] | Account Use Policies | Use conditional access policies to block logins from non-compliant devices or from outside defined organization IP ranges.[^6]  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1078.001-Default_Accounts\|T1078.001]] | Default Accounts |
| [[kb/mitre/attack/techniques/T1078.002-Domain_Accounts\|T1078.002]] | Domain Accounts |
| [[kb/mitre/attack/techniques/T1078.003-Local_Accounts\|T1078.003]] | Local Accounts |
| [[kb/mitre/attack/techniques/T1078.004-Cloud_Accounts\|T1078.004]] | Cloud Accounts |




> [!info]- References
> [^1]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)

> [^2]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)

> [^3]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)

> [^4]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)

> [^5]: [volexity_0day_sophos_FW](https://www.volexity.com/blog/2022/06/15/driftingcloud-zero-day-sophos-firewall-exploitation-and-an-insidious-breach/)

> [^6]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)

> [^7]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


