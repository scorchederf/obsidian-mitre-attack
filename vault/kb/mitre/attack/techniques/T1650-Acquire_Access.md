---
aliases: 
    - T1650
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/resource_development
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1650-Acquire_Access
tactic: 
     - Resource Development
platforms:
     - PRE
permissions required:
     - none
---

## Description

Adversaries may purchase or otherwise acquire an existing access to a target system or network. A variety of online services and initial access broker networks are available to sell access to previously compromised systems.[^3] [^4] [^2]  In some cases, adversary groups may form partnerships to share compromised systems with each other.[^1] <br><br>Footholds to compromised systems may take a variety of forms, such as access to planted backdoors (e.g., [[kb/mitre/attack/techniques/T1505.003-Web_Shell\|Web Shell]]) or established access via [[kb/mitre/attack/techniques/T1133-External_Remote_Services\|External Remote Services]]. In some cases, access brokers will implant compromised systems with a “load” that can be used to install additional malware for paying customers.[^3] <br><br>By leveraging existing access broker networks rather than developing or obtaining their own initial access capabilities, an adversary can potentially reduce the resources required to gain a foothold on a target network and focus their efforts on later stages of compromise. Adversaries may prioritize acquiring access to systems that have been determined to lack security monitoring or that have high privileges, or systems that belong to organizations in a particular sector.[^3] [^4] <br><br>In some cases, purchasing access to an organization in sectors such as IT contracting, software development, or telecommunications may allow an adversary to compromise additional victims via a [[kb/mitre/attack/techniques/T1199-Trusted_Relationship\|Trusted Relationship]], [[kb/mitre/attack/techniques/T1111-Multi-Factor_Authentication_Interception\|Multi-Factor Authentication Interception]], or even [[kb/mitre/attack/techniques/T1195-Supply_Chain_Compromise\|Supply Chain Compromise]].<br><br>**Note:** while this technique is distinct from other behaviors such as [[kb/mitre/attack/techniques/T1597.002-Purchase_Technical_Data\|Purchase Technical Data]] and [[kb/mitre/attack/techniques/T1589.001-Credentials\|Credentials]], they may often be used in conjunction (especially where the acquired foothold requires [[kb/mitre/attack/techniques/T1078-Valid_Accounts\|Valid Accounts]]).




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-Pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls.  |






> [!info]- References
> [^1]: [CISA Karakurt 2022](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-152a)

> [^2]: [Krebs Access Brokers Fortune 500](https://krebsonsecurity.com/2012/10/service-sells-access-to-fortune-500-firms/)

> [^3]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)

> [^4]: [CrowdStrike Access Brokers](https://www.crowdstrike.com/blog/access-brokers-targets-and-worth/)


