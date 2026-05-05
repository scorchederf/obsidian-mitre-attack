---
aliases: 
    - S1071
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S1071-Rubeus
---

## Description

[[kb/mitre/attack/software/S1071-Rubeus\|Rubeus]] is a C# toolset designed for raw Kerberos interaction that has been used since at least 2020, including in ransomware operations.[^2] [^3] [^1] [^4] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1482-Domain_Trust_Discovery\|T1482]] | Domain Trust Discovery | [[kb/mitre/attack/software/S1071-Rubeus\|Rubeus]] can gather information about domain trusts.[^1] [^4]  |
| [[kb/mitre/attack/techniques/T1558.001-Golden_Ticket\|T1558.001]] | Golden Ticket | [[kb/mitre/attack/software/S1071-Rubeus\|Rubeus]] can forge a ticket-granting ticket.[^2]  |
| [[kb/mitre/attack/techniques/T1558.002-Silver_Ticket\|T1558.002]] | Silver Ticket | [[kb/mitre/attack/software/S1071-Rubeus\|Rubeus]] can create silver tickets.[^2]  |
| [[kb/mitre/attack/techniques/T1558.003-Kerberoasting\|T1558.003]] | Kerberoasting | [[kb/mitre/attack/software/S1071-Rubeus\|Rubeus]] can use the `KerberosRequestorSecurityToken.GetRequest` method to request kerberoastable service tickets.[^2]  |
| [[kb/mitre/attack/techniques/T1558.004-AS-REP_Roasting\|T1558.004]] | AS-REP Roasting | [[kb/mitre/attack/software/S1071-Rubeus\|Rubeus]] can reveal the credentials of accounts that have Kerberos pre-authentication disabled through AS-REP roasting.[^2] [^1] [^4]   |





> [!info]- References
> [^1]: [DFIR Ryuk's Return October 2020](https://thedfirreport.com/2020/10/08/ryuks-return/)

> [^2]: [GitHub Rubeus March 2023](https://github.com/GhostPack/Rubeus)

> [^3]: [FireEye KEGTAP SINGLEMALT October 2020](https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html)

> [^4]: [DFIR Ryuk 2 Hour Speed Run November 2020](https://thedfirreport.com/2020/11/05/ryuk-speed-run-2-hours-to-ransom/)


