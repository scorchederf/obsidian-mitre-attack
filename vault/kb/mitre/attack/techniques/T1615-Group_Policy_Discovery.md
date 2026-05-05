---
aliases: 
    - T1615
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1615-Group_Policy_Discovery
tactic: 
     - Discovery
platforms:
     - Windows
permissions required:
     - none
---

## Description

Adversaries may gather information on Group Policy settings to identify paths for privilege escalation, security measures applied within a domain, and to discover patterns in domain objects that can be manipulated or used to blend in the environment. Group Policy allows for centralized management of user and computer settings in Active Directory (AD). Group policy objects (GPOs) are containers for group policy settings made up of files stored within a predictable network path `\<DOMAIN>\SYSVOL\<DOMAIN>\Policies\`.[^4] [^2] <br><br>Adversaries may use commands such as `gpresult` or various publicly available PowerShell functions, such as `Get-DomainGPO` and `Get-DomainGPOLocalGroup`, to gather information on Group Policy settings.[^1] [^5]  Adversaries may use this information to shape follow-on behaviors, including determining potential attack paths within the target network as well as opportunities to manipulate Group Policy settings (i.e. [[kb/mitre/attack/techniques/T1484-Domain_or_Tenant_Policy_Modification\|Domain or Tenant Policy Modification]]) for their benefit.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] includes various modules for enumerating Group Policy.[^5]  |
| [[kb/mitre/attack/software/S0521-BloodHound\|S0521]] | BloodHound | [[kb/mitre/attack/software/S0521-BloodHound\|BloodHound]] has the ability to collect local admin information via GPO.[^3]  |








> [!info]- References
> [^1]: [Microsoft gpresult](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/gpresult)

> [^2]: [ADSecurity GPO Persistence 2016](https://adsecurity.org/?p=2716)

> [^3]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)

> [^4]: [TechNet Group Policy Basics](https://blogs.technet.microsoft.com/musings_of_a_technical_tam/2012/02/13/group-policy-basics-part-1-understanding-the-structure-of-a-group-policy-object/)

> [^5]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)


