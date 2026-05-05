---
aliases: 
    - T1110
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/credential_access
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
mitre-attack: kb/mitre/attack/techniques/T1110-Brute_Force
tactic: 
     - Credential Access
platforms:
     - Containers - ESXi - IaaS - Identity Provider - Linux - macOS - Network Devices - Office Suite - SaaS - Windows
permissions required:
     - none
---

## Description

Adversaries may use brute force techniques to gain access to accounts when passwords are unknown or when password hashes are obtained.[^8]  Without knowledge of the password for an account or set of accounts, an adversary may systematically guess the password using a repetitive or iterative mechanism.[^2]  Brute forcing passwords can take place via interaction with a service that will check the validity of those credentials or offline against previously acquired credential data, such as password hashes.<br><br>Brute forcing credentials may take place at various points during a breach. For example, adversaries may attempt to brute force access to [[kb/mitre/attack/techniques/T1078-Valid_Accounts\|Valid Accounts]] within a victim environment leveraging knowledge gathered from other post-compromise behaviors such as [[kb/mitre/attack/techniques/T1003-OS_Credential_Dumping\|OS Credential Dumping]], [[kb/mitre/attack/techniques/T1087-Account_Discovery\|Account Discovery]], or [[kb/mitre/attack/techniques/T1201-Password_Policy_Discovery\|Password Policy Discovery]]. Adversaries may also combine brute forcing activity with behaviors such as [[kb/mitre/attack/techniques/T1133-External_Remote_Services\|External Remote Services]] as part of Initial Access. <br><br>If an adversary guesses the correct password but fails to login to a compromised account due to location-based conditional access policies, they may change their infrastructure until they match the victim’s location and therefore bypass those policies.[^5] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0378-PoshC2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] has modules for brute forcing local administrator and AD user accounts.[^7]  |
| [[kb/mitre/attack/software/S0488-CrackMapExec\|S0488]] | CrackMapExec | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can brute force supplied user credentials across a network range.[^3]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Proactively reset accounts that are known to be part of breached credentials either immediately, or after detecting bruteforce attempts. |
| [[kb/mitre/attack/mitigations/M1027-Password_Policies\|M1027]] | Password Policies | Refer to NIST guidelines when creating password policies.[^4]  |
| [[kb/mitre/attack/mitigations/M1032-Multi-factor_Authentication\|M1032]] | Multi-factor Authentication | Use multi-factor authentication. Where possible, also enable multi-factor authentication on externally facing services. |
| [[kb/mitre/attack/mitigations/M1036-Account_Use_Policies\|M1036]] | Account Use Policies | Set account lockout policies after a certain number of failed login attempts to prevent passwords from being guessed. Too strict a policy may create a denial of service condition and render environments un-usable, with all accounts used in the brute force being locked-out. Use conditional access policies to block logins from non-compliant devices or from outside defined organization IP ranges.[^6]  Consider blocking risky authentication requests, such as those originating from anonymizing services/proxies.[^1]  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1110.001-Password_Guessing\|T1110.001]] | Password Guessing |
| [[kb/mitre/attack/techniques/T1110.002-Password_Cracking\|T1110.002]] | Password Cracking |
| [[kb/mitre/attack/techniques/T1110.003-Password_Spraying\|T1110.003]] | Password Spraying |
| [[kb/mitre/attack/techniques/T1110.004-Credential_Stuffing\|T1110.004]] | Credential Stuffing |




> [!info]- References
> [^1]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)

> [^2]: [Dragos Crashoverride 2018](https://www.dragos.com/wp-content/uploads/CRASHOVERRIDE2018.pdf)

> [^3]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)

> [^4]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)

> [^5]: [ReliaQuest Health Care Social Engineering Campaign 2024](https://www.reliaquest.com/blog/health-care-social-engineering-campaign/)

> [^6]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)

> [^7]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)

> [^8]: [TrendMicro Pawn Storm Dec 2020](https://www.trendmicro.com/en_us/research/20/l/pawn-storm-lack-of-sophistication-as-a-strategy.html)


